import cherrypy
import pymongo
import json
import sys

from Cheetah.Template import Template

# core pytavia modules
from core import database
from core import html
from core import config
from core import pytavia
from core import templating

# stdlib , these are functions that handle standard things
from stdlib import email
from stdlib import push
from stdlib import s3aws

# custom modules
from modules import pytavia_main

class handler(pytavia.web):

    def __init__(self):
        pytavia.web.__init__(self)
    #end def

    def index(self, **kwargs):
        html_page  = pytavia_main.pytavia_main().html_process({
            "html" : self.html_pages["index.html"]
        })
        return html_page
    #end def
    index.exposed = True

    # ADD ADDITIONAL HANDLERS BELOW #

#end class

