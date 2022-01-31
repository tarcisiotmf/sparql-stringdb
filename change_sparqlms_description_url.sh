#!/bin/bash

#Set up the sparql micro-service server in the ShapeGraph and ServiceDescription .ttl files
#SPARQL-MS server
SPARQL_MS_SERVER="http:\/\/localhost" 
# Root path of the deployed services as SPARQL micro-services 
SMSPATH=./services

#MacOS - comment the line below if you are using Linux-based OS instead of MacOS
sed -i '' "s/http:\/\/localhost/$SPARQL_MS_SERVER/g" $SMSPATH/*/*/*.ttl
#Linux -  uncomment the line below if you are using Linux-based OS instead of MacOS
#sed -i "s/http:\/\/localhost/$SPARQL_MS_SERVER/g" $SMSPATH/*/*/*.ttl