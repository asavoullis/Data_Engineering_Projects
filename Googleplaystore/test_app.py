import unittest
import json
from Flask_API import DataAPI
from config import Config


class TestDataAPI(unittest.TestCase):
    def setUp(self):
        """ The setUp method is called before each test method. It initializes an instance of DataAPI for testing. """
        config = Config()
        self.data_api = DataAPI(config)

    # Each test method begins with the test_ prefix, making it recognizable as a test method.
    # Tests are executed in alphabetical order

    def test_index_endpoint(self):
        with self.data_api.app.test_client() as client:
            response = client.get('/')
            # Fail if the two objects are equal as determined by the '!=' operator.
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"Welcome to the Google Play Store Data API", response.data)

    def test_filter_one_column_endpoint(self):
        with self.data_api.app.test_client() as client:
            response = client.get('/filter_one_column?column_name=Category&column_value=ART_AND_DESIGN')
            self.assertEqual(response.status_code, 200)

            response_missing_params = client.get('/filter_one_column')
            self.assertEqual(response_missing_params.status_code, 400)
            self.assertIn(b"Both 'column_name' and 'column_value' query parameters are required.",
                          response_missing_params.data)

    def test_get_all_data_endpoint(self):
        with self.data_api.app.test_client() as client:
            response = client.get('/get_all_data')
            self.assertEqual(response.status_code, 200)

            data = json.loads(response.json)
            self.assertIsInstance(data, list)
            self.assertTrue(len(data) > 0)

    def test_get_data_endpoint(self):
        with self.data_api.app.test_client() as client:
            params = {"Rating": "4.1", "Category": "ART_AND_DESIGN"}
            response = client.get('/get_data', query_string=params)
            self.assertEqual(response.status_code, 200)

    def test_get_data_tabular_endpoint(self):
        with self.data_api.app.test_client() as client:
            params = {"Rating": "4.1", "Category": "ART_AND_DESIGN"}
            response = client.get('/get_data_tabular', query_string=params)
            self.assertEqual(response.status_code, 200)

    def test_sort_data_endpoint(self):
        with self.data_api.app.test_client() as client:
            params = {"sort_column": "Rating", "sort_order": "desc"}
            response = client.get('/sort_data', query_string=params)
            self.assertEqual(response.status_code, 200)

    def test_summary_statistics_endpoint(self):
        with self.data_api.app.test_client() as client:
            response = client.get('/summary_statistics')
            self.assertEqual(response.status_code, 200)

            data = response.json.get('data', {})

            self.assertIn('Rating', data)

            rating_stats = data['Rating']
            self.assertGreaterEqual(float(rating_stats['3']), 0.0)
            self.assertLessEqual(float(rating_stats['4']), 5.0)


if __name__ == '__main__':
    unittest.main()
