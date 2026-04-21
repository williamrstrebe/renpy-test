# =========================================
# Minimal VN Dating Sim Systems (Ren'Py)
# Lightweight draft – no images, text only
# =========================================

# ---------- INIT ----------
init python:

    # ---- TIME SYSTEM ----
    class GameTime:
        def __init__(self):
            self.hour = 8
            self.minute = 0

        def advance(self, minutes):
            self.minute += minutes
            while self.minute >= 60:
                self.minute -= 60
                self.hour += 1
            if self.hour >= 24:
                self.hour -= 24

        def get_str(self):
            return f"{self.hour:02d}:{self.minute:02d}"

    # ---- NEEDS SYSTEM ----
    class Needs:
        def __init__(self):
            self.hunger = 100
            self.thirst = 100
            self.energy = 100

        def decay(self, minutes):
            factor = minutes / 60
            self.hunger -= 2 * factor
            self.thirst -= 3 * factor
            self.energy -= 2 * factor
            self.clamp()

        def clamp(self):
            self.hunger = max(0, min(100, self.hunger))
            self.thirst = max(0, min(100, self.thirst))
            self.energy = max(0, min(100, self.energy))

    # ---- NPC SYSTEM ----
    class NPC:
        def __init__(self, name):
            self.name = name
            self.affinity = 0
            self.stage = "unknown"
            self.location = "home"

        def update_schedule(self, hour):
            if 8 <= hour < 12:
                self.location = "school"
            elif 12 <= hour < 18:
                self.location = "city"
            else:
                self.location = "home"

        def interact(self):
            self.affinity += 1
            if self.affinity >= 5:
                self.stage = "acquaintance"

    # ---- GLOBAL STATE ----
    time = GameTime()
    needs = Needs()
    npc = NPC("Alex")

    current_location = "home"

    # ---- ACTIVITY HANDLER ----
    def do_activity(name, minutes, hunger=0, thirst=0, energy=0):
        time.advance(minutes)
        needs.decay(minutes)

        needs.hunger += hunger
        needs.thirst += thirst
        needs.energy += energy
        needs.clamp()

        npc.update_schedule(time.hour)


# ---------- UI ----------
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


# ---------- GAME LOOP ----------
label start:

    show screen hud

    jump main_loop


label main_loop:

    "You are at [current_location]."

    menu:

        "Go to School (60 min)":
            $ current_location = "school"
            $ do_activity("travel", 60)
            jump main_loop

        "Go to City (60 min)":
            $ current_location = "city"
            $ do_activity("travel", 60)
            jump main_loop

        "Stay Home (5 min)":
            $ current_location = "home"
            $ do_activity("idle", 5)
            jump main_loop

        "Eat (restore hunger)":
            if current_location == "home":
                $ do_activity("eat", 10, hunger=20)
                "You eat something."
            else:
                "No food here."
            jump main_loop

        "Drink (restore thirst)":
            $ do_activity("drink", 5, thirst=15)
            "You drink something."
            jump main_loop

        "Sleep (restore energy)":
            if current_location == "home":
                $ do_activity("sleep", 120, energy=40)
                "You take a nap."
            else:
                "You can't sleep here."
            jump main_loop

        "Look for NPC":
            if npc.location == current_location:
                menu:
                    "Talk to [npc.name]":
                        $ do_activity("talk", 10)
                        $ npc.interact()
                        "[npc.name] talks with you."
            else:
                "No one here."
            jump main_loop