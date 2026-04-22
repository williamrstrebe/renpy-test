# Onboarding — working on this Ren’Py project

Use this checklist when you (or a tool) start work on this codebase.

## 1. Confirm environment

- **SDK:** Ren’Py **8.5.2** at `E:\renpy-8.5.2-sdk`.
- **Project path:** workspace root containing `game/` and `project.json`.

## 2. Read guidelines before editing story or architecture

1. **[`renpy-skill/main-renpy-skill.md`](../renpy-skill/main-renpy-skill.md)** — Default rules: where `default`/`define` live, label style, screens location, branching patterns.
2. Pull in a **topic skill** only when relevant:
   - UI-heavy work → `renpy-skill/renpy-screens.md`
   - Stats / progression → `renpy-skill/renpy-rpg.md`
   - Places / travel UI → `renpy-skill/renpy-maps.md`
   - Minigames → `renpy-skill/renpy-minigames.md`

## 3. Understand current code shape

- **`game/script.rpy`** is now entrypoint-only (`label start`).
- **`game/story/prototype_loop.rpy`** contains the current playable loop labels.
- **`game/systems/core_systems.rpy`** holds simulation logic/state.
- **`game/systems/backgrounds.rpy`** holds BG image declarations and the `bg_fit` transform.
- **`game/screens/hud.rpy`** defines the custom HUD screen.
- **[`docs/project-state.md`](project-state.md)** — Current architecture and navigation model (including neighborhood as a screen with hotspots).
- **[`docs/current-prototype.md`](current-prototype.md)** and **[`PROJECT.md`](../PROJECT.md)** summarize behavior and structure.

## 4. Gap between skill and current tree

The project has started the split into `story/`, `systems/`, and `screens/`, but still has room to align further with the skill:

- Add a dedicated `systems/flags.rpy` with `default` state declarations.
- Continue splitting story labels by chapter/scene.
- Keep `script.rpy` focused as an entrypoint router only.

## 5. Sanity checks after changes

- Launch the game from the launcher; confirm `label start` runs and menus work.
- If you add `default` variables, plan to consolidate into a `systems/flags.rpy`-style module when aligning with the skill.
