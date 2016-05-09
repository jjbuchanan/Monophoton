mkdir datacards
mkdir results
python datacard_command_printer.py > datacard_assembler_commands.sh
chmod 777 datacard_assembler_commands.sh
./datacard_assembler_commands.sh
python limit_command_lister.py > results/limit_commands.sh
cd results
chmod 777 limit_commands.sh
./limit_commands.sh
cd ..
python results_lister.py > combined_results.txt
