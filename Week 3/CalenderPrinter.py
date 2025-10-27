# Created a calander printer to print the month correctly according to user input 
def calander_printer():
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

    
    


        
    

    
    """  calander_header = "S   M   T   W   T   F   S"
    print(calander_header)

    counter = 1

    for week in range(4):
        row = ""
        
        for day in range(7):
            if gaps > 0:
                row += "--  "
                gaps -= 1
            else:
                if counter > 9:
                    row += str(counter)+"  "
                    counter += 1
                else:
                    row += str(counter)+"   "
                    counter += 1
        print(row) 
    ########    
        

 """
calander_printer()