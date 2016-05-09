from __future__ import print_function
import sys

for line in open("acceptances_and_xsecs.txt").readlines():
  line = line.strip()
  if len(line) < 2:
    continue
  parts = line.split()
  label = parts[0]
  acceptance = float(parts[1])
  xsec = float(parts[2])
  integrated_lumi = 2320.0
  true_rate = acceptance*xsec*integrated_lumi
  rate_for_card = true_rate
  r_true_multiplier = 1.0
  while rate_for_card > 1.0:
    rate_for_card /= 10.0
    r_true_multiplier /= 10.0
  while rate_for_card < 0.1:
    rate_for_card *= 10.0
    r_true_multiplier *= 10.0
  print("python datacard_assembler.py "+str(rate_for_card)+" > datacards/datacard_"+label+".txt")
  print("echo '"+label+" "+str(r_true_multiplier)+"' >> r_true_multipliers.txt")
  print("echo datacard_"+label+".txt >> datacard_list.txt")