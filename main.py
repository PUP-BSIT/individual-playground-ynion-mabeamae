#SOURCE CODE SWITCH CASE

choice = input("Enter your choice 1-10: ")

match choice:

    case "1":
        #Question 1
        print("(Ma. Bea Mae Ynion)  What is the sum of 130 + 125 + 191?") 

        print("a. 335")
        print("b. 456")
        print("c. 446")
        print("d. 426")

        user_answer = str(input("Enter your answer (a,b,c, or d): "))

        if user_answer == "c":
             print("Correct!")
        else:
             print(f"{user_answer} is incorrect. The correct answer is c. 446")

    case "2":
        #Question 2
        print("(Ma. Bea Mae Ynion) 50 times of 8 is equal to:")

        print("a. 80")
        print("b. 400")
        print("c. 800")
        print("d. 4000")

        user_answer = str(input("Enter your answer (a, b, c or d): "))

        if user_answer == "b":
             print("Correct!")
        else:
             print(f"{user_answer} is incorrect. The correct answer is b.")

    case "3":

        print ("(Patricia Joy Relente)  Bonbon is ten years older than his sister. If Bonbon was twenty-five years of age in 1983, in what year could he have been born?")

        print ("a. 1948")
        print ("b. 1953")
        print ("c. 1958")
        print ("d. 1963")

        user_answer = str(input("Enter your answer (a,b,c, or d): "))

        if user_answer == "c":
            print("Correct!")

        else:
            print(f"{user_answer} is incorrect. The correct answer is c. 1958")

    case "4":

        print ("(Patricia Joy Relente) What is the value of pi rounded to two decimal places?")

        print("a. 3.15")
        print("b. 3.14")
        print("c. 3.16")
        print("d. 3.17")

        user_answer = str(input("Enter your answer (a,b,c, or d): "))

        if user_answer == "b":
            print("Correct!")
        else:
            print(f"{user_answer} is incorrect. The correct answer is b. 3.14")

    case "5":
        # Question 5
        print("(Justine Delima) What programming language was used to create Minecraft?\n\n")

        print("a. C++")
        print("b. C")
        print("c. Java")
        print("d. COBOL")

        user_answer = str(input("\nEnter your answer (a, b, c, or d): "))

        if user_answer == 'c':
            print("Correct!\n")
        else:
            print(f"{user_answer} is incorrect. C (Java) is the correct answer.\n")

    case "6":
        # Question 6
        print("(Justine Delima) When was Avril Lavigne's first album entitled 'Let Go' released?\n\n")

        print("a. 1999")
        print("b. 2001")
        print("c. 2002")
        print("d. 2004")

        user_answer = str(input("\nEnter your answer(a, b, c, or d): "))

        if user_answer == 'c':
            print("Correct!\n")
        else:
            print(f"{user_answer} is incorrect. C (2002) is the correct answer.\n")

    case "7":
        pass
        #(member_4): Do item 7.

    case "8":
        pass
        #(member_4): Do item 8.

    case "9":
        pass
        #(member_5): Do item 9.

    case "10":
        pass
        #(member_5): Do item 10.