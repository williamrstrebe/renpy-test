# Current prototype (`game/script.rpy`)

This document describes the **implemented** dating/simulation sketch. **Backgrounds** are shown from `game/images/bg/` based on **`current_location`** and the clock; see **[`backgrounds-and-time.md`](backgrounds-and-time.md)** for path → tag mapping and `time_period()` rules.

## Purpose

Demonstrate a **repeatable game loop**: location changes, time advance, decaying needs, one NPC whose location follows a crude schedule and who can gain **affinity**.

## Architecture

### `game/systems/core_systems.rpy` (`init python`)

| Piece | Role |
|-------|------|
| **`GameTime`** | `hour`, `minute`; `advance(minutes)` wraps past midnight; `get_str()` for HUD. |
| **`Needs`** | `hunger`, `thirst`, `energy` (0–100); `decay(minutes)` scales by time; `clamp()`. |
| **`NPC`** | Single NPC named **Alex** (the NPC’s name — not necessarily the player); `affinity`, `stage` (`unknown` → `acquaintance` at affinity ≥ 5), `location`. |
| **`update_schedule(hour)`** | 08:00–12:00 → school; 12:00–18:00 → neighborhood; otherwise home. |
| **`interact()`** | Increments affinity; updates `stage` at threshold. |
| **`time_period()`** | Maps `time.hour` to `morning` / `afternoon` / `night` for background image tags. |
| **`get_location_bg()`** | Returns the image tag string for `current_location` and `time_period()`. |
| **Globals** | `time`, `needs`, `npc`, **`current_location`** string (player-facing place). |
| **`do_activity(name, minutes, hunger=0, thirst=0, energy=0)`** | Advances clock, applies need decay, applies optional deltas, clamps needs, refreshes NPC schedule from current hour. |

### `game/systems/backgrounds.rpy` (`init`)

- Declares all currently used background image tags.
- Defines `transform bg_fit` so backgrounds are centered and sized to `config.screen_width` / `config.screen_height`.

### `game/screens/hud.rpy`

- **`screen hud()`** — Top-left frame: time, player `current_location`, three need bars as integers, NPC name, NPC location, affinity and stage.

### `game/screens/neighborhood.rpy`

- **`screen neighborhood_screen()`** — Shows `bg neighborhood [time_period()]` at `bg_fit`. **Go home:** `imagebutton` with transparent idle, hover image `hover nh home`, `Jump("location_home_menu")`. Optional **`debug_click`** to log mouse position when tuning future hotspots. The old `location_neighborhood_menu` / text-menu approach is not used for neighborhood in the current loop (see `prototype_loop.rpy`).

- **Intended pattern:** more locations can use full-screen or layered **screen + imagebutton** actions so navigation is not only `menu:` choices.

### `game/story/prototype_loop.rpy`

| Label | Behavior |
|-------|-----------|
| **`prototype_start`** | `show screen hud`, then `scene expression get_location_bg() at bg_fit` with dissolve, then `jump prototype_main_loop`. |
| **`prototype_main_loop`** | `scene expression get_location_bg() at bg_fit` with dissolve; narration line; dispatches by `current_location` — for **neighborhood** uses `call screen neighborhood_screen()` (imagebutton hotspots) instead of a `menu` label. |

### `game/story/location_home.rpy`

- Home menu options (`location_home_menu`) including **Eat**, **Drink**, and **Sleep**.

### `game/story/location_school.rpy`

- School menu options (`location_school_menu`) focused on wait/travel/NPC interaction.

### `game/story/location_shared.rpy`

- Shared label `location_try_npc_interaction` used by the **home** and **school** `menu:` labels (neighborhood is screen-based for now; add a call to this label from a button if neighborhood gains NPC interaction).

### `game/script.rpy`

- Keeps only `label start` and jumps to `prototype_start` (entrypoint-only pattern from `renpy-skill`).

### Design notes / limitations

- **`do_activity`’s first argument `name`** is unused (only timing and need deltas matter).
- **Player location vs NPC:** `current_location` is updated by menu choices; NPC location comes from **time**, not from “traveling together.” Meeting the NPC requires being in the same named place when the schedule overlaps. The NPC’s midday location is **`neighborhood`** (aligned with player place names).
- **Background loading pattern:** images are explicitly declared in `game/systems/backgrounds.rpy` and displayed with `scene expression get_location_bg() at bg_fit`; this avoided prior cases where assets were found but not rendered and ensures full-screen fit.
- **Home-only self-care actions:** Eat/Drink/Sleep are only available in `location_home_menu`.
- **Saving:** State lives in ordinary Python objects created in `init python`; verify save/load behavior if you rely on persistence for these classes (Ren’Py normally pickles `store` contents — test after structural changes).

## Relation to `renpy-skill`

For growth beyond this prototype, **`renpy-skill/main-renpy-skill.md`** recommends centralizing `default` state, moving screens to dedicated files, and splitting chapters into `story/`. See **[`docs/onboarding.md`](onboarding.md)** for migration guidance.
