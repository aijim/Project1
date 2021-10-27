import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    file_list = []

    if not os.path.exists(path):
        return file_list

    file_list = []
    if os.path.isfile(path):
        if path.endswith(suffix):
            file_list.append(path)
        return file_list
    else:
        files = os.listdir(path)
        for file in files:
            if file=="." or file=="..":
                continue
            if os.path.isfile(os.path.join(path,file)):
                if file.endswith(suffix):
                    file_list.append(os.path.join(path,file))
            else:
                file_list = file_list + find_files(suffix, os.path.join(path,file))

    return file_list

# test case 1 - find files in testdir
print(find_files(".c", "./testdir"))

# test case 2 - when a file path is specified
print(find_files(".h", "./testdir/testdir/t1.h"))

# test_case 3 - when specified path does not exist
print(find_files(".c", "./testdir/subdir6"))