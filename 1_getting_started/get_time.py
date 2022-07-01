import datetime

now = datetime.datetime.now()
print(now)
print(type(now))

print("Please Enter:", input())
new_now = datetime.datetime.now()
print(new_now)
print((new_now-now).seconds)
print(type(new_now-now))