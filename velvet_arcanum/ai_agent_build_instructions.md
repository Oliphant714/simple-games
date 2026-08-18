# AI Agent Build Instructions for The Velvet Arcanum

## Purpose

Build the game as a modular, story-driven HTML game with a simple daily loop, college-based spell routes, and a mystery that is controlled mostly by story flags, variables, and content data rather than hard-coded logic.

The game should be structured so separate pieces can be developed and tested independently without creating a heavy load on the codebase or slowing runtime.

## Primary Design Rules

- Keep the core engine small.
- Put story content in data files, not in the renderer.
- Let flags, variables, and node data control most behavior.
- Use reusable systems for choices, dialogue, relationship changes, and scene resolution.
- Avoid building unique code paths for every event when a shared template can do the job.
- Separate the game into feature slices so work can happen concurrently.

## Reference Materials

Use these existing notes in the `html_game` folder as the source of truth:

- `html_game_build_elements.md`
- `magic_school_story_outline.md`

The outline already defines the school setting, the seven colleges, the two-track college structure, the mystery tone, the daily loop, the NPC ideas, the locations, and the job structure.

## Recommended Project Split

Build the game in separate parts so different pieces can be worked on in parallel.

### 1. Core Shell

Responsible for:

- Page layout
- Scene rendering area
- Buttons and input handling
- Basic navigation between game states
- Restart flow

Keep this layer generic. It should not know specific story details.

### 2. Story Data

Responsible for:

- Story nodes
- Branches
- Day progression
- Ending triggers
- College-specific content references
- Job events
- Relationship scenes

This should live in data-first structures, ideally one or more separate files.

### 3. Game State Engine

Responsible for:

- Current day
- Current time block
- Current location
- Current college
- Current track
- Energy
- Relationships
- Inventory
- Mystery flags
- Story variables

This engine should expose small functions for reading and updating state.

### 4. College Modules

Create one content module for each college:

- Civic Law
- Vital Sciences
- Computational Arts
- Built Worlds
- Thought and Ethics
- Civic Commerce
- Arts and Influence

Each college module should define:

- College identity text
- Track A and Track B descriptions
- Spell list
- College-specific event hooks
- Unique unlock conditions

### 5. NPC Modules

Create NPC content separately from core story logic.

Each NPC should define:

- Name
- College association
- Relationship score
- Relationship thresholds
- Event triggers
- Dialogue snippets
- Special flag interactions

NPC scenes should be data-driven so they can be expanded without changing the engine.

### 6. Location Modules

Each location should be its own content block or module:

- Dorm
- Classroom
- Library
- Courtyard
- Job location
- Any later unlocked locations

Each location should contain:

- Available actions by time of day
- Encounter hooks
- Story flag requirements
- College-specific variations

### 7. Job Modules

Jobs should be separate from school content so they can be added, removed, or modified without affecting the rest of the game.

Each job should include:

- Gig description
- Daily duties
- Rewards
- Relationship effects
- Event hooks
- Special perks

### 8. Mystery / Flag System

This is the most important gameplay driver.

Use:

- Story flags for major discoveries
- Boolean variables for simple yes/no conditions
- Numeric counters for repeated progress or suspicion
- Track-based variables for college-specific access
- Relationship thresholds for social gates

Examples:

- `has_seen_date_glitch`
- `library_clue_count`
- `law_track_clearance`
- `npc_trust_felix`
- `mystery_awareness`
- `temporal_anomaly_level`

This system should drive most scene variation and should be more important than hard-coded branches.

## Build Order

Use this order so the project stays manageable and can be built in parallel.

### Phase 1: Foundation

Build first:

- Game shell
- State object
- Scene renderer
- Basic choice system
- Basic text input system
- Restart logic
- A single test scene

### Phase 2: Time Loop

Add:

- Day counter
- Morning / midday / afternoon / evening time blocks
- Dorm wake-up scene
- End-of-day rest scene
- Simple action menu for each time block

### Phase 3: College Selection

Add:

- Main character setup
- Gender choice
- Name choice
- College choice
- Track choice within the selected college
- College-specific starting spells

### Phase 4: Shared World Systems

Add:

- Relationships
- Energy consumption
- Inventory or key-item tracking
- General flags and variables
- Shared class attendance template
- Shared social encounter template

### Phase 5: Content Expansion

Add each content slice independently:

- College modules
- NPC modules
- Job modules
- Location variation hooks
- Mystery clue nodes
- Endings

### Phase 6: Mystery and Endgame

Add:

- Date glitch system
- Inconsistent NPC reactions
- Hidden clue accumulation
- Secret unlock conditions
- Endgame choices

## Concurrency Plan

The work should be split so multiple parts can be built at the same time.

### Parallel Workstream A: Engine and UI

Build:

- Core shell
- State engine
- Renderer
- Choice input handling
- Basic scene transitions

### Parallel Workstream B: Story Data

Build:

- Day-by-day story structure
- Flags and variables list
- College metadata
- General event templates
- Ending conditions

### Parallel Workstream C: NPC Content

Build:

- Main NPC cast
- Relationship thresholds
- NPC-specific clue events
- Rival/friend/romance paths

### Parallel Workstream D: Locations and Jobs

Build:

- Dorm, classroom, library, courtyard, job sites
- Part-time job event tables
- Rewards and perks
- Location-based clue hooks

### Parallel Workstream E: Mystery Content

Build:

- Temporal or contradiction-based clues
- Teacher and student inconsistencies
- Secret progression chain
- Endgame revelation routes

Each workstream should rely on the shared state contract so it can be developed without rewriting the others.

## Data-First Rules

Use data and flags for almost everything.

Good examples:

- A scene appears only if a flag is set.
- A choice is unlocked if a relationship score is high enough.
- A college spell works if the player has the matching track.
- A mystery event changes based on the day counter or suspicion variable.

Avoid hard-coded one-off logic when a flag-driven template can handle it.

## Suggested Flag Categories

### Global Flags

- Main mystery discoveries
- Date anomalies
- Major story beats
- Endgame unlocks

### College Flags

- Current college
- Current track
- Track-specific spell unlocks
- College reputation milestones

### NPC Flags

- Trust
- Rivalry
- Romance interest
- Scene completion

### Location Flags

- Location unlocked
- Hidden object found
- Repeated visit marker
- Special event available

### Job Flags

- Job acquired
- Shift count
- Coworker trust
- Job perk unlocked

## Spell Design Rules

Spells should be simple and useful across multiple systems.

Each spell should define:

- Name
- College
- Track
- Cost or requirement
- Primary use
- Secondary use
- Flag interactions

Example spell behavior:

- Reveal hidden clue
- Unlock a dialogue branch
- Reduce a social penalty
- Repair an object
- Change a story variable

## Performance and Load Guidance

Keep runtime light by design.

- Load only the shared engine at start.
- Load college, NPC, location, and job content lazily or by module.
- Avoid large monolithic scene files.
- Reuse templates for common event types.
- Keep images, audio, and special effects optional and isolated.
- Prefer text and state-driven changes over complex animation or simulation.

## Minimum Viable Build

The first playable version should include:

- One college choice
- One track choice
- One dorm loop
- One class loop
- One part-time job
- Three NPCs
- A few shared flags
- One mystery clue chain
- One ending

That version should already prove the structure works before the rest of the content is added.

## Final Implementation Goal

By the time the first complete build is done, the game should behave like a modular visual novel / life simulator hybrid:

- Easy to expand
- Easy to debug
- Easy to run
- Easy to branch by flags
- Easy to add new college content without touching the core engine

If a choice, event, or consequence can be expressed as data, it should be.
