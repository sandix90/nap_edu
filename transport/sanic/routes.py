from typing import List

from configs.config import ApplicationConfig
from transport.sanic.base import SanicEndpoint
from transport.sanic.endpoints.health import HealthEndpoint


def get_routes(config: ApplicationConfig) -> List[SanicEndpoint]:

    return [
        HealthEndpoint(config, "/health", ["GET"]),
    ]