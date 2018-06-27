#####################################################
#                                                   #
# HANDLES MONGO DATABASE FOR NOW                    #
#                                                   #
#####################################################
import time
import copy
import pymongo
import os
import sys
import config

from bson.objectid import ObjectId

#
# Define the models/collections here for the mongo db
# vincentalexander1986@gmail.com
#
db = {
    "db_user"  : {
        "_id"      : ObjectId(), 
        "name"     : "",
        "password" : ""
    }
}
