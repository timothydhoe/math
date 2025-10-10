def main():
    """
    Programme that converts Celsius to Fahrenheit and the otherway around.

    User input is an integer (temp) and a string(°C or °F).
    Programme prints out the converted temperature.
    """
    temp, celsius = get_temp()
    # print(temp)
    # print(celsius)


    if celsius:
        converted_temp = c_to_f(temp)
    else:
        converted_temp = f_to_c(temp)

    print_conversion(temp, converted_temp, celsius)


def get_temp():
    print("\n")
    print("What conversion would you like to do?")
    print("-------------------------------------")
    print("To Fahrenheit(°F): press 'F'")
    print("To Celcius(°C): press 'C")

    celsius = True # Assumes user starts with Celcius value.

    while True:
        user_conversion = (input(">>> ")).lower()
        if user_conversion == 'f':
            celsius = False
            break
        if user_conversion == 'c':
            break
        else:
            print("Please enter 'F' to conversion to Fahrenheit or 'C' for conversion to Celcius")

    while True:
        if celsius == True:
            user_temp = int(input("What's the temperature in Fahrenheit: "))
            return user_temp, celsius
        user_temp = int(input("What's the temperature in Celsius: "))
        return user_temp, celsius


def c_to_f(temp_c):
    """
    Function that converts temperature in Celsius to Fahrenheit.
    Formula: C = (5/9) * (F - 32)
    """
    C = (5/9) * (temp_c - 32)
    return C
    

def f_to_c(temp_f):
    """
    Function that converts temperature in Celsius to Fahrenheit.
    Formula: F = ((9/5) * C) + 32
    """
    F = ((9/5) * temp_f) + 32
    return F 

def print_conversion(temp, converted_temp, celsius):
    """
    Print function that takes the original temperature,
    the converted temperature and method to print out the result.
    """
    print("\n")
    print("=============================")
    if celsius:
        print(f"{temp}°F is {converted_temp}°C.")
    else:
        print(f"{temp}°C is {converted_temp}°F")
    print("\n")



main()