#!/bin/sh

# Script to test the SPARQL microservices over the STRING database WEB APIs
# TO EDIT: the SPARQL Micro-service server URL
export server_sparqlms=http://localhost
export log_file=test_output.log
export query=select%20*%20where%20%7B%3Fs%20%3Fp%20%3Fo%7D
export save_file=test_queries.temp
read -r -d '' query_funtional_annot << EOM
PREFIX dct: <http://purl.org/dc/terms/> 
SELECT * where { ?s ?p ?o;  dct:identifier "9606.ENSP00000269305". }
EOM
read -r -d '' query_prot_interaction << EOM
PREFIX dct: <http://purl.org/dc/terms/> 
SELECT * where { ?s ?p ?o. optional{ ?var  dct:identifier "9606.ENSP00000269305"}. }
EOM
read -r -d '' query_mapIds << EOM
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX orth: <http://purl.org/net/orth#>
select * where {
?s ?p ?o;
  rdfs:label "TP53";
  orth:organism ?o.
?o dct:identifier "9606" .}
EOM

#check if any rdf:type statement was retrieved
test_sparqlms_results()
{
  webapi_name=$1
  if grep -q "type" "$save_file"; then
    echo "INFO: $webapi_name successfully executed" >> $log_file;
  else 
    echo "ERROR: $webapi_name was executed but it did not return any value, probably an error occured." >> $log_file; 
  fi
}
echo "Running tests:"
#Test getFunctionalAnnotation and getFunctionalAnnotation_sd SPARQL endpoints
curl --header "Accept: application/sparql-results+json" "${server_sparqlms}/service/stringdb/getFunctionalAnnotation?query=${query}&proteinId=9606.ENSP00000269305" > ${save_file}
test_sparqlms_results getFunctionalAnnotation 
curl --header "Accept: application/sparql-results+json" ${server_sparqlms}/service/stringdb/getFunctionalAnnotation_sd \
 --data-urlencode "query=${query_funtional_annot}"  > ${save_file}
test_sparqlms_results getFunctionalAnnotation_sd
#Test getAllFunctionalInteractionNetwork and getAllFunctionalInteractionNetwork_sd SPARQL endpoints
curl --header "Accept: application/sparql-results+json" "${server_sparqlms}/service/stringdb/getAllFunctionalInteractionNetwork?query=${query}&proteinIds=TP53%0dEGFR%0dCDK2" > ${save_file}
test_sparqlms_results getAllFunctionalInteractionNetwork 
curl --header "Accept: application/sparql-results+json" ${server_sparqlms}/service/stringdb/getAllFunctionalInteractionNetwork_sd \
  --data-urlencode "query=${query_prot_interaction}" > ${save_file}
test_sparqlms_results getAllFunctionalInteractionNetwork_sd 
#Test getAllPhysicalInteractionNetwork and getAllPhysicalInteractionNetwork_sd SPARQL endpoints
curl --header "Accept: application/sparql-results+json" "${server_sparqlms}/service/stringdb/getAllPhysicalInteractionNetwork?query=${query}&proteinIds=TP53%0dEGFR%0dCDK2" > ${save_file}
test_sparqlms_results getAllPhysicalInteractionNetwork
curl --header "Accept: application/sparql-results+json" ${server_sparqlms}/service/stringdb/getAllPhysicalInteractionNetwork_sd \
  --data-urlencode "query=${query_prot_interaction}" > ${save_file}
test_sparqlms_results getAllPhysicalInteractionNetwork_sd 
#Test getAllPhysicalInteractionNetwork and getAllPhysicalInteractionNetwork_sd SPARQL endpoints
curl --header "Accept: application/sparql-results+json" "${server_sparqlms}/service/stringdb/getPhysicalInteractionNetwork?query=${query}&proteinIds=TP53%0dEGFR%0dCDK2" > ${save_file}
test_sparqlms_results getPhysicalInteractionNetwork
curl --header "Accept: application/sparql-results+json" ${server_sparqlms}/service/stringdb/getPhysicalInteractionNetwork_sd \
  --data-urlencode "query=${query_prot_interaction}" > ${save_file}
test_sparqlms_results getPhysicalInteractionNetwork_sd 
#Test getFunctionalInteractionNetwork and getFunctionalInteractionNetwork_sd SPARQL endpoints
curl --header "Accept: application/sparql-results+json" "${server_sparqlms}/service/stringdb/getFunctionalInteractionNetwork?query=${query}&proteinIds=TP53%0dEGFR%0dCDK2" > ${save_file}
test_sparqlms_results getFunctionalInteractionNetwork
curl --header "Accept: application/sparql-results+json" ${server_sparqlms}/service/stringdb/getFunctionalInteractionNetwork_sd \
  --data-urlencode "query=${query_prot_interaction}" > ${save_file}
test_sparqlms_results getFunctionalInteractionNetwork_sd
#Test mapIds and mapIds_sd SPARQL endpoints
curl --header "Accept: application/sparql-results+json" "${server_sparqlms}/service/stringdb/mapIds?query=${query}&proteinId=TP53&speciesId=9606" > ${save_file}
test_sparqlms_results mapIds
curl --header "Accept: application/sparql-results+json" ${server_sparqlms}/service/stringdb/mapIds_sd \
  --data-urlencode "query=${query_mapIds}" > ${save_file}
test_sparqlms_results mapIds_sd
#Test getVersion and getVersion_sd SPARQL endpoints
curl --header "Accept: application/sparql-results+json"   "${server_sparqlms}/service/stringdb/getVersion?query=${query}" > ${save_file}
test_sparqlms_results getVersion
curl --header "Accept: application/sparql-results+json"   "${server_sparqlms}/service/stringdb/getVersion_sd?query=${query}"  > ${save_file}
test_sparqlms_results getVersion_sd
rm test_queries.temp
echo "Testing Report"
cat $log_file
echo "This report was saved at $log_file"