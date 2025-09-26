from abc import ABC, abstractmethod
from typing import List, Tuple
import neurograd as ng
from neurograd.tensor import Tensor
from neurograd import xp
from neurograd.utils.memory import maybe_log_op_memory, start_op_timing
from neurograd.utils.no_grad import is_grad_enabled
from neurograd.amp.autocast import is_autocast_enabled
from neurograd.amp.utils import maybe_cast_tensor



class Function(ABC):
    name = None

    def __init__(self):
        self.parent_tensors: List[Tensor] = []

    def __call__(self, *inputs) -> Tensor:
        processed_inputs = []
        for i, inp in enumerate(inputs):
            if isinstance(inp, Tensor):
                processed_inputs.append(inp)
            else:
                try:
                    data = xp.asarray(inp)
                    processed_inputs.append(Tensor(data, requires_grad=False))
                except Exception as e:
                    raise TypeError(f"Input {i} must be convertible to xp array, got {type(inp)}") from e    
        # AUTOCAST if enabled
        op_name = getattr(self, 'name', None) or self.__class__.__name__
        if is_autocast_enabled():
            if op_name != 'Cast':  # Avoid recursion with Cast operations
                processed_inputs = [maybe_cast_tensor(inp, op_name=op_name) for inp in processed_inputs]
        
        # Start timing if profiling is enabled
        timing_context = start_op_timing()
        
        # Computations
        grad_on = is_grad_enabled()
        if grad_on:
            self.parent_tensors = processed_inputs
        else:
            self.parent_tensors = []
        output_data = self.forward(*[inp.data for inp in processed_inputs])
        requires_grad = any(inp.requires_grad for inp in processed_inputs) if grad_on else False
        output = Tensor(output_data, requires_grad=requires_grad, grad_fn=(self if (grad_on and requires_grad) else None))
        # Do memsave if ops has one
        parents_for_hooks = self.parent_tensors if grad_on else processed_inputs
        if hasattr(self, "_memsave") and getattr(self, "memsave", False):
            self._memsave(parents_for_hooks, output)
        # Optional per-op memory and timing logging (enabled only inside MemoryMonitor)
        maybe_log_op_memory(f"{op_name}_fwd", parents_for_hooks, output_data, timing_context)
        return output

    @abstractmethod
    def forward(self, *inputs: xp.ndarray) -> xp.ndarray:
        """
        Forward pass of the function.
        Must be implemented by subclasses.
        """
        pass

    @abstractmethod
    def backward(self, grad_output: xp.ndarray) -> Tuple[xp.ndarray, ...]:
        """
        Backward pass of the function.
        Must be implemented by subclasses.
        Returns gradients with respect to inputs.
        """
        pass

    def _handle_broadcasting(self, grad: xp.ndarray, original_shape: tuple) -> xp.ndarray:
        if grad is None:
            return None
        if grad.shape == original_shape:
            return grad
        # Left-pad original shape with 1s to align with grad.ndim
        aligned_orig = (1,) * (grad.ndim - len(original_shape)) + tuple(original_shape)
        # Axes where the original had size 1 (i.e., broadcasted) and grad expanded (>1)
        axes = tuple(i for i, (g, o) in enumerate(zip(grad.shape, aligned_orig)) if o == 1 and g != 1)
        if axes:
            # Single fused reduction over all needed axes
            grad = xp.sum(grad, axis=axes, keepdims=True, dtype=grad.dtype)
        # Final reshape to the exact original shape
        return grad.reshape(original_shape)
