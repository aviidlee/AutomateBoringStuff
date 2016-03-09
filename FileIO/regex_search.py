# Project in chapter 8 of Al Sweigart's automation book. 

# Would be more useful to have the program also return which
# file the matching line was from. 

import sys, os, re

def find_matches(dir, regex):
    matches = []
    recursive_find_matches(dir, regex, matches)
    return matches

def recursive_find_matches(dir, regex, matches):
    '''Open all .txt files in dir and puts matching lines into matches.

    Parameters:
        -- dir string the absolute path of directory to search in 
        -- regex re.compile the regular expression 
    
    Require: dir is an existing directory  
    '''
    print "Processing items in directory %s" % (dir)

    # TODO regex isn't quite correct; should have $ at end, but python errors.
    isText = re.compile(r'txt')

    for item in os.listdir(dir):
        print "Processing %s" % (item)
        # for isfile to work, must provide the path, not just file name! 
        filePath = os.path.join(dir, item)
        if os.path.isfile(filePath):
            # Check is a .txt file 
            if(isText.search(item) != None):
                file = open(filePath)
                print filePath
                lines = file.readlines()
                for line in lines:
                    res = re.findall(regex, line)
                    if len(res) > 0:
                        matches.append(line)
                     
                file.close()

        else:
            print "Found directory; searching recursively..."
            recursive_find_matches(os.path.join(dir, item), regex, matches)

    return

if __name__ == "__main__":
    usageMessage = "Usage: regex_search.py <directory to search in> <regex>"
    
    if len(sys.argv) != 3:
        print usageMessage
        sys.exit()

    directory = os.path.abspath(sys.argv[1])
    

    if not os.path.isdir(directory):
        print "Supplied directory ", directory, "does not exist."
        sys.exit()

    try:
        regex = re.compile(sys.argv[2])
        matches = find_matches(directory, regex)
        if len(matches) == 0:
            print "No matches found."
        for match in matches:
            print match

    except:
        print "Unexpected error occured: ", sys.exc_info()[0]
        sys.exit()


    