
    
class character:

    def __init__(self):
        self.hp =  1000
        self.atk = 100
        self.threshold = 2
        self.xpos = 0
        self.ypos = 0
        self.delay = 0.5
        self.frames = 60


class monster: 

    def __init__(self):
        self.hp = 8000
        self.atk = 40
        self.exp = 500
        self.xpos = 0
        self.ypos = 0 
        self.respawn = 10

