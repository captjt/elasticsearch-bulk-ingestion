"""
Upload module that has numerous method calls to
    - read from a local .csv
    - read from a publically hosted .csv
    - create a new index (if already created also delete old index)
    TODO
    - create to an existing index
    - delete an index
    - delete certain records from an index
    - update records in an index
"""

"""
read_file function that will take in a csv's local path and return a list ready to be bulk
    uploaded with ElasticSearch's _bulk capability
@variable filename  : type String
@return             : type list
"""
def read_file(filename, index_name, type_name, id_field):
    import csv

    print ('reading .csv file...')

    csv_file = open(filename, 'rt', encoding='utf-8')
    reader = csv.reader(csv_file)

    header = reader.__next__()
    header = [item.lower() for item in header]

    bulk_upload_data = []

    for row in reader:

        # we must create a dict for each 'record' or row from our .csv
        single_record = {}

        for i in range(0, len(row)-1):
            # catch if there are more values in the csv than the header allocate for
            if (i > len(header)-1):
                break
            # create a dictionary for each row we are uploading
            single_record[header[i]] = row[i]

        """
        this dictionary is for the elasticsearch indexing
        _index : name of the 'index'
        _type  : type of the 'index'
        _id    : unique id for each 'index' uploaded
        """
        op_dict = {
            "index": {
                "_index": index_name,
                "_type": type_name,
                "_id": single_record[id_field]
            }
        }

        # add to our big bulk upload data array -> each 'record' op_dict and body_dict
        bulk_upload_data.append(op_dict)
        bulk_upload_data.append(single_record)

    return bulk_upload_data

"""
bulk_create function that will take a correctly formatted list of valid ElasticSearch data
    and return a response
@variable data      : type list
@return             : type dict
"""
def bulk_create(data, es_host, index_name):
    from elasticsearch import Elasticsearch

    # create ES client -> create index
    es = Elasticsearch(hosts=[es_host])

    if es.indices.exists(index_name):
        print("deleting '%s' index..." % (index_name))
        res = es.indices.delete(index=index_name)
        print("     response: '%s'" % (res))

    # you can change these settings -- I am locally using one shard and no replicas
    body_settings = {
        "settings" : {
            "number_of_shards": 1,
            "number_of_replicas": 0
        }
    }

    print('creating %s index...' % (index_name))
    res = es.indices.create(index=index_name, body=body_settings)
    print('     response: %s' % (res))

    # we are going to bulk index the uploaded data
    print('indexing...')

    res = es.bulk(index=index_name, body=data, refresh=True)

    return res
