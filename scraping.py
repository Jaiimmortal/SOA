import bs4 as bs
import requests
import webbrowser

values = input('Enter the question or error ')

try:
    url = 'https://stackoverflow.com/search?q='+values

    resp = requests.get(url).text
    soup = bs.BeautifulSoup(resp,'lxml')
    print(soup.title.text)
    URLS = []
    title = []
    upvotes = []
    dicts = {}

    for votes in soup.find_all('span',class_='vote-count-post '):
        upvotes.append(votes.text)
    
    for div in soup.find_all('div',class_='question-summary search-result'):
        a = div.find('a')
        URLS.append('https://stackoverflow.com' + a.attrs['href'])
        title.append(a.attrs['title'])
        
    print(str(len(URLS)) + ' number of hits!')
    
    print('Choice \t Upvotes \t Title of the question')
    for eachHit in range(len(title)):
        print(str(eachHit+1) + '\t' + upvotes[eachHit] + '\t\t' + title[eachHit])
    for eachurl in range(len(URLS)):
        dicts[eachurl+1] = URLS[eachurl]

    ch = int(input("Enter the choice "))
    answer = dicts.get(ch)
    webbrowser.open_new(answer)

except Exception as e:
    print(str(e))
    


    
