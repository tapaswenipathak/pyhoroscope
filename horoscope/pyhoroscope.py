import urllib2
from lxml import etree
import re

####################################################################
# API
####################################################################


'''
If something breaks, give below error message.
'''
ERROR_MESSAGE = "Couldn't retrieve data, We are working to fix this."

class Horoscope:

    @staticmethod
    def get_todays_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/" + sunsign + \
            "/" + sunsign + "-daily-horoscope.action"
        response = urllib2.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        date = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div/div/div[2]/section/div[2]/div/div/div[1]/h3/span/text()"))
        date = date.replace("['(", "").replace(")']", "")
        horoscope = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div/div/div[2]/section/div[2]/div/div/div[1]/span/text()"))
        horoscope = horoscope.replace("[u'", "").replace("']", "")
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
            "//*[@id=\"main-wrapper\"]/div/div/div[2]/section/div[10]/div[2]/div/span[2]/span/text()[2]"))
        sanskrit_name = sanskrit_name.replace(
            "[\' : ", "").replace(" |\\n\']", "").replace("['", "")
        meaning_of_name = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div/div/div[2]/section/div[10]/div[2]/div/span[2]/span/text()[3]"))
        meaning_of_name = meaning_of_name.replace(
            "[\' : ", "").replace(" |\\n\']", "").replace("['", "")
        lord = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div/div/div[2]/section/div[10]/div[2]/div/span[2]/span/text()[5]"))
        lord = lord.replace("[\' : ", "").replace(" |\\n\']", "").replace("['", "")
        Type = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div/div/div[2]/section/div[10]/div[2]/div/span[2]/span/text()[4]"))
        Type = Type.replace("[\' : ", "").replace(" |\\n\']", "").replace("['", "").replace(" |']", "")
        lucky_day = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div/div/div[2]/section/div[10]/div[2]/div/span[2]/span/text()[6]"))
        lucky_day = lucky_day.replace("[\' : ", "").replace(" |\\n\']", "").replace("[' ", "")
        lucky_number = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div/div/div[2]/section/div[10]/div[2]/div/span[2]/span/text()"))
        lucky_number = str(re.findall(r"\d+,", lucky_number))
        lucky_number = lucky_number.replace("['", "").replace(",']", "").replace("'", "").replace(",,", ",")
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
        response = urllib2.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        date = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div/div/div[2]/section/div[2]/div/div/h3/span/text()"))
        date = date.replace("[u'\\n", "").replace("']", "").replace("\\u2013", "-")
        horoscope = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div/div/div[2]/section/div[2]/div/div/span/text()"))
        horoscope = horoscope.replace("['", "").replace("']", "")
        dict = {
            'date': date,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_monthly_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/" + sunsign + \
            "/" + sunsign + "-monthly-horoscope.action"
        response = urllib2.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        date = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div/div/div[2]/section/div[2]/div/div/h3/span/text()"))
        date = date.replace("['\\n", "").replace("']", "")
        horoscope = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div/div/div[2]/section/div[2]/div/div/span/text()[1]"))
        horoscope = horoscope.replace("['", "").replace("']", "")
        dict = {
            'date': date,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_yearly_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/" + sunsign + \
            "/" + sunsign + "-yearly-horoscope.action"
        response = urllib2.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        date = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div/div/div[2]/section/div[2]/div/div/h3/span/text()"))
        date = date.replace("['\\n", "").replace("']", "")
        horoscope = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div/div/div[2]/section/div[2]/div/div/span/text()"))
        horoscope = horoscope.replace("[u'", "").replace("']", "").replace("\\xe2\\x80\\x99s", "")
        dict = {
            'date': date,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict
