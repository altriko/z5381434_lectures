import os

MAINDIR = '/Users/altrikowicaksono/PycharmProjects/FINS5546/lectures'
SRCFILE = os.path.join(MAINDIR,'iso.txt')

def common_word(pth):
    '''
    Parameters
    -------


    Returns
    -------

    '''
    with open(pth, mode='rt') as fobj:
        content = fobj.read()
        content_2 = content.lower().split()
        dict = {}
        for i in content_2:
            if i not in dict.keys():
                dict[i] = 1
            elif i in dict.keys():
                dict[i] += 1
        maxcount = None
        maxword = None
        for word, count in dict.items():
            if maxcount is None or count > maxcount:
                maxword = word
                maxcount = count

        print(f"The most frequent word with {maxcount} mention is {maxword.upper()}")
        # sort_dict = sorted(dict.items(), key=lambda x: x[1])
        # print(sort_dict)
        # # return(f'The most common word is {} with {}')

## Solution from lecturer:
def freqword(filepath):
    with open(filepath) as file:
        counts = dict()
        for line in file:
            words = line.split()
            for word in words:
                counts[word] = counts.get(word,0) + 1
 # Find the most frequent word
        maxcount = None
        maxword = None
        for word,count in counts.items():
            if maxcount is None or count > maxcount:
                maxword = word
                maxcount = count
 # Return the result
    return(f"The most frequent word is: {maxword}, and the number of times appeared is: {maxcount}")
### Call the function
# freqword('iso.txt')


if __name__ == "__main__":
    # Test functions
    common_word(SRCFILE)
    print(freqword(SRCFILE))
