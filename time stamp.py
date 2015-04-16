import time
import datetime

List = []
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime("%m-%d-%Y %H:%M:%S")
idL = input( "Enter ID:" )
timeStamp = idL +" "+ st
List.append(timeStamp)
print(List)
