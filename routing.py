from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from  AppRehabilitation.views  import RutinaLuxacionConsumer, RutinaLesionMediaConsumer
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator


application = ProtocolTypeRouter({
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                 path('rutina/luxacion/', RutinaLuxacionConsumer.as_asgi()),
                 path('rutina/lesion/media/', RutinaLesionMediaConsumer.as_asgi()),
            ])
        )
    ),
})
