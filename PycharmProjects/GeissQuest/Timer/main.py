import time
from storage import load_data, save_data

OPTIONS = [ 10, 25, 30, 45, 60]

def choose_time():
    print("Choose the Time")
    for i, minutes in enumerate(OPTIONS, start=1):
        print(f"{i}. {minutes} minutes")

    while True:
        choice = input("Select (1-5): ")
        if choice.isdigit() and 1 <= int(choice) <= len(OPTIONS):
            return OPTIONS[int(choice) - 1]

        else:
            print("No cheating -_- please select 1-5")




def start_timer(minutes):
    print(f"Timer starts for {minutes} minutes..")
    time.sleep(minutes * 60)
    print("STOP!!!")



def main():
    data = load_data()
    minutes = choose_time()
    start_timer(minutes)

    data['total_minutes'] += minutes
    save_data(data)

    print(f"Congrats, you worked for {minutes} minutes today!")
    print(f"Total time: {data['total_minutes']} minutes")




if __name__ == "__main__":
    main()
