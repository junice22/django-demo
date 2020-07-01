from django.test import TestCase, SimpleTestCase

class simpleTest(SimpleTestCase):
    def test_hello(self):
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)

# Create your tests here.
