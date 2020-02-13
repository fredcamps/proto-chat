"""
Main package for main handler.
"""
from .base import BaseRequestHandler


class MainHandler(BaseRequestHandler):
    """Handler for status checking"""

    def get(self):
        """GET Method"""
        self.write({"status": "Ok"})
