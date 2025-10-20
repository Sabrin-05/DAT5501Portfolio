import unittest 
from DurationCalc import dur_calc

class my_unit_tests(unittest.TestCase):
    def test_date_calc(self):
        '''function checks that the difference between user input and todays date is correct
        '''
        
        self.assertEqual(dur_calc(2025-10-1), 20)

        

# run the tests
if __name__ == "__main__":
    unittest.main()