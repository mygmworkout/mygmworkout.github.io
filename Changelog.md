# Changelog

## [Unreleased]
- Improved mobile responsiveness with stacked controls and full-width dropdowns on smaller screens.
- Implemented `localStorage` to save and restore user preferences (active exercise, sets, rest times, pace, sound settings, and voice selection) across page reloads.
- Updated main heading brand name to "GM 1".
- Removed description text and equipment specifications from the top header for a cleaner UI.
- Disabled auto-play on initial page load and when changing exercise categories.
- Added automatic progression to the next exercise in the category once all sets are completed.
- Introduced an adjustable `Ex. Rest` stepper (defaults to 60s) to manage transition time between exercises.
- Replaced the horizontal exercise chips (`.rail`) and category tabs (`.tabs`) with a streamlined dropdown menu system.
- Added a Category dropdown and an Exercise dropdown in `index.html`.
- Set the default category order to: Pilates Straps, Cable Strength, Stretch & Mobility.
- Ensured the Pilates Straps category is selected by default when loading the page.
- Adjusted CSS (`.exsel`) so both dropdowns fit side-by-side cleanly.
