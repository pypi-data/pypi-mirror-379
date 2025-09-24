.. _feature_comparison:

Feature Comparison Matrix
========================

PyDelt vs. Other Numerical Differentiation and Function Approximation Tools
--------------------------------------------------------------------------

This comparison matrix highlights the key features and capabilities of PyDelt compared to other popular tools for numerical differentiation and function approximation.

.. list-table::
   :header-rows: 1
   :widths: 20 15 15 15 15 15 15

   * - Feature
     - PyDelt
     - SciPy
     - NumDiffTools
     - FinDiff
     - JAX
     - SymPy
   * - **Differentiation Approach**
     - Interpolation-based + Autodiff
     - Numerical + Spline-based
     - Adaptive Finite Differences
     - Finite Differences
     - Automatic Differentiation
     - Symbolic Differentiation
   * - **Universal API**
     - ✓ (``.fit().differentiate()``)
     - ✗ (Different APIs)
     - ✗ (Different APIs)
     - ✓ (Unified Diff class)
     - ✓ (``jax.grad``)
     - ✓ (``sympy.diff``)
   * - **Multivariate Calculus**
     - ✓ (Gradient, Jacobian, Hessian, Laplacian)
     - Partial
     - ✓ (Gradient, Jacobian, Hessian)
     - ✓ (Partial derivatives)
     - ✓ (Full support)
     - ✓ (Full support)
   * - **Higher-order Derivatives**
     - ✓ (Any order)
     - ✓ (Limited)
     - ✓ (Any order)
     - ✓ (Any order)
     - ✓ (Any order)
     - ✓ (Any order)
   * - **Noise Robustness**
     - ✓✓✓ (Multiple methods)
     - ✓✓ (Splines)
     - ✓✓ (Richardson extrapolation)
     - ✓ (Limited)
     - ✗ (Sensitive to noise)
     - ✗ (N/A for symbolic)
   * - **Stochastic Calculus**
     - ✓ (Itô & Stratonovich)
     - ✗
     - ✗
     - ✗
     - ✗
     - ✗
   * - **Method Selection**
     - ✓✓✓ (Multiple methods)
     - ✓✓ (Limited)
     - ✓ (Limited)
     - ✓ (Limited)
     - ✓ (Forward/Reverse mode)
     - ✓ (Symbolic only)
   * - **Neural Network Integration**
     - ✓ (PyTorch & TensorFlow)
     - ✗
     - ✗
     - ✗
     - ✓ (Native)
     - ✗
   * - **Masking Support**
     - ✓
     - ✗
     - ✗
     - ✗
     - ✓
     - ✗
   * - **Callable Derivatives**
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
     - ✓
   * - **Accuracy Control**
     - ✓✓✓ (Method-specific)
     - ✓✓ (Limited)
     - ✓✓✓ (Adaptive)
     - ✓✓ (Order control)
     - ✓✓✓ (Exact)
     - ✓✓✓ (Exact)
   * - **High-dimensional Scaling**
     - ✓✓✓ (Neural networks)
     - ✓ (Limited)
     - ✓ (Limited)
     - ✓✓ (Vectorized)
     - ✓✓✓ (Optimized)
     - ✓ (Limited)
   * - **Mixed Partial Derivatives**
     - ✓ (Neural networks only)
     - ✗
     - ✓
     - ✓
     - ✓
     - ✓
   * - **PDE Solving**
     - ✗
     - ✓
     - ✗
     - ✓
     - ✓
     - ✓
   * - **Integration Methods**
     - ✓
     - ✓✓✓ (Multiple methods)
     - ✗
     - ✗
     - ✗
     - ✓
   * - **Visualization Tools**
     - ✓✓✓ (Interactive)
     - ✗
     - ✗
     - ✗
     - ✗
     - ✓

Key Differentiators
------------------

1. **Universal Differentiation Interface**: PyDelt provides a consistent ``.fit().differentiate()`` pattern across all interpolation methods, making it easy to switch between different approaches.

2. **Multiple Interpolation Methods**: PyDelt offers a wide range of interpolation techniques (LLA, GLLA, Spline, FDA, LOWESS, LOESS, Neural Networks) with a unified interface, allowing users to choose the best method for their specific data.

3. **Stochastic Calculus Support**: PyDelt is the only library that provides built-in support for stochastic calculus with Itô and Stratonovich corrections, making it ideal for financial and physical modeling of stochastic processes.

4. **Noise Robustness**: PyDelt's interpolation-based approach provides superior noise handling compared to direct finite difference methods, with LLA and GLLA methods specifically designed for noisy data.

5. **Comprehensive Multivariate Calculus**: PyDelt offers a complete suite of multivariate calculus operations (gradient, Jacobian, Hessian, Laplacian) with consistent APIs.

6. **Hybrid Approach**: PyDelt combines traditional numerical methods with automatic differentiation, offering the best of both worlds for different problem domains.

7. **Interactive Visualizations**: PyDelt provides built-in visualization tools for understanding derivative behavior and comparing different methods.

Method Selection Guide
---------------------

* **For low-dimensional, smooth data**: SciPy's spline-based methods or PyDelt's SplineInterpolator
* **For noisy data**: PyDelt's LLA/GLLA/GOLD/FDA methods or LOWESS/LOESS
* **For high-dimensional problems**: PyDelt's NeuralNetworkInterpolator or JAX
* **For stochastic processes**: PyDelt's stochastic extensions
* **For symbolic expressions**: SymPy
* **For PDE solving**: FinDiff or SciPy
* **For exact derivatives**: JAX or SymPy

References
---------

1. SciPy: https://docs.scipy.org/doc/scipy/reference/interpolate.html
2. NumDiffTools: https://github.com/pbrod/numdifftools
3. FinDiff: https://github.com/maroba/findiff
4. JAX: https://github.com/jax-ml/jax
5. SymPy: https://docs.sympy.org/latest/tutorials/intro-tutorial/calculus.html
