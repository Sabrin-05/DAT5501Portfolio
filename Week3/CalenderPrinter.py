#~~~~~~~~~~~~~~~~~~~~~~~~~
#Calendar Printer Function
#~~~~~~~~~~~~~~~~~~~~~~~~~
def calander_printer():
    """
    Prints the calander for a specific week and month 

    Returns:
    None: This function prints the calendar directly but does not return any value.
    """
    
    num_days = int(input('how many days in the month?:'))
    start_day = input('what day of the week does the month start on?:')
    day_of_week = {'Sunday': 0,
                   'Monday': 1, 
                   'Tuesday': 2,
                   'Wednesday': 3,
                   'Thursday': 4, 
                   'Friday': 5, 
                   'Saturday': 6
    }
    
    counter = 1 - day_of_week[start_day]
    
    print("____________________________________")
    print("| Su | Mo | Tu | We | Th | Fr | Sa |")
    print("|____|____|____|____|____|____|____|")

    while counter <= num_days:
        row = "|"
        for i in range(7):
            if counter <= 0 or counter > num_days:
                row += " -- |"
            else:
                if counter < 10:
                    row += "  " + str(counter) + " |"
                else:
                    row += " " + str(counter) + " |"
            counter += 1 
        print(row)

calander_printer()