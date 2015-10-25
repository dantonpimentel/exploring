import re
import requests
from bs4 import BeautifulSoup, NavigableString, Tag


def clean_str(data):
    return data.strip()


class TagHandler(object):
    def __getattr__(self, item):
        return self.__dict__.get(item, self.default_handler)

    def process_data(self, tag_class, tag_content):
        return getattr(self, tag_class.replace(" ", "_"))(tag_content)

    @staticmethod
    def default_handler(tag_content):
        return TagHandler._extract_text(tag_content)

    @staticmethod
    def cardTitle(tag_content):
        return {'title': clean_str(tag_content.get_text()),
                'link': tag_content.a['href']}

    @staticmethod
    def manaCost(tag_content):
        return clean_str(" ".join(img['alt'] for img in tag_content.find_all("img")))

    @staticmethod
    def _extract_text(tag_content):
        text = ''
        if isinstance(tag_content, NavigableString):
            text += tag_content.strip()
        elif tag_content.name == 'img':
            text += '(' + tag_content['alt'] + ')'
        elif tag_content.children:
            for tag in tag_content:
                text += TagHandler._extract_text(tag)
        else:
            text += tag_content.get_text().strip()
        return text


URL = 'http://gatherer.wizards.com/Pages/Search/Default.aspx'

page = 0
cards = []
while True:
    response = requests.get(URL, params={'set': '["Battle for Zendikar"]',
                                         'page': str(page)})
    print(response.content)  # DEBUG
    html_parser = BeautifulSoup(response.content.decode('utf-8'), 'html.parser')
    tag_handler = TagHandler()

    for card_info in html_parser.find_all("div", attrs={"class": "cardInfo"}):
        card = {}
        for tag in card_info:
            if isinstance(tag, NavigableString) or tag.name == "br":
                continue
            class_attr = tag['class'][0]
            card[class_attr] = tag_handler.process_data(tag_class=class_attr, tag_content=tag)
        cards.append(card)

    #if not html_parser.find_all('a', string=' >'):
    if not any(a.get_text().strip() == '>' for a in html_parser.find_all(
            "a", href=re.compile('.*/Pages/Search/Default\.aspx.*'))):
        break

    page += 1

print('-----')
for card in cards:
    for k, v in card.items():
        print("{} = {}".format(k, v).encode('utf-8'))
    print('-----')

print("Total amount of cards queried: {}".format(len(cards)))
print('-----')