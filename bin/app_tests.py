import unittest

import app as api
from flask import Flask

app = Flask(__name__)

class TestAPIs(unittest.TestCase):

    def test_get_MovieLogs(self):
        movieLogsTest = [
            {
                'id': 1,
                'title': 'Looper',
                'rating': 5, 
                'comment': "I liked it."
            },
            {
                'id': 2,
                'title': 'V For Vendetta',
                'rating': 5, 
                'comment': "I also liked it."
            }
        ]

        with app.app_context():
            import pdb; pdb.set_trace()  # breakpoint 81e5f918 //
            self.assertEqual(api.get_MovieLogs(), movieLogsTest)

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()