from cached_fields.handlers import CachedFieldSignalHandler, for_class


class InvoiceSignalHandler(CachedFieldSignalHandler):

    @for_class('handledapp.Invoice')
    def handle_calculate_total(instance):
        return instance.item.price * instance.quantity

    def gherk(self):
        pass