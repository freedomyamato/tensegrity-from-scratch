# Robotics and adaptive-structure study

## Question

How do command bounds, gain and a simulated measurement affect a simple feedback trace, and what additional evidence would be needed for a physical tensegrity robot?

Read the NASA SUPERball case-study record in [references](../references/README.md). It documents real tensegrity robotic hardware and sensing; our v1 lab is much simpler and does not reproduce that platform.

## Digital investigation

1. Run the default controller trace and hand-check the first two steps.
2. Use `controller_step` in a local script to compare two gains within the same command bounds.
3. Introduce a fixed simulated sensor bias, label it synthetic, and observe how the command responds.
4. Test invalid/nonfinite sensor input; the API rejects it rather than continuing with an invented reading.
5. Explain why command bounds do not establish force bounds, stability or hardware safety.

## Extension requirements

A future physical controller would need a plant model, calibrated sensors, actuator and force limits, fault handling, emergency stop and suitably qualified review. Hardware drivers and physical actuation are intentionally outside the v1 course. A six-strut robotic build is not supplied or validated here.

## Deliverable

A parameter/trace comparison, independent calculations, fault-case table and hardware-review proposal. Do not describe a mock trace as a functioning robot.
