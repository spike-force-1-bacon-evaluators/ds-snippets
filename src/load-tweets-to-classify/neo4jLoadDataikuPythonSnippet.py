# in dataiku uncomment the following line 
# import dataiku 
import sys
import numpy as np
import py2neo
import pandas
from pandas import DataFrame
from py2neo import Graph,authenticate, Node, Relationship

def get_conn_string():
    return "http://MYNEO4JUSER:MYNEO4JPASS@138.68.146.141:7474/db/data"

def create_neo4j_connection(addr):
    return Graph(addr)

def load_unclassified_tweets(str,graph):
    df = DataFrame(graph.data(str))
    return df
    
def send_output(df):
    # Recipe outputs
    output = dataiku.Dataset('Output')
    output.write_with_schema(df)

if __name__ == "__main__":
    query1 = "MATCH (t:Tweet) WHERE NOT (t)-->(:SentimentAnalysis) return t.id as IDComment, t.text as CReview, t.date as CDate"
    query2 = "MATCH (t:Tweet)-->(r:Restaurant) WITH collect(t) as ts,r WHERE size(ts)>30 WITH r MATCH (a:SentimentAnalysis)<--(t:Tweet)-->(r) RETURN t.id as IDComments, t.text as CReviews, t.date as CDate, t.written_by as IDPerson, r.id as IDRestaurant, r.name as RName, r.followers as RFollowers a.class as Class"
    df = load_unclassified_tweets(
        query1, #set here your query 1 or 2
        create_neo4j_connection(get_conn_string()))
    send_output(df)
