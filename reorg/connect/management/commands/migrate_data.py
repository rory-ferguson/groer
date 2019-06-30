from django.core.management.base import BaseCommand

from connect.models import OpenPayments
from connect.socrata import Socrata


socrata = Socrata(domain="openpaymentsdata.cms.gov", dataid="8pru-svmk") 

def db_has_data():
    try:
        if OpenPayments.objects.all()[0]:
            return True
    except IndexError:
        return False

def dataset_count():
    """ Returns total count of db
    """
    return OpenPayments.objects.count()

def dataset_first_last_count():
    """ Returns tuple of the dataset first row, last row and total count
    """
    return (socrata.get_dataset_first_record_id(), socrata.get_dataset_last_record_id(), socrata.get_dataset_total_count())

def db_first_last_count():
    """ Returns tuple of the db first row, last row and total count
    """
    return (OpenPayments.objects.first().record_id, OpenPayments.objects.last().record_id, OpenPayments.objects.count())

def verify_dataset_db():
    """
    """
    a = dataset_first_last_count()
    b = db_first_last_count()
    if a == b:
        return True
    else:
        if a[0] == b[0]:  # First row
            return a[2] - b[2], b[2]
        else:
            return False

def write_json_to_db(data):
    """ Write JSON formatted data to the db with bulk_create
    """
    print('Writing to db...')
    try:
        OpenPayments.objects.bulk_create([ OpenPayments(**i) for i in data ])
    except TypeError as e:
        print(f'Error migrating row. {e}')


class Command(BaseCommand):
    help = 'Pulls data from webpage and updates DB'

    def handle(self, *args, **options):
        if not db_has_data():
            data = socrata.fetch_api_dataset(limit=1, offset=0,  order="record_id")
            write_json_to_db(data)

        while True:
            print('\nVerifying the data in the dataset and db are the same...')
            verify_data = verify_dataset_db()
            if verify_data == True:
                print('Database is up to date')
                break
            elif verify_data == False:
                print('Data does not match!')
                print('Manual resync of data required!')
                break
            else:
                """ This section is to limit the database rows to 50000 """
                count = dataset_count()
                if verify_data[0] > count:
                    if count == 50000:
                        print('Database is up to date')
                        break
                    limit = 50000 - count
                    data = socrata.fetch_api_dataset(limit=limit, offset=verify_data[1], order="record_id")
                else:
                    data = socrata.fetch_api_dataset(limit=verify_data[0], offset=verify_data[1], order="record_id")
                write_json_to_db(data)
            # else:
            #     data = socrata.fetch_api_dataset(limit=verify_data[0], offset=verify_data[1], order="record_id")
            #     write_json_to_db(data)