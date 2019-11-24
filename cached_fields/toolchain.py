from .exceptions import CachedFieldDoesNotExist

class CachedFieldsToolchain(object):
    def __init__(self, model):
        self.model = model
        self.cache_values = {}
        setattr(self.model, '_dcf_cache_values', self.cache_values)

    def last_updated(self, field):
        if field in getattr(self.model, '_dcf_trigger_params', []):
            return getattr(self.model, '_dcf_last_update_{}'.format(field))
        raise Exception("Field is not a cached field")

    def set_cache_value(self, field, value):
        if not hasattr(self.model, field):
            raise CachedFieldDoesNotExist("'{}' is not a valid cached field on this model".format(field))
        self.cache_values[field] = value
        setattr(self.model, '_dcf_cache_values', self.cache_values)
        self.model.save()