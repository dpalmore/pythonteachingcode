# [ ] create, call and test the adding_report() function

def adding_report(report):
    total = 0
    while True:
        add_numbers = input("Input an integer to add to the total or 'Q' to quit: ") 

        items = ""
        if add_numbers.isdigit():
            thisnumber = int(add_numbers)
            print("thisnumber =",thisnumber,type(thisnumber))
            total = total + thisnumber
            print("new total = ",total)
            if report == "A":
                item = add_numbers
            else:
                print(add_numbers)
        elif add_numbers.startswith("Q"):
            if report == "A":
                print(total)
                print(item)
                break
            else:
                print(total)
                break
        else:
            print("Input is invalid")
            

            
            
                
        
        
adding_report("A")