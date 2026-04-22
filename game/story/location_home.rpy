label location_home_menu:
    $ current_location = "home"
    scene expression get_location_bg() at bg_fit
    with dissolve

    menu:

        "Wait 1 hour":
            $ do_activity("idle", 60)
            jump prototype_main_loop

        "Go to School (60 min)":
            $ current_location = "school"
            $ do_activity("travel", 60)
            jump prototype_main_loop

        "Go to your Neighborhood (60 min)":
            $ current_location = "neighborhood"
            $ do_activity("travel", 60)
            jump prototype_main_loop

        "Eat (restore hunger)":
            $ do_activity("eat", 10, hunger=20)
            "You eat something."
            jump prototype_main_loop

        "Drink (restore thirst)":
            $ do_activity("drink", 5, thirst=15)
            "You drink something."
            jump prototype_main_loop

        "Sleep (restore energy)":
            $ do_activity("sleep", 120, energy=40)
            "You take a nap."
            jump prototype_main_loop

        "Look for NPC":
            call location_try_npc_interaction
            jump prototype_main_loop
