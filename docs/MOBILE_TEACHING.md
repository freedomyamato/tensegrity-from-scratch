# Mobile teaching integration v2.1

Open the existing app and select **Teach**, or open any lesson and choose **Open teaching assistant**.

- **Lesson plan:** choose one of 48 source lessons and 30, 45, 60 or 90 minutes; export the preparation and timed plan.
- **Build coach:** follow the supported three-strut tabletop pilot one step at a time; record observations locally.
- **Quiz:** five bilingual foundation checks plus the selected authored English course check; explanations appear after answering.
- **Learner review:** enter an anonymous label, observed evidence, four optional ratings and support used. Missing dimensions stay unobserved and do not enter the average.
- **Adapt a lesson:** choose quiet surroundings, large task cards or an observation alternative.
- **Experiment plan:** prepare a controlled joint-drift comparison and download a brief.

Use the assistant language selector for English/Chinese controls, task cards and foundation checks. The existing 48-lesson source content remains English. Assistant backup is separate from the existing course-progress backup; export both if needed. Records stay in this browser and are not synchronized between devices.

## AI conversation status
This release includes a **Copy lesson context** button and an **Open ChatGPT** link. Copy and paste the context for a custom AI conversation. The app itself uses authored offline workflows, not generated chat replies. In-app generative chat remains blocked on API setup; no secret is embedded in client JavaScript and no unconfigured endpoint is represented as working. OpenAI Developers must be enabled for the supported API-key setup flow, with the owner's approval before account/billing configuration.

## Checks and limits
Run `node tests/assistant.test.cjs` from the source root. Checks exercise the six views, contextual routing, timing, language switch, delayed quiz feedback, coaching persistence, sparse review averages, escaped user text, backup validation and precache coverage. Existing course storage uses the same key and schema. A changed service worker prompts an existing controlled app to reload once when its new cache is active.

The local browser runtime lacked a Chromium binary; visual phone-size checks and actual iPhone/Android testing were not completed. Offline asset inclusion was checked, but a real service-worker install/reload should be tested on a device. Install through Safari Add to Home Screen or Chrome Install app; this remains a PWA, not a native store release.
