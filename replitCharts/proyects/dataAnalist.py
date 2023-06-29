import statistics as st
import numpy

variableA = [1,2,3,4,5,6,7,8,9]
print('Esto no se debe de estar llamando')

if __name__ == '__dataAnalist__':
  def mean(listNumbers):
    result = numpy.mean(listNumbers)
    return result
  def median(listNumbers):
    result = numpy.median(listNumbers)
    return result
  def mode(listNumbers):
    num = numpy.array(listNumbers)
    result = st.mode(num)
    return result
  def range(listNumbers): 
    result = numpy.ptp(listNumbers)
    return result