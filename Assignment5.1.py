import sys
def throws():
    return 5/0

try:
    throws()
except ZeroDivisionError:
    print ("division by zero!")
except Exception as err:
    print ('Caught an exception', sys.exc_info()[0])
finally:
    print ('In finally block for cleanup')		