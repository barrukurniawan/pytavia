import sys
import os
import config

class html:

    html_dict = {}

    def __init__(self):
        pass
    #end def

    """
        Get all the newly developed html pages
    """
    def _get_html_pages(self):
        html_page_list  = os.listdir( config.G_HTML_PAGES )
        for html_page in html_page_list:
            full_path   = config.G_HTML_PAGES + "/" + html_page
            html_handle = open( full_path , 'r' )
            html_raw    = html_handle.read()
            self.html_dict[html_page] = html_raw
        #end for
        return self.html_dict
    #end def

#end class
