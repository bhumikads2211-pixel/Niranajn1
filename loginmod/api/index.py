from loginmod.asgi import application

async def app(scope, receive, send):
    await application(scope, receive, send)
