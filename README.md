To get r limits:

Copy the folder "limits" into your working directory

Copy your own "acceptances_and_xsecs.txt" into that folder

 - Each line in acceptances_and_xsecs.txt should have the format
    Label Acceptance Xsec(in pb)
 - A working example is provided

Within that folder, run getLimits.sh

The output will be a file "combined_results.txt" whose lines have the format

 Label Observed Expected_2p5 Expected_16p0 Expected_50p0 Expected_84p0 Expected_97p5

How getLimits.sh gets the limits:

For each sample, it takes Acceptance*Xsec and multiplies this by the integrated luminosity

(specified by the variable "integrated_lumi" in datacard_command_printer.py) to obtain the

expected number of signal events occurring in data.

In order to guarantee convergence when using the combine tool, the true expected event number

is scaled to lie between 0.1 and 1.0 by a scale factor. This scale factor is recorded and

later used to de-scale the results of combine to obtain the true limit values.

A datacard is assembled for each sample, with the only difference among the datacards being

the (scaled) expected number of signal events. The datacard setup is specified in

datacard_boilerplate_1.txt, datacard_assembler.py, and datacard_boilerplate_2.txt.

These datacards are submitted to the combine tool one after the other. The results are scaled

by the appropriate factor and collected in combined_results.txt.