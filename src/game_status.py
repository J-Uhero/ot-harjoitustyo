from status import Status

class GameStatus:
    def __init__(self):
        self._status = Status.READY
    
    def get_status(self):
        return self._status

    def set_status(self, new):
        self._status = new
