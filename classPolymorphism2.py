class Bird:
    def flight(self):
        print("Most of birds can fly.")

class sparrow(Bird):
    def flight(self):
        print("Sparrow can fly.")

obj_spr=sparrow()
obj_spr.flight()