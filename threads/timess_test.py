import time

print(time.ctime(0))
print(time.ctime(100000))

print(time.ctime(time.time()))

time_obj = time.localtime()
print(time_obj)

time.strftime("%B %d %Y %H:%M:%S", time_obj)

utc_obj = time.gmtime()

time.strftime("%B %d %Y %H:%M:%S", utc_obj)

time_sting = "20 April, 2026"

tobj = time.strptime(time_sting, "%d %B, %Y")
tobj.tm_year

time_tup = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
time_str = time.asctime(time_tup)

time.mktime(time_tup)
