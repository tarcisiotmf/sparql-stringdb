sparql_endpoint="http://localhost:8890/sparql/"

q1_label="Get proteins that directly and functionally interact with 3847.GLYMA08G27070.1"
q1='''PREFIX string: <http://purl.org/stringdb#>
PREFIX dct:<http://purl.org/dc/terms/>

SELECT DISTINCT * WHERE {

SERVICE <http://localhost/service/stringdb/getFunctionalInteractionNetwork_sd> {
?proteinURI_A string:functionallyInteractsWith ?proteinURI_B.
?proteinURI_A skos:prefLabel ?geneA_name.
?proteinURI_A dct:identifier "3847.GLYMA08G27070.1".
?proteinURI_B skos:prefLabel ?geneB_name .
#WEB API FUNCTION INPUT
OPTIONAL { ?_var_ dct:identifier "3847.GLYMA08G27070.1" } }}
'''

q2_label="Get proteins that directly and physically interact with 3847.GLYMA08G27070.1"
q2='''PREFIX string: <http://purl.org/stringdb#>
PREFIX dct:<http://purl.org/dc/terms/>

SELECT DISTINCT * WHERE {

SERVICE <http://localhost/service/stringdb/getPhysicalInteractionNetwork_sd> {
?proteinURI_A string:physicallyInteractsWith ?proteinURI_B.
?proteinURI_A skos:prefLabel ?geneA_name.
?proteinURI_A dct:identifier "3847.GLYMA08G27070.1".
?proteinURI_B skos:prefLabel ?geneB_name .
#WEB API FUNCTION INPUT
OPTIONAL { ?_var_ dct:identifier "3847.GLYMA08G27070.1" } }}

'''
q3_label="Get all function annotations for the protein 3847.GLYMA08G27070.1"
q3='''prefix orth: <http://purl.org/net/orth#> 
prefix skos: <http://www.w3.org/2004/02/skos/core#>
prefix terms: <http://purl.org/dc/terms/> 
prefix obo: <http://purl.obolibrary.org/obo/>
prefix up: <http://purl.uniprot.org/core/>
prefix sio: <http://semanticscience.org/resource/> 
prefix : <http://purl.org/stringdb#> 

SELECT * WHERE {

SERVICE <http://localhost/service/stringdb/getFunctionalAnnotation_sd> {
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

'''
q4_label="Get STRING database version"
q4='''SELECT * WHERE {
SERVICE <http://localhost/service/stringdb/getVersion_sd> {
?s ?p ?v }}
'''
q5_label="Get the corresponding STRING identifier of TP53 human gene."
q5='''prefix orth: <http://purl.org/net/orth#> 
prefix skos: <http://www.w3.org/2004/02/skos/core#>
prefix dce: <http://purl.org/dc/elements/1.1/>
prefix terms: <http://purl.org/dc/terms/> 
prefix obo: <http://purl.obolibrary.org/obo/>
prefix up: <http://purl.uniprot.org/core/>
prefix sio: <http://semanticscience.org/resource/> 
SELECT * WHERE {

SERVICE <http://localhost/service/stringdb/mapIds_sd> {
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
'''
q6_label="Get all proteins that functionally interact with 3847.GLYMA08G27070.1"
q6='''PREFIX string: <http://purl.org/stringdb#>
PREFIX dct:<http://purl.org/dc/terms/>

SELECT DISTINCT * WHERE {

SERVICE <http://localhost/service/stringdb/getAllFunctionalInteractionNetwork_sd> {
?proteinURI_A string:functionallyInteractsWith ?proteinURI_B.
?proteinURI_A skos:prefLabel ?geneA_name.
?proteinURI_A dct:identifier "3847.GLYMA08G27070.1".
?proteinURI_B skos:prefLabel ?geneB_name .
#WEB API FUNCTION INPUT
OPTIONAL { ?_var_ dct:identifier "3847.GLYMA08G27070.1" } }} '''

q7_label="Get all proteins that physically interact with 3847.GLYMA08G27070.1"
q7='''PREFIX string: <http://purl.org/stringdb#>
PREFIX dct:<http://purl.org/dc/terms/>

SELECT DISTINCT * WHERE {

SERVICE <http://localhost/service/stringdb/getAllPhysicalInteractionNetwork_sd> {
?proteinURI_A string:physicallyInteractsWith ?proteinURI_B.
?proteinURI_A skos:prefLabel ?geneA_name.
?proteinURI_A dct:identifier "3847.GLYMA08G27070.1".
?proteinURI_B skos:prefLabel ?geneB_name .
#WEB API FUNCTION INPUT
OPTIONAL { ?_var_ dct:identifier "3847.GLYMA08G27070.1" } }}

'''
q8_label="What are the  direct protein-protein functional interactions of a rice gene that is orthologous to the OMT2 wheat gene"
q8='''PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
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


'''


queries=[[q1_label,q1],[q2_label,q2],[q3_label,q3],[q4_label,q4],[q5_label,q5],[q6_label,q6],[q7_label,q7],
         [q8_label,q8]]
