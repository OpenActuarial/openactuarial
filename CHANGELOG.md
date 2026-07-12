# Changelog

## 0.2.1

- README refreshed (canonical `Experience` contract, `ExperienceSet`
  workbook layer, claims-listing fitting in lossmodels/extremeloss).
- The meta-package is now a real, importable package (`openactuarial`
  exposes `__version__`) with a smoke test importing all seven pinned
  packages -- so the release gate verifies the one thing this package
  promises: the pinned ecosystem resolves and imports.

## 0.2.0

Floors raised to the canonical-`Experience` releases: `actuarialpy>=0.45`
(introduces the shared `Experience` container), `experiencestudies>=0.4`
(study functions over it), `projectionmodels>=0.7` (`project` entrypoint),
and `ratingmodels>=0.8` (`from_experience` constructors). Installing
`openactuarial` now always resolves a coherent post-migration set.

## 0.1.0

Initial release. Pure metadata: installing `openactuarial` installs the
seven ecosystem packages (`actuarialpy`, `experiencestudies`,
`projectionmodels`, `ratingmodels`, `lossmodels`, `extremeloss`,
`risksim`) at open floors. No runtime code of its own.
