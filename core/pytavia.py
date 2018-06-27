import cherrypy
import json
import sys
import os

import model
import html
import config

""" Basic web framework requirements for pytavia """

class web:

    html_pages = {}

    def __init__(self):
        self.html_pages = html.html()._get_html_pages()
    #end def

    """ check that the cookie is valid """
    def _web_check_cookie(self, params):
        pass
    #end def

    """ check there is nothing bad in the input value """
    def _web_check_input(self, params):
        pass
    #end def

    """ This is how we logout """
    def logout(self):
        cherrypy.lib.sessions.expire()
        raise cherrypy.HTTPRedirect('/')
    #end if

# end class
#
# web configuration
#
appconfig = {
        '/data' : {
                'tools.staticdir.on'  : True,
                'tools.staticdir.dir' : config.G_SESSION_STORAGE
        },
        '/css' : {
                'tools.staticdir.on'  : True,
                'tools.staticdir.dir' : config.G_HOME_PATH + '/settings/static/css'
        },
        '/img' : {
                'tools.staticdir.on'  : True,
                'tools.staticdir.dir' : config.G_HOME_PATH + '/settings/static/img'
        },
        '/images' : {
                'tools.staticdir.on'  : True,
                'tools.staticdir.dir' : config.G_HOME_PATH + '/settings/static/images'
        },
        '/js' : {
                'tools.staticdir.on'  : True,
                'tools.staticdir.dir' : config.G_HOME_PATH + '/settings/static/js'
        },
        '/font' : {
                'tools.staticdir.on'  : True,
                'tools.staticdir.dir' : config.G_HOME_PATH + '/settings/static/font'
        },
        '/lib'  : {
                'tools.staticdir.on'  : True,
                'tools.staticdir.dir' : config.G_HOME_PATH + '/settings/static/lib'
        },
}
config_update = {
        'tools.sessions.on'            : True   ,
        'server.socket_timeout'        : 0      ,
        'tools.sessions.storage_type'  : 'file' ,
        'tools.sessions.storage_path'  : config.G_SESSION_STORAGE,
        'server.socket_host'           : "hostname",
        'server.socket_port'           : "port",
        'engine.autoreload.on'         : False,
        'engine.timeout_monitor.on'    : False,
        'error_page.402'               : config.G_HOME_PATH + "/settings/error/error.html",
        'error_page.404'               : config.G_HOME_PATH + "/settings/error/error.html",
        'error_page.500'               : config.G_HOME_PATH + "/settings/error/error.html",
        'error_page.501'               : config.G_HOME_PATH + "/settings/error/error.html"
}
