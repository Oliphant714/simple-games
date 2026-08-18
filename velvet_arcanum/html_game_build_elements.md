# HTML Choice-and-Word Game Build Elements

This document lists the core elements needed to build a simple, story-driven HTML game focused on choices and word interactions.

## 1. Core Game Structure

- Intro screen
- Main story screen
- Choice system (buttons or links)
- Word input system (single-word or short phrase)
- Ending screen(s)
- Restart option

## 2. Essential Pages and Layout

- Single-page app layout is enough for most projects.
- Recommended sections:
  - Title and chapter/scene header
  - Story text area
  - Choice area (2-4 options)
  - Word input area
  - Feedback/result area
  - Inventory/state summary (optional)

## 3. Story Data Model

Build your story as nodes. Each node should include:

- Unique id
- Narrative text
- Optional image or mood class
- Choice options and target node ids
- Optional word challenge or prompt
- Success/fail outcomes for word checks
- Any state changes (flags, score, inventory)

## 4. State Management

Track game state in JavaScript:

- currentNodeId
- playerName (optional)
- flags (met_guard, found_key, etc.)
- inventory array
- score or reputation
- number of turns or time remaining (optional)

## 5. Choice Mechanics

- Render choices dynamically from the current node.
- Disable or hide choices when requirements are not met.
- Support conditional choices based on state flags or inventory.
- Keep choice text clear and action-oriented.

## 6. Word Mechanics

Common word-based interactions:

- Guessing a password/keyword
- Filling a missing word in a phrase
- Choosing a synonym from typed input
- Entering a command word (listen, inspect, hide)

Implementation tips:

- Normalize input with trim and lowercase.
- Accept known variants (color/colour, yes/y).
- Provide clear feedback for wrong answers.
- Allow retry rules (infinite, limited, or cost-based).

## 7. Content and Writing Requirements

- Keep scenes short (2-6 sentences).
- End each scene with a meaningful decision.
- Include consequences that are visible soon after choices.
- Use recurring characters, clues, and callbacks.
- Plan at least 3 endings:
  - Positive ending
  - Neutral ending
  - Failure ending

## 8. UI and UX Essentials

- Large readable text and high contrast
- Clear primary action buttons
- Keyboard support for input submit
- Mobile-friendly layout
- Feedback messages for every interaction
- Progress indicator (chapter, scene number, or path)

## 9. Technical Checklist

- HTML:
  - Semantic containers for story and controls
- CSS:
  - Readable typography
  - Distinct styles for choices, input, and alerts
- JavaScript:
  - Story node renderer
  - Choice click handlers
  - Word input validator
  - State updater
  - Ending router

## 10. Optional Enhancements

- Save/load with localStorage
- Typewriter text effect
- Background music and light sound effects
- Achievement system
- Gallery of discovered endings
- Accessibility options (font size controls, reduced motion)

## 11. Testing Checklist

- Every node is reachable or intentionally gated.
- No dead-end nodes without restart or ending.
- Word prompts accept intended answer variants.
- Invalid input is handled gracefully.
- Restart fully resets state.
- Mobile and desktop both work.

## 12. Suggested Folder Contents

- index.html
- styles.css
- game.js
- story-data.js
- assets/ (optional images/audio)

## 13. Minimum Viable Build (MVP)

If you want to start small, build only:

- 12-20 story nodes
- 2 word challenges
- 3 endings
- 1 persistent stat (like trust)
- Restart button

This MVP is enough to feel complete and replayable.
