# Tensegrity from Scratch

**Learn it. Build it. Measure it. Teach it.**

A teaching repository designed for Ivan’s solar-sculpture, community-learning and workforce-skills interests. Twelve phases contain **48 authored lessons**, worked examples, activities, teach-back quizzes and separate facilitator answers. Approximately **180 hours** including practice is a planning estimate. All course materials are available offline.

![Labeled three-strut prism](assets/prism.svg)

## Start in five minutes

**[Open the Android/iPhone learning app](https://tensegrity-learn-mobile.toyspredator.chatgpt.site).** See [Mobile app](docs/MOBILE_APP.md) for installation. App source, offline support and phone-based labs are in [app/](app/README.md).

1. Extract the package and open **[reader.html](reader.html)** in a browser for the searchable course reader. It needs no server, login or internet connection.
2. Read **[Getting started](docs/START_HERE.md)** or **[中文入门](docs/START_HERE_ZH.md)**.
3. Choose a route in **[Learning paths](learning-paths/README.md)**.
4. Start lesson 01 from **[Course contents](COURSE.md)**. Keep observations in your own private notebook.
5. If teaching others, use the **[Facilitator handbook](facilitator/HANDBOOK.md)** and the ready-to-run **[90-minute workshop](facilitator/WORKSHOP_90_MIN.md)**.

The early lessons need paper and a small classroom kit. Digital lessons need Python 3.10 or newer and **no third-party Python packages**. On Windows, `py -3` may replace `python3` below.

```bash
python3 -m tensegrity prism
python3 -m tensegrity solar examples/solar_readings.csv
python3 -m unittest discover -s tests -v
python3 scripts/check_repository.py
```

Run those commands from this folder, containing README.md and tensegrity/. See **[Lab guide](labs/README.md)** for all seven computational labs and expected outputs.

## What is included

| Material | Entry point |
|---|---|
| 48 lessons with objectives, worked examples, practice and quizzes | [COURSE.md](COURSE.md) |
| One worksheet per lesson | Each lesson’s `experiments/worksheet.md` |
| Twelve phase quizzes and twelve answer keys | [Assessment guide](assessments/README.md) |
| Three-strut build procedure, node schedule and printable jigs | [Build guide](builds/three-strut-prism.md) |
| Seven standard-library computational labs | [labs/README.md](labs/README.md) |
| Solar sculpture, community kit and robotics capstone briefs | [Projects](projects/README.md) |
| Accessible teaching and practical inspection activities | [Facilitator handbook](facilitator/HANDBOOK.md) |
| English/Chinese getting-started guides and glossary | [Glossary](docs/GLOSSARY.md) |
| Evidence, inspection, budget and capstone templates | [Templates](templates/README.md) |
| Local progress helper and tutor instructions | [Tutor guide](tutor/README.md) |
| Optional research branch | [Quantum Tensegrity research module](research/QUANTUM_TENSEGRITY.md) |
| Source notes, tests, CI and publishing instructions | [References](references/README.md) · [Publishing](docs/PUBLISHING.md) |

## Learning method

Observe → explain → sketch → calculate → build or simulate → measure → compare → document → teach back. Each phase requires evidence, not only correct quiz answers. Use the [rubric](assessments/RUBRIC.md) and clearly distinguish measured, calculated and synthetic data.

Your flagship project is **“One estate, one solar sculpture”** at tabletop scale, compared with a conventional frame. The project evaluates assembly, angle retention, weight and maintenance. Any claimed energy improvement requires a separate fair measurement.

## Release scope

This is a complete **version 1 teaching package**, with all 48 lesson documents and supporting activities implemented. English is the lesson language; Chinese material covers onboarding and terminology, not full lesson translations. It is not an accredited course.

The computational examples are verified against independent mathematical results and boundary cases. The physical kit, lesson timings, accessibility adaptations and learner outcomes have **not been validated in a classroom or a physical engineering test**. Educators should pilot activities and adapt them before wider delivery. Mechanical calculations are educational idealizations, not structural approval software.

Full-scale roofs, floating arrays, public sculptures and occupied structures require qualified site-specific design and review. The optional Quantum Tensegrity branch is a hypothesis-development exercise, not an established physical theory. See [Boundaries](docs/BOUNDARIES.md).

## Maintain and publish

The lesson source is `scripts/course_data.py`; generated Markdown and reader are checked into the repository so learners need not run a generator.

```bash
python3 scripts/build_course.py
python3 scripts/check_repository.py
python3 -m unittest discover -s tests -v
```

The source repository is [freedomyamato/tensegrity-from-scratch](https://github.com/freedomyamato/tensegrity-from-scratch). See [Contributing](CONTRIBUTING.md) before editing and [Publishing](docs/PUBLISHING.md) for updates or copies in another account.

## License and attribution

Original materials and code are released under the [MIT license](LICENSE). The staged, artifact-based course architecture was inspired by [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch). This is an independent tensegrity curriculum; upstream prose, code and images are not bundled. See [Source notes](references/README.md).
