import requests

MAX_API_QUERIES = 10000

class Socrata:

    def __init__(self, domain, dataid):
        self.domain = domain
        self.dataid = dataid
        self.default_api_path = "/resource/"
        self.headers = {'X-App-Token': 'sugMj0hPK2rjw6mrLmTO9ZD4T'}
        self.url = f'https://{self.domain}{self.default_api_path}{self.dataid}.json'

    def url(self):
        """ Return json api endpoint """
        return f'https://{self.domain}{self.default_api_path}{self.dataid}.json'

    def get_dataset_total_count(self):
        """ Get total count of the dataset
        """
        return int(requests.get(f'{self.url}?$select=count(*)', headers=self.headers).json()[0]['count'])

    def get_dataset_record_by_limit_offset_order(self, limit, offset, order):
        """ Get data with the below url parameters
        """
        return requests.get(f'{self.url}?$limit={limit}&$offset={offset}&$order={order}', headers=self.headers).json()[0][order]

    def get_dataset_by_limit_offset_order(self, limit, offset, order):
        """ Get data with the below url parameters
        """
        print(f'Requesting {limit} new records')
        print(f'{self.url}?$limit={limit}&$offset={offset}&$order={order}')
        return requests.get(f'{self.url}?$limit={limit}&$offset={offset}&$order={order}', headers=self.headers).json()

    def get_dataset_first_record_id(self):
        """ First record of the dataset sorted by record_id
        """
        return self.get_dataset_record_by_limit_offset_order(limit=1, offset=0, order="record_id")

    def get_dataset_last_record_id(self):
        """ Last record of the dataset sorted by record_id
        """
        offset = int(self.get_dataset_total_count()) - 1
        return self.get_dataset_record_by_limit_offset_order(limit=1, offset=offset, order="record_id")

    def fetch_api_dataset(self, limit, offset, order):
        """ Set the limit on the request with a max of 10000
            MAX_API_QUERIES == 10000
        """
        if limit >= MAX_API_QUERIES:
            return self.get_dataset_by_limit_offset_order(limit=MAX_API_QUERIES, offset=offset, order="record_id")
        else:
            return self.get_dataset_by_limit_offset_order(limit=limit, offset=offset, order="record_id")
