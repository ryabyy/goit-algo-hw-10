**Goal:** Calculate the definite integral of a function on a specified range with various methods, one of which is to be the Monte Carlo method, compare results.

**Function integrated:**
- y = x^2

**Algorithms used:**
- _Analytical calulation_
- _SciPy quad method_
- _Monte Carlo method_

**Results:**
After performing the integral calulations analytically and with the use of the SciPy quad method, which yield the same results up to a decent amount of decimals (5+), the benchmark is set.
Calculating the integral with the Monte Carlo method leads to a similar result, obviously depending on the number of points. Having the number at 15000, which is relatively easy and quick for the modern computer, leads to integral approximations which,
during testing, normally took values differing from the benchmark in the second decimal place, sometimes in the first too. If needed and if the function is not too difficult, the precision can be easily increased by increasing the number of random points
to be drawn for the Monte Carlo method. However, it is worth mentioning that the more direct approaches are more adequate, if they are viable and attainable in an affordable amount of time (namely: analytical, if possible, and SciPy quad, etc.). In some
cases, one might want to alternatively use the numerical integral approximations - like the trapezoidal or the Simpson's methods.
