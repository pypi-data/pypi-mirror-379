"""
#####################################################################
Copyright (C) 2025 Michele Cappellari  
E-mail: michele.cappellari_at_physics.ox.ac.uk  

Updated versions of this software are available at:  
https://pypi.org/project/powerbin/  

If you use this software in published research, please acknowledge it as:  
“PowerBin method by Cappellari (2025, MNRAS submitted)”  
https://arxiv.org/abs/2509.06903  

This software is provided “as is”, without any warranty of any kind,  
express or implied.  

Permission is granted for:  
 - Non-commercial use.  
 - Modification for personal or internal use, provided that this  
   copyright notice and disclaimer remain intact and unaltered  
   at the beginning of the file.  

All other rights are reserved. Redistribution of the code, in whole or in part,  
is strictly prohibited without prior written permission from the author.  

#####################################################################

V1.0.0: PowerBin created — MC, Oxford, 10 September 2025

"""

from importlib import resources

import numpy as np
import matplotlib.pyplot as plt

from powerbin import PowerBin

#-----------------------------------------------------------------------------

"""
Usage example for the PowerBin class.

Input data
----------
Columns 1–4 of the text file sample_data_ngc2273 contain:
    x, y coordinates of each spaxel, followed by their Signal and Noise.

Capacity interface (new)
------------------------
PowerBin accepts the capacity in two equivalent forms:

1) Array-like (additive capacity):
   Provide a 1D array dens of length N, where dens[j] is the per‑pixel
   capacity. In this example we use dens = (S/N)^2, which is additive in
   the Poisson limit.

2) Callable (non-additive capacity allowed):
   Provide a function capacity(indices) -> float that returns the total
   capacity for the bin formed by the integer indices into xy. This form
   can encode non-additive effects (e.g., correlated noise).

Target
------
target_capacity is the desired value of the capacity you choose.
If you define capacity as (S/N)^2, set target_capacity = target_sn**2.
For plotting S/N, you can request a square-root scaling of the capacity.

This example lets you compare additive (array input) and non‑additive
(callable input) behaviors by toggling `covariance`.
"""

data_path = resources.files('powerbin') / 'examples/sample_data_ngc2273.txt'
x, y, signal, noise = np.loadtxt(data_path).T
xy = np.column_stack([x, y])

target_sn = 50

# --- Define Capacity Specification ---
# PowerBin can work with two types of capacity specification:
# 1. An array: For simple, additive capacities (e.g., Poisson noise), where
#    the bin capacity is the sum of pixel capacities. This is the fastest method.
# 2. A function: For complex, non-additive capacities (e.g., correlated noise),
#    where the bin capacity is a custom function of its member pixels.

# This flag toggles between the two methods for demonstration.
# Set to True for the additive array, False for the non-additive function.
additive = True

if additive:
    # ADDITIVE CASE: Use a pre-calculated array for efficiency.
    # The capacity (S/N)^2 is additive when noise is Poissonian.
    # This is the recommended approach for the additive case.
    capacity_spec = (signal / noise)**2

else:
    # NON-ADDITIVE CASE: Define a function for custom capacity logic.
    # This example models correlated noise, where S/N does not improve as
    # fast as sqrt(N_pixels). We penalize the S/N by a factor that grows
    # with the number of pixels in the bin (`len(index)`).
    def capacity_spec(index):
        """
        Calculates a non-additive S/N, penalized for bin size to model
        the effect of correlated noise. The result is squared to maintain
        the (S/N)^2 capacity definition.
        """
        # Standard S/N for the bin
        sn = np.sum(signal[index]) / np.sqrt(np.sum(noise[index]**2))
        # Apply penalty for correlated noise
        sn /= 1 + 1.07 * np.log10(len(index))
        return sn**2

pow = PowerBin(xy, capacity_spec, target_capacity=target_sn**2)

# The binning was performed on (S/N)^2, but for plotting we want S/N.
# Apply a square-root scaling to the capacity before plotting.
pow.plot(capacity_scale='sqrt', ylabel='S/N')

plt.show(block=True)
