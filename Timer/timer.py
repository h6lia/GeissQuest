import time

OPTIONS = [15, 25, 30, 45, 60] #sch


def choose_time():
    print("Choose your session length for today to earn clover and feed Geissi! (1 Clover = 15 min)")

    for i, minutes in enumerate(OPTIONS, start=1):
        print(f"{i}. {minutes} minutes")

    prompt = "Set the time and press enter:"

    while True:
        choice = input(prompt)

        if choice.isdigit() and 1 <= int(choice) <= 5:
            return OPTIONS[int(choice) - 1]
        else:
            print("Enter a number between 1 to 5!")
            prompt = "Try again: "


def choose_display_mode():
    while True:
        choice = input("Show timer countdown? (y/n): ").lower()
        if choice in ["y", "n"]:
            return choice == "y"
        print("Please enter 'y' or 'n'")

#def input_thread(q):
    while True:
        q.put(input().lower())


#def timer_controls():
    choice = input("Press q to stop timer: ").lower()

    while choice not in ["q"]:
        choice = input("q").lower()

    return choice


def start_timer(minutes, show_countdown=True):

    print(f"Timer starts for {minutes} minutes now.\n")


    try:


        for remaining in range(minutes, 0, -1):


            if show_countdown:
                print(f"{remaining} min remaining")

            for _ in range(60):
                time.sleep(1)

                elapsed = minutes - remaining + 1

                if elapsed % 15 == 0:
                    print("You get a clover!")


                    #stop = input("Press q+ENTER to stop the time: ")

                    #f stop.lower() == "q":
                    #    print("Timer stopped.")
                     #   return None

                    #if stop.lower() == "w":
                     #   print("Restarting timer!")
                      #  return "restart"




        print("Session finished!")

    except KeyboardInterrupt:
        print("\nTimer manually stopped!")

    finally:
        input("Press Enter to exit from Timer: ")