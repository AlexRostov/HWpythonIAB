# curtime = str(datetime.datetime.now())[-6:]
import datetime

randomNum = datetime.datetime.now().microsecond%10

print (f'Случайное число: {(randomNum) }')