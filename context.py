class ContextLockedException(Exception):
    pass


class Context(object):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.is_lock = False

    def set(self, key, value):
        if self.is_lock:
            raise ContextLockedException(key)

        setattr(self, key, value)

    def lock(self):
        self.is_lock = True

    def unlock(self):
        self.is_lock = False