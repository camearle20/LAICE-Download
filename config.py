import ConfigParser
import os

# Default values
defaults = {
    "mysql": {
        "address": "0.0.0.0",
        "username": "user",
        "password": "pass",
        "database": "db"
    },
    "output": {
        "location": "~/"
    },
    "general": {
        "interval": "10s"
    }
}

parser = ConfigParser.ConfigParser()  # Get a parser instance
settings = None


def read_config():
    global settings

    for (section, local_settings) in defaults.iteritems():  # Iterate the sections
        parser.add_section(section)  # Add the section to the parser
        for setting, value in local_settings.iteritems():  # Iterate the values
            parser.set(section, setting, value)  # Add the section, setting, and value to the defaults

    if os.path.isfile("config.ini"):
        parser.read("config.ini")
    else:
        parser.write(open("config.ini", "wb"))

    settings = parser._sections


def get(section, key):
    return settings[section][key]
