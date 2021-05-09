import unittest
import json
from api.app import app



class Tests(unittest.TestCase):
    # setup and teardown
    def setUp(self):
        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    # executed after each test
    def tearDown(self):
        pass

    ###############
    #### tests ####
    ###############

    def test_main_page(self):
        get = self.app.get('/status', follow_redirects=True)
        self.assertEqual(get.status_code, 200)
        service_name = 'myapplication'
        version = 'lastcommitsha'
        response = json.loads(get.get_data(as_text=True))
        self.assertIn(service_name, response)
        self.assertIn(version, response[service_name][0])



if __name__ == "__main__":
    unittest.main()

