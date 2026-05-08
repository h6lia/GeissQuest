from stats.stats import show_stats
from timer.timer import choose_time, start_timer, choose_display_mode

print("=== GeissQuest Menu ===")


def run_menu():
    while True:

        print("\na. Start Timer")
        print("b. Show Stats")
        print("c. Exit")

        choice = input("Choose a/b/c: ").lower()

        if choice == "a":
            minutes = choose_time()
            show_countdown = choose_display_mode()
            start_timer(minutes, show_countdown)
        elif choice == "b":
            show_stats()
        elif choice == "c":
            print("Goodbye Geissi!")
            exit()

        else:
            print("Please enter a, b, or c")
