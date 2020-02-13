'''
Handler for socket and protocols definitions
'''
import tornado.escape
import tornado.websocket

MESSAGE_ROOM_TYPE = 'room'
MESSAGE_USER_TYPE = 'user'


class WebsocketHandler(tornado.websocket.WebSocketHandler):
    """
    Websocket handler definition
    """
    connections = set()
    message_type = None
    src = None
    destination = None

    def open(self, msg_type, src, dest, *args, **kwargs):
        '''Open socket event,
           must be called ACL rules or priority rules here'''
        print("Opening websocket")
        self.connections.add(self)
        self.message_type = msg_type
        self.src = src
        self.destination = dest

    def _should_send_message(self, src, destination) -> bool:
        should_msg_to_room = self.message_type == MESSAGE_ROOM_TYPE and \
                self.destination == destination
        should_msg_to_user = self.message_type == MESSAGE_USER_TYPE and \
            self.destination == src

        return should_msg_to_room or should_msg_to_user

    def on_message(self, message):
        data = {"type": self.message_type,
                "src": self.src,
                "destination": self.destination,
                "message": message}
        text = u"{} said {} to {}".format(self.src,
                                          message, self.destination)
        print(data)
        for conn in self.connections:
            if self._should_send_message(conn.src, conn.destination):
                conn.write_message(text)
        self.write_message(text)

    def on_close(self):
        self.connections.remove(self)
        print("Closing websocket")
