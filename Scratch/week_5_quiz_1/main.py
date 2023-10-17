import os
def safe_open(pth, mode='rt'):
    """ Opens the file in `pth` using the mode in `mode` and returns 
    a file object. 

    Will not open a file in writing mode if the file already exists and has
    some content.

    Parameters
    ----------
    pth : str
        Location of the file
    mode : str
        How to open the file. Typically 'w' for writing, 'r' for reading, 
        and 'a' for appending. See the `open` function for more options.
        Defaults to 'rt'
    """
    if 'r' in mode or 'a' in mode: #Condition 1
        open(pth,mode)
    elif 'w' in mode:
        if os.path.exists(pth) == False: #Condition 2
            open(pth,mode)
        elif os.path.exists(pth) == True: #Condition 3
            fobj = open(pth,"rt")
            fobj_2 = fobj.read()
            if len(fobj_2) >0:
                raise Exception
            else:
                open(pth,mode)
    else:
        raise Exception
    return open(pth,mode)

if __name__ == "__main__":
    # Opening an existing file with content for reading
    with safe_open("/Users/altrikowicaksono/PycharmProjects/FINS5546/Scratch/week_5_quiz_1/test_file_exists_with_content.txt", mode='r') as fobj:
       print(fobj.read())

    # Opening an existing file with no content for writing - should work
    with safe_open("/Users/altrikowicaksono/PycharmProjects/FINS5546/Scratch/week_5_quiz_1/test_file_exists_no_content.txt", mode='w') as fobj:
       fobj.write('content')


    # Opening an existing file with content for writing - should raise Exception
    with safe_open("/Users/altrikowicaksono/PycharmProjects/FINS5546/Scratch/week_5_quiz_1/test_file_exists_with_content.txt", mode='w') as fobj:
       fobj.write('content')


