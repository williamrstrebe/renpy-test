label location_school_menu:

    menu:

        "Wait 1 hour":
            $ do_activity("idle", 60)
            jump prototype_main_loop

        "Go Home (60 min)":
            $ current_location = "home"
            $ do_activity("travel", 60)
            jump prototype_main_loop

        "Go to your Neighborhood (60 min)":
            $ current_location = "neighborhood"
            $ do_activity("travel", 60)
            jump prototype_main_loop

        "Look for NPC":
            call location_try_npc_interaction
            jump prototype_main_loop
