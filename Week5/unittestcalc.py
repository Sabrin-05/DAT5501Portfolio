import unittest 
import numpy as np
from DurationCalc import dur_calc

class my_unit_tests(unittest.TestCase):
    def test_date_calc(self):
        '''
        Function checks that the difference between user input and todays date is correct
        '''
        test_date = "2025-10-01"
        test_date2 = "2025-09-01"
        assumed_result = np.datetime64(test_date) - np.datetime64(test_date2)

        actual_result = dur_calc(test_date)
    
        self.assertEqual(assumed_result,test_date)
        

        

# run the tests
if __name__ == "__main__":
    unittest.main()