"""
Configuration module that has a constructor of 5 values
    @variable file_url  : type String
        This is the .csv file path that you want to read from
    @variable es_host   : type dict
        This is the elasticsearch host and port number
    @variable index_name: type String
        This is the index of the dataset you are going to be creating
    @variable type_name : type String
        This is the type of data you are going to be creating
    @variable id_field  : type String
        This is an identifier of each type you are going to be creating

    Example field values...
        settings = config(
            "/path/to/filename.ext",
            {"host":"your-domain", "port":9200},
            "twitter",
            "tweet",
            "tweet-id"
        )
"""
class Config(object):


    def __init__(self, file_url, es_host, index_name, type_name, id_field):

        self.file_url = file_url
        self.es_host = es_host
        self.index_name = index_name
        self.type_name = type_name
        self.id_field = id_field
