# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2026-06-07

### Changed
- Sped up the voice rate for the "3-2-1 Go" countdowns and explicitly linked the exercise start (`beginCounting`) to the speech synthesizer's `onend` event to completely eliminate audio overlap.
- Delayed the start of the visible Set Rest and Ex. Rest countdown timers (and circular SVG animations) until the voice has fully finished speaking the set completion and rest duration phrases.
- Explicitly synchronized the final 3-2-1 visual countdown numbers during rest periods to wait for the speech synthesizer's `onend` event, ensuring the text never ticks down faster than the voice can speak them.
- Replaced the awkward "0" in the rep counter at the beginning of exercises with "Ready" (when idle) and "Go" (when actively starting) for a more intuitive workout flow.
- Replaced the single-color stick figure with a highly stylized, colored 2D anatomical character (featuring a face profile, chest, skin tones, t-shirt, shorts, sneakers, and hair) that perfectly integrates with the existing procedural animation engine.
- Implemented a dynamic normal-vector mathematical solver to automatically flip the face, hair, and anatomy directions on exercises where the character is facing away from the machine (e.g. Standing Punch) or lying face-down (e.g. Breaststroke).
- Removed the "Pilates on the GM1 — the Free Lift workaround" informational section from the bottom of the page.
- Heavily prioritized standard and modern premium US voices (including Zira, Mark, David, Aria, Jenny, Guy, Ana, Christopher, Eric, Michelle, Roger, Steffan, Alex, Susan, Tom, Nathan, Matthew, Salli, Justin, Kendra, Joey, and Ivy) so they float to the top of the dropdown list, while completely blocking/removing all Apple novelty joke voices (e.g. Boing, Bubbles, Wobble) from the UI entirely.
- Aggressively compressed and optimized the mobile layout (`< 600px`) by reducing padding, margins, font sizes, and control button scales to ensure the entire interface fits entirely on a mobile phone screen without vertical scrolling. Also placed the category and exercise dropdowns side-by-side on mobile.
- Flawlessly synced the visual exercise steps (`<ol class="steps">`) to dynamically highlight exactly as the voice reads each step aloud during the intro phase.
- Dynamically collapse the exercise info (`.info`), pacebar, and setbar during active sets *and* rest periods to maintain a clean focus purely on the workout animation. They restore only when previewing or done.
- Perfectly synchronized the spoken voice counts with the on-screen character animation by dynamically driving the counts directly from the animation frame loop.
- Refined the `.setbar` and `.pacebar` controls (Sets, Set Rest, Ex. Rest, Voice, and Pace) globally to be more compact by tightening gaps, padding, and font sizes.
- Heavily compressed and optimized the mobile layout to fit all exercise info (controls, steps, load, setup, and animation) on a single screen without scrolling. This includes converting the `setup` info to a 3-column row and reshaping the `setbar` into a compact 2x2 grid.
- Swapped the order of the `.stage` (animation) and `.info` (exercise details) sections in the layout, and adjusted their CSS borders to maintain correct visual separation.
- Moved the "Print / Save PDF" button from the top navigation area to the bottom of the page, centered in its own wrapper.
- Adjusted CSS (`.exsel`) so both dropdowns fit side-by-side cleanly.
- Moved the global `.controls`, `.pacebar`, and `.setbar` to the very top of the exercise card (above the info section) for easier access.
- Replaced the horizontal exercise chips (`.rail`) and category tabs (`.tabs`) with a streamlined dropdown menu system.
- Disabled auto-play on initial page load and when changing exercise categories.
- Updated main heading brand name to "GM 1".
- Improved mobile responsiveness with stacked controls and full-width dropdowns on smaller screens.

### Added
- Created a cool spinner animation for initial page load.
- Implemented a circular SVG progress ring countdown for the Set Rest and Ex. Rest phases.
- Added auto-advancing logic to seamlessly progress to the next category of exercises when one is completed.
- Set the default category order to: Pilates Straps, Cable Strength, Stretch & Mobility.
- Ensured the Pilates Straps category is selected by default when loading the page.
- Added a Category dropdown and an Exercise dropdown in `index.html`.
- Introduced an adjustable `Ex. Rest` stepper (defaults to 60s) to manage transition time between exercises.
- Added automatic progression to the next exercise in the category once all sets are completed.
- Implemented `localStorage` to save and restore user preferences (active exercise, sets, rest times, pace, sound settings, and voice selection) across page reloads.

### Removed
- Removed the general fitness guidance and instructions text from the page footer to further streamline the layout.
- Removed description text and equipment specifications from the top header for a cleaner UI.
