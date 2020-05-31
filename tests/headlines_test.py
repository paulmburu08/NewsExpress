import unittest
from app.models import TopHeadline

class HeadlinesTest(unittest.TestCase):
    '''
    Test Class to test behaviour of the TopHeadline class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_headline = TopHeadline('Paul','Car stolen','My car was stolen by the police','/sllajdj','/sasdsea',"2020-05-30T18:38:33Z")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_headline,TopHeadline))

if __name__ == '__main__':
    unittest.main()