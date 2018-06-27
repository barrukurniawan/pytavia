###########################################################
#                                                         #
# All application configurations go here                  #
#                                                         #
###########################################################

# This is the home path for the home of this project
G_HOME_PATH="/opt/linkertise/python/pytavia"

# This is where all the cookies are stored
G_SESSION_STORAGE=G_HOME_PATH + "/settings/storage"

# This is path we have to the HTML pages
G_HTML_PAGES=G_HOME_PATH + "/settings/template"

# This is where we have all the databases we want to connect to 
G_DATABASE_CONNECT=[
    {"dbname" : "database1", "dbstring" : "mongodb://10.0.0.26:27017/database1"},
    {"dbname" : "database2", "dbstring" : "mongodb://10.0.0.26:27017/database2"},
]

# Set the aws keys section
G_AWS_SECRET="<aws-secret>"
G_AWS_KEY="<aws-key>"
G_AWS_BUCKET="bucket-name"

# set the post mark emailer keys 
G_POSTMARK_API_SERVER_TOKEN="<postmark token>"
G_POSTMARK_API_SENDER_EMAIL="<postmark email>"
