import cherrypy
import pymongo
import json
import sys

# custom modules
import handler

# core libraries
from core import config
from core import pytavia

"""
    Main application server
        Python Framework PyTAVIA 
            ([Py]thon framework built in BA[TAVIA])
"""

if __name__ == '__main__':
    config_update = pytavia.config_update
    appconfig     = pytavia.appconfig

    if len(sys.argv) == 3:
        config_update["server.socket_host"] = sys.argv[1]
        config_update["server.socket_port"] = int(sys.argv[2])

        cherrypy.config.update( config_update )
        cherrypy.quickstart   ( handler.handler() , config=appconfig )
    else:
        print "usage: python server.py <ipaddress> <port>"
    #end if
#end if



