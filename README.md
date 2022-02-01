# sparql-stringdb
SPARQL endpoint over STRING database Web APIs and its related [ontology](http://tarcisiotmf.github.io/sparql-stringdb/).

## How to set up the SPARQL endpoint over the STRING DB Web APIs
To set up the SPARQL endpoint please first deploy the SPARQL micro-service (SPARQL-MS), instructions are available in [SPARQL-MS git repository](https://github.com/frmichel/sparql-micro-service). For an ease deployment, we  recommend the [SPARQL-MS docker container setup](https://github.com/frmichel/sparql-micro-service/tree/master/deployment/docker). Then, if a folder **services** does not exist, copy the folder [services](services/) into the SPARQL-MS directory where you have run docker-compose, else just copy [stringdb](services/) folder into the existing **services** directory. The stringdb folder contains configuration files, mostly access details to the STRING Web API functions and mappings (i.e. [SPARQL construct queries](https://www.w3.org/TR/sparql11-query/#construct)) to populate the [ontology](http://tarcisiotmf.github.io/sparql-stringdb/).

For a quick test of the deployed SPARQL-MS endpoints, run the shell script [test_sparqlms_stringdb.sh](test_sparqlms_stringdb.sh). Please change the variable ```server_sparqlms=http://localhost```, if the SPARQL-MS is deployed in a URL different from localhost. A report cotaining the test results is generated and saved (i.e. test_output.log) in the current directory of the script execution.

## Query performance evaluation
A performace evaluation was done with several queries that are fully described in [query_evaluation](query_evaluation/README.md).   

## Towards a protein-protein interaction ontology: the STRING database use case
The ontology used to structure the STRING database Web API responses are fully described and available in [STRING DB ontology documentation](http://tarcisiotmf.github.io/sparql-stringdb/). 

The official persitent URL of this ontology is http://purl.org/stringdb .

## License 
The files in this repository are under [CC0 1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/). However, note that terms that are not prefixed with http://purl.org/stringdb# at the [STRING database Web API ontology](http://tarcisiotmf.github.io/sparql-stringdb/) may be subject to another license, please refer to the original ontology of the term for further license details (often metioned within the "Is defined by" subsection / property). 
