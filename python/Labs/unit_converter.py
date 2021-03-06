#! python3

# v4 updated solution

def get_user_distance():
    return float((input("What is the distance?: ")))

def get_user_input():
    user_input = input("What measurement type would you like convert?: (inchs, feet, yards, meters, mils, kilometers) ")
    return user_input

def get_user_output():
    user_output = input("What measurement would you like to get back?: ")
    return user_output

def main():
    measure_dict = {    "inches": 0.02,
                        "feet": 0.30,
                        "yards": 0.91,
                        "meters": 1,
                        "miles": 1609.34,
                        "kilometers": 1000,
    }

    get_distance = get_user_distance()
    user_input = get_user_input()
    user_output = get_user_output()
    result = (get_distance*((measure_dict[user_input])/measure_dict[user_output]))
    print(f"\n{result} {user_output}")
    
main()

x = []
