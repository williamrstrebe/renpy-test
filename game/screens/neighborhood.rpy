screen debug_click():
    key "mouseup_1" action Function(renpy.notify, str(renpy.get_mouse_pos()))

screen neighborhood_screen():
    add "bg neighborhood [time_period()]" at bg_fit

    imagebutton:
        idle Solid("#0000")
        hover Transform("hover nh home", fit="contain")
        xpos 1330
        ypos 430
        xsize 250
        ysize 160
        tooltip "Your Home"
        action Jump("location_home_menu")

#label location_neighborhood_menu:

 #   show screen debug_click
