# Contributing

Edit lesson content in `scripts/course_data.py`, then run `python3 scripts/build_course.py`. Do not edit generated lesson Markdown or the reader alone because a rebuild would overwrite those changes. Other handbooks/templates are maintained directly.

For every change, preserve objectives, worked example, practical steps, expected behavior, limitations, three matched quiz answers and an evidence artifact. Label hypothetical values and source technical claims. Do not invent field validation, learner outcomes, partnerships or current regulatory approvals.

Run numerical tests and `scripts/check_repository.py`. For computational changes add an independent known-result or boundary-case test. Rebuild generated files and review the diff; do not commit learner-data, outputs or identifying photographs.

Physical activity proposals need a gentle pilot and review appropriate to their tools, participants and context. Record actual physical validation separately from code verification. Improved Chinese translations should be checked for mechanics terminology and equivalent meaning.

Contributors are welcome to propose corrections through issues or pull requests after the repository is published. Include the lesson ID, problem, evidence and proposed change. Do not post private learner records.
