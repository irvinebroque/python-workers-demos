from js import Response, Ai
from hello import hello

async def fetch(request):
    name = (await request.json()).name
    return Response.new(hello(name))