from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models.query import QuerySet

import inspect

"""
    How the decorator should work.

    Layer 1: for_class
        The for_class decorator should accept all relevant variables and plumb them down
        into the correct layers. For example, the class name should be 

"""

def what(*args, **kwargs):
    print(args, kwargs)
    print("DURK" * 3)

def for_class(class_name, signals=[pre_save], prefetch=[], *args, **kwargs):
    """
        Receivers, by default should hook into post_save of the class.
    """
    def return_function(decorated, *args, **kwargs):
        """
            Prefetch fields are passed down, so that when they are executed by run_method
            they can be handled.
        """
        def wrapper(self, *args, **kwargs): 
            def drapper(self, *args, **kwargs):
                return decorated(self, *args, **kwargs)
            self.__class__.methods[class_name] = (drapper, prefetch,)
            self.__class__.signals[class_name] = signals
            receiver(signals, sender=class_name)(self.__class__.propogate_signal)
        return wrapper

    return return_function

class CachedFieldSignalHandler(object):
    methods = {}
    signals = {}

    def __init__(self, *args, **kwargs):
        method_list = self.__dir__()
        for method in method_list:
            if method[:7] == "handle_":
                getattr(self, method)()
        super(CachedFieldSignalHandler, self).__init__(*args, **kwargs)

    @classmethod
    def propogate_signal(cls, *args, **kwargs):
        print(args, kwargs)

    def connect_receiver(self, sender, signal, callback):
        """
            This needs to redirect all signals to this class to handle the callback.
        """
        return receiver(signal=signal, sender=sender)(callback)
    @classmethod
    def run_method(cls, instance, callback):
        """
            self.run_method(instance, self.methods[sender], prefetch_related=[])
            If instance is of type QuerySet, and its elements are of type sender, apply prefetch to it.
            If instance is either list or tuple, and its elements are of type sender, just loop through it.
            If instance is of type sender, just run the method on this instance.
        """
        callback, prefetch = callback
        if isinstance(instance, QuerySet):
            instance = instance.prefetch_related(*prefetch)
            for i in instance:
                cls.execute(i, callback)
        elif isinstance(instance, (list, tuple,)):
            for i in instance:
                cls.execute(i, callback)
        else:
            cls.execute(i, callback)

    @classmethod
    def execute(cls, instance, callback):
        result = callback(instance)
        instance.set_cache_value('field_name', result)

    def provision_signals(self):
        for class_name, signal in self.signals:
            self.connect_receiver(class_name, signal, self.methods[class_name])

    def as_handler(self, *args, **kwargs):
        """
            1. Connect all signals
        """
        # cls.provision_signals()
        pass