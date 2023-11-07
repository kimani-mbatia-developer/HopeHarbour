import unittest
import requests
from  import app

class TestAdminAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_pending_applications(self):
        response = self.app.get('/admin/applications')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("message", data)
        self.assertIn("data", data)
        self.assertEqual(data["message"], "Success")
        self.assertTrue(isinstance(data["data"], list))

    def test_approve_application(self):
        response = self.app.put('/admin/applications/approve/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("message", data)
        self.assertIn("data", data)
        self.assertEqual(data["message"], "Application approved successfully")

    def test_reject_application(self):
        response = self.app.put('/admin/applications/reject/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("message", data)
        self.assertIn("data", data)
        self.assertEqual(data["message"], "Application rejected successfully")

    def test_delete_charity(self):
        response = self.app.delete('/admin/charities/delete/1')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertIn("message", data)
        self.assertIn("data", data)
        self.assertEqual(data["message"], "Charity deleted successfully")

if __name__ == '__main__':
    unittest.main()
