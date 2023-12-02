## To execute vm_translator_v2.py:

Have vm_translator_v2.py and folder containing your vm files are in the same folder/directory.

Then type Python vm_translator_v2.py [project-final].asm ./[foldername]/ into the command line, make sure you are in Python 3.8.8 or higher. Then once it works it should create a new file called [project-final].asm. This will also create intermediate [filename].i files for each .vm file within the input folder. Use the Assembler.sh to convert the .asm file to a .hack file. Run the .hack file on the CPUEmulator.sh to verify functionality.

You can also use my own assembler and CPU that I designed.