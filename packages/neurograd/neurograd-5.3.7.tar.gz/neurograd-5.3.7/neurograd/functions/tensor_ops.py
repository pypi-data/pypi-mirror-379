import neurograd as ng
from neurograd import xp
from .base import Function
from neurograd.nn.module import Module
from typing import TYPE_CHECKING, Union, Tuple, Sequence
import numpy as np
from numpy.typing import ArrayLike
if TYPE_CHECKING:
    from neurograd.tensor import Tensor



class Reshape(Function, Module):
    name = "Reshape"
    """Reshape tensor to new shape"""
    def __init__(self, new_shape):
        Function.__init__(self)
        Module.__init__(self)
        self.new_shape = new_shape
        self.original_shape = None
    def forward(self, A: xp.ndarray) -> xp.ndarray:
        self.original_shape = A.shape
        return xp.reshape(A, self.new_shape)
    def backward(self, grad_output: xp.ndarray) -> xp.ndarray:
        A = self.parent_tensors[0]
        return xp.reshape(grad_output, self.original_shape) if A.requires_grad else None
    
class Flatten(Function, Module):
    name = "Flatten"
    """Flatten tensor with flexible dims"""
    def __init__(self, start_dim: int = 1, end_dim: int = -1):
        Function.__init__(self)
        Module.__init__(self)
        self.start_dim = start_dim
        self.end_dim = end_dim
    def forward(self, A: xp.ndarray) -> xp.ndarray:
        # normalize dims
        start = self.start_dim if self.start_dim >= 0 else len(A.shape) + self.start_dim
        end   = self.end_dim   if self.end_dim   >= 0 else len(A.shape) + self.end_dim
        # flatten [start..end] into a single dim
        new_shape = (
            A.shape[:start] +
            (-1,) +
            A.shape[end + 1:]
        )
        return A.reshape(new_shape)
    def backward(self, grad_output: xp.ndarray) -> xp.ndarray:
        A = self.parent_tensors[0]
        return grad_output.reshape(A.shape) if A.requires_grad else None


class Squeeze(Function, Module):
    name = "Squeeze"
    """Remove dimensions of size 1 from tensor"""
    def __init__(self, axis=None):
        Function.__init__(self)
        Module.__init__(self)
        self.axis = axis
    def forward(self, A: xp.ndarray) -> xp.ndarray:
        return xp.squeeze(A, axis=self.axis)
    def backward(self, grad_output: xp.ndarray) -> xp.ndarray:
        A = self.parent_tensors[0]
        return grad_output.reshape(A.shape) if A.requires_grad else None


class ExpandDims(Function, Module):
    name = "ExpandDims"
    """Add new axis of size 1 at specified position"""
    def __init__(self, axis):
        Function.__init__(self)
        Module.__init__(self)
        self.axis = axis
    def forward(self, A: xp.ndarray) -> xp.ndarray:
        return xp.expand_dims(A, axis=self.axis)
    def backward(self, grad_output: xp.ndarray) -> xp.ndarray:
        A = self.parent_tensors[0]
        return xp.squeeze(grad_output, axis=self.axis) if A.requires_grad else None

class Concatenate(Function):
    name = "Concatenate"
    def __init__(self, axis):
        Function.__init__(self)
        self.axis = axis
    def forward(self, *inputs: xp.ndarray) -> xp.ndarray:
        return xp.concatenate(inputs, axis=self.axis)
    def backward(self, grad_output: xp.ndarray) -> Tuple[xp.ndarray, ...]:
        inputs = self.parent_tensors
        split_indices = [tensor.shape[self.axis] for tensor in inputs]
        split_indices = xp.cumsum(split_indices)[:-1]
        split_grad = xp.split(grad_output, indices_or_sections=split_indices, axis=self.axis)
        split_grad = [g if tensor.requires_grad else None for g, tensor in zip(split_grad, inputs)]
        return tuple(split_grad)


class Slice(Function, Module):
    """
    Differentiable slice/index operation.
    Supports basic indexing (slices, ints, None, Ellipsis) and propagates
    gradients by scattering them back into the input shape.
    """
    name = "Slice"
    def __init__(self, key):
        Function.__init__(self)
        Module.__init__(self)
        self.key = key
    def forward(self, A: xp.ndarray) -> xp.ndarray:
        return A[self.key]
    def backward(self, grad_output: xp.ndarray) -> Tuple[xp.ndarray]:
        A = self.parent_tensors[0]
        if not A.requires_grad:
            return None
        # Accumulate gradients back to the sliced positions
        grad_input = xp.zeros(A.shape, dtype=grad_output.dtype)
        grad_input[self.key] += grad_output
        return grad_input


class Cast(Function):
    name = "Cast"
    def __init__(self, target_dtype):
        super().__init__()
        self.target_dtype = target_dtype
        self.original_dtype = None
    def forward(self, input_data: xp.ndarray) -> xp.ndarray:
        self.original_dtype = input_data.dtype
        if self.original_dtype == self.target_dtype:
            return input_data
        return input_data.astype(self.target_dtype, copy=False)
    def backward(self, grad_output: xp.ndarray):
        x = self.parent_tensors[0]
        if not x.requires_grad:
            return None
        if grad_output.dtype == self.original_dtype:
            return grad_output
        return grad_output.astype(self.original_dtype, copy=False)

