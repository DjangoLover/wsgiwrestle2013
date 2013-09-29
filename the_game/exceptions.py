class GameFullError(ValueError):
    def __init__(self, *args, **kwargs):
        super(GameFullError, self).__init__(*args, **kwargs)
