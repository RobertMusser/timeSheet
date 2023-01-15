
from datetime import datetime
import time
import pickle # for long term storage

# represents an entrie sheet of shifts
# handles colapsing multiple shifts from one day
class Sheet:
    def __init__(self):
        self.shifts = []

    # adds a new shift. If theres another shift in that day already, collapses hours
    def addShift(self, newShift):
        for oldShift in self.shifts:
            if oldShift.date == newShift.date:
                # collapse hours
                newShift.hours += oldShift.hours
                # remove dup shift
                self.shifts.remove(oldShift)
        self.shifts.append(newShift)

    def report(self):
        earned = 0
        for s in self.shifts:
            print(s.report())
            earned += s.hours * 14.05
        print("total earnings: " + str(earned))

# represents a shift of work. Has date and duration
class Shift:
    def __init__(self, duration):
        self.date  = datetime.today().strftime("%d/%m/%Y") 
        self.hours = duration

    def report(self):
        return str(self.date) + ": " + str(self.hours) + " hour(s)"

