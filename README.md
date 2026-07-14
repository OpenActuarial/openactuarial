# OpenActuarial

[![PyPI](https://img.shields.io/pypi/v/openactuarial)](https://pypi.org/project/openactuarial/)
[![Python](https://img.shields.io/pypi/pyversions/openactuarial)](https://pypi.org/project/openactuarial/)

A dependency-light Python ecosystem for general actuarial work — from experience
analysis and projection through rating, reserving, and loss modeling to tail
estimation and portfolio capital.

Small, composable packages that take and return plain pandas and numpy, share one
set of conventions — tidy tables, explicit distribution parameterizations,
reproducible randomness — and build on a common primitives layer, `actuarialpy`,
rather than a framework you have to buy into.

| Package | Role |
|---|---|
| [actuarialpy](https://github.com/OpenActuarial/actuarialpy) | Calculation primitives, the canonical `Experience` data contract, and the `ExperienceSet` workbook layer (one construction call over source tables) |
| [experiencestudies](https://github.com/OpenActuarial/experiencestudies) | Experience reporting, actual-vs-expected, claimant and concentration analysis |
| [projectionmodels](https://github.com/OpenActuarial/projectionmodels) | Claim, premium, and expense projection over a renewal horizon |
| [ratingmodels](https://github.com/OpenActuarial/ratingmodels) | Manual and experience rating, credibility, indication, GLM relativities |
| [reservingmodels](https://github.com/OpenActuarial/reservingmodels) | Claims development and stochastic reserving: chain ladder, Bornhuetter-Ferguson, Mack, and the ODP bootstrap of the predictive reserve distribution; builds triangles from a claims-listing `Experience` |
| [lossmodels](https://github.com/OpenActuarial/lossmodels) | Severity and frequency fitting, aggregate loss distributions; fits directly from a claims-listing `Experience` |
| [extremeloss](https://github.com/OpenActuarial/extremeloss) | Extreme-value tails: POT/GPD, GEV, return levels, splicing; fits directly from a claims-listing `Experience` |
| [risksim](https://github.com/OpenActuarial/risksim) | Portfolio Monte Carlo, dependence, reinsurance contracts, risk measures |

## Install

```bash
pip install openactuarial     # all eight packages, one tested set
pip install actuarialpy       # - or any package on its own
```

`openactuarial` is a meta-package with no code of its own: it pins the **exact
versions** of all eight packages that were tested together as a release train, so
a single command installs a known-good combination, and each release bumps those
pins to the next tested train. Prefer looser ranges? Install the packages
individually — each declares its own compatible range (`>=X.Y,<X.Y+1`). Requires
Python 3.10+.

## Docs & examples

Full API reference and worked examples that run end to end:
**[openactuarial.org](https://openactuarial.org)**. Every package's test suite
reruns nightly against the current PyPI releases (the [ecosystem
smoke](https://github.com/OpenActuarial/docs/actions/workflows/ecosystem-smoke.yml)),
so cross-package drift surfaces within a day.

## License

MIT — see [LICENSE](LICENSE).
