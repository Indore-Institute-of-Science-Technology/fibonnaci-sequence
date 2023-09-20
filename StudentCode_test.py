import StudentCode;
from IOWrapper import IOWrapper
testIO= IOWrapper()
expectedIO= IOWrapper()
expectedIO2= IOWrapper()
expectedIO3= IOWrapper()
def test_hello():
    expectedIO.print("Y Axis")
    expectedIO2.print("X Axis")
    expectedIO3.print("No Axis")
    assert (StudentCode.runner(testIO,0,2)).check(expectedIO)
    assert (StudentCode.runner(testIO,2,0)).check(expectedIO2)
    assert (StudentCode.runner(testIO,2,2)).check(expectedIO3)
    print("Passed")
    #"X axis" or print "Y Axis"
