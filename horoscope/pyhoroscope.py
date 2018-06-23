import urllib.request
from lxml import etree
import re

####################################################################
# API
####################################################################

class Horoscope:

    @staticmethod
    def get_todays_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/horoscopes/daily-horoscope/" + sunsign
        response = urllib.request.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        date = str(tree.xpath(
			"//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        date = date.replace("['(", "").replace(")']", "")

        date_website = "-".join(date.split('-')[::-1])
        date_local = str(datetime.now().astimezone()).split(' ')[0]
        if date_local < date_website :
            url = "https://www.ganeshaspeaks.com/horoscopes/yesterday-horoscope/" + sunsign
            response = requests.get(url)
            tree = html.fromstring(response.content)
            horoscope = str(tree.xpath(
                "//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        elif date_local > date_website :
            url = "https://www.ganeshaspeaks.com/horoscopes/tomorrow-horoscope/" + sunsign
            response = requests.get(url)
            tree = html.fromstring(response.content)
            horoscope = str(tree.xpath(
                "//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        else :
            horoscope = str(tree.xpath(
                "//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = horoscope.replace("[u'", "").replace("']", "")
        dict = {
            'date': date,
            'horoscope': horoscope,
            'sunsign': sunsign
            }
        return dict

    @staticmethod
    def get_weekly_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/horoscopes/weekly-horoscope/" + sunsign
        response = urllib.request.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        week = str(tree.xpath(
			"//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        week = week.replace("[u'\\n", "").replace("']", "").replace("\\u2013", "-")
        horoscope = str(tree.xpath(
			"//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = horoscope.replace("['", "").replace("']", "")
        dict = {
            'week': week,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_monthly_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/horoscopes/monthly-horoscope/" + sunsign
        response = urllib.request.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        month = str(tree.xpath(
			"//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        month = month.replace("['\\n", "").replace("']", "")
        horoscope = str(tree.xpath(
			"//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()[1]"))
        horoscope = horoscope.replace("['", "").replace("']", "")
        dict = {
            'month': month,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_yearly_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/horoscopes/yearly-horoscope/" + sunsign
        response = urllib.request.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        year = str(tree.xpath(
			"//*[@id=\"daily\"]/div/div[1]/div[1]/div[2]/div/p/text()"))
        year = year.replace("['\\n", "").replace("']", "")
        horoscope = str(tree.xpath(
			"//*[@id=\"daily\"]/div/div[1]/div[2]/p[1]/text()"))
        horoscope = horoscope.replace("[u'", "").replace("']", "").replace("\\xe2\\x80\\x99s", "")
        dict = {
            'year': year,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict
