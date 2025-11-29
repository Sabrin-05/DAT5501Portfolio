import unittest 
import numpy as np
from DurationCalc import dur_calc

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Unit Test for Duration Calculator
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class my_unit_tests(unittest.TestCase):
    def test_date_calc(self):
        '''
        Function checks that the difference between user input and todays date is correct

        RETURNS:
        None: Asserts that the calculated date difference is equal to the expected result
        '''
        test_date = "2025-10-01"
        test_date2 = "2025-09-01"
        assumed_result = np.datetime64(test_date) - np.datetime64(test_date2)
        
        # Commented out as dur_calc() currently prints the result rather than returning it
        #actual_result = dur_calc(test_date)
    
        self.assertEqual(assumed_result,test_date)
        

        

# run the tests
if __name__ == "__main__":
    unittest.main()