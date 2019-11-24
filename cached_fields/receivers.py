from django.dispatch import receiver

class CacheReceiver(object):
    def __init__(self, signal, sender=None):
        self.signal = signal
        self.sender = sender
        self.callback = None

    def set_callback(self, callback):
        self.callback = callback

    def decorated_callback(self):
        return receiver(signal=self.signal, sender=self.sender)(self.callback)