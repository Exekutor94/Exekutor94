import datetime as datetime
import time as time
import math as math
import keyboard



class Timer:

    def __init__(self, sleep_duration=None, arena_remaining_time = None):
        self.arena_total_time = (60*10) + 5  # 10 min in seconds (5 sec added to be save)
        self.arena_remaining_time = 0 if arena_remaining_time is None else arena_remaining_time
        self.sleep_duration = 5 if sleep_duration is None else sleep_duration
        self.iterator = 0
        self.max_iterator = math.ceil(180/self.sleep_duration)

    def sleep(self, new_duration=None):
        duration = self.sleep_duration if new_duration is None else new_duration
        for _ in range(duration):
            if keyboard.is_pressed("q") or keyboard.is_pressed("esc"):
                return True
            time.sleep(1)  # sleep - duration seconds
        self.redute_timer(duration)

    def redute_timer(self, duration):
        self.arena_remaining_time -= duration
        if self.arena_remaining_time < 0:
            self.arena_remaining_time = 0

    def is_arena_ready(self):
        return self.arena_remaining_time == 0
    
    def restart_arena_timer(self):
        self._restart_iterator()
        self.arena_remaining_time = self.arena_total_time

    def print_remaining_time(self):
        if self.iterator == 0:
            self._restart_iterator()
            print("🔚🎹\t Hold 'q' or 'esc' to exit program")
            if self.arena_remaining_time == 0:
                print("🤺✅\tAttack is ready!")
            else:
                if self.arena_remaining_time >= 60:
                    minutes = round((self.arena_remaining_time/60), 2)
                    suffix = f"{minutes} minutes"
                    if minutes < 2:
                        suffix = suffix[:-1]
                else:
                    suffix = f"{self.arena_remaining_time} seconds"
                    if self.arena_remaining_time == 1:
                        suffix = suffix[:-1]
                time_of_attack = datetime.datetime.now() + datetime.timedelta(seconds=self.arena_remaining_time)
                print(f"🤺❌\tAttack will be ready in {suffix}! ({time_of_attack.strftime('%H:%M:%S')})")
            print()
        else:
            self.iterator -= 1
    
    def _restart_iterator(self):
        self.iterator = self.max_iterator
