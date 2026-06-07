# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed
- Swapped the order of the `.stage` (animation) and `.info` (exercise details) sections in the layout, and adjusted their CSS borders to maintain correct visual separation.
- Moved the "Print / Save PDF" button from the top navigation area to the bottom of the page, centered in its own wrapper.
- Adjusted CSS (`.exsel`) so both dropdowns fit side-by-side cleanly.
- Replaced the horizontal exercise chips (`.rail`) and category tabs (`.tabs`) with a streamlined dropdown menu system.
- Disabled auto-play on initial page load and when changing exercise categories.
- Updated main heading brand name to "GM 1".
- Improved mobile responsiveness with stacked controls and full-width dropdowns on smaller screens.

### Added
- Set the default category order to: Pilates Straps, Cable Strength, Stretch & Mobility.
- Ensured the Pilates Straps category is selected by default when loading the page.
- Added a Category dropdown and an Exercise dropdown in `index.html`.
- Introduced an adjustable `Ex. Rest` stepper (defaults to 60s) to manage transition time between exercises.
- Added automatic progression to the next exercise in the category once all sets are completed.
- Implemented `localStorage` to save and restore user preferences (active exercise, sets, rest times, pace, sound settings, and voice selection) across page reloads.

### Removed
- Removed description text and equipment specifications from the top header for a cleaner UI.
