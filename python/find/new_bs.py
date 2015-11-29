import urllib2
from BeautifulSoup import BeautifulSoup
def getFBDirectory(url):
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page)
    L = soup('ul')
    soup = BeautifulSoup(''.join(str(l) for l in L))
    L = soup('li')
    soup = BeautifulSoup(''.join(str(l) for l in L))
    L = soup('a')
    all_names = []
    for l in L:
        all_names.append({'name':str(l.contents[0]).strip(), 'url':str(l['href'])})
    return all_names
print getFBDirectory("https://www.facebook.com/directory/people/G")
