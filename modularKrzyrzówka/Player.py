class Player:
    def __init__(self, nick):
        self.nick = nick
        self.points = 0

    def addPoints(self,toAdd):
        self.points+=toAdd

    def get_nick(self):
        return self._nick

    def set_nick(self, nick):
        self._nick = nick

    def get_points(self):
        return self._points

    def set_points(self, points):
        self._points = points

    def __eq__(self, other):
        if self.nick==other:
            return True
        return False