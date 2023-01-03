# Implement a function that receives the following arguments:
# file_path (str, a path to a local file)
# start_line (int, line number to start reading from)
# end_line (int, the last line to read)
# The function should return a string that contains the lines
# that have been read. Note, you should check the correctness of
# the arguments (for example, whether there are enough lines in the file,
# or whether the file exists). Raise exceptions when needed.
import os.path


def file_function(file_path:str, start_line:int, end_line:int):
    with open(file_path,"r") as fh:
        lines = []
        if not os.path.exists(file_path):
            raise ValueError
        if end_line < start_line:
            raise ValueError
        for i,line in enumerate(fh):
            lines.append(line)
        if len(lines) < start_line or len(lines) < end_line:
            raise ValueError
        print(lines[start_line:end_line])

a = file_function("/Users/noabelfer/Downloads/alice_in_wonderland (1).txt", 5,20)

