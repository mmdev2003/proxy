from .capture import controller as capture_controller

from .redirect.get import controller as get_redirect_controller


def include_routers(app):
    app.include_router(capture_controller.router, prefix="/api", tags=["add_domain"])

    app.include_router(get_redirect_controller.router, prefix="/api", tags=["redirect"])
