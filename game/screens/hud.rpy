## L toggles visibility (init python below); no other L binding in this project.
default hud_shown = True

screen hud():
    if hud_shown:
        frame:
            xalign 0.01
            yalign 0.01
            vbox:
                text "Time: [time.get_str()]"
                text "Location: [get_location_hud_name()]"
                text "Hunger: [int(needs.hunger)]"
                text "Thirst: [int(needs.thirst)]"
                text "Energy: [int(needs.energy)]"
                text "NPC ([npc.name]) at: [npc.location] | Affinity: [npc.affinity] ([npc.stage])"

init 999 python:
    config.keymap["toggle_debug_hud"] = [ "K_l" ]

    def _toggle_debug_hud():
        store.hud_shown = not store.hud_shown
        renpy.restart_interaction()

    config.underlay.insert(0, renpy.Keymap(toggle_debug_hud=_toggle_debug_hud))
