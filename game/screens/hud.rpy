screen hud():
    frame:
        xalign 0.01
        yalign 0.01
        vbox:
            text "Time: [time.get_str()]"
            text "Location: [current_location]"
            text "Hunger: [int(needs.hunger)]"
            text "Thirst: [int(needs.thirst)]"
            text "Energy: [int(needs.energy)]"
            text "NPC ([npc.name]) at: [npc.location] | Affinity: [npc.affinity] ([npc.stage])"
