The PowerBin Package
====================

**PowerBin: Fast Adaptive Data Binning with Centroidal Power Diagrams**

.. image:: https://users.physics.ox.ac.uk/~cappellari/images/powerbin-logo.svg
    :target: https://users.physics.ox.ac.uk/~cappellari/software/#sec:powerbin
    :width: 100
.. image:: https://img.shields.io/pypi/v/powerbin.svg
    :target: https://pypi.org/project/powerbin/
.. image:: https://img.shields.io/badge/arXiv-2509.06903-orange.svg
    :target: https://arxiv.org/abs/2509.06903
.. image:: https://img.shields.io/badge/DOI-10.48550/arXiv.2509.06903-green.svg
    :target: https://doi.org/10.48550/arXiv.2509.06903
    
This `PowerBin` package provides a Python implementation of the **PowerBin** algorithm — a modern alternative to the classic Voronoi binning method. Like Voronoi binning, it performs 2D adaptive spatial binning to achieve a nearly constant value per bin of a chosen *capacity* (e.g., signal‑to‑noise ratio or any other user‑defined function of the bin spaxels).

**Key advances over the classic method include:**

-   **Centroidal Power Diagram:** Produces bins that are nearly round, convex, and connected, and eliminates the disconnected or nested bins that could occur with earlier approaches.

-   **Scalability:** The entire algorithm scales with **O(N log N)** complexity, removing the **O(N^2)** bottleneck previously present in both the bin-accretion and regularization steps. This makes processing million‑pixel datasets practical.

-   **Stable CPD construction:** Generates the tessellation via a heuristic inspired by packed soap bubbles, avoiding the numerical fragility of formal CPD solvers with realistic non-additive capacities (e.g., correlated noise).

The algorithm combines a fast initial bin-accretion phase with iterative regularization, and is described in detail in `Cappellari (2025) <https://arxiv.org/abs/2509.06903>`_.

.. contents:: :depth: 2

Attribution
-----------

If you use this software for your research, please cite `Cappellari (2025)`_.
The BibTeX entry for the paper is::

    @ARTICLE{Cappellari2025,
        author = {{Cappellari}, M.},
        title = "{PowerBin: Fast adaptive data binning with Centroidal Power Diagrams}",
        journal = {MNRAS},
        eprint = {2509.06903},
        year = 2025,
        note = {submitted}
    }

Installation
------------

install with::

    pip install powerbin

Without write access to the global ``site-packages`` directory, use::

    pip install --user powerbin

To upgrade ``PowerBin`` to the latest version use::

    pip install --upgrade powerbin

Usage Examples
--------------

To learn how to use the ``PowerBin`` package, copy, modify and run
the example programs in the ``powerbin/examples`` directory.
It can be found within the main ``powerbin`` package installation folder
inside `site-packages <https://stackoverflow.com/a/46071447>`_.
The detailed documentation is contained in the docstring of the file
``powerbin/powerbin.py``, or on `PyPi <https://pypi.org/project/powerbin/>`_.

Minimal example
---------------

Below is a minimal usage example you can copy into a script (or run the
provided example in ``powerbin/examples/powerbin_example.py``).

This example demonstrates the two ways to specify the bin capacity:

1.  **As an array** (if ``additive=True``): For simple, additive capacities
    (e.g., when noise is Poissonian), where the bin capacity is the sum of
    pixel capacities. This is the fastest and recommended method for this case.
2.  **As a function** (if ``additive=False``): For complex, non-additive
    capacities (e.g., to model correlated noise), where the bin capacity is a
    custom function of its member pixels.

.. code-block:: python

    from importlib import resources
    import numpy as np
    import matplotlib.pyplot as plt
    from powerbin import PowerBin

    data_path = resources.files('powerbin') / 'examples/sample_data_ngc2273.txt'
    x, y, signal, noise = np.loadtxt(data_path).T
    xy = np.column_stack([x, y])

    target_sn = 50

    # This flag toggles between the two capacity specification methods.
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

    pow = PowerBin(xy, capacity_spec, target_capacity=target_sn**2, verbose=1)

    # The binning was performed on (S/N)^2, but for plotting we want S/N.
    # Apply a square-root scaling to the capacity before plotting.
    pow.plot(capacity_scale='sqrt', ylabel='S/N')

    plt.show()

###########################################################################
