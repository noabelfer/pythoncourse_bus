import os


def search_files(path, extension) -> list:
    fileslist = []
    filesname = []
    for (root, dirs, files) in os.walk(path):
        for f in files:
            if f.endswith("." + extension):
                fileslist.append(os.path.join(root, f))
                filesname.append(f)
                count_col_line(f)



def count_col_line(path) -> tuple:

    with open(path) as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
        print(len(lines))
        ncol = 1+ lines[0].count(',')
        print(path,len(lines),ncol)
        return(ncol, len(lines))
