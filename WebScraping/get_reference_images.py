''' Automatically download high-quality reference images matching the entered keywords.

@TODO use argparse to make commandline manipulations easier.
@TODO instead of taking an explicit file prefix, just use concat of search terms.
@TODO try to add sites besides flickr.
'''

import requests, sys, webbrowser, bs4, time, re, os, logging
import argparse 

### All of these globals get overwritten by main. 
# Number of images to retrieve; set through the commandline. 
numImages = 10
# Directory to store photos to. 
photoDir = ''
# Prefix of photo names
prefix = 'fox'
path = './'
imageCount = 0

logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')

def get_file_name():
    '''
    path - the folder in which we want to store the images
    prefix - the prefix of the photo name; e.g., fox. 
    
    returns the full path filename for the image.
    '''
    global imageCount
    imageCount = imageCount + 1
    fileName = '%s_%d.jpg' % (prefix, imageCount)
    return os.path.join(path, fileName)

# terms - list of search terms
def search_flickr(terms):
    # Search for large (minimum dimension 1024px) on Flickr
    res = requests.get('https://www.flickr.com/search/?dimension_search_mode=min&height=1024&width=1024&advanced=1&text=' + '%20'.join(terms))
    
    res.raise_for_status()

    # Get the script element in which all the delicious image URLs live
    script = bs4.BeautifulSoup(res.text)
    images = script.text.split('"pathAlias":')

    # the pathAlias, which is some kind of user ID, should be the first thing.
    aliasRe = re.compile(r'^"(.+)","username"')

    # For the id of the image itself; extracted from a bizarre URL(?) otf 
    # \\/\\/farm4.staticflickr.com\\/3821\\/18866248995_1c625e93a5_c.jpg
    # The important part is that you have 4 digits, \\/ then the id, then underscore.
    imageRe = re.compile(r'(\d{4}\\/)(\d+)_')

    # Because of the way we split, the first item in the list is just gunk
    for i in range(1, min(len(images), numImages)+1):
        #print images[i]
        pathAlias = aliasRe.search(images[i]).group(1)
        # Get the id of the actual image 
        imageID = imageRe.search(images[i]).group(2)
        # Download in original size
        imageURL = "https://www.flickr.com/photos/%s/%s/sizes/o/" % (pathAlias, imageID)
        print "Retrieving image from " + imageURL
        res = requests.get(imageURL)
        # It is possible that we are not allowed to download the original...
        if(res.status_code == 200):
            soup = bs4.BeautifulSoup(res.text)
            im = soup.select("#allsizes-photo img")
            src = im[0].get('src')
            res = requests.get(src)

            if res.status_code == 200:
                # Get the path name 
                path = get_file_name()
                logging.info('Writing image to disk with filename %s' % (path))
                with open(path, 'wb') as file:
                    for chunk in res:
                        file.write(chunk)
        else:
            i = i-1


if __name__ == '__main__':
    usage = 'Usage: get_reference_images.py <numImages> <folder> <filename prefix> <keywords>'
    
    if len(sys.argv) < 5:
        print usage 
        sys.exit()

    try:
        numImages = int(sys.argv[1])
    except ValueError:
        print 'First argument must be the number of images to download.'

    path = os.path.abspath(sys.argv[2])
    prefix = sys.argv[3]

    print 'Requested %d images to be saved to %s using filename prefix %s' % (numImages, path, prefix)
    print 'Searching Flickr using keyword(s) ' + ', '.join(sys.argv[4:])

    search_flickr(sys.argv[4:])



    
