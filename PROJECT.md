# Project overview — Ren’Py dating / simulation prototype

This repository is a **Ren’Py 8.5.2** visual novel project: a **minimal text-only prototype** combining a menu-driven loop with light simulation (time, needs, one NPC). It uses the standard launcher GUI assets under `game/gui/` and now has an initial split into `game/systems/`, `game/screens/`, and `game/story/`.

## SDK and how to run

| Item | Location / value |
|------|-------------------|
| Ren’Py SDK | `E:\renpy-8.5.2-sdk` |
| Project root | This folder (`test`) |
| Game scripts | `game/*.rpy` |

**Typical workflow:** open the Ren’Py Launcher, choose this directory as the project, then **Launch Project**. Building and translation tools expect that layout.

## Key configuration

- **`project.json`** — Build metadata (e.g. `packages: ["pc"]`, `force_recompile`).
- **`game/options.rpy`** — `config.name` / `build.name`: **test**; `config.save_directory`: **`test-1776731718`** (Windows saves under `%APPDATA%\RenPy\<save_directory>`).
- **`game/screens.rpy`** / **`game/gui.rpy`** — Generated-style GUI; unchanged from a standard template except your story does not rely on CGs yet.

## Repository layout (what matters)

```
test/
├── PROJECT.md              ← This file (start here)
├── README.md               ← Short repo blurb
├── project.json
├── docs/                   ← Extra context docs (prototype, onboarding)
├── renpy-skill/            ← Ren’Py conventions & patterns (read before major changes)
└── game/
    ├── script.rpy          ← Entry label only (`start` → `prototype_start`)
    ├── systems/
    │   ├── backgrounds.rpy ← BG image declarations + `bg_fit`
    │   └── core_systems.rpy
    ├── screens/
    │   ├── hud.rpy
    │   └── neighborhood.rpy   ← `neighborhood_screen` (imagebutton hotspots, not a menu label)
    ├── story/
    │   ├── prototype_loop.rpy
    │   ├── location_home.rpy
    │   ├── location_school.rpy
    │   └── location_shared.rpy
    ├── options.rpy
    ├── screens.rpy, gui.rpy
    ├── gui/                ← Theme images
    ├── tl/None/common.rpym ← Translation scaffold
    └── libs/libs.txt
```

The code now follows a **first-pass** split toward the `renpy-skill` target structure. Next phases can add dedicated `systems/flags.rpy`, chapter files, and more granular systems.

## Authoritative guidelines: `renpy-skill/`

Before refactoring or adding features, read the skill files (they are the project’s agreed practices):

| File | Use when |
|------|----------|
| [`renpy-skill/main-renpy-skill.md`](renpy-skill/main-renpy-skill.md) | Structure, naming, characters, flags, branching, saves, screens overview |
| [`renpy-skill/renpy-screens.md`](renpy-skill/renpy-screens.md) | Complex UI, screen language, HUDs, modals |
| [`renpy-skill/renpy-rpg.md`](renpy-skill/renpy-rpg.md) | Stats, leveling, equipment-style systems |
| [`renpy-skill/renpy-maps.md`](renpy-skill/renpy-maps.md) | World map / location navigation |
| [`renpy-skill/renpy-minigames.md`](renpy-skill/renpy-minigames.md) | Embedded minigames (state + screen + labels) |

**Note:** `main-renpy-skill.md` sometimes refers to paths like `references/renpy-rpg.md`. In this repo the equivalent files are directly under **`renpy-skill/`** with names `renpy-rpg.md`, etc.

## Related docs in `docs/`

- **[`docs/project-state.md`](docs/project-state.md)** — Snapshot of architecture, navigation (menus vs screen hotspots), file map, and extension notes for agents.
- **[`docs/current-prototype.md`](docs/current-prototype.md)** — What the prototype implements line-by-line (systems, HUD, loop).
- **[`docs/backgrounds-and-time.md`](docs/backgrounds-and-time.md)** — How BG images map to tags, `time_period()`, and NPC place alignment.
- **[`docs/onboarding.md`](docs/onboarding.md)** — Quick checklist for humans or assistants joining the project.

## Production / git

`.gitignore` excludes Ren’Py artifacts (`game/cache`, `*.rpyc`, logs, saves path under `game/saves`). Commit source `.rpy` files; let the engine regenerate cache and bytecode locally.
