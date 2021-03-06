start = input("Are you ready for a quiz?: ")
if start == "yes":
    points = 0
    print ("Lets go!!!")
    print("Q1) What is the capital of Alaska? ")
    print("1)Melbourne")
    print("2)Anchorage")
    print("3)Juneau")
    answer = int(input("Answer: "))
    if answer == 3:
        print ("That's right!")
        points = points + 1
        print(" ")
        print("Q2) Can you store the value \"cat\"  in a variable of type int? ")
        print("1)yes")
        print("2)no")
        answer = int(input("Answer: "))
        if answer == 2:
            print("That's right")
            points = points + 1
            print("Q3)What is the result of 3+3?")
            print("1)7")
            print("2)6")
            print("3)15")
            answer = int(input("Answer: "))
            if answer == 2:
                points = points + 1
                print("Thats correct")
                print("Total points: " + points)
                if points == 3:
                    print("Congratulations you answer all  questions correct")
                    print("Thank you for playing")
                elif points == 2:
                    print("Well done you only miss 1 question")
                    print("Thank you for playing")
                elif points == 1:
                    print("Nice try")
                else:
                    print("You suck")
            else:
                print("The correct answer is 6")
        else:
            print("The correct answer is No")
    else:
        print("The correct answer is Juneau")
else:
    print("See you next time")
