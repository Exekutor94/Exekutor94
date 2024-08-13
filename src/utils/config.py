class Config:

    def __init__(self, file_name=None):
        self.config_dict = {}
        self._set_default_values()

        if file_name == None:
            file_name = "files/CONFIG.txt"

        try:
            with open(file_name, "r") as f:
                for line in f:
                    line = line.replace(" ", "")[:-1]
                    if line.startswith("#") or len(line) < 3:
                        continue
                    line_split = line.split("=")
                    if len(line_split) != 2:
                        continue
                    key = line_split[0].upper()
                    value = line_split[1].upper()
                    value = self._parse_value(value)
                    self.config_dict[key] = value
                    if self.config_dict["SETTINGS"] == False:
                        return
        except Exception as e:
            print(f"Reading config file - {e}")
        finally:
            self._set_file_values()

    def _set_default_values(self):
        self.MASK = True
        self.WINDOW_SIZE = None
        self.HOF_POSITION = None
        self.SCAN_DIRECTION_UP = None
        self.FILE_SAVE = True
        self.SPEED = 1
        self.DEBUG_ON = False
        self.SCAN_LIMIT = 5000
        self.DIFF_LIMIT = 3.0

        self.config_dict["SETTINGS"] = None
        self.config_dict["MASK"] = None
        self.config_dict["WINDOW_SIZE"] = None
        self.config_dict["HOF_POSITION"] = None
        self.config_dict["SCAN_DIRECTION_UP"] = None
        self.config_dict["FILE_SAVE"] = None
        self.config_dict["SPEED"] = None
        self.config_dict["DEBUG_ON"] = False
        self.config_dict["SCAN_LIMIT"] = None
        self.config_dict["DIFF_LIMIT"] = None


    def _parse_value(self, value):
        if len(value) == 0 or value == "NONE" or value == None:
            return None
        elif value == "TRUE":
            return True
        elif value == "FALSE":
            return False
        elif self._is_number(value):
            return float(value)
        elif self._is_tuple(value):
            tmp_tuple = str(value)[1:-1]
            tmp_list = tmp_tuple.split(",")
            return (int(tmp_list[0]),int(tmp_list[1]))
        else:
            return None


    def _is_number(self, value):
        if value is None:
            return False
        try:
            float(value)
            return True
        except:
            return False


    def _is_tuple(self, value):
        if value is None:
            return False
        value = str(value)
        if not value.startswith("("):
            return False
        if not value.endswith(")"):
            return False
        value = value[1:-1]
        tmp_tuple = value.split(",")
        if len(tmp_tuple) != 2:
            return False
        if not self._is_number(tmp_tuple[0]) or not self._is_number(tmp_tuple[1]):
            return False
        return True


    def _set_file_values(self):
        if isinstance(self.config_dict["MASK"], bool):
            self.MASK = self.config_dict["MASK"]
        if isinstance(self.config_dict["WINDOW_SIZE"], tuple):
            self.WINDOW_SIZE = self.config_dict["WINDOW_SIZE"]
        if isinstance(self.config_dict["HOF_POSITION"], float):
            number = int(self.config_dict["HOF_POSITION"])
            if number < 1:
                number = None
            elif number > 1000000000:
                number = 1000000000
            self.HOF_POSITION = number
        if isinstance(self.config_dict["SCAN_DIRECTION_UP"], bool):
            self.SCAN_DIRECTION_UP = self.config_dict["SCAN_DIRECTION_UP"]
        if isinstance(self.config_dict["FILE_SAVE"], bool):
            self.FILE_SAVE = self.config_dict["FILE_SAVE"]
        if isinstance(self.config_dict["SPEED"], float):
            number = self.config_dict["SPEED"]
            if number < 0:
                number = 1
            elif number > 10:
                number = 10
            self.SPEED = number
        if isinstance(self.config_dict["SCAN_LIMIT"], float):
            number = int(self.config_dict["SCAN_LIMIT"])
            if number < 10:
                number = 5000
            elif number > 1000000000:
                number = 1000000000
            self.SCAN_LIMIT = number
        if isinstance(self.config_dict["DIFF_LIMIT"], float):
            number = self.config_dict["DIFF_LIMIT"]
            if number < 0.1:
                number = 3.0
            elif number > 1000:
                number = 1000
            self.DIFF_LIMIT = number
