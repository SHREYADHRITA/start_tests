from configparser import ConfigParser

config = ConfigParser()

config["default"] = {
    "digits": 1000,
    "max_tries": 5,
    "plyer_name": "unknown"
}
config["Shreya"] = {
    "digits": 1000,
    "max_tries": 5,
    "plyer_name": "shreya",
    "cheat": "on"
}


with open("number.ini", "w") as f:
    config.write(f)