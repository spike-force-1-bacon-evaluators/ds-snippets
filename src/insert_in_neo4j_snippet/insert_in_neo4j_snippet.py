# in dataiku uncomment the following line
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

def store_classified_tweets(graph):
   df = dataiku.Dataset("Remove_IDRestaurant_prepared_scored_prepared").get_dataframe()
   for d in df.iterrows():
       t_id = str(d[1][0])
       t_class = str(d[1][1])
       cypher_qr="MERGE (t:Tweet{id:'"+t_id+"'}) MERGE (c:SentimentAnalysis{class:"+t_class+"}) MERGE (t)-[:HAS_CLASS]->(c)"
       a = graph.run(cypher_qr)
   
def send_output(df):
   # Recipe outputs
   output = dataiku.Dataset("togo_weight_model")
   output.write_with_schema(df)

def load_data(str,graph):
   df = DataFrame(graph.data(str))
   return df    
   
if __name__ == "__main__":
   store_classified_tweets(create_neo4j_connection(get_conn_string()))
   query2 = "MATCH (t:Tweet)-->(r:Restaurant) WITH collect(t) as ts,r WHERE size(ts)>30 WITH r MATCH (a:SentimentAnalysis)<--(t:Tweet)-->(r) RETURN t.id as IDComments, t.text as Review, t.date as CDate, t.written_by as IDPerson, r.id as IDRestaurant, r.name as RName, r.followers as RFollowers, a.class as prediction"
   df = load_data(
       query2,
       create_neo4j_connection(get_conn_string()))
   send_output(df)