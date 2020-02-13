import json
import datetime
import time

#
# Reads information about workers and their work shifts from the file specified by argv[1].
# The data is in JSON format.
# Computes and prints out the total number of hours and the corresponding total pay for each worker.
# The information is printed out in alphabetical order of names.
#
# JSON file contains following information:
# -list of workers
# -list of ID:s
# -list of times when workers have checked in to work
# -list of times when workers have checked out from work
#


def calculator(filename):
   data = {}
   with open(filename) as f:
      data = json.load(f)
      data['workers'].sort(key=lambda x: x['name'])
      data['checked out'].sort(key=lambda x: x['worker id'])
      data['checked in'].sort(key=lambda x: x['worker id'])

   for worker in data['workers']:
      workingTime = 0
      id = worker['id']
      name = worker['name']
      wage = float(worker['hourly wage'])
      checkOutTimes = []
      checkInTimes = []

      i = 0
      for checkOut in data['checked out']:
         if checkOut['worker id'] == id:
            checkOutTimes.append(data['checked out'][i]['time'])
         i += 1    

      j = 0
      for checkIn in data['checked in']:
         if checkIn['worker id'] == id:
            checkInTimes.append(data['checked in'][j]['time'])
         j += 1   

      for i in range(0,len(checkOutTimes)):
         time1 = time.strptime(checkOutTimes[i], '%Y-%m-%dT%H:%M:%S')
         time2 = time.strptime(checkInTimes[i], '%Y-%m-%dT%H:%M:%S')

         time1 = time.mktime(time1[:-1] + (0,))
         time2 = time.mktime(time2[:-1] + (0,))
         differ = time1-time2
         differ = differ / 60 / 60
         workingTime = workingTime + differ
         differ = 0
         time1 = None
         time2 = None

      print("{} {}: {} hours, hourly wage {}, total pay {}".format(id, name, workingTime,wage, wage*workingTime))

if __name__ == "__main__":
   calculator("shifts.json") 
   print()
   calculator("shifts2.json")