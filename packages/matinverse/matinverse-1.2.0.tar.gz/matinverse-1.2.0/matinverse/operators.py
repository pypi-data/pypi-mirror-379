from .geometry2D import Geometry2D
from .geometry3D import Geometry3D
from .fields import Fields
import jax.numpy as jnp


def SurfaceIntegral(geometry: Geometry2D | Geometry3D, 
              data: jnp.ndarray, 
              condition) -> jnp.ndarray:
         
         inds = geometry.select_boundary(condition)

         return jnp.einsum("...s,s -> ...", data[..., inds], geometry.boundary_areas[inds])
    