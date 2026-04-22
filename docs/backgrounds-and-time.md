# Backgrounds and the time system — current implementation

This note records the **working** background-loading approach in `game/script.rpy`.

## What changed and why it works

Background files were found by path but not reliably drawn when switching through Python calls. The current implementation fixed that by:

1. Defining backgrounds explicitly in an `init:` block with Ren'Py `image` statements.
2. Returning a dynamic image name from Python (`get_location_bg()`).
3. Using Ren'Py script flow to display it with `scene expression ...`.
4. Applying a reusable `bg_fit` transform so backgrounds fill the configured screen.

This keeps image declaration and scene updates in standard Ren'Py behavior, avoiding mismatches between Python display calls and script-stage updates.

## Declared image tags

In `init:`:

- `image bg home front morning = "images/bg/home/front/morning.png"`
- `image bg home front afternoon = "images/bg/home/front/afternoon.png"`
- `image bg home front night = "images/bg/home/front/night.png"`
- `image bg school front morning = "images/bg/school/front/morning.png"`
- `image bg school front afternoon = "images/bg/school/front/afternoon.png"`
- `image bg school front night = "images/bg/school/front/night.png"`
- `image bg neighborhood morning = "images/bg/neighborhood/morning.png"`
- `image bg neighborhood afternoon = "images/bg/neighborhood/afternoon.png"`
- `image bg neighborhood night = "images/bg/neighborhood/night.png"`

## Time → period

`time_period()` maps `time.hour` to image suffixes:

| Period | Hours (`time.hour`) |
|--------|----------------------|
| **morning** | 5 ≤ hour < 12 |
| **afternoon** | 12 ≤ hour < 18 |
| **night** | 0–4 and 18–23 |

## Location + period selection

`get_location_bg()` builds the final image tag string from current state:

- `neighborhood` → `bg neighborhood <period>`
- `school` → `bg school front <period>`
- `home` → `bg home front <period>`

## Runtime usage

Both loop entry points update visuals with Ren'Py-native scene flow:

- `label prototype_start`: `scene expression get_location_bg() at bg_fit` + `with dissolve`
- `label prototype_main_loop`: `scene expression get_location_bg() at bg_fit` + `with dissolve`

So each loop refresh reflects both travel changes and time progression from any activity.

## Fit transform

`bg_fit` is defined in `game/systems/backgrounds.rpy`:

- `xalign 0.5`, `yalign 0.5`
- `xsize config.screen_width`, `ysize config.screen_height`

This makes each selected background fill the game viewport, which resolves mismatch between source image dimensions and the active game resolution.

## NPC schedule alignment

The playable locations are **home**, **school**, and **neighborhood**. NPC midday scheduling now uses **`neighborhood`** (not `city`) so `Look for NPC` can match actual player locations.

## Notes for future refactor

- Home already has extra sets (`home/kitchen`, `home/2nd_bathroom`) for later room-specific states.
- The file is intentionally monolithic for prototype speed; later it should be split into smaller files (`systems`, `screens`, story labels) per `renpy-skill` guidance.
