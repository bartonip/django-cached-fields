from cached_fields.handlers import CachedFieldSignalHandler, for_class

class InvoiceSignalHandler(CachedFieldSignalHandler):
    @for_class('reverseapp.Invoice')
    def handle_calculate_total(instance):
        return instance.item.price * instance.quantity

    @for_class('reverseapp.Item')
    def handle_calculate_total_from_item(instance):
        return instance.invoices.all()