class Pad(Function, Module):
    name = "Pad"
    """Pad tensor with zeros or specified value (optimized for constant padding)"""
    def __init__(self, pad_width: Union[Sequence, ArrayLike, int], mode='constant', 
                 constant_values=0, memsave=False, **kwargs):
        self.pad_width_input = pad_width
        self.mode = mode
        self.constant_values = constant_values
        self.kwargs = kwargs
        self.memsave = memsave
    def forward(self, A: xp.ndarray) -> xp.ndarray:
        # Normalize pad_width
        if isinstance(self.pad_width_input, int):
            pad_width = [(self.pad_width_input, self.pad_width_input)] * A.ndim
        elif isinstance(self.pad_width_input, Sequence) and isinstance(self.pad_width_input[0], int):
            pad_width = [(p, p) for p in self.pad_width_input]
        else:
            pad_width = list(self.pad_width_input)
        self.pad_width = pad_width
        # Optimized constant zero-padding
        if self.mode == "constant" and self.constant_values == 0:
            # optimized zero-padding
            new_shape = tuple(A.shape[i] + sum(pad) for i, pad in enumerate(pad_width))
            B = xp.zeros(new_shape, dtype=A.dtype)
            slices = tuple(slice(l, l + A.shape[i]) for i, (l, _) in enumerate(pad_width))
            B[slices] = A
            return B
        else:
            # fallback to general xp.pad
            return xp.pad(A, pad_width=self.pad_width, mode=self.mode, 
                          constant_values=self.constant_values, **self.kwargs)
    def backward(self, grad_output: xp.ndarray) -> xp.ndarray:
        A = self.parent_tensors[0]
        if not A.requires_grad:
            return None
        slices = tuple(slice(l, None if u == 0 else -u) for (l, u) in self.pad_width)
        return grad_output[slices]
    def _memsave(self, parent_tensors: Sequence["Tensor"], output_tensor: "Tensor"):
        if not hasattr(self, "pad_width"):
            raise RuntimeError("pad_width not set; call forward() first.")
        del parent_tensors[0].data
        # ng.flush(gc=False)
        slices = tuple(slice(l, None if u == 0 else -u) for (l, u) in self.pad_width)
        parent_tensors[0].data = output_tensor.data[slices]



class Clone(Function, Module):
    """
    Return a copy of the input tensor that participates in autograd.
    The backward pass is identity (passes gradients through unchanged).
    """
    name = "Clone"
    def __init__(self):
        Function.__init__(self)
        Module.__init__(self)
    def forward(self, A: xp.ndarray) -> xp.ndarray:
        return A.copy() # underlying data copied
    def backward(self, grad_output: xp.ndarray) -> Tuple[xp.ndarray]:
        A = self.parent_tensors[0]
        return grad_output if A.requires_grad else None



class SlidingWindowView(Function, Module):
    """
    Smart Vectorized Sliding Window View with AutoDiff Support and
    sliding view buffer to avoid unnecessary memory allocation.
    """
    def __init__(self, window_shape: Sequence[int],
                 axes: Union[int, Tuple[int, ...]] = (2, 3),
                 strides: Union[int, Tuple[int, ...]] = (1, 1)):
        Function.__init__(self)
        Module.__init__(self)
        self.axes = axes if isinstance(axes, tuple) else (axes,)
        self.strides = strides if isinstance(strides, tuple) else \
                       tuple(strides for _ in range(len(self.axes)))
        self.window_shape = window_shape if isinstance(window_shape, tuple) else \
                           tuple(window_shape for _ in range(len(axes)))
    def forward(self, A: xp.ndarray) -> xp.ndarray:
        slices = [slice(None)] * A.ndim
        for ax, stride in zip(self.axes, self.strides):
            slices[ax] = slice(None, None, stride)
        self.slices = tuple(slices)
        return xp.lib.stride_tricks.sliding_window_view(
            A, self.window_shape, self.axes)[self.slices]
    def backward(self, grad_output: xp.ndarray) -> xp.ndarray:
        A = self.parent_tensors[0]
        if not A.requires_grad:
            return None
        grad_buffer = xp.zeros(A.shape, dtype=grad_output.dtype)
        kwargs = {"writeable": True} if xp is np else {}
        grad_view = xp.lib.stride_tricks.sliding_window_view(
            grad_buffer, self.window_shape, self.axes, **kwargs
        )[self.slices]
        # Accumulate gradients using cached view
        grad_view += grad_output
        return grad_buffer
    


def reshape(A, new_shape):
    return Reshape(new_shape)(A)
def flatten(A, start_dim: int = 1, end_dim: int = -1):
    return Flatten(start_dim, end_dim)(A)
def squeeze(A, axis=None):
    return Squeeze(axis)(A)
def expand_dims(A, axis):
    return ExpandDims(axis)(A)
def concat(tensors: Sequence["Tensor"], axis: int) -> "Tensor":
    return Concatenate(axis=axis)(*tensors)
def cast(A, target_dtype):
    return Cast(target_dtype)(A)
def pad(A, pad_width, mode='constant', constant_values=0, memsave=False, **kwargs):
    return Pad(pad_width, mode, constant_values, memsave=memsave, **kwargs)(A)
def sliding_window_view(A, window_shape: Sequence[int], axes: Union[int, Tuple[int, ...]] = (2, 3), 
                        strides: Union[int, Tuple[int, ...]] = (1, 1)):
    return SlidingWindowView(window_shape, axes, strides)(A)
def clone(A):
    return Clone()(A)


# newaxis constant for numpy-style indexing
newaxis = None
