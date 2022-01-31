import datetime
from SPARQLWrapper import SPARQLWrapper, CSV
from queries_sparqlms import *
import pandas as pd
from pandas.io.parsers import *
from math import sqrt
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    sparql = SPARQLWrapper(sparql_endpoint)
    query_id = 1
    n=10
    with open("query_test_sparqlms.csv", 'a+') as file:
        file.write("Query id,Question,Mean (seconds),Standard deviation,#Results\n")
    for query_label, sparql_query in queries:
        total = 0
        time_list = []
        for i in range(n):
            t0 = datetime.datetime.now().timestamp()
            sparql.setQuery(sparql_query)
            sparql.setReturnFormat(CSV)
            results = sparql.query().response
            t1 = datetime.datetime.now().timestamp()
            total = total + t1-t0
            time_list.append(t1-t0)
            print(query_label,str(i))
        csv_result_panda = pd.read_csv(results, sep=',', low_memory=False)
        mean = total / (n * 1.0)
        sum_sd = 0
        for t in time_list:
            sum_sd = sum_sd + (t-mean)*(t-mean)
        sd = sqrt(sum_sd / ((n-1) * 1.0))
        with open("query_test_sparqlms.csv",'a+') as file:
            row = "Q"+str(query_id)+","+query_label+","+ str(mean)+","+ str(sd)+"," + str(csv_result_panda.shape[0])\
                  +"\n"
            file.write(row)
        query_id = query_id + 1



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
