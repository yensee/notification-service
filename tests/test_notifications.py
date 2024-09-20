import unittest
from app import create_app
from flask import json

class NotificationServiceTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_send_email_notification(self):
        response = self.client.post('/notifications/send',
                                    data=json.dumps({"type": "email"}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Notification sent', response.get_data(as_text=True))

    def test_send_sms_notification(self):
        response = self.client.post('/notifications/send',
                                    data=json.dumps({"type": "sms"}),
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Notification sent', response.get_data(as_text=True))

if __name__ == '__main__':
    unittest.main()
