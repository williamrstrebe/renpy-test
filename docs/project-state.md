# Project state (living snapshot)

**Audience:** future contributors and assistants. **Scope:** what exists today, how pieces connect, and conventions to extend without breaking flow.

**Related:** [`PROJECT.md`](../PROJECT.md) (layout and skills), [`current-prototype.md`](current-prototype.md) (line-by-line behavior), [`backgrounds-and-time.md`](backgrounds-and-time.md) (BG tags and time).

---

## What this is

Ren’Py **8.5.2** visual novel prototype: **menu-driven location loop** plus light simulation (time, needs, one NPC, affinity), with backgrounds keyed by **place** and **time of day**. Entry is `label start` → `prototype_start` in [`game/story/prototype_loop.rpy`](../game/story/prototype_loop.rpy). [`game/script.rpy`](../game/script.rpy) only jumps to the story; no logic there.

---

## Authoritative project practices

- **`renpy-skill/`** — Agreed structure, Ren’Py patterns, when to use screens vs labels. Read [`main-renpy-skill.md`](../renpy-skill/main-renpy-skill.md) before large refactors.
- **Saves / state** — `time`, `needs`, `npc`, `current_location` are created in `init python` in [`game/systems/core_systems.rpy`](../game/systems/core_systems.rpy). Treat save/load as something to re-test after structural changes (pickle of store objects).

---

## Simulation (Python, `init python`)

| Concept | Where | Notes |
|--------|--------|--------|
| **Clock** | `GameTime` | `hour`/`minute`, `advance(minutes)` wraps; `get_str()` for HUD. |
| **Needs** | `Needs` | `hunger`, `thirst`, `energy` 0–100; `decay` + `clamp`. |
| **NPC** | `NPC("Alex")` | `affinity`, `stage` (e.g. `acquaintance` at ≥5), `location` from schedule. |
| **Schedule** | `update_schedule(hour)` | 08:00–12:00 school; 12:00–18:00 neighborhood; else home. |
| **Player place** | `current_location` | String: `home`, `school`, `neighborhood` (and room for more). |
| **Activities** | `do_activity(name, minutes, hunger=, thirst=, energy=)` | Advances time, decays needs, optional deltas, updates NPC hour-based location. The `name` argument is not used for logic today. |
| **BG tag helper** | `get_location_bg()` + `time_period()` | `time_period()` → `morning` / `afternoon` / `night` for image suffixes. |

---

## Visuals and assets

- **Declared images** in [`game/systems/backgrounds.rpy`](../game/systems/backgrounds.rpy): `image bg …` for home front, school front, neighborhood; **`image hover nh home`** for the neighborhood “go home” hover overlay; **`transform bg_fit`** fills `config.screen_width` × `config.screen_height`.
- **On-disk art** under `game/images/bg/…` and `game/images/hover/…` (e.g. neighborhood time variants, `neighborhood_home.png` for hover).
- **Extra BG folders** (e.g. `home/kitchen`, `home/2nd_bathroom`) exist for future room-specific views; not wired into `get_location_bg()` yet.

---

## Story flow and navigation

1. **`prototype_start`** — `show screen hud`, `scene expression get_location_bg() at bg_fit` with dissolve, `jump prototype_main_loop`.
2. **`prototype_main_loop`** — Refreshes scene, one narration line, then branches on `current_location`.

| Location | Mechanism | Exit pattern |
|----------|-----------|--------------|
| **home** | `jump location_home_menu` | Ren’Py `menu:` (travel, wait, eat/drink/sleep, NPC). |
| **school** | `jump location_school_menu` | Same style `menu:`. |
| **neighborhood** | `call screen neighborhood_screen()` | **Not** a `menu` label. Screen shows BG + **imagebutton** hot spots; e.g. “home” uses invisible idle + hover image, `action Jump("location_home_menu")`. |

**Design intent (2026):** add more **on-screen interactive regions** (imagebuttons with positioned hovers) so the player is not limited to text menus. Neighborhood is the first instance; the commented **`debug_click`** screen in the same file can be re-enabled to print mouse coordinates while tuning new buttons.

**Shared NPC flow** — [`game/story/location_shared.rpy`](../game/story/location_shared.rpy) `location_try_npc_interaction`: if `npc.location == current_location`, optional talk; else “No one here.”

---

## Screens

| Screen | File | Role |
|--------|------|------|
| **`hud()`** | [`game/screens/hud.rpy`](../game/screens/hud.rpy) | Time, `current_location`, need integers, NPC line (location, affinity, stage). |
| **`neighborhood_screen()`** | [`game/screens/neighborhood.rpy`](../game/screens/neighborhood.rpy) | Full-screen neighborhood BG; **go home** hotspot (invisible `Solid` idle, `hover nh home` on hover) → `location_home_menu`. |
| **`debug_click()`** | same file | Optional: click-to-log mouse position (for placing future buttons). |

---

## Configuration worth knowing

- [`game/options.rpy`](../game/options.rpy) — `config.name` / build name, `config.save_directory`, etc. (see `PROJECT.md`).

---

## Intentional limitations (do not “fix” by surprise)

- Player location is updated by **menus / screen actions**; NPC location is **time-based**. Same-place meetings require schedule overlap, not travel together.
- Home-only self-care: Eat / Drink / Sleep only in `location_home_menu`.
- Neighborhood no longer uses a `location_neighborhood_menu` **menu** label; old `jump` to that is commented in favor of the screen. Extend neighborhood by adding **more `imagebutton` blocks** (or a data-driven loop) in `neighborhood_screen` or a follow-on screen.

---

## Repository layout (accurate to story/screens split)

- `game/story/` — `prototype_loop.rpy`, `location_home.rpy`, `location_school.rpy`, `location_shared.rpy` (neighborhood flow is not a story menu label; UI lives in `game/screens/neighborhood.rpy`).
- `game/screens/` — `hud.rpy`, `neighborhood.rpy`.
- `game/systems/` — `core_systems.rpy`, `backgrounds.rpy`.

When this document drifts, prefer updating the **file list** and the **neighborhood** row in the navigation table first.
