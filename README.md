# openactuarial

One install for the full OpenActuarial ecosystem.

[![PyPI](https://img.shields.io/pypi/v/openactuarial)](https://pypi.org/project/openactuarial/)
[![Python](https://img.shields.io/pypi/pyversions/openactuarial)](https://pypi.org/project/openactuarial/)

## Overview

`openactuarial` is a meta-package: it contains no code of its own and exists
to install the seven OpenActuarial packages in one step. The ecosystem covers
general actuarial workflows — experience analysis, projection, rating and
pricing, loss modeling, tail estimation, and portfolio simulation — as small
packages that share conventions and compose across seams.

## Installation

```bash
pip install openactuarial
```

Requires Python 3.10 or newer.

`openactuarial` pins **exact versions** of every package: each release
installs the one combination that was tested together as a release train.
If you want looser version ranges, install the individual packages instead —
they declare compatible ranges (`>=X.Y,<X.Y+1`) rather than exact pins. Each package can also be installed
individually (`pip install actuarialpy`, and so on).

## What gets installed

| Package | Role |
|---|---|
| [actuarialpy](https://github.com/OpenActuarial/actuarialpy) | Calculation primitives, the canonical `Experience` data contract, and the `ExperienceSet` workbook layer (one construction call over source tables) |
| [experiencestudies](https://github.com/OpenActuarial/experiencestudies) | Experience reporting, actual-vs-expected, claimant and concentration analysis |
| [projectionmodels](https://github.com/OpenActuarial/projectionmodels) | Claim, premium, and expense projection over a renewal horizon |
| [ratingmodels](https://github.com/OpenActuarial/ratingmodels) | Manual and experience rating, credibility, indication, GLM relativities |
| [lossmodels](https://github.com/OpenActuarial/lossmodels) | Severity and frequency fitting, aggregate loss distributions; fits directly from a claims-listing `Experience` |
| [extremeloss](https://github.com/OpenActuarial/extremeloss) | Extreme-value tails: POT/GPD, GEV, return levels, splicing; fits directly from a claims-listing `Experience` |
| [risksim](https://github.com/OpenActuarial/risksim) | Portfolio Monte Carlo, dependence, reinsurance contracts, risk measures |

## Version policy

Dependencies are declared as open floors, so `pip install openactuarial`
resolves to the latest release of every package. Cross-package compatibility
is exercised nightly by the ecosystem smoke workflow, which reruns every
package's test suite against current PyPI releases. For reproducible
environments, pin the individual packages in your own requirements or
constraints file.

## Documentation

Full API references and nine end-to-end worked examples:
**[openactuarial.org](https://openactuarial.org)**.

## License

MIT — see [LICENSE](LICENSE).
