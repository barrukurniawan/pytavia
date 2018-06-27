#-------------------------------------------------------------------------------#
#                                                                               #
# This is where we put all of our email messages, then we can                   #
# reference what we want to use from the email module by passing the            #
# message_key                                                                   #
#                                                                               #
#-------------------------------------------------------------------------------#

message_registration   = """ PUT MESSAGE HERE """
message_confirmation   = """ PUT MESSAGE HERE """
message_password_reset = """ PUT MESSAGE HERE """
message_purchase       = """ PUT MESSAGE HERE """

# This is the message dict so we can get what we need and 
#   we can get the message_key 
message = {
    "message_registration"   : message_registration  ,
    "message_confirmation"   : message_confirmation  ,
    "message_password_reset" : message_password_reset, 
    "message_purchase"       : message_purchase
}
