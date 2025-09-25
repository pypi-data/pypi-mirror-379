from common.otlp.metrics.meter import Meter
from common.service.otlp.metric.base_metric import BaseOtlpMetricService


class OtlpMetricService(BaseOtlpMetricService):

    def get_meter(self):
        return Meter
