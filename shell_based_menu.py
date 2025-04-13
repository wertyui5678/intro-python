def problem_1():
    print("================Vehicle Alarm=================")
    headlight = input("Enter whether the headlight is on or off: ").strip().lower()
    door = input("Enter whether the door is open or closed: ").strip().lower() 
    ignition = input("Enter whether the ignition is on or off: ").strip().lower() 
    condition_1 = (headlight == "on" and ignition != "on")
    condition_2 = (door == "open" and ignition == "on")
    
    if condition_1 or condition_2:
        print("Alarm on")
    else:
        print("Alarm Off")

def problem_2():
    print("================Seatbelt Alarm=================")
    print("Answer yes or no:\n")
    drivers_seat =  input("Is the drivers seat in use? ").strip().lower()
    drivers_seatbelt = input("Has the driver fastened their seat belt? ").strip().lower()
    passenger_seat = input("Is the passenger seat in use? ").strip().lower()
    passenger_seatbelt= input("Has the passenger fastened their seat belt? ").strip().lower()
    ignition = input("Is the ignition on? ").strip().lower()
    
    condition_1 = (ignition == "yes" and drivers_seat== "yes" and drivers_seatbelt != "yes")
    condition_2 = (ignition == "yes" and passenger_seat == "yes" and passenger_seatbelt != "yes")

    if condition_1 or condition_2:
        print("Alarm on")
    else:
        print("Alarm Off")

def problem_3():
    print("================Syrup Tank=================")
    print("Answer yes or no for inlet calculations:\n")
    Lmax = input("has the maximum been reached? ").strip().lower()
    Lmin = input("has the minimum been reached? ").strip().lower()
    Finlet = input("is there currently flow into the tank? ").strip().lower()
    
    condition_1 = (Lmax != "yes" and Lmin != "yes" and Finlet != "yes")
    condition_2 = (Lmax != "yes" and Lmin != "yes" and Finlet == "yes")
    condition_3 = (Lmax != "yes" and Lmin == "yes" and Finlet == "yes")
    condition_4 = (Lmax == "yes" and Lmin != "yes" and Finlet != "yes")
    condition_5 = (Lmax == "yes" and Lmin != "yes" and Finlet == "yes")

    if condition_1 or condition_2 or condition_3:
        print("Inlet on")
    elif condition_4 or condition_5:
        print("invalid input")
    else:
        print("Inlet Off")

    print("\nAnswer yes or no for outlet calculations:\n")
    Lmax_2 = input("has the maximum been reached? ").strip().lower()
    Lmin_2 = input("has the minimum been reached? ").strip().lower()
    Finlet_2 = input("is there currently flow into the tank? ").strip().lower()
    Temperature = input("is the liquid at the correct temperature? ").strip().lower()

    condition_6 = (Lmax_2 != "yes" and Lmin_2 == "yes" and Finlet_2 != "yes" and Temperature == "yes")
    condition_7 = (Lmax_2 == "yes" and Lmin_2 == "yes" and Finlet_2 != "yes" and Temperature == "yes")
    condition_8 = (Lmax_2 == "yes" and Lmin_2 != "yes" and Finlet_2 != "yes" and Temperature != "yes")
    condition_9 = (Lmax_2 == "yes" and Lmin_2 != "yes" and Finlet_2 != "yes" and Temperature == "yes")
    condition_10 = (Lmax_2 == "yes" and Lmin_2 != "yes" and Finlet_2 == "yes" and Temperature != "yes")
    condition_11 = (Lmax_2 == "yes" and Lmin_2 != "yes" and Finlet_2 == "yes" and Temperature == "yes")
    
    if condition_6 or condition_7:
        print("outlet on")
    elif condition_8 or condition_9 or condition_10 or condition_11:
        print("invalid input")
    else:
        print("outlet Off")

def main():
    while True:
        print("=================================")
        print("Enter 1 for problem 1: ")
        print("\nEnter 2 for problem 2: ")
        print("\nEnter 3 for problem 3: ")
        print("\nEnter 0 to exit the program: ")
        print("=================================")

        choice = input("Input your choice here: ")
        if choice == "1":
            problem_1()
       
        if choice == "2":
            problem_2()

        if choice == "3":
            problem_3()

        if choice == "0":
            exit()

main()