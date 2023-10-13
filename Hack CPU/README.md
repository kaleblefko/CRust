# Hack CPU
Folder containing projects designed to create the Hack CPU architecture.

Rundown of file types:
- .hdl is a HDL file, this is the code that was written
- .cmp is a compare file, the hardware simulator would compare the hdl output to this to verify, this can be looked at to understand expected behavior
- .tst is a test file that would set the inputs of .hdl files and run the logic gate circuits coded within to produce an output that was then compared to the .cmp file
