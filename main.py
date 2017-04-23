import bs4 as bs
import requests
import webbrowser

values = input('Enter the question or error ')
try:
    url = 'https://stackoverflow.com/search?q='+values
    print(url)
    resp = requests.get(url).text
    soup = bs.BeautifulSoup(resp,'lxml')
    print(soup.title.text)
    URLS = []
    title = []
    dicts = {}
    for div in soup.find_all('div',class_='question-summary search-result'):
        a = div.find('a')
        URLS.append('https://stackoverflow.com' + a.attrs['href'])
        title.append(a.attrs['title'])
    print(str(len(URLS)) + ' number of hits!')
    for eachHit in range(len(title)):
        print(str(eachHit+1) + ' ' + title[eachHit])
    for eachurl in range(len(URLS)):
        dicts[eachurl+1] = URLS[eachurl]

    ch = int(input("Enter the choice "))
    answer = dicts.get(ch)
    webbrowser.open_new(answer)

except Exception as e:
    print(str(e))
    
#headers = {}
#headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"

    
