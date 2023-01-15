
# Make tracking my times easy!

from datetime import datetime
import time
from classy import *
import pickle as pickle # for long term storage

filename = "timesheet.pickle"

# gets the timesheet from bin file
def myUnpickle(fn):
    with open(fn, "rb") as in_file:
        o = pickle.load(in_file)
    return o

# writes the timesheet back to bin file
def myPickle(o, fn):
    with open(fn, "wb") as out_file:
        pickle.dump(o, out_file, protocol=pickle.HIGHEST_PROTOCOL)
    return 0

# get valid input
first_in = input("(s)tart work \n(r)eport \n(o)verride mode \n> ")
while first_in not in ["s", "r", "o"]:
    first_in = input("invalid input \n(s)tart work \n(r)eport \n(o)verride mode \n> ")

# start work
if first_in == "s":
    start_time = time.time() # number of secounds from jan 1 1970 (start of unix time)
    end_in = input("working... \n(e)nd work \n> ")
    while end_in != "e":
        end_in = input("invalid input \n(e)nd work \n> ")
    hours_worked = (time.time() - start_time) / 60 / 60
    # make new shift
    shift = Shift(hours_worked)
    sheet = myUnpickle(filename)
    # add this shift to the sheet
    sheet.addShift(shift)
    # write the sheet back to file
    myPickle(sheet, filename)
    print(shift.report())

# report mode
elif first_in == "r":
    # read the sheet from pickle
    sheet = myUnpickle(filename)
    sheet.report()

# override mode
elif first_in == "o":
    # get sheet of times from pickle file
    sheet = myUnpickle(filename)
    sheet.report()
    minus_hours = input("number of hours to remove: ")
    while not minus_hours.replace(".", "").isnumeric():
        minus_hours = input("real numbers only: ") 
    # subtract minus hours from anywhere on the sheet
    while minus_hours > 0:
        sheet.shifts[0].hours -= minus_hours
        # either we need to subtract from the next shift as well
        if sheet.shifts[0].hours < 0:
            minus_hours = sheet.shifts[0].hours * -1
            del sheet.shifts[0]
        # or we're done subtracting here
        else:
            minus_hours = 0
    # write the sheet back to file
    myPickle(sheet, filename)
    print("done")

