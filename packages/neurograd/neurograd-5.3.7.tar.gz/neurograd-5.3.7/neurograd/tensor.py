from . import xp
import numpy as real_np
from typing import Optional, List, Callable, Union, Tuple, Sequence
from numpy.typing import ArrayLike


class Tensor:
    id = 0 # Unique identifier for each tensor

    def __new__(cls, data, *args, **kwargs):
        if isinstance(data, Tensor):
            return data
        return super().__new__(cls)

    def __init__(self, data, requires_grad: bool = False,
                 grad_fn: Optional[Callable] = None, name: Optional[str] = None,
                 dtype: Optional[str] = None):
        if isinstance(data, Tensor):
            return # avoid rewrapping a Tensor
        if not isinstance(data, xp.ndarray):
            self.data = xp.array(data, dtype=dtype) if dtype is not None else xp.array(data)
        elif dtype is not None:
            self.data = data.astype(dtype, copy=False)
        else:
            self.data = data
        self.requires_grad = requires_grad # whether to compute gradients for this tensor
        self.grad = None # gradient of this tensor
        self.grad_fn = grad_fn # function that created this tensor
        if name:
            self.name = name
        else:
            self.name = f"UnnamedTensor_{Tensor.id}"
            Tensor.id += 1
        self.device = 'cpu' if xp is real_np else 'cuda'
        self.dtype = dtype or self.data.dtype


    def backward(self, grad=None, retain_graph: bool = False, preserve_ancestors: int = 4):
        """
        Compute gradients using automatic differentiation.
        
        Args:
            grad: Initial gradient. If None, assumes scalar output (gradient of 1).
            retain_graph: If True, the graph is retained for multiple backward passes.
            preserve_ancestors: If > 0, preserves the .data attribute for the final `n`
                                intermediate tensors in the graph before the output.
                                This is useful for accessing their values (e.g., for metrics)
                                after the backward pass, at the cost of memory.
        """
        if not self.requires_grad:
            raise RuntimeError("Cannot do backprop for a tensor that does not require grad.")
        
        if grad is None:
            if self.data.size != 1:
                raise RuntimeError(
                    "backward() can only be called for scalar outputs. "
                    "For non-scalar outputs, gradient must be provided."
                )
            grad = xp.ones_like(self.data)
        
        # Build the computational graph using topological sort
        topo_order = []
        visited = set()
        
        def build_topo(tensor):
            if id(tensor) in visited: return
            visited.add(id(tensor))
            if tensor.grad_fn is not None:
                for parent in tensor.grad_fn.parent_tensors:
                    if parent.requires_grad:
                        build_topo(parent)
                topo_order.append(tensor)
        
        build_topo(self)
        
        # --- NEW LOGIC: Identify which nodes to preserve based on the new parameter ---
        nodes_to_preserve = set()
        if preserve_ancestors > 0 and topo_order:
            # Get the last 'preserve_ancestors' tensors from the sorted list.
            # These are the tensors closest to the output tensor `self`.
            preserved_tensors = topo_order[-preserve_ancestors:]
            nodes_to_preserve = {id(t) for t in preserved_tensors}
        # --- END NEW LOGIC ---

        if self.grad is None:
            self.grad = grad
        else:
            xp.add(self.grad, grad, out=self.grad)
        
        for tensor in reversed(topo_order):
            if tensor.grad_fn is None: continue
                
            grad_output = tensor.grad
            
            from neurograd.utils.memory import start_op_timing, maybe_log_op_memory
            op_name = getattr(tensor.grad_fn, 'name', None) or tensor.grad_fn.__class__.__name__
            timing_context = start_op_timing()
            parent_grads = tensor.grad_fn.backward(grad_output)
            maybe_log_op_memory(f"{op_name}_bwd", [grad_output], parent_grads, timing_context)
            
            if not isinstance(parent_grads, tuple):
                parent_grads = (parent_grads,)
            
            for parent_tensor, parent_grad in zip(tensor.grad_fn.parent_tensors, parent_grads):
                if parent_tensor.requires_grad and parent_grad is not None:
                    if parent_tensor.grad is None:
                        parent_tensor.grad = parent_grad
                    else:
                        xp.add(parent_tensor.grad, parent_grad, out=parent_tensor.grad)
            
            # --- MODIFIED MEMORY CLEARING LOGIC ---
            if not retain_graph:
                is_leaf = tensor.grad_fn is None
                # Check if the current tensor's ID is in the set of nodes to preserve.
                is_preserved = id(tensor) in nodes_to_preserve

                tensor.grad_fn = None
                
                # Only clear data for intermediate tensors that are not marked for preservation.
                if not is_leaf and not is_preserved:
                    tensor.grad = None
                    # Note: We don't clear `self` (the tensor backward is called on), but
                    # `self` is never in topo_order, so this check is implicitly handled.
                    tensor.data = None
            # --- END MODIFIED LOGIC ---


    def cast(self, dtype):
        try: 
            # Check if already the correct dtype
            if self.data.dtype == dtype:
                return self
            
            # Use proper autograd casting operation
            from neurograd.functions.tensor_ops import Cast
            cast_op = Cast(target_dtype=dtype)
            return cast_op(self)
        except Exception as e:
            raise TypeError(f"{dtype} isn't a supported data type for the array module: {e}.")
    
    def to_half(self):
        """Convenience method to cast to FP16"""
        return self.cast(xp.float16)
    
    def to_float(self):
        """Convenience method to cast to FP32"""
        return self.cast(xp.float32)
    
    def is_half(self) -> bool:
        """Check if tensor is in FP16"""
        return self.data.dtype == xp.float16
    
    def is_float(self) -> bool:
        """Check if tensor is in FP32"""
        return self.data.dtype == xp.float32
    
    def to_double(self):
        """Convenience method to cast to FP64"""
        return self.cast(xp.float64)
    
    def is_double(self) -> bool:
        """Check if tensor is in FP64"""
        return self.data.dtype == xp.float64
    
    def to_dtype(self, dtype):
        """Convenience method to cast to specified dtype"""
        if isinstance(dtype, str):
            dtype = getattr(xp, dtype)
        return self.cast(dtype)
    
    def is_floating_point(self) -> bool:
        """Check if tensor has floating point dtype"""
        return self.data.dtype.kind == 'f'
    
    def is_integer(self) -> bool:
        """Check if tensor has integer dtype"""
        return self.data.dtype.kind in ['i', 'u']
    
    def get_dtype(self):
        """Get the dtype of the tensor"""
        return self.data.dtype
    

    
    def to(self, device):
        """Move tensor to specified device ('cpu' or 'cuda')."""
        if device == self.device:
            return self
            
        if device == 'cpu':
            # Move to CPU
            if xp is not real_np:  # Currently on GPU
                import cupy as cp
                cpu_data = cp.asnumpy(self.data)
                return Tensor(cpu_data, requires_grad=self.requires_grad,
                            grad_fn=self.grad_fn, name=f"{self.name}_cpu")
            else:
                return self  # Already on CPU
        elif device == 'cuda':
            # Move to GPU
            if xp is real_np:  # Currently on CPU
                try:
                    import cupy as cp
                    gpu_data = cp.asarray(self.data)
                    return Tensor(gpu_data, requires_grad=self.requires_grad,
                                grad_fn=self.grad_fn, name=f"{self.name}_cuda")
                except ImportError:
                    raise RuntimeError("CuPy not available. Cannot move tensor to CUDA.")
            else:
                return self  # Already on GPU
        else:
            raise ValueError(f"Unsupported device: {device}. Use 'cpu' or 'cuda'.")
         
    
    def zero_grad(self):
        self.grad = None  # Reset gradient to None
    
    def __add__(self, other) -> 'Tensor':
        from .functions.arithmetic import Add
        return Add()(self, other)
    
    def __radd__(self, other) -> 'Tensor':
        # For right addition (e.g., 5 + tensor)
        if isinstance(other, (int, float)):
            other = Tensor(xp.array(other), requires_grad=False)
        return other.__add__(self)
    
    def __sub__(self, other) -> 'Tensor':
        from .functions.arithmetic import Sub
        return Sub()(self, other)
    
    def __rsub__(self, other) -> 'Tensor':
        if isinstance(other, (int, float)):
            other = Tensor(xp.array(other), requires_grad=False)
        return other.__sub__(self)
    
    def __mul__(self, other) -> 'Tensor':
        from .functions.arithmetic import Mul
        return Mul()(self, other)
    
    def __rmul__(self, other) -> 'Tensor':
        if isinstance(other, (int, float)):
            other = Tensor(xp.array(other), requires_grad=False)
        return other.__mul__(self)
    
    def __truediv__(self, other) -> 'Tensor':
        from .functions.arithmetic import Div
        return Div()(self, other)
    
    def __rtruediv__(self, other) -> 'Tensor':
        if isinstance(other, (int, float)):
            other = Tensor(xp.array(other), requires_grad=False)
        return other.__truediv__(self)
    
    def __div__(self, other) -> 'Tensor':
        return self.__truediv__(other)
    
    def __pow__(self, other) -> 'Tensor':
        from .functions.arithmetic import Pow
        return Pow()(self, other)

    def __rpow__(self, other) -> 'Tensor':
        if isinstance(other, (int, float)):
            other = Tensor(xp.array(other), requires_grad=False)
        return other.__pow__(self)
    
    def __neg__(self) -> 'Tensor':
        return self * Tensor(xp.array(-1.0), requires_grad=self.requires_grad)
    
    def __matmul__(self, other) -> 'Tensor':
        from .functions.linalg import MatMul
        return MatMul()(self, other)
    
    def __rmatmul__(self, other) -> 'Tensor':
        if isinstance(other, (int, float)):
            other = Tensor(xp.array(other), requires_grad=False)
        return other.__matmul__(self)
    
    def __eq__(self, other) -> 'Tensor':
        """Element-wise equality comparison."""
        if isinstance(other, Tensor):
            result = self.data == other.data
        else:
            result = self.data == other
        return Tensor(result, requires_grad=False, name=f"{self.name}_eq")
    
    def __ne__(self, other) -> 'Tensor':
        """Element-wise not-equal comparison."""
        if isinstance(other, Tensor):
            result = self.data != other.data
        else:
            result = self.data != other
        return Tensor(result, requires_grad=False, name=f"{self.name}_ne")
    
    def __lt__(self, other) -> 'Tensor':
        """Element-wise less-than comparison."""
        if isinstance(other, Tensor):
            result = self.data < other.data
        else:
            result = self.data < other
        return Tensor(result, requires_grad=False, name=f"{self.name}_lt")
    
    def __le__(self, other) -> 'Tensor':
        """Element-wise less-than-or-equal comparison."""
        if isinstance(other, Tensor):
            result = self.data <= other.data
        else:
            result = self.data <= other
        return Tensor(result, requires_grad=False, name=f"{self.name}_le")
    
    def __gt__(self, other) -> 'Tensor':
        """Element-wise greater-than comparison."""
        if isinstance(other, Tensor):
            result = self.data > other.data
        else:
            result = self.data > other
        return Tensor(result, requires_grad=False, name=f"{self.name}_gt")
    
    def __ge__(self, other) -> 'Tensor':
        """Element-wise greater-than-or-equal comparison."""
        if isinstance(other, Tensor):
            result = self.data >= other.data
        else:
            result = self.data >= other
        return Tensor(result, requires_grad=False, name=f"{self.name}_ge")
    
    def dot(self, other) -> 'Tensor':
        return self.__matmul__(other)
    
    def tensordot(self, other, axes) -> 'Tensor':
        from .functions.linalg import TensorDot
        return TensorDot(axes=axes)(self, other)

    def sum(self, axis=None, keepdims=False) -> 'Tensor':
        """Sum of tensor elements over given axis."""
        from .functions.reductions import Sum
        return Sum(axis=axis, keepdims=keepdims)(self)
    
    def mean(self, axis=None, keepdims=False) -> 'Tensor':
        """Mean of tensor elements over given axis."""
        from .functions.reductions import Mean
        return Mean(axis=axis, keepdims=keepdims)(self)
    
    def max(self, axis=None, keepdims=False) -> 'Tensor':
        """Maximum of tensor elements over given axis."""
        from .functions.reductions import Max
        return Max(axis=axis, keepdims=keepdims)(self)
    
    def min(self, axis=None, keepdims=False) -> 'Tensor':
        """Minimum of tensor elements over given axis."""
        from .functions.reductions import Min
        return Min(axis=axis, keepdims=keepdims)(self)
    
    def std(self, axis=None, keepdims=False) -> 'Tensor':
        """Standard deviation of tensor elements over given axis."""
        from .functions.reductions import Std
        return Std(axis=axis, keepdims=keepdims)(self)
    
    def var(self, axis=None, keepdims=False) -> 'Tensor':
        """Variance of tensor elements over given axis."""
        from .functions.reductions import Var
        return Var(axis=axis, keepdims=keepdims)(self)

    def argmin(self, axis=None) -> 'Tensor':
        """Indices of minimum values along an axis."""
        result = xp.argmin(self.data, axis=axis)
        return Tensor(result, requires_grad=False, name=self.name + "_argmin")

    def argmax(self, axis=None) -> 'Tensor':
        """Indices of maximum values along an axis."""
        result = xp.argmax(self.data, axis=axis)
        return Tensor(result, requires_grad=False, name=self.name + "_argmax")
    
    def log(self) -> 'Tensor':
        from .functions.math import Log
        return Log()(self)
    
    def exp(self) -> 'Tensor':
        from .functions.math import Exp
        return Exp()(self)
    
    def sin(self) -> 'Tensor':
        from .functions.math import Sin
        return Sin()(self)
    
    def cos(self) -> 'Tensor':
        from .functions.math import Cos
        return Cos()(self)
    
    def tan(self) -> 'Tensor':
        from .functions.math import Tan
        return Tan()(self)
    
    def sqrt(self) -> 'Tensor':
        from .functions.math import Sqrt
        return Sqrt()(self)
    
    def cbrt(self) -> 'Tensor':
        from .functions.math import Cbrt
        return Cbrt()(self)
    
    def log10(self) -> 'Tensor':
        from .functions.math import Log10
        return Log10()(self)
    
    def log2(self) -> 'Tensor':
        from .functions.math import Log2
        return Log2()(self)
    
    def abs(self) -> 'Tensor':
        from .functions.math import Abs
        return Abs()(self)
    
    def clip(self, min_val=None, max_val=None) -> 'Tensor':
        from .functions.math import Clip
        return Clip(min_val, max_val)(self)
    
    def relu(self) -> 'Tensor':
        from .functions.activations import ReLU
        return ReLU()(self)
    
    def relu6(self) -> 'Tensor':
        from .functions.activations import ReLU6
        return ReLU6()(self)
    
    def sigmoid(self) -> 'Tensor':
        from .functions.activations import Sigmoid
        return Sigmoid()(self)
    
    def tanh(self) -> 'Tensor':
        from .functions.activations import Tanh
        return Tanh()(self)
    
    def leaky_relu(self, negative_slope: float = 0.01) -> 'Tensor':
        from .functions.activations import LeakyReLU
        return LeakyReLU(negative_slope=negative_slope)(self)
    
    def transpose(self, axes=None) -> 'Tensor':
        from .functions.linalg import Transpose
        return Transpose(axes=axes)(self)

    @property
    def T(self) -> 'Tensor':
        """Transpose of the tensor."""
        return self.transpose()
    @property
    def shape(self) -> tuple:
        """Shape of the tensor."""
        return self.data.shape
    @property
    def ndim(self) -> int:
        return self.data.ndim
    @property
    def size(self) -> int:
        return self.data.size
    @property
    def ndim(self) -> int:
        return self.data.ndim
     
    def __len__(self):
        return len(self.data)
    
    def reshape(self, new_shape: Union[int, Tuple[int, ...]]) -> 'Tensor':
        """Reshape the tensor to a new shape."""
        from .functions.tensor_ops import Reshape
        return Reshape(new_shape=new_shape)(self)

    def flatten(self, start_dim: int = 1, end_dim: int = -1) -> 'Tensor': # copy
        """Return a flattened 1D VIEW of the tensor, still attached to the computational graph."""
        from .functions.tensor_ops import Flatten
        return Flatten(start_dim=start_dim, end_dim=end_dim)(self)

    def squeeze(self, axis=None) -> 'Tensor':
        """Remove dimensions of size 1 from the tensor."""
        from .functions.tensor_ops import Squeeze
        return Squeeze(axis=axis)(self)

    def expand_dims(self, axis) -> 'Tensor':
        """Add new axis of size 1 at specified position"""
        from .functions.tensor_ops import ExpandDims
        return ExpandDims(axis=axis)(self)
    
    def pad(self, pad_width: Union[Sequence, ArrayLike, int], mode='constant', **kwargs) -> 'Tensor':
        """Pad the tensor with specified padding width and mode."""
        from .functions.tensor_ops import Pad
        return Pad(pad_width=pad_width, mode=mode, **kwargs)(self)

    def copy(self) -> 'Tensor':
        """Return a copy of the tensor."""
        copied_data = self.data.copy()
        new_tensor = Tensor(
            data=copied_data,
            requires_grad=self.requires_grad,
            grad_fn=None,  # Copy doesn't preserve gradient function
            name=self.name + "_copy",
            dtype=self.data.dtype
        )
        # Copy gradient if it exists
        if self.grad is not None:
            new_tensor.grad = self.grad.copy()
        return new_tensor

    def detach(self) -> 'Tensor':
        """
        Return a new tensor detached from the graph.
        Shares the same underlying storage (no data copy) but does not
        require gradients and has no grad_fn.
        """
        return Tensor(
            data=self.data,  # share storage, no copy
            requires_grad=False,
            grad_fn=None,
            name=self.name + "_detached",
            dtype=self.data.dtype,
        )

    def clone(self) -> 'Tensor':
        """
        Return a copy of the tensor that participates in autograd.
        If this tensor requires gradients, the clone will too, and
        gradients will flow back to this tensor through the clone op.
        """
        from .functions.tensor_ops import Clone
        return Clone()(self)

    def __getitem__(self, key):
        """Differentiable slicing/indexing that participates in autograd."""
        from .functions.tensor_ops import Slice
        return Slice(key)(self)

    def __setitem__(self, key, value):
        """Allow setting values using index."""
        if isinstance(value, Tensor):
            self.data[key] = value.data
        else:
            self.data[key] = value

    def visualize_graph(self, **kwargs):
        """
        Visualize the computational graph that led to this tensor.
        
        Args:
            **kwargs: Additional arguments passed to the graph visualizer
            
        Returns:
            matplotlib Figure object
        """
        from .utils.graph import visualize_graph
        return visualize_graph(self, **kwargs)
    
    def save_graph(self, filename: str, **kwargs):
        """
        Save a visualization of the computational graph to file.
        
        Args:
            filename: Path to save the image
            **kwargs: Additional arguments passed to the graph visualizer
        """
        from .utils.graph import save_graph
        save_graph(self, filename, **kwargs)
    
    def print_graph(self):
        """
        Print a text representation of the computational graph structure.
        """
        from .utils.graph import print_graph_structure
        print_graph_structure(self)
    
    def graph_stats(self):
        """
        Get statistics about the computational graph.
        
        Returns:
            Dictionary containing graph statistics
        """
        from .utils.graph import get_graph_stats
        return get_graph_stats(self)
    
    def __hash__(self):
        """Make tensor hashable using its id."""
        return hash(id(self))
    
    def __repr__(self):
        """Return a string representation of the tensor."""
        return f"Tensor(data={self.data}, requires_grad={self.requires_grad}, grad_fn={self.grad_fn}, name={self.name})"

    def __str__(self):
        """Return a string representation of the tensor."""
        return f"Tensor({self.data})"

