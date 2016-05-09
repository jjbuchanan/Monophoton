from __future__ import print_function
import sys

#Prints a datacard customized for a sample
#argv[1] = expected rate for the sample, multiplied by the r_true multiplier

for line in open("datacard_boilerplate_1.txt").readlines():
  line = line.strip()
  print(line)
toPrint = "rate             "
toPrint += sys.argv[1]
toPrint += "      42.10       10.69       7.35        1.366        5.90        3.07      4.00"
print(toPrint)
for line in open("datacard_boilerplate_2.txt").readlines():
  line = line.strip()
  print(line)