from elasticsearch import Elasticsearch

from config import Config as config

settings = config(
        "./students.csv",
        {"host":"localhost", "port":9200},
        "vsfs-students",
        "document",
        "applicant_id"
    )

# create ES client => search
es = Elasticsearch(hosts=[settings.es_host])

# sanity checking
print("searching last name - Aaron...")
test_search = es.search(index=settings.index_name,
        body={
            "query": {
                "match": {
                    "key" : "value"
                }
            }
        }
    )
print("     response: \n '%s'" % (test_search))

print("\nresults:")
for hit in test_search['hits']['hits']:
    print('     ', hit["_source"])