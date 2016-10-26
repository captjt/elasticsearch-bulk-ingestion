# configuration variables
import sys as _sys

import utils.config as config
from utils.uploader import (
    read_file,
    bulk_create,
)


def main(argv):
    settings = config.Config(
        "./path/to/directory/filename.csv",
        {"host":"localhost", "port":9200},
        "twitter",
        "tweet",
        "tweet_id"
    )

    upload_data = read_file(
        settings.file_url,
        settings.index_name,
        settings.type_name,
        settings.id_field,
    )

    response = bulk_create(
        upload_data,
        settings.es_host,
        settings.index_name,
    )

    if (response):
        print('finished bulk upload...')
        return 0
    else:
        print('there was an error in your bulk_create method call')
        return 0

if __name__ == '__main__':
    _sys.exit(main(_sys.argv[1:]))
