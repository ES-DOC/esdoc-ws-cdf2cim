# -*- coding: utf-8 -*-

"""
.. module:: handlers.cmip5_simulation.py.py
   :license: GPL/CeCIL
   :platform: Unix
   :synopsis: ES-DOC CDF2CIM - CMIP5 simulation publication handler.

.. module author:: Mark A. Greenslade <momipsl@ipsl.jussieu.fr>


"""
import tornado

from cdf2cim_ws.utils import io_manager
from cdf2cim_ws.utils.http import process_request



class CMIP5SimulationRequestHandler(tornado.web.RequestHandler):
    """CMIP5 simulation publication request handler.

    """
    def post(self):
        """HTTP POST handler.

        """
        def _write():
            """Writes cdf2cim content to file system.

            """
            io_manager.write(self.request.data)


        def _set_output():
            """Sets response output.

            """
            self.output = {
                "message": "CDF2CIM-WS: cdf2cim file written to file system"
            }


        # Process request.
        process_request(self, [
            _write,
            _set_output,
            ])
