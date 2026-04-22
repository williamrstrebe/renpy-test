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

    def time_period():
        """Morning / afternoon / night from store.time.hour (used for BG tags)."""
        h = time.hour
        if 5 <= h < 12:
            return "morning"
        if 12 <= h < 18:
            return "afternoon"
        return "night"

    def player_matches_npc_location():
        """True if the NPC and player are in the same map place (home sub-rooms count as home)."""
        pl = current_location
        nloc = npc.location
        if nloc == "home":
            return pl in (
                "home",
                "home_kitchen",
                "home_bathroom",
                "home_bedroom",
            )
        return pl == nloc

    def get_location_hud_name():
        loc = current_location
        if loc == "home":
            return "Home (front)"
        if loc == "home_kitchen":
            return "Home — kitchen"
        if loc == "home_bathroom":
            return "Home — bathroom"
        if loc == "home_bedroom":
            return "Home — bedroom"
        if loc == "school":
            return "School"
        if loc == "neighborhood":
            return "Neighborhood"
        return loc

    def get_location_bg():
        p = time_period()
        loc = current_location

        if loc == "neighborhood":
            return f"bg neighborhood {p}"
        if loc == "school":
            return f"bg school front {p}"
        if loc == "home_kitchen":
            return f"bg home kitchen {p}"
        if loc == "home_bathroom":
            return f"bg home bathroom {p}"
        if loc == "home_bedroom":
            return "bg home bedroom"
        if loc == "home":
            return f"bg home front {p}"
        return f"bg home front {p}"

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
                self.location = "neighborhood"
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
