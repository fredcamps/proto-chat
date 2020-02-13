'''MainHandler test cases'''
import tornado.testing
from app import TornadoApplication


class TestCaseMainHandler(tornado.testing.AsyncHTTPTestCase):
    '''Test case for MainHandler'''

    def get_app(self):
        app = TornadoApplication()
        return app

    def tearDown(self):
        tornado.ioloop.IOLoop.instance().stop()

    def test_main_handler_request_should_retrieve_200_status(self):
        """Test MainHandler Request should retrieve 200 http status code."""
        response = self.fetch("/", method="GET")
        self.assertEqual(response.code, 200)
