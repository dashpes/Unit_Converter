def display_menu():
    
    #flag to check if they entered the correct number for the first set of questions
    flag = False
    
    #keeps checking to see if they enetered in a number to select which way to convert
    while flag == False:
        print("Select which way you would like to convert:\n")
        print("\t1: Metric to Imperial")
        print("\t2: Imperial to Metric")
        print("\t3: Quit")
        choice_one = int(input("\nEnter the number of your choice: "))
        print("-------------------------------------------------------------")
        
        if choice_one == 1:
        #need to include another while loop for this and the elif statement
            flag = True
            print("\nYou will be converting from Metric to Imperial\nSelect which value you would like to convert:\n")
            print("\t1: Kilometers to Miles")
            print("\t2: Meters to Feet")
            print("\t3: Celsius to Farenheit")
            print("\t4: Kilograms to Pounds")
            choice_two = int(input("\nEnter the number of the conversion you would like to make: "))
            print("-------------------------------------------------------------")
            return choice_two
        
        elif choice_one == 2:
            flag = True
            print("\nYou will be converting from Imperial to Metric\nSelect which value you would like to convert:\n")
            print("\t1: Miles to Kilometers")
            print("\t2: Feet to Meters")
            print("\t3: Farenheit to Celsius")
            print("\t4: Pounds to Kilograms")
            choice_two = int(input("\nEnter the number of the conversion you would like ot make: "))
            choice_two += 4
            print("-------------------------------------------------------------")
            return choice_two
        
        elif choice_one == 3:
            print("\nGoodbye!\n")
            return 9
            flag = True
            break

        else:
            print("\nInvalid choice. Please select a valid option\n")