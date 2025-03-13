from leopard import Sprite, Trigger, Costume, Sound

class Ball(Sprite):
    def __init__(self, *args):
        super().__init__(*args)

        self.costumes = [
            Costume("ball-a", "./Ball/costumes/ball-a.svg", {"x": 22, "y": 22}),
            Costume("ball-b", "./Ball/costumes/ball-b.svg", {"x": 22, "y": 22}),
            Costume("ball-c", "./Ball/costumes/ball-c.svg", {"x": 22, "y": 22}),
            Costume("ball-d", "./Ball/costumes/ball-d.svg", {"x": 22, "y": 22}),
            Costume("ball-e", "./Ball/costumes/ball-e.svg", {"x": 22, "y": 22}),
        ]

        self.sounds = [
            Sound("Boing", "./Ball/sounds/Boing.wav"),
            Sound("Pop", "./Ball/sounds/Pop.wav"),
        ]

        self.triggers = [
            Trigger(Trigger.GREEN_FLAG, self.when_green_flag_clicked),
        ]

    def when_green_flag_clicked(self):
        self.goto(-208, 15)
        self.move(100)

