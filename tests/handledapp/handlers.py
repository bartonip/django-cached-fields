from cached_fields.handlers import CachedFieldSignalHandler, for_class


class InvoiceSignalHandler(CachedFieldSignalHandler):

    @for_class('handledapp.Invoice')
    def handle_calculate_total(instance):
        return instance.item.price * instance.quantity

class CarrotMultipleHandler(CachedFieldSignalHandler):
    @for_class('handledapp.Carrot')
    def handle_multiplication(instance):
        return instance.value_one * instance.value_two

class CarrotAdditionHandler(CachedFieldSignalHandler):
    @for_class('handledapp.Carrot')
    def handle_addition(instance):
        return instance.value_one + instance.value_two
