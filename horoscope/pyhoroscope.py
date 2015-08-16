import urllib2
from bs4 import BeautifulSoup
from lxml import etree
import ast


####################################################################
# API
####################################################################


'''
If something breaks, give below error message.
Horoscope will always be greater then THRESH.
'''
ERROR_MESSAGE = "Couldn't retrieve data, We are working to fix this."
THRESH = 35

'''
Narrowest tag to fetch the horoscope and date.
'''

CLASS_NAME = "g5-box-25 first daily-hor sunsign-bx50"
DATE_TAG = "soup.a"


class Horoscope:

    @staticmethod
    def get_todays_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/" + sunsign + \
            "/" + sunsign + "-daily-horoscope.action"
        html_doc = urllib2.urlopen(url)
        soup = BeautifulSoup(html_doc.read(), "html.parser")
        raw_data = str(soup.find_all("div", CLASS_NAME))
        soup = BeautifulSoup(raw_data, "html.parser")
        horoscope = ERROR_MESSAGE
        date = ""
        if soup:
            date = eval(DATE_TAG).string[2:-1]
            for string in soup.stripped_strings:
                if len(string) > THRESH:
                    horoscope = string
                    break

        dict = {
            'date': date,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def know_all_about(sunsign):
        url = "http://www.ganeshaspeaks.com/" + sunsign + ".action"
        response = urllib2.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        sanskrit_name = str(tree.xpath(
            "/html/body/div/div/div[4]/section[4]/div/div/div[1]/p/text()[2]"))
        sanskrit_name = sanskrit_name.replace(
            "[\' : ", "").replace(" |\\n\']", "")
        meaning_of_name = str(tree.xpath(
            "/html/body/div/div/div[4]/section[4]/div/div/div[1]/p/text()[3]"))
        meaning_of_name = meaning_of_name.replace(
            "[\' : ", "").replace(" |\\n\']", "")
        lord = str(tree.xpath(
            "/html/body/div/div/div[4]/section[4]/div/div/div[1]/p/text()[5]"))
        lord = lord.replace("[\' : ", "").replace(" |\\n\']", "")
        Type = str(tree.xpath(
            "/html/body/div/div/div[4]/section[4]/div/div/div[1]/p/text()[4]"))
        Type = Type.replace("[\' : ", "").replace(" |\\n\']", "")
        lucky_day = str(tree.xpath(
            "/html/body/div/div/div[4]/section[4]/div/div/div[1]/p/text()[6]"))
        lucky_day = lucky_day.replace("[\' : ", "").replace(" |\\n\']", "")
        lucky_number = str(tree.xpath(
            "/html/body/div/div/div[4]/section[4]/div/div/div[1]/p/text()[7]"))
        lucky_number = lucky_number.replace("[\' : ", "").replace("\\n']", "")
        dict = {
            'sanskrit_name': sanskrit_name,
            'meaning_of_name': meaning_of_name,
            'lord': lord,
            'type': Type,
            'lucky_day': lucky_day,
            'lucky_number': lucky_number,
        }
        return dict

    @staticmethod
    def get_weekly_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/" + sunsign + \
            "/" + sunsign + "-weekly-horoscope.action"
        html_doc = urllib2.urlopen(url)
        soup = BeautifulSoup(html_doc.read(), "html.parser")
        raw_data = str(soup.find_all("div", CLASS_NAME))
        soup = BeautifulSoup(raw_data, "html.parser")
        horoscope = ERROR_MESSAGE
        week = ""
        if soup:
            week = eval(DATE_TAG).string[2:-2]
            for string in soup.stripped_strings:
                if len(string) > THRESH:
                    horoscope = string
                    break

        dict = {
            'week': week,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_monthly_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/" + sunsign + \
            "/" + sunsign + "-monthly-horoscope.action"
        html_doc = urllib2.urlopen(url)
        soup = BeautifulSoup(html_doc.read(), "html.parser")
        raw_data = str(soup.find_all("div", CLASS_NAME))
        soup = BeautifulSoup(raw_data, "html.parser")
        horoscope = ERROR_MESSAGE
        month = ""
        if soup:
            month = eval(DATE_TAG).string[2:-2]
            for string in soup.stripped_strings:
                if len(string) > THRESH:
                    horoscope = string
                    break

        dict = {
            'month': month,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_yearly_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/" + sunsign + \
            "/" + sunsign + "-yearly-horoscope.action"
        html_doc = urllib2.urlopen(url)
        soup = BeautifulSoup(html_doc.read(), "html.parser")
        raw_data = str(soup.find_all("div", CLASS_NAME))
        soup = BeautifulSoup(raw_data, "html.parser")
        horoscope = ERROR_MESSAGE
        year = ""
        if soup:
            year = eval(DATE_TAG).string[2:-2]
            for string in soup.stripped_strings:
                if len(string) > THRESH:
                    horoscope = string
                    break

        dict = {
            'year': year,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict
