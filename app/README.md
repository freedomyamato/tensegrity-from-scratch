# Tensegrity Learn — mobile app

**Live app:** https://tensegrity-learn-mobile.toyspredator.chatgpt.site

An installable progressive web app for Android and iPhone. All 48 course lessons, one multiple-choice knowledge check per lesson, existing teach-back questions, private notes, self-reported reviewed status and seven interactive JavaScript labs are included.

## Install and use

Open the published app link in your phone browser. On Android Chrome use Install app or Add to Home screen. On iPhone Safari use Share → Add to Home Screen; leave Open as Web App enabled if shown. Wait for **Ready offline** in Settings before expecting offline use.

The app opens your selected learning path. Continue into a lesson, try the activity, answer its knowledge check and keep relevant evidence. Marking a lesson reviewed is self-reported progress; it does not imply a verified physical experiment or qualification.

Labs run directly on the device: prism geometry, constrained twist scan, unilateral cable spring, ideal Euler column, one-DOF vibration, loaded solar-energy integration and bounded mock control. No Python or remote AI service is needed.

## Progress and privacy

Notes, quiz choices and review dates stay in this browser’s local storage. Export a JSON backup in Progress and import it on another device. Restoring a backup shows a preview and requires pressing Restore; it replaces the existing record. Clearing browser data can remove progress and cached lessons. Offline storage is subject to browser retention/eviction, so keep backups.

There is no cloud sync, learning-account backend, analytics or accredited certificate. The hosting provider may process normal request logs. The app contains English lessons and downloadable Chinese onboarding/glossary material, not full Chinese translations.

## Development and tests

UI source is in app/. Rebuild course data, icons and offline asset list with:

```bash
python3 scripts/build_mobile.py
python3 scripts/check_mobile.py
node --test tests/mobile_models.test.cjs tests/mobile_offline.test.cjs
```

For local development serve the repository with a normal static server and open its app/ directory on localhost. Production installation/offline support requires HTTPS. The service worker uses relative paths and scope, so the app can be hosted at an origin root or subdirectory.

The source is ready for static hosting. `build_mobile.py --site-dist /absolute/path/to/dist` copies the current app into a companion deployment directory. Site identity and credentials are not stored in this public teaching repository.

## Release verification and limits

JavaScript models are checked against independent closed forms, known energies and boundary cases. The offline-cache lifecycle is tested in an isolated service-worker simulation, including missing-content detection. Course data matches the authored 48 lessons exactly.

Physical-device installation, real-browser layout and mobile service-worker behavior have not been tested on an Android/iPhone during this release. The app includes browser installation support; no signed APK/IPA or app-store listing is supplied. Optional browser WebMCP navigation/progress tools are feature-detected but supported-context validation was unavailable.

Mechanical and solar labs retain the original course’s educational limitations. Mock control must not be connected to motors. A stable-looking geometry or small equilibrium residual does not certify a real structure.
