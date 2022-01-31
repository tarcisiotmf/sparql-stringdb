#Query Evaluation Examples

The python script [main.py](main.py) along with [queries_sparqlms.py](queries_sparqlms.py) calculate the mean and 
standard deviation of the query execution in terms of response time in seconds. The queries are detailed in the next sections and retrieve data from STRING and OMA databases. The table below summarises the output 
results in [query_test_sparqlms.csv](query_test_sparqlms.csv). In our examples, we consider the protein 
3847.GLYMA08G27070.1 (i.e. [C6TAY1 protein](https://www.uniprot.org/uniprot/C6TAY1)).

In this script, the federated SPARQL endpoint URL address is assigned to the variable ```sparql_endpoint=http://localhost:8890/sparql/``` in [queries_sparqlms.py](queries_sparqlms.py). Similarly, the queries defined in [queries_sparqlms.py](queries_sparqlms.py) and described in the next sections are addressed over the SPARQL micro-services deployed at ```http://localhost/service/stringdb/```. To run the script and reproduce the results summarised below, replace the federated SPARQL endpoint URL and SPARQL-MS URL address with your own setup. Further information of how to set-up the SPARQL-MS over STRING database are available in the README.md file of this git repository.


| Query | Query text                                                                                                                                | Mean (s) | Std deviation | #Results |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------|----------|---------------|----------|
| Q1    | [Get proteins that directly and functionally interact with 3847.GLYMA08G27070.1](#q1---query-1)                                           | 0.95     | 0.51          | 10       |
| Q2    | [Get proteins that directly and physically interact with 3847.GLYMA08G27070.1.1](#q2---query-2)                                           | 0.31     | 0.03          | 0        |
| Q3    | [Get all function annotations for the protein 3847.GLYMA08G27070.1](#q3---query-3)                                                        | 0.74     | 0.12          | 26       |
| Q4    | [Get STRING database version](#q4---query-4)                                                                                              | 0.26     | 0.02          | 3        |
| Q5    | [Get the corresponding STRING identifier of TP53 human gene.](#q5---query-5)                                                              | 0.32     | 0.01          | 1        |
| Q6    | [Get all proteins that directly and functionally interact with 3847.GLYMA08G27070.1](#q6---query-6)                                       | 0.91     | 0.21          | 36       |
| Q7    | [Get all proteins that directly and physically interact with 3847.GLYMA08G27070.1](#q7---query-7)                                         | 0.37     | 0.07          | 0        |
| Q8    | [What are the  direct protein-protein functional interactions of a rice gene that is orthologous to the OMT2  wheat gene?](#q8---query-8) | 1.33     | 0.48          | 10       |


## [STRING database](https://string-db.org) queries

The following subsections describes each SPARQL endpoint and the corresponding evaluated query. In the  SPARQL micro-service (SPARQL-MS) 
URI addresses ‘sd’ is an acronym for service description followed with a version number, if any
(e.g. getFunctionalInteractionNetwork_sd2 ).
The documentation of the STRING database ontology used to model the data is described in a separated document at 
[STRING database Web API ontology](). Moreover, in the queries below the input parameter of the Web API functions such 
as the ‘proteinIds’ argument value provided to the Web API function at 
https://string-db.org/api/json/network?identifiers={proteinIds} must be encapsulated as an optional triple pattern, 
because the input value is not always directly link with all output values (e.g. protein-protein network result):  
```OPTIONAL { ?_var_ dct:identifier "3847.GLYMA08G27070.1" } ```


### Q1 - Query 1
**Query:** Get proteins that directly and functionally interact with 3847.GLYMA08G27070.1 
(i.e. [C6TAY1 protein](https://www.uniprot.org/uniprot/C6TAY1))

**Web API function required:** https://string-db.org/api/json/network?identifiers={proteinIds} 
where ‘proteinIds’ is a variable.

**SPARQL-MS endpoint:** http://localhost/service/stringdb/getFunctionalInteractionNetwork_sd

**SPARQL query:**
```commandline
PREFIX string: <http://purl.org/stringdb#>
PREFIX dct:<http://purl.org/dc/terms/>

SELECT DISTINCT * WHERE {

SERVICE <http://localhost/service/stringdb/getFunctionalInteractionNetwork_sd> {
?proteinURI_A string:functionallyInteractsWith ?proteinURI_B.
?proteinURI_A skos:prefLabel ?geneA_name.
?proteinURI_A dct:identifier "3847.GLYMA08G27070.1".
?proteinURI_B skos:prefLabel ?geneB_name .
#WEB API FUNCTION INPUT
OPTIONAL { ?_var_ dct:identifier "3847.GLYMA08G27070.1" } }}
```

### Q2 - Query 2
**Query:** Get proteins that directly and physically interact with 3847.GLYMA08G27070.1.1

**Web API function required:** https://string-db.org/api/json/network?identifiers={proteinIds}&network_type=physical   
where ‘proteinIds’ is a variable.

**SPARQL-MS endpoint:** http://localhost/service/stringdb/getFunctionalInteractionNetwork_sd

**SPARQL query:**
```commandline
PREFIX string: <http://purl.org/stringdb#>
PREFIX dct:<http://purl.org/dc/terms/>

SELECT DISTINCT * WHERE {

SERVICE <http://localhost/service/stringdb/getPhysicalInteractionNetwork_sd> {
?proteinURI_A string:physicallyInteractsWith ?proteinURI_B.
?proteinURI_A skos:prefLabel ?geneA_name.
?proteinURI_A dct:identifier "3847.GLYMA08G27070.1".
?proteinURI_B skos:prefLabel ?geneB_name .
#WEB API FUNCTION INPUT
OPTIONAL { ?_var_ dct:identifier "3847.GLYMA08G27070.1" } }}
```

### Q3 - Query 3
**Query:** Get all function annotations for the protein 3847.GLYMA08G27070.1

**Web API function required:** : https://string-db.org/api/json/functional_annotation?identifiers={proteinId} where 
‘proteinId’ is a variable. 

**SPARQL-MS endpoint:** http://localhost/service/stringdb/getFunctionalAnnotation_sd . It is mandatory to provide the protein identifier (e.g. gene names, UniProtKB accession 
number, STRING DB identifiers, Ensembl ids) via the property http://purl.org/dc/terms/identifier (dct:identifier) 
in the SPARQL graph pattern. Note that the URI format that represents the protein in the constructed graph based 
on the API function call response is defined as follows:  
https://string-db.org/cgi/network?identifier={urlencode(proteinId)}.

**SPARQL query:**
```commandline
prefix orth: <http://purl.org/net/orth#> 
prefix skos: <http://www.w3.org/2004/02/skos/core#>
prefix terms: <http://purl.org/dc/terms/> 
prefix obo: <http://purl.obolibrary.org/obo/>
prefix up: <http://purl.uniprot.org/core/>
prefix sio: <http://semanticscience.org/resource/> 
prefix : <http://purl.org/stringdb#> 

SELECT * WHERE {

SERVICE <http://by1amv.eu.seeds.basf.net/service/stringdb/getFunctionalAnnotation_sd> {
 ?protein a orth:Protein;      
 owl:sameAs ?proteinURI ;        
    orth:organism  ?organism;
    skos:prefLabel ?prefGeneLabel;
    rdfs:label ?geneLabel;
    terms:identifier "3847.GLYMA08G27070.1"; #WEB API function input
    obo:RO_0001018 <https://string-db.org>. #contained in
?organism a orth:Organism;
    terms:identifier ?ncbiTaxonId ;
    obo:RO_0002162 ?taxon.
?taxon a up:Taxon;
    terms:identifier ?ncbiTaxonId .
<https://string-db.org> rdf:type sio:SIO_000750. #A database.
{?proteinURI  up:classifiedWith ?term_URI . 
?term_URI a up:Concept;
 skos:inScheme ?vocabulary;
 rdfs:label ?description;
 skos:prefLabel ?description.
} UNION {
OPTIONAL{?proteinURI rdfs:seeAlso ?db_URI.}
?db_URI a up:Resource;
rdfs:comment ?description;
up:database ?db . } }}
```

### Q4 - Query 4
**Query:** Get STRING database version. 

**Web API function required:** https://string-db.org/api/json/version.

**SPARQL-MS endpoint:** http://localhost/service/stringdb/getVersion_sd

**SPARQL query:**
```commandline
SELECT * WHERE {
SERVICE <http://by1amv.eu.seeds.basf.net/service/stringdb/getVersion_sd> {
?s ?p ?v }}
```

### Q5 - Query 5
**Query:** : Get the corresponding STRING identifier of TP53 human gene. 

**Web API function required:** https://string-db.org/api/json/get_string_ids?identifiers={proteinId}&species={speciesId}
where ‘proteinId’ and ‘speciesId’ are variables.

**SPARQL-MS endpoint:** http://localhost/service/stringdb/mapIds_sd . It is mandatory to provide the species 
NCBI identifier associated with the protein via the orth:organism/dct:identifer property path and the id 
(or label) of the protein we want to be mapped.

**SPARQL query:**
```commandline
prefix orth: <http://purl.org/net/orth#> 
prefix skos: <http://www.w3.org/2004/02/skos/core#>
prefix dce: <http://purl.org/dc/elements/1.1/>
prefix terms: <http://purl.org/dc/terms/> 
prefix obo: <http://purl.obolibrary.org/obo/>
prefix up: <http://purl.uniprot.org/core/>
prefix sio: <http://semanticscience.org/resource/> 
SELECT * WHERE {

SERVICE <http://by1amv.eu.seeds.basf.net/service/stringdb/mapIds_sd> {
?proteinURI a orth:Protein;              
    orth:organism  ?organism;
    skos:prefLabel ?prefName;
    terms:identifier ?stringdb_id;
    rdfs:label "TP53"; #WEB API function input
    dce:description ?description.

?organism a orth:Organism;
    obo:RO_0002162 ?taxon.
?taxon a up:Taxon;
    terms:identifier "9606" ; #WEB API function input
    up:scientificName ?taxon_name. }}
```

### Q6 - Query 6
**Query:** Get all proteins that directly and functionally interact with 3847.GLYMA08G27070.1. 

**Web API function required:** https://string-db.org/api/json/interaction_partners?identifiers={proteinIds}&limit=0 
where ‘proteinIds’ is a variable.

**SPARQL-MS endpoint:** http://localhost/service/stringdb/getAllFunctionalInteractionNetwork_sd

**SPARQL query:**
```commandline
PREFIX string: <http://purl.org/stringdb#>
PREFIX dct:<http://purl.org/dc/terms/>

SELECT DISTINCT * WHERE {

SERVICE <http://localhost/service/stringdb/getAllFunctionalInteractionNetwork_sd> {
?proteinURI_A string:functionallyInteractsWith ?proteinURI_B.
?proteinURI_A skos:prefLabel ?geneA_name.
?proteinURI_A dct:identifier "3847.GLYMA08G27070.1".
?proteinURI_B skos:prefLabel ?geneB_name .
#WEB API FUNCTION INPUT
OPTIONAL { ?_var_ dct:identifier "3847.GLYMA08G27070.1" } }} 
```

### Q7 - Query 7
**Query:** Get all proteins that directly and physically interact with 3847.GLYMA08G27070.1

**Web API function required:** https://string-db.org/api/json/interaction_partners?identifiers={proteinIds}&limit=0&network_type=physical 
where ‘proteinIds’ is a variable.

**SPARQL-MS endpoint:** http://localhost/service/stringdb/getAllPhysicalInteractionNetwork_sd

**SPARQL query:**
```commandline
PREFIX string: <http://purl.org/stringdb#>
PREFIX dct:<http://purl.org/dc/terms/>

SELECT DISTINCT * WHERE {

SERVICE <http://localhost/service/stringdb/getAllPhysicalInteractionNetwork_sd> {
?proteinURI_A string:physicallyInteractsWith ?proteinURI_B.
?proteinURI_A skos:prefLabel ?geneA_name.
?proteinURI_A dct:identifier "3847.GLYMA08G27070.1".
?proteinURI_B skos:prefLabel ?geneB_name .
#WEB API FUNCTION INPUT
OPTIONAL { ?_var_ dct:identifier "3847.GLYMA08G27070.1" } }}
```

## Federated query over [OMA](https://omabrowser.org) and [STRING](https://string-db.org) databases.
### Q8 - Query 8
**Query:** What are the  direct protein-protein functional interactions of a rice gene that is orthologous to the OMT2 
wheat gene?
 
**Web API function required:** https://string-db.org/api/json/network?identifiers={proteinIds} 
where ‘proteinIds’ is a variable.

**SPARQL endpoints:** 
- STRING DB SPARQL-MS: http://localhost/service/stringdb/getFunctionalInteractionNetwork_sd
- OMA SPARQL endpoint: https://sparql.omabrowser.org/sparql/

**SPARQL query:**
```commandline
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX dc: <http://purl.org/dc/elements/1.1/>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX ensembl: <http://rdf.ebi.ac.uk/resource/ensembl/>
PREFIX oma: <http://omabrowser.org/ontology/oma#>
PREFIX orth: <http://purl.org/net/orth#>
PREFIX sio: <http://semanticscience.org/resource/>
PREFIX taxon: <http://purl.uniprot.org/taxonomy/>
PREFIX up: <http://purl.uniprot.org/core/>
PREFIX void: <http://rdfs.org/ns/void#>
PREFIX lscr: <http://purl.org/lscr#>
prefix : <http://purl.org/stringdb#>

####
####Uniprot id parameter as triple. 
####
select * {
{ select * { SERVICE <https://sparql.omabrowser.org/sparql/> {
select distinct ?OMAProt_wheat ?gene_wheat ?gene_rice ?geneA_name (?protein2 as ?protein_rice) ?uniprot_rice ?uniprot_rice_id {
VALUES ?gene_wheat {"OMT2"}
?cluster a orth:OrthologsCluster.
?cluster orth:hasHomologousMember ?node1.
?cluster orth:hasHomologousMember ?node2.
?node2 orth:hasHomologousMember* ?protein2.
?node1 orth:hasHomologousMember* ?OMAProt_wheat.
?OMAProt_wheat a orth:Protein;
rdfs:label ?gene_wheat;
orth:organism ?organism1.
?organism1 ?p ?taxon1.
?taxon1 up:scientificName "Triticum aestivum".
?protein2 a orth:Protein;
orth:organism ?organism2.
?organism2 ?p ?taxon.
?taxon up:scientificName "Oryza sativa subsp. japonica".
?protein2 lscr:xrefUniprot ?uniprot_rice;
rdfs:label ?gene_rice. 
?uniprot_rice dct:identifier ?uniprot_rice_id.
BIND(STRDT(?gene_rice,xsd:string) as ?geneA_name) 
filter(?node1 != ?node2)}} 

SERVICE <http://localhost/service/stringdb/getFunctionalInteractionNetwork_sd> 
{ optional{ ?_var_ dct:identifier ?uniprot_rice_id }
?proteinURI_A :functionallyInteractsWith ?proteinURI_B.
?proteinURI_A skos:prefLabel ?geneA_name.
?proteinURI_B skos:prefLabel ?geneB_name .
}
}}
}
```