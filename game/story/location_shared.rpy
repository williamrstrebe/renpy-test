label location_try_npc_interaction:

    if player_matches_npc_location():
        menu:
            "Talk to [npc.name]":
                $ do_activity("talk", 10)
                $ npc.interact()
                "[npc.name] talks with you."
    else:
        "No one here."

    return
