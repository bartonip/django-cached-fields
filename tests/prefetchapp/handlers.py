from cached_fields.handlers import CachedFieldSignalHandler, for_class

class OrderSummaryCacheHandler(CachedFieldSignalHandler):
    @for_class('prefetchapp.OrderSummary', prefetch=['services'])
    def handle_order_summary_calculation(instance):
        result = 0
        for i in instance.services.all():
            result += i.total
        return result

    @for_class('prefetchapp.Service')
    def handle_service_calculation(instance):
        return instance.order