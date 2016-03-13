# rename_dates.py 
# Given a directory, looks for files whose names contain an American-style date
# and renames such files to have European-style (DD-MM-YY) dates instead.

# From Chapter 9 of Al Sweigart's Automate the boring stuff book. 

# Single digit day/months MUST have leading 0's; i.e., must be 04-12-2012 rather than
# 4-12-2012. We also note that some dates are ambiguous (03-02-2016 could be from either
# style) and that we cannot take this into account with regex. 

import re, os, shutil, sys

# Regex for identifying dates in the form MM-DD-YYYY
americanDate = re.compile(r'''^(.*?)
    ((0|1)\d)- # digits for month
    ((0|1|2|3)\d)- # digits for day 
    ((19|20)\d\d) # Digits for year 
    (.*?)$ # stuff after the date 
    ''', re.VERBOSE)

def rename_files(path):
    # Loop over files in working directory 
    for folder, subfolders, files in os.walk(path):
        for file in files:
            print file
            mo = americanDate.search(file)
            if mo == None:            
                continue

            month = mo.group(2)
            day = mo.group(4)
            year = mo.group(6)

            oldDate = month + '-' + day + '-' + year
            print oldDate
            europeanDate = day + '-' + month + '-' + year 
            print europeanDate
            newFile = file.replace(oldDate, europeanDate)
            
            print 'Renaming %s to %s' % (file, newFile)

            fullOldPath = os.path.abspath(os.path.join(folder, file))
            fullNewPath = os.path.abspath(os.path.join(folder, newFile))
            shutil.move(fullOldPath, fullNewPath)

if __name__ == '__main__':
    usage = 'Usage: rename_files <directory>'
    if len(sys.argv) != 2:
        print usage 
        sys.exit()

    path = sys.argv[1]

    if(not os.path.isdir(path)):
        print "%s is not a directory" % path
        sys.exit()

    print "Renaming files in %s to have Europena-style dates..." % path 
    rename_files(path)