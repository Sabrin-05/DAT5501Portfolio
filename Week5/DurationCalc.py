# A duration calculator that allows user to input a date an calculate how many days ago that was

import numpy as np 
import datetime 


def dur_calc():
    user_date = np.datetime64(input("Enter the date that you would like to work out: e.g.(YYYY-MM-DD)"))
    today = np.datetime64('today')
    calc = user_date - today
    print(calc)


dur_calc()

