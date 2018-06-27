#####################################################
#                                                   #
# Add all of your custom classes here .. this is    #
# just a sample display of your custom class        #
#                                                   #
#####################################################

from core import templating

class pytavia_main:

    def __init__(self):
        pass
    
    def html_process(self, params):
        html_raw  = params["html"]
        html_page = templating.Templating().render(
            html_raw,
            { "introduction" : "Hello World" }
        )
        return html_page

#end class
