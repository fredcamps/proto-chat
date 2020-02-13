"""
Url dispatching here.
"""
from .handlers import main
from .handlers import websocket

url_patterns = [
    (r'/', main.MainHandler),
    (r'/websocket/(?P<msg_type>[^\/]+)/?(?P<src>[^\/]+)/?(?P<dest>[^\/]+)?',
     websocket.WebsocketHandler),
]
