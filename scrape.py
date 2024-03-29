import requests
from bs4 import BeautifulSoup
import pprint

for numpage in range(2,4):
  res= requests.get('https://news.ycombinator.com/news?p='+ str(numpage))
  soup= BeautifulSoup(res.text, 'html.parser')
  links = soup.select('.titleline > a')
  subtext =  soup.select('.subtext')

  def sort_by_votes(hnli):
    return sorted(hnli, key=lambda k:k['votes'], reverse=True)


  def create_custom_hn(links,subtext):
    hn = []
    for idx,item in enumerate(links):
      title = item.getText()
      href = item.get('href')
      vote= subtext[idx].select('.score')
      if len(vote):
        points = int(vote[0].getText().replace(' points', ''))
        if points > 99:
          hn.append({'title':title,'link':href, 'votes': points})
    return sort_by_votes(hn)

  pprint.pprint(create_custom_hn(links,subtext))