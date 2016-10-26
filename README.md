# Welcome to elasticsearch-bulk-ingestion
An [elasticsearch-py](https://github.com/elastic/elasticsearch-py) bulk data ingestion wrapper!

### Purpose
The main purpose started out as a way to ingest a relational dataset into an ElasticSearch service.
There are a lot of features and functionality I would like to build on top of this small module in
the near future. [elasticsearch-py](https://github.com/elastic/elasticsearch-py) is a great package
that supplies the low level features we all love for ElasticSearch.

## Goals

* To become a full fledged bulk ingestion wrapper
* Current Functionality
    * A read_file method that reads a local .csv file and prepares it for the create upload
    * A bulk_create method that ingests the prepared data and creates and entity indexed based on the dataset
    * The bulk_create method will delete the old entity if it has already been created
* Future Functionality
    * To read from external .csv resources
    * To write to multiple ElasticSearch servers
    * To read multiple .csv resources for preparation
    * Update already existing entities based on .csv data
    * Delete an entity based on .csv records
    * Update (patch) records in an entity based on .csv records