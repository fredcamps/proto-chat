"""Websocket handlers tests"""
from tornado.httpclient import HTTPClientError
import tornado.gen
import tornado.httpserver
import tornado.ioloop
import tornado.testing
import tornado.websocket
from app import TornadoApplication


class TestCaseWebsocketHandler(tornado.testing.AsyncTestCase):
    '''WebsocketHandler Unit Testing'''

    def setUp(self):
        super().setUp()
        app = TornadoApplication()
        server = tornado.httpserver.HTTPServer(app)
        socket, self.port = tornado.testing.bind_unused_port()
        server.add_socket(socket)

    def tearDown(self):
        tornado.ioloop.IOLoop.instance().stop()

    def _get_connection_1(self):
        return tornado.websocket.websocket_connect(
            'ws://localhost:{}/websocket/user/cl1/cl2'.format(self.port)
        )

    def _get_connection_2(self):
        return tornado.websocket.websocket_connect(
            'ws://localhost:{}/websocket/user/cl2/cl1'.format(self.port)
        )

    def _get_connection_3(self):
        return tornado.websocket.websocket_connect(
            'ws://localhost:{}/websocket/room/cl1/room1'.format(self.port)
        )

    def _get_connection_4(self):
        return tornado.websocket.websocket_connect(
            'ws://localhost:{}/websocket/room/cl2/room1'.format(self.port)
        )

    def _get_invalid_connection(self):
        return tornado.websocket.websocket_connect(
            'ws://localhost:{}/websocket/'.format(self.port)
        )

    @tornado.testing.gen_test
    def test_websocket_should_retrieve_message_from_each_users(self):
        '''Test if websocket retrieves message from each users.'''
        client1 = yield self._get_connection_1()
        client2 = yield self._get_connection_2()
        client1.write_message("Hello client 2")
        response = yield client2.read_message()
        self.assertEqual("cl1 said Hello client 2 to cl2", response)

    @tornado.testing.gen_test
    def test_websocket_should_retrieve_message_from_each_rooms(self):
        '''Test if websocket retrieves message from each users.'''
        client1 = yield self._get_connection_3()
        client2 = yield self._get_connection_4()
        client1.write_message("Hello room1")
        response = yield client2.read_message()
        self.assertEqual("cl1 said Hello room1 to room1", response)

    @tornado.testing.gen_test
    def test_websocket_can_be_close(self):
        '''Test if websocket can be closed.'''
        client = yield self._get_connection_1()
        yield client.close()

    @tornado.testing.gen_test
    def test_websocket_should_not_connect(self):
        '''Test if websocket should not connect'''
        with self.assertRaises(HTTPClientError):
            yield self._get_invalid_connection()
