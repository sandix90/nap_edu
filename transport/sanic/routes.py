from typing import List

from configs.config import ApplicationConfig
from context import Context
from transport.sanic.base import SanicEndpoint
from transport.sanic import endpoints


def get_routes(config: ApplicationConfig, context: Context) -> List[SanicEndpoint]:
    params = [
        config,
        context
    ]

    return [
        endpoints.HealthEndpoint(config, context, "/health", ["GET"]),
        endpoints.GetEmployeeEndpoint(config, context, "/employee/<eid:int>", {"GET"}),
        endpoints.CreateEmployeeEndpoint(config, context, "/employee", {"POST"}),

    ]