def for_class(class_name, *args, **kwargs):
    def return_function(decorated, *args, **kwargs):
        def wrapper(self, *args, **kwargs): 
            def drapper(self, *args, **kwargs):
                return decorated(self, *args, **kwargs)
            self.__class__.methods[class_name] = drapper
        return wrapper
    return return_function

class CachedFieldSignalHandler(object):
    methods = {}
    trigger_classes = []
    
    def run_method(self, name, *args, **kwargs):
        return self.methods[name](self, *args, **kwargs)

    def as_handler(self, instance, sender, **args, **kwargs):
        try:
            func = self.methods[sender.__name__]
        except KeyError:
            raise NoHandlerError("No handler is registered for class {}".format())
        else:
            result = func(*args, **kwargs)

            if result and hasattr(self, "action"):
                return self.action(result)