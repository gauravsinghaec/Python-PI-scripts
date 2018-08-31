import os, re, sys

def search_files(impact_text,target_dir):
    """
    search_files: method to find impacted files
    Args:
        impact_text (data type: str): The keyword to be searched
        target_dir (data type: str): The directory path to be looked into
    Returns:

    Examples:
        >>>python findImpactedFile.py abc E:\folder1\folder2
        Impacted files are as below:
        1. E:\folder1\folder2\folder3\file1.html
        2. E:\folder1\folder2\folder3\file2.html
        3. E:\folder1\folder2\folder3\file3.html
        4. E:\folder1\folder2\folder4\file4.py
        5. E:\folder1\folder2\folder4\file5.py
    """
    # continue method implementation below.

    i = 1
    # Change the current working directory
    os.chdir(r"%s" % target_dir)
    rootdir =os.getcwd()
    # List all the files in the directory
    file_names = [os.path.join(dirpath, filename) for dirpath, dirnames, filenames in os.walk(rootdir)
                                 for filename in filenames]
    # Find the impact_text in all the files to get the impact list
    print("Impacted files are as below: ");
    for file_name in file_names:
        myfile = open(file_name,mode='r',encoding='ISO-8859-1')
        file_content = myfile.read()
        if file_name.find('.pyc') !=-1:
            pass
        elif file_content.find(impact_text) != -1:
            print(str(i) +". "+ file_name);
            i = i + 1

search_files(sys.argv[1],sys.argv[2])