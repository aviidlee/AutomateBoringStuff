# Web scraping 
## Getting the web page 

    import requests
    response = requests.get((<url string>))
    response.raise_for_status() 
    response.text 

## Saving web pages to disk
Important thing here is that we must preserve **unicode** encoding.
Thus we require the `wb` (write in binary) option.

    res = requests.get(<url>)
    # Check that we actually got the page 
    res.raise_for_status()
    file = open(<fileName>, 'wb')
    # Handle file in parts to avoid consuming lots of memory
    for chunk in res.iter_content(<number of bytes each chunk contains>):
        file.write(chunk)

## Parsing HTML 
    import bs4
    soupObject = bs4.BeautifulSoup(<htmlText>)

To find html elements, use **CSS selectors**:
    soupObject.select('<html tag>')
    soupObject.select('div')
    soupObject.select('<css selector>')

Matches returned as a list of Tags
    tag.getText()
    str(tag)
    tag.attrs
    tag.get(<attribute, like href or src>)