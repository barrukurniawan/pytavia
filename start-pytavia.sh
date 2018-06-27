#/bin/bash
#
# Start the pytavia service here ...
#
# TODO:
#	- create a single logger location
#	- create a script that can download all dependcies or install pip
#	- create sample apps that use each and every part of the framework
#		* templating
#		* database access
#		* email, s3, push notifications 	
#
python server.py 10.0.0.5 8000
