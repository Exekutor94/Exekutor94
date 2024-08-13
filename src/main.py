import keyboard
from time import sleep
from datetime import datetime, timedelta



def main():

    # intro talk
    version = "0.1"
    print("Welvome to SFGame-DailyBot v" + version)
    print("\t\t\t-by Gaara3San\n")
    print("Place your game on main monitor and on fullscreen\n")

    # init
    iter_number = 0
    time_start = datetime.now()
    time_now = time_start + timedelta(minutes=90)

    ATTACK_TIMER = 605

    # main loop
    while True:
        # exit program
        if keyboard.is_pressed("q") or keyboard.is_pressed("esc"):
            break
        
        time_diff_sec = (time_now - time_start).total_seconds()

        # player attack timer
        if time_diff_sec > ATTACK_TIMER:
            print("Attacking!")
            time_start = time_now
        else:
            print(f"Attack is not ready! Wait {round((ATTACK_TIMER/60)-(time_diff_sec/60), 2)} minutes")

        time_now = datetime.now()
        # wait until next iteration
        sleep(10)
        iter_number += 1
        if iter_number > 30:
            iter_number = 0

    print("See you soon! 😼")


if __name__ == "__main__":
    main()
