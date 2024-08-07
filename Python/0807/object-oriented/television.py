class Television:
    def __init__(self, channel=24, volume=10, on=False):
        self.channel = channel
        self.volume = volume
        self.on = on
    
    def setOn(self):
        self.on = True

    def show(self):
        print(self.channel, self.volume, self.on)

    def setChannel(self, channel):
        self.channel = channel

    def getChannel(self):
        return self.channel
    
    def volumeUp(self):
        self.volume += 1

    def volumeDown(self):
        self.volume -= 1

def setSilentMode(t):
    t.volume = 2


tv1 = Television()
setSilentMode(tv1)
tv1.on = True
tv1.show()
tv1.setChannel(21)
tv1.show()
