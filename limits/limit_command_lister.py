from __future__ import print_function
import sys

for datacard in open("datacard_list.txt").readlines():
  datacard = datacard.strip()
  if len(datacard) < 2:
    continue
  label = datacard[len("datacard_"):-len(".txt")]
  toPrint = "combine -M Asymptotic ../datacards/"+datacard+" -n "+label+" | while read SRC; do echo $SRC; done > results_"+label+".txt"
  print(toPrint)