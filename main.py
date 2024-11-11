import DisplayMenu
import ConversionFunctions


def main():
    flag = True
    while flag == True:
        selection = DisplayMenu.display_menu()

        if selection == 1:
            val = float(input("\nEnter the Kilometers: "))
            CalcVal = ConversionFunctions.kilometers_to_miles(val)
            print (f"\n{val} Kilometers is equal to {CalcVal} miles\n")
        elif selection == 2:
            val = float(input("\nEnter the Meters: "))
            CalcVal = ConversionFunctions.meters_to_feet(val)
            print (f"\n{val} Meters is equal to {CalcVal} Feet\n")
        elif selection == 3:
            val = float(input("\nEnter the temperature in Celsius: "))
            CalcVal = ConversionFunctions.celsius_to_fahrenheit(val)
            print (f"\n{val} degrees Celsius is equal to {CalcVal} degrees fehrenheit\n")
        elif selection == 4:
            val = float(input("\nEnter the weight in kilograms: "))
            CalcVal = ConversionFunctions.kilograms_to_pounds(val)
            print (f"\n{val} Kilograms is equal to {CalcVal} pounds\n")
        elif selection == 5:
            val = float(input("\nEnter the Miles: "))
            CalcVal = ConversionFunctions.miles_to_kilometers(val)
            print (f"\n{val} Miles is equal to {CalcVal} kilometers\n")
        elif selection == 6:
            val = float(input("\nEnter the feet: "))
            CalcVal = ConversionFunctions.feet_1to_meters(val)
            print (f"\n{val} Feet is equal to {CalcVal} Meters\n")
        elif selection == 7:
            val = float(input("\nEnter the temperature in Fehrenheit: "))
            CalcVal = ConversionFunctions.fahrenheit_to_celsius(val)
            print (f"\n{val} degrees fahrenheit is equal to {CalcVal} degrees Celsius\n")
        elif selection == 8:
            val = float(input("\nEnter the weight in pounds: "))
            CalcVal = ConversionFunctions.pounds_to_kilograms(val)
            print (f"\n{val} Pounds is equal to {CalcVal} Kilograms\n")
        elif selection == 9:
            flag = False
            break
            


if __name__ == "__main__":
    main()