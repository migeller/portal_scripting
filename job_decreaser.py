#!/usr/bin/env python

"""

 MetaCode Job Decreaser, version 1.0
 Copyright (c) 2014, MetaCode, Inc. All Rights Reserved.
 Call this puppy via cron when you want to decrease simultaneous jobs.

"""

__author__ = 'MetaCode, Inc.'
=__version__ = "$Revision: 1.0 $"
__date__ = "$Date: 20/05/05 21:57:19 $"
__copyright__ = "Copyright (c) 2014, MetaCode, Inc. All Rights Reserved."
__license__ = "Python"

import requests

# Global Variables
portal_server="127.0.0.1"
portal_user="admin"
portal_pass="admin"
job_number="6"
headers = {'Content-Type': 'application/xml', 'Accept': 'application/xml'}

# Derived Variables
url = "http://%s:8080/API/configuration/properties" % portal_server

response = requests.put(url, auth=(portal_user, portal_pass), headers=headers)