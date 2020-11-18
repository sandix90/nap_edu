from sanic import Sanic, Blueprint

from configs.config import ApplicationConfig
from context import Context
from .routes import get_routes
from hooks import init_sqlite_db


def configure_sanic(config: ApplicationConfig, context: Context) -> Sanic:
    init_sqlite_db(context, config)

    app = Sanic(__name__)

    bp = Blueprint(config.sanic.blueprint, url_prefix=config.sanic.blueprint)

    [bp.add_route(
        route,
        methods=route.methods,
        uri=route.uri,
        strict_slashes=True,
        name=route.__name__

    ) for route in get_routes(config, context)]

    app.blueprint(bp)

    return app
