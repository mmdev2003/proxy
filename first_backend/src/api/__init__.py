from .add_domain import controller as create_link_controller
from .check_domain import controller as check_domain_controller

from .redirect.get import controller as get_redirect_controller


def include_routers(app):
    app.include_router(create_link_controller.router, prefix="/api", tags=["add_domain"])
    app.include_router(check_domain_controller.router, prefix="/api", tags=["check_domain"])

    app.include_router(get_redirect_controller.router, prefix="/api", tags=["get redirect"])
