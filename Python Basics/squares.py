def square_of_numbers(numbers):
    for my_number in numbers:
        print("the number is ", my_number)

        if my_number.__class__ in [int, float]:
            square = my_number ** 2

            if my_number % 2 == 0:
                print("this is an even number")
                print("the square of ", my_number, " is ", square)
            else:
                print("this is an odd number")
                print("the square of ", my_number, " is ", square)
        
        else:
            type_of_my_number = my_number.__class__
            print(f"this is not an integer but a type of {type_of_my_number}")

        print()