from utils.timer import Timer
from utils.window_size import get_full_window_size
from album import Album



def main():
    # intro talk
    version = "1.0"
    print("\nWelvome to SFGame-DailyBot v" + version)
    print("\t\t\t-by Gaara3San\n")
    print("Place your game on main monitor and on fullscreen\n")

    # init
    app_screen_size = get_full_window_size()
    hof_position = int(input("🤴\t Hall of Fame start position: "))
    arena_rem_time = int((float(input("🤺\t Arena remaining time (minutes): ")))*60.0) + 5
    timer = Timer(sleep_duration=5, arena_remaining_time=arena_rem_time)
    album = Album(screen_size=app_screen_size, position=hof_position)

    print()
    # main loop
    while True:
        # player attack
        if timer.is_arena_ready():
            searching_time = album.find_and_kill_player()
            timer.restart_arena_timer()
            timer.redute_timer(searching_time)
            print()
            
        # wait until next iteration
        timer.print_remaining_time()
        if timer.sleep(10):  # press 'q' or 'esc' to exit program
            break

    print("😼😴\t SFGame-DailyBot deactivated. See you soon!\n")


if __name__ == "__main__":
    main()
