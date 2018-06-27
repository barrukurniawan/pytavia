import traceback
from   Cheetah.Template import Template

class Templating:

    def __init__(self):
        pass

    def render(self, template, data):
        html_page = ""
        try:
            html_page = Template(
                template,
                searchList = [ data ]
            ) 
            return str( html_page )
        except Exception, e:
            print "Templating.render() failed: " + str(e) 
            print traceback.format_exc()
            print template
            html_page = "<html><body align='center'>ERROR HAS OCCURED on page - "+ str(e) + "</body></html>"
            return str( html_page )
        #end try
    #end def
#end class
