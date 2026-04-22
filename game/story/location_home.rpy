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

        "Go to the kitchen":
            $ current_location = "home_kitchen"
            jump prototype_main_loop

        "Go to the bathroom":
            $ current_location = "home_bathroom"
            jump prototype_main_loop

        "Go to the bedroom":
            $ current_location = "home_bedroom"
            jump prototype_main_loop

        "Look for NPC":
            call location_try_npc_interaction
            jump prototype_main_loop


label location_home_kitchen:
    $ current_location = "home_kitchen"
    scene expression get_location_bg() at bg_fit
    with dissolve

    menu:

        "Eat (restore hunger)":
            $ do_activity("eat", 10, hunger=20)
            "You eat something."
            jump prototype_main_loop

        "Drink (restore thirst)":
            $ do_activity("drink", 5, thirst=15)
            "You drink something."
            jump prototype_main_loop

        "Wait 1 hour":
            $ do_activity("idle", 60)
            jump prototype_main_loop

        "Return to the front of the house":
            $ current_location = "home"
            jump prototype_main_loop

        "Look for NPC":
            call location_try_npc_interaction
            jump prototype_main_loop


label location_home_bathroom:
    $ current_location = "home_bathroom"
    scene expression get_location_bg() at bg_fit
    with dissolve

    menu:

        "Wait 1 hour":
            $ do_activity("idle", 60)
            jump prototype_main_loop

        "Return to the front of the house":
            $ current_location = "home"
            jump prototype_main_loop

        "Look for NPC":
            call location_try_npc_interaction
            jump prototype_main_loop


label location_home_bedroom:
    $ current_location = "home_bedroom"
    scene expression get_location_bg() at bg_fit
    with dissolve

    menu:

        "Sleep (restore energy)":
            $ do_activity("sleep", 120, energy=40)
            "You get some rest."
            jump prototype_main_loop

        "Wait 1 hour":
            $ do_activity("idle", 60)
            jump prototype_main_loop

        "Return to the front of the house":
            $ current_location = "home"
            jump prototype_main_loop

        "Look for NPC":
            call location_try_npc_interaction
            jump prototype_main_loop
