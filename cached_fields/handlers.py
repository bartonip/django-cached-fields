from django.db.models.signals import post_save

def for_class(class_name, signals=[post_save], *args, **kwargs):
    """
        Receivers, by default should hook into post_save of the class.
    """
    def return_function(decorated, *args, **kwargs):
        def wrapper(self, *args, **kwargs): 
            def drapper(self, *args, **kwargs):
                    
                return decorated(self, *args, **kwargs)
            self.__class__.methods[class_name] = drapper
            for s in signals:
                self.__class__.connect_receiver(class_name, s, drapper)
        return wrapper
    return return_function

class CachedFieldSignalHandler(object):
    methods = {}
    trigger_classes = []
    
    def run_method(self, name, *args, **kwargs):
        return self.methods[name](self, *args, **kwargs)

    def as_handler(self, instance, sender, *args, **kwargs):
        try:
            func = self.methods[sender.__name__]
        except KeyError:
            raise NoHandlerError("No handler is registered for class {}".format())
        else:
            result = func(*args, **kwargs)

            if result and hasattr(self, "action"):
                return self.action(result)