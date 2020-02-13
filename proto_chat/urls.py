"""
Url dispatching here.
"""
from .handlers import main
from .handlers import web_socket

url_patterns = [
    (r'/', main.MainHandler),
    (r'/websocket/(?P<msg_type>[^\/]+)/?(?P<src>[^\/]+)/?(?P<dest>[^\/]+)?',
     web_socket.WebsocketHandler),
]
