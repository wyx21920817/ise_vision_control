#
# conversions.py – module with functions to convert between units #
# Convert among Fahrenheit, Celsius and Kelvin .
#
def fahr2cel(fahr):
    """Convert from Fahrenheit to Celsius. Argument:
    fahr – the temperature in Fahrenheit 
    """
    celsius = (fahr - 32) * (5/9) 
    return celsius


def cel2fahr(celsius):
    """Convert from Celsius to Fahrenheit. Argument:
    celsius – the temperature in Celsius 
    """
    fahr = (celsius / (5/9)) + 32
    return fahr

def fahr2kelvin(fahr):
    """Convert from Fahrenheit to Kelvin. Argument:
    fahr – the temperature in Fahrenheit 
    """
    kelvin = (fahr - 32) * (5/9) +273.15
    return kelvin

def cel2kelvin(celsius):
    """Convert from Celsius to Kelvin. Argument:
    celsius – the temperature in Celsius 
    """
    kelvin = celsius +273.15
    return kelvin

def kelvin2fahr(kelvin):
    """Convert from  Kelvin to Fahrenheit. Argument:
    kelvin – the temperature in Kelvin 
    """
    fahr = (kelvin-273.15)*(9/5) +32
    return fahr

def kelvin2cel(kelvin):
    """Convert from  kelvin to Celsius. Argument:
    kelvin – the temperature in kelvin 
    """
    celsius = kelvin - 273.15
    return celsius


def main():
    print('\nTesting textfun.py ')
    # put your testing code in here
    print("\nTESTING CONVERSIONS\n")
    testF = 100
    testC = fahr2cel(testF)
    print("Fahrenheit is ", testF, " Celsius is ", testC)
    print('Testing complete')

if __name__ == '__main__':
    main()