from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import transactions.routing
import dashboard.routing


application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            transactions.routing.websocket_urlpatterns + dashboard.routing.websocket_urlpatterns
        )
    ),
})