# NON-DIFF
def zeros(shape: Union[int, List[int]], dtype: Optional[str] = None,
          requires_grad: bool = False) -> Tensor:
    return Tensor(xp.zeros(shape, dtype=dtype), requires_grad=requires_grad)

def ones(shape: Union[int, List[int]], dtype: Optional[str] = None,
         requires_grad: bool = False) -> Tensor:
    return Tensor(xp.ones(shape, dtype=dtype), requires_grad=requires_grad)

def zeros_like(tensor: Tensor, requires_grad: bool = False) -> Tensor:
    return Tensor(xp.zeros_like(tensor.data, dtype=tensor.data.dtype), requires_grad=requires_grad, name=tensor.name + "_zeros_like")

def ones_like(tensor: Tensor, requires_grad: bool = False) -> Tensor:
    return Tensor(xp.ones_like(tensor.data, dtype=tensor.data.dtype), requires_grad=requires_grad, name=tensor.name + "_ones_like")

def empty(shape: Union[int, List[int]], dtype: Optional[str] = None,
          requires_grad: bool = False) -> Tensor:
    return Tensor(xp.empty(shape, dtype=dtype), requires_grad=requires_grad)

def arange(start: int, stop: int, step: int = 1, dtype: Optional[str] = None,
           requires_grad: bool = False) -> Tensor:
    return Tensor(xp.arange(start, stop, step, dtype=dtype), requires_grad=requires_grad)

def eye(n: int, dtype: Optional[str] = None,
        requires_grad: bool = False) -> Tensor:
    return Tensor(xp.eye(n, dtype=dtype), requires_grad=requires_grad)

def argmin(tensor: Tensor, axis: Optional[int] = None) -> Tensor:
    """Return indices of minimum values along an axis."""
    return tensor.argmin(axis=axis)

def argmax(tensor: Tensor, axis: Optional[int] = None) -> Tensor:
    """Return indices of maximum values along an axis."""
    return tensor.argmax(axis=axis)
