import os


def search_path(path: str) -> dict:
    files_dict = {}
    files_list = []
    files_and_dirs = os.listdir(path)
    # print(files_and_dirs)

    for a in files_and_dirs:
        if a is dir():
            files_dict[]=a
        os.walk(a)
    print(files_dict)


if __name__ == '__main__':
    d = search_path('/Users/noabelfer/Downloads')

