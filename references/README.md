# Source notes and provenance

The 48-lesson prose, diagrams, templates and computational code in this package are original. They are an independent adaptation of a staged, artifact-based learning approach, not an official upstream extension. No upstream source-code files or imagery are copied into this release.

## Course architecture

[AI Engineering from Scratch](https://github.com/rohitg00/ai-engineering-from-scratch), rohitg00. The upstream README was reviewed for its phase progression, practical artifacts and evidence-oriented study loop. Our topic sequence, lesson count and workload estimates are original design choices.

## Advanced tensegrity reading

[Second-Order Rigidity and Prestress Stability for Tensegrity Frameworks](https://doi.org/10.1137/S0895480192229236), Robert Connelly and Walter Whiteley. The publisher abstract reviewed during framework preparation distinguishes rigidity and prestress stability. Full-paper results have not been independently reproduced here; this is an advanced reading pointer, not a claim that the course implements its complete tests.

## Robotics case study

[System Design and Locomotion of SUPERball, an Untethered Tensegrity Robot](https://ntrs.nasa.gov/citations/20160001750), Andrew P. Sabelhaus and collaborators, ICRA 2015, NASA NTRS record 20160001750. The record/abstract describes a constructed tensegrity robot, sensing/actuation and a locomotion example. It supports studying real robotics evidence, not equating this package’s mock controller with NASA hardware.

## Transparent mathematical derivations

[Model notes](../docs/MODEL_NOTES.md) derive the course’s geometry and analytic equilibrium independently. Standard definitions and idealizations for springs, Euler columns, one-DOF oscillators and trapezoidal integration are stated in the lab guide and code. Hypothetical material inputs and synthetic electrical readings are not inferred from the cited robotics project.

When extending the course, prefer primary papers, official technical reports and original data. Record which sections were reviewed and which results were actually implemented. Use references to support specific claims rather than attaching unrelated authority to an untested idea.

## Supplementary mechanics and CI references

[MIT OpenCourseWare: Euler–Bernoulli beams and column buckling](https://www.ocw.mit.edu/courses/2-002-mechanics-and-materials-ii-spring-2004/bc25a56b5a91ad29ca5c7419616686f7_lec2.pdf) is an independent university reading pointer for ideal column assumptions and buckling scaling; it is not a kit-material rating.

[OpenStax: Damped Harmonic Motion](https://openstax.org/books/college-physics-ap-courses/pages/16-7-damped-harmonic-motion) provides introductory reading on oscillator energy dissipation.

The CI workflow uses `actions/checkout@v6` and `actions/setup-python@v6`, checked against their tagged official READMEs: [checkout](https://github.com/actions/checkout/blob/v6/README.md) and [setup-python](https://github.com/actions/setup-python/blob/v6/README.md). The workflow is provided for future GitHub runs; no hosted CI run occurred before publication.
