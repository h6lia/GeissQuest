from timer.storage import load_data


def show_stats():
    data = load_data()

    print("\n-- Your stats ---")
    print(f"total clover stats: {data['total_clover']}")
    print(f"Total time today: {data['total_minutes']} minutes")
    input("\nPress Enter to return to the menu:")
