# -*- coding: utf-8 -*-

"""
.. module:: handlers.verify_membership.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC CDF2CIM - verify GitHub team membership endpoint.

.. moduleauthor:: Mark Conway-Greenslade <momipsl@ipsl.jussieu.fr>


"""
import datetime as dt

import tornado

import cdf2cim_ws
from cdf2cim_ws.utils.http import process_request
from cdf2cim_ws.utils.http_security import authorize
from cdf2cim_ws.utils.http_security import authenticate



# Query parameter names.
_PARAM_LOGIN = 'login'
_PARAM_TOKEN = 'token'


class VerifyAuthorizationRequestHandler(tornado.web.RequestHandler):
    """Authorization request handler.

    """
    def get(self):
        """HTTP GET handler.

        """
        def _verify():
            """Verifies membership.

            """
            authorize(authenticate((
                self.get_argument(_PARAM_LOGIN),
                self.get_argument(_PARAM_TOKEN)
                )))


        def _set_output():
            """Sets response to be returned to client.

            """
            self.output = {
                "message": "ES-DOC CDF2CIM publication membership is active",
                "version": cdf2cim_ws.__version__
            }


        # Process request.
        process_request(self, [
            _verify,
            _set_output
            ])
