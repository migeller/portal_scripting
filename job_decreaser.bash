#!/bin/bash

# MetaCode Job Decreaser, version 1.0
# Copyright (c) 2014, MetaCode, Inc. All Rights Reserved.

# Global Variables

portalserver="127.0.0.1"
portaluser="admin"
portalpass="admin"

jobnumber="6"

# PUT Call

curl -s -O /dev/null -H 'Content-Type: application/xml' -X PUT -d "<ConfigurationPropertyDocument xmlns=\"http://xml.vidispine.com/schema/vidispine\"><key>concurrentjobs</key><value>${jobnumber}</value></ConfigurationPropertyDocument>" -u ${portaluser}:${portalpass} http://${portalserver}:8080/API/configuration/properties 2>/dev/null

exit 0
