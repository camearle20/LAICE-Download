# LAICE Data downloader
# Pulls data from the UVI database
# and parses it into a human readable
# format

import config  # Import the config parser and read the config
config.read_config()

import MySQLdb  # Driver for reading mysql data
import time

import parser

VERSION = 1.0

# Delays for the time set in the config, or defaults to 1 second
def wait():
    interval = config.get("general", "interval")
    timeUnit = ''.join([i for i in interval if not i.isdigit()])
    multiplier = 1
    if (timeUnit == 's'):
        multiplier = 1
    elif (timeUnit == 'm'):
        multiplier = 60
    elif (timeUnit == 'h'):
        multiplier = 3600
    elif (timeUnit == 'd'):
        multiplier = 86400
    try:
        delay = int(''.join([i for i in interval if i.isdigit()]))
    except:
        delay = 1
    delay = delay * multiplier
    time.sleep(delay)


if __name__ == "__main__":
    print "LAICE Downloader v" + str(VERSION)
    print "Will pull from " + config.get("mysql", "username") + "@" + config.get("mysql", "address") + " on database " + config.get("mysql", "database")
    print "Outputting to " + config.get("output", "location")
    print "Fetching data every " + config.get("general", "interval")

    db = MySQLdb.connect(host=config.get("mysql", "address"),  # Connect to the database with the configured settings
                         user=config.get("mysql", "username"),
                         passwd=config.get("mysql", "password"),
                         db=config.get("mysql", "database"))

    cur = db.cursor()  # Get a "cursor" which can be used to execute queries

    cur.execute("SELECT * FROM datatable")

    row = cur.fetchall()[0]
    print parser.parse(row[1])
