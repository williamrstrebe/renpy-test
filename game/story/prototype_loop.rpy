label prototype_start:

    show screen hud
    scene expression get_location_bg() at bg_fit
    with dissolve

    jump prototype_main_loop


label prototype_main_loop:

    scene expression get_location_bg() at bg_fit
    with dissolve

    "You are at [current_location]."

    if current_location == "home":
        jump location_home_menu
    elif current_location == "school":
        jump location_school_menu
    elif current_location == "neighborhood":
        #jump location_neighborhood_menu
        call screen neighborhood_screen()
    else:
        "This place is not implemented yet."
        $ current_location = "home"
        jump prototype_main_loop
