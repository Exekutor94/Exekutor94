import win32gui



def _window_enum_handler(hwnd, resultList):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        resultList.append((hwnd, win32gui.GetWindowText(hwnd)))


# this function searches for the Game Application and returns it window_handle
def _get_app_list(handles=[]):
    mlst = []
    win32gui.EnumWindows(_window_enum_handler, handles)
    for handle in handles:
        if "Shakes & Fidget" in handle[1]:
            mlst.append(handle)
    return mlst

def get_full_window_size(config=None):
    print()
    # search for the Game Window and store it in the shakes variable
    if config is not None and isinstance(config.WINDOW_SIZE, tuple):
        rect = [0, 0, config.WINDOW_SIZE[0], config.WINDOW_SIZE[1]]
        print(f"📏📓\tWindow size set by config file - {rect}")
    else:
        appwindows = _get_app_list()
        if len(appwindows) == 0:  # SFGame app not found
            rect = [0, 0, 1928, 1048]
            print(f"📏❌\tSteam game not found, set to default value - {rect}")
        else:
            shakes = appwindows[0][0]
            # set the Game Window as the active window
            win32gui.SetForegroundWindow(shakes)
            # store the coordinates which we use later to find and crop the images
            rect = win32gui.GetWindowRect(shakes)
            print(f"📏🧿\tWindow size set by Steam app - {rect}")
    if rect[2] < 10 or rect[3] < 10:
            print(f"📏❌\tSteam game is minimalized or invalid config values (too small size values), set to default value - {rect}")
            rect = [0, 0, 1928, 1048]
    print()
    return rect

def get_arena_cropbox(rect = None, config=None):
    rect = get_full_window_size(config) if rect is None else rect
    leftcrop = int(rect[2] / 1.68)
    topcrop = int(rect[3] / 29.94)
    rightcrop = int(rect[2] / 38.56)
    botcrop = int(rect[3] / 2.49)
    #print(f"📐✅\tFinal crop image")
    return (leftcrop, topcrop, rightcrop, botcrop)
