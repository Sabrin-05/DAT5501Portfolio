

def comp_int_calculator():
    '''
    Function calculates total savings for each year based on initial savings, years of saving and annual interest rate

    Returns:
    None: Function prints out the annual saving totals
    '''
    initial_saving = float(input("Enter your initial amount of savings: "))
    years = int(input("Enter the number of years you're saving for (whole numbers only): "))
    interest_rate = float(input("Enter the annual interest rate (decimal): "))
    # comp_periods = int(input("Enter (in months) the compounding period: "))
    # comp_periods = comp_periods/12
    time = 0 # time acts as a counter between the starting year and the total years being saved for
    running_total = initial_saving # running_total is a variable amount, increasing with each calculation and increment of time
    for time in range(0, years): # for each year/compounding period up to the entered number of years
        print(f"Year {time}: £{running_total}")
        time += 1
        running_total = running_total * (1 + interest_rate)
        # running_total = initial_saving*(1 + interest_rate/comp_periods)**(comp_periods*time)

def savings_double_calc():
    '''
    Function calculates number of years it takes for initial savings to double according to interest rate
    
    Returns:
    None: Function currently not complete but would print out the number of years taken to double savings 
    '''
    initial_savings =  float(input("Enter your initial amount of savings: "))
    interest_rate = float(input("Enter the annual interest rate (decimal): "))
    doubled_savings = initial_savings * 2
    # years_to_double = # number of years it takes for the savings to double. for this, 'double' can be greater than or equal to 'doubled_savings'
    # incomplete
        
comp_int_calculator()
