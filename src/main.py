import keyboard

from utils.timer import Timer
from album import Album


def main():

    # intro talk
    version = "0.1"
    print("\nWelvome to SFGame-DailyBot v" + version)
    print("\t\t\t-by Gaara3San\n")
    print("Place your game on main monitor and on fullscreen\n")

    # init
    timer = Timer(sleep_duration=5)
    position = 10000
    album = Album(position)

    # main loop
    while True:
        # player attack
        if timer.is_arena_ready():
            searching_time = album.find_and_kill_player()
            timer.restart_arena_timer()
            print(searching_time)
            timer.redute_timer(searching_time)
            
        # wait until next iteration
        timer.print_remaining_time()
        if timer.sleep(10):  # press 'q' or 'esc' to exit program
            break

    print("See you soon! 😼\n")


if __name__ == "__main__":
    main()
