import insert_in_neo4j_snippet as lt4sa

def test_get_conn_string():
    assert lt4sa.get_conn_string() == "http://MYNEO4JUSER:MYNEO4JPASS@138.68.146.141:7474/db/data"
