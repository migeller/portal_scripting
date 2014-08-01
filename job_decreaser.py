#!/usr/bin/env python

"""

 MetaCode Job Decreaser, version 1.0
 Copyright (c) 2014, MetaCode, Inc. All Rights Reserved.
 Call this puppy via cron when you want to decrease simultaneous jobs.

"""

__name__ = 'job_decreaser.py'
__author__ = 'MetaCode, Inc.'
__version__ = 'Revision 1.0'
__date__ = '$Id:$'
__copyright__ = 'Copyright (c) 2014, MetaCode, Inc. All Rights Reserved.'
__license__ = 'Python'
__ide__ = 'PyCharm'

import requests

# Global Variables
portal_server="127.0.0.1"
portal_user="admin"
portal_pass="admin"
job_number="6"
headers = {'Content-Type': 'application/xml', 'Accept': 'application/xml'}

# Derived Variables
url = "http://%s:8080/API/configuration/properties" % portal_server

xml = "<ConfigurationPropertyDocument xmlns=\"http://xml.vidispine.com/schema/vidispine\"><key>concurrentjobs</key><value>%s</value></ConfigurationPropertyDocument>" % job_number

response = requests.put(url, data=xml, auth=(portal_user, portal_pass), headers=headers)

print response.content

exit()