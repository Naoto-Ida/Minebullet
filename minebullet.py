from pushbullet import Pushbullet

class Minebullet(object):
    def __init__(self, apiKey):
        self.pb = Pushbullet(apiKey)

    def notify(self):
        with open(".players") as f:
          for i, l in enumerate(f):
              pass
        push = mb.pb.push_note("Minebullet", "Your server has " + str(i) + " players online")

if __name__ == "__main__":
    apiKey = ""
    mb = Minebullet(apiKey)
    mb.notify()
