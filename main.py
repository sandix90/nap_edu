from configs.config import ApplicationConfig
from context import Context
from transport.sanic.configurate import configure_sanic


if __name__ == '__main__':
    config = ApplicationConfig()
    context = Context()
    sanic = configure_sanic(config, context)

    sanic.run(host=config.sanic.host, port=config.sanic.port)
