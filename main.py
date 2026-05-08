from timer.timer import choose_time, choose_display_mode, start_timer
from timer.utils import reset_daily_minutes
from timer.storage import load_data, save_data
from menu.menu import run_menu


def main():
    print(""
          "Hello Geissi!")
    run_menu()
    data = load_data()
    reset_daily_minutes(data)

    minutes = choose_time()
    show_countdown = choose_display_mode()

    start_timer(minutes, show_countdown)

    clover = minutes // 10
    data['total_minutes'] += minutes
    data['total_clover'] += clover
    save_data(data)





    print(f"Congrats, you worked for {minutes} minutes today!")
    print(f"You've earned {clover} Clover(s) so far")


if __name__ == "__main__":
        main()
