
# Only run when setting a new timesheet

import pickle
from classy import *

filename = input("WARNING only run when setting up a new timesheet! \nfilename(*.pickle): ")
with open(filename + ".pickle", "wb") as out_file:
    sheet = Sheet()
    pickle.dump(sheet, out_file, protocol=pickle.HIGHEST_PROTOCOL)
print("done")

