label location_try_npc_interaction:

    if npc.location == current_location:
        menu:
            "Talk to [npc.name]":
                $ do_activity("talk", 10)
                $ npc.interact()
                "[npc.name] talks with you."
    else:
        "No one here."

    return
