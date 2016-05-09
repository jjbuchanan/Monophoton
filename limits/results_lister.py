from __future__ import print_function
import sys

print("Label Observed Expected_2p5 Expected_16p0 Expected_50p0 Expected_84p0 Expected_97p5")

r_true_multipliers = {}
for line in open("r_true_multipliers.txt"):
  line = line.strip()
  if len(line) < 2:
    continue
  label = line.split()[0]
  scale_factor = float(line.split()[1])
  r_true_multipliers[label] = scale_factor

for datacard in open("datacard_list.txt").readlines():
  datacard = datacard.strip()
  if len(datacard) < 2:
    continue
  label = datacard[len("datacard_"):-len(".txt")]
  result = "results/results_"+label+".txt"
  observed = "not_found"
  expected2p5 = "not_found"
  expected16p0 = "not_found"
  expected50p0 = "not_found"
  expected84p0 = "not_found"
  expected97p5 = "not_found"
  for line in open(result).readlines():
    line = line.strip()
    if len(line) > len("Observed Limit: r < ") and line[:len("Observed Limit: r < ")]=="Observed Limit: r < ":
      observed_scaled = float(line[len("Observed Limit: r < "):])
      observed_true = r_true_multipliers[label]*observed_scaled
    elif len(line) > len("Expected 2.5%: r < ") and line[:len("Expected 2.5%: r < ")]=="Expected 2.5%: r < ":
      expected2p5_scaled = float(line[len("Expected 2.5%: r < "):])
      expected2p5_true = r_true_multipliers[label]*expected2p5_scaled
    elif len(line) > len("Expected 16.0%: r < ") and line[:len("Expected 16.0%: r < ")]=="Expected 16.0%: r < ":
      expected16p0_scaled = float(line[len("Expected 16.0%: r < "):])
      expected16p0_true = r_true_multipliers[label]*expected16p0_scaled
    elif len(line) > len("Expected 50.0%: r < ") and line[:len("Expected 50.0%: r < ")]=="Expected 50.0%: r < ":
      expected50p0_scaled = float(line[len("Expected 50.0%: r < "):])
      expected50p0_true = r_true_multipliers[label]*expected50p0_scaled
    elif len(line) > len("Expected 84.0%: r < ") and line[:len("Expected 84.0%: r < ")]=="Expected 84.0%: r < ":
      expected84p0_scaled = float(line[len("Expected 84.0%: r < "):])
      expected84p0_true = r_true_multipliers[label]*expected84p0_scaled
    elif len(line) > len("Expected 97.5%: r < ") and line[:len("Expected 97.5%: r < ")]=="Expected 97.5%: r < ":
      expected97p5_scaled = float(line[len("Expected 97.5%: r < "):])
      expected97p5_true = r_true_multipliers[label]*expected97p5_scaled
  toPrint = label+" "+str(observed_true)+" "+str(expected2p5_true)+" "+str(expected16p0_true)+" "+str(expected50p0_true)+" "+str(expected84p0_true)+" "+str(expected97p5_true)
  print(toPrint)