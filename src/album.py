from time import sleep, time
import math

import keyboard  # pip install keyboard

from utils.window_size import get_arena_cropbox
from utils.screenshot import *


class Album:
    def __init__(self, screen_size, position, direction="up", config=None):
        self.position = position
        self.scan_direction_key = "down" if direction == "down" else "up"
        self.screen_size = screen_size
        self.cropbox = get_arena_cropbox(screen_size, config)
        self.config = config
        self.old_image_crop = None
        self.speed = 1
        self.min_diff_scrap = 30
        # images
        init_crop_img = crop_screenshot(self.screen_size, self.cropbox)
        self.black_bg_img = None        
        try:
            self.mask_img = load_image('files/mask.png').convert("L").resize(init_crop_img.size)
        except Exception as e:
            print(f"Problem with mask - {e}")
            self.mask_img = None
        self.black_bg_img = create_black_image(init_crop_img.size)
        #mask_img.save("DEBUG/mask_img_debug.png")
        #black_bg_img.save("DEBUG/black_bg_img_debug.png")

    def _open_HoF(self, position):
        pass

    def _find_player(self):
        t_before = time()
        sleep(self.speed*3)
        for iter in range(1000):
            if keyboard.is_pressed("q") or keyboard.is_pressed("esc"):
                break
            base_image_crop = crop_and_mask_screenshot(self.screen_size, self.cropbox, self.black_bg_img, self.mask_img)
            #new_image_crop.save("DEBUG/first_base_img.png")
            # Player is not refreshed
            if self.old_image_crop is not None and compare(self.old_image_crop, base_image_crop) < 100.0:
                print(f"Player {self.position} is not refreshed")
                for _ in range(3):
                    sleep(self.speed*0.2)
                    keyboard.press_and_release("down")
                    sleep(self.speed*0.2)
                    keyboard.press_and_release("up")
                sleep(self.speed*0.3)
                base_image_crop = crop_and_mask_screenshot(self.screen_size, self.cropbox, self.black_bg_img, self.mask_img)
            # Check next player
            self.old_image_crop = base_image_crop
            base_image_crop.save(f"DEBUG/base_image_{iter}.png")
            for k in range(3):
                sleep(self.speed*0.3)
                tmp_image_crop = crop_and_mask_screenshot(self.screen_size, self.cropbox, self.black_bg_img, self.mask_img)
                tmp_image_crop.save(f"DEBUG/tmp_image_{iter}_{k}.png")
                diff_img = compare(base_image_crop, tmp_image_crop)
                print(f"Taking screenshot {k} player {self.position} - new difference {diff_img}")
                if diff_img > self.min_diff_scrap:
                    t_after = time()
                    seconds = math.ceil(t_after - t_before)
                    print(f"🤺🔍✅\tNew player with scrap was found! Searching time: {seconds} seconds. Position HoF: {self.position} ({iter}/1000)")
                    return (True, seconds)  # found, searching time
            if iter % 20 == 0:
                print(f"🤺🔍❌\tNew player with scrap not found ({iter}/1000)")
            self._move_to_next_player()
        t_after = time()
        return (False, math.ceil(t_after - t_before))  # found, searching time
    
    def _move_to_next_player(self):
        keyboard.press_and_release(self.scan_direction_key)
        sleep(self.speed*2)
        if self.scan_direction_key == "down":
            self.position += 1
        else:
            self.position -= 1

    def _attack(self):
        for _ in range(4):
            #keyboard.press_and_release("enter")
            sleep(1)
        print("Player killed")

    def find_and_kill_player(self):
        found, _ = self._find_player()
        if found:
            self._attack()
            self._move_to_next_player()
            found, searching_time = self._find_player()
            return searching_time if found else 0
        else:
            return 0
