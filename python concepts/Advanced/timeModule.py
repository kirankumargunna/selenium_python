# import time
# from datetime import timedelta, datetime
# from logging import Formatter
# import logging
#
# from IPython.core.magics.execution import Timer
#
# #
# # from sqlalchemy.sql.functions import localtime
# #
# # print(time.gmtime(1))
# #
# # print(time.time())   #time in second since epoch
# # print(time.ctime(time.time()))  #humman readable time format
# #
# # print(time.localtime(time.time()))
# #
# #
# # s = time.strftime("%a, %b %d %Y %H:%M:%S:%f",time.gmtime(time.time()))
# # print(s)
# #
# # print(time.asctime(time.gmtime()))
# #
#
#
# t=time.gmtime()  # strucuted time
# print(t)
# t=time.time()
# print(t)         # unix time or timestamp epoch format
#
# t=time.localtime(time.time())
# print(t)
#
# t=time.asctime(t)
# print(t)
# print( "lsdjfld",Formatter.converter(1739357356.1798453))
#
# print(Formatter.converter(time.time()).tm_gmtoff)  #returns the time zone offset in seconds from UTC (i.e., the difference between local time and UTC).in seconds
#
# print(timedelta(seconds=(Formatter.converter(time.time()).tm_gmtoff)))  # return time in the format of days.hours.min.seconds
#
#
#
# timezone=Formatter.converter(time.time()).tm_zone
# print("timezone  ", timezone )
# seconds=timedelta(seconds=Formatter.converter(time.time()).tm_gmtoff)
# print(seconds)
#
# Timezone=timezone(timedelta(seconds=seconds), timezone)
#
# print(Timezone)


import sys
from _pytest._io import TerminalWriter

# Manually providing a stream like sys.stdout (terminal output)
def custom_function(writer: TerminalWriter):
    writer.write("This is a custom message", yellow=True)
    writer.write("This is an error message", red=True)
    writer.write("This is a success message", green=True)

# Create a TerminalWriter instance with sys.stdout and pass it to the function
custom_function(TerminalWriter(sys.stdout))
