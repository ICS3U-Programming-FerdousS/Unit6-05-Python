# Created by: Ferdous Sediqi
# Created on: April. 27 2022
# created by: Ferdous Sediqi
# This program asks the user for their marks then append it to a list
# and then in a function using a loop calculate the average of marks


# function to calclate the average
def calc_average(list_of_int):
    sum_num = 0
    # for each loop to find the average
    for a_number in list_of_int:
        sum_num = sum_num +  a_number
    if len(list_of_int) == 0:
        return "-1"
    else:
        average = sum_num / len(list_of_int)
    return average
        
    

def main():
    #declare the list
    list_of_int = []

    # using while loop to keep asking user for marks    
    while True:
        
        # Ask user to input their number
        user_num = input("Enter your mark : ")
            
        # cast input to int
        try:
            # Casting to int
            user_num_as_int = int(user_num)
            if user_num_as_int < 0:
                break
            list_of_int.append(user_num_as_int)
        except Exception:
            # If the user enters a invalid input
            print("Invalid input.")

    # call the function and display the average            
    average_num = calc_average(list_of_int)
    print("the average is {:.1f}".format(average_num))
    

if __name__ == "__main__":
    main()
