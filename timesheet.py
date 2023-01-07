
# Make tracking my times easy!

from datetime import datetime
import time
import pickle # for long term storage
from classy import *

filename = "timesheet.pickle"

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
    # get sheet of times from pickle file
    with open(filename, "rb") as in_file:
        sheet = pickle.load(in_file)
    # add this shift to the sheet
    sheet.addShift(shift)
    # write the sheet back to file
    with open(filename, "wb") as out_file:
        pickle.dump(sheet, out_file, protocol=pickle.HIGHEST_PROTOCOL)
    print(shift.report())

# report mode
elif first_in == "r":
    # read the sheet from pickle
    with open(filename, "rb") as in_file:
        sheet = pickle.load(in_file)
    earned = 0
    for shift in sheet.shifts:
        print(shift.report())
        earned += shift.hours * 14.05
    print("total earned: " + str(earned))

# override mode
elif first_in == "o":
    print("override mode not implemented")

