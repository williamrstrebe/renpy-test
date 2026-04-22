label prototype_start:

    show screen hud
    scene expression get_location_bg() at bg_fit
    with dissolve

    jump prototype_main_loop


label prototype_main_loop:

    scene expression get_location_bg() at bg_fit
    with dissolve

    "You are at [get_location_hud_name()]."

    if current_location == "home":
        jump location_home_menu
    elif current_location == "home_kitchen":
        jump location_home_kitchen
    elif current_location == "home_bathroom":
        jump location_home_bathroom
    elif current_location == "home_bedroom":
        jump location_home_bedroom
    elif current_location == "school":
        jump location_school_menu
    elif current_location == "neighborhood":
        #jump location_neighborhood_menu
        call screen neighborhood_screen()
    else:
        "This place is not implemented yet."
        $ current_location = "home"
        jump prototype_main_loop
