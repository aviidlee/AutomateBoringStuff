#! python3
# Opens several Google search results. Modified from Al Sweigart's book.

import requests, sys, webbrowser, bs4, time

if __name__ == '__main__':
    usage = ''
    
    if len(sys.argv) < 3:
        print usage 
        sys.exit()

    try:
        numPages = int(sys.argv[1])
    except ValueError:
        print 'First argument must be the number of pages to open.'

    print('Googling ' + ' '.join(sys.argv[2:]))
    res = requests.get('http://google.com/search?q=' + ' '.join(sys.argv[2:]))
    res.raise_for_status()

    print('Search successfull. Opening links...')
    soup = bs4.BeautifulSoup(res.text)
    linkElems = soup.select('.r a')
    numOpen = min(numPages, len(linkElems))
    
    if(numOpen > 0):
        webbrowser.open_new('http://google.com' + linkElems[0].get('href'))
        time.sleep(2)
    else:
        print "No results found."

    for i in range(1, numOpen):
        webbrowser.open_new_tab('http://google.com' + linkElems[i].get('href'))

