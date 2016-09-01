import urllib2
from lxml import etree
import re

####################################################################
# API
####################################################################

class Horoscope:

    @staticmethod
    def get_todays_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/" + sunsign + \
            "/" + sunsign + "-daily-horoscope.action"
        response = urllib2.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        date = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div[4]/div/div[1]/section/div[2]/div[1]/div/div[1]/h3/span/text()"))
        date = date.replace("['(", "").replace(")']", "")
        horoscope = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div[4]/div/div[1]/section/div[2]/div[1]/div/div[1]/span/text()"))
        horoscope = horoscope.replace("[u'", "").replace("']", "")
        dict = {
            'date': date,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_weekly_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/" + sunsign + \
            "/" + sunsign + "-weekly-horoscope.action"
        response = urllib2.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        week = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div[4]/div/div[1]/section/div[2]/div[1]/div/h3/span/text()"))
        week = week.replace("[u'\\n", "").replace("']", "").replace("\\u2013", "-")
        horoscope = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div[4]/div/div[1]/section/div[2]/div[1]/div/span/text()"))
        horoscope = horoscope.replace("['", "").replace("']", "")
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
        response = urllib2.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        month = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div[4]/div/div[1]/section/div[2]/div/div/h3/span/text()"))
        month = month.replace("['\\n", "").replace("']", "")
        horoscope = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div[4]/div/div[1]/section/div[2]/div/div/span/text()[1]"))
        horoscope = horoscope.replace("['", "").replace("']", "")
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
        response = urllib2.urlopen(url)
        htmlparser = etree.HTMLParser()
        tree = etree.parse(response, htmlparser)
        year = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div[4]/div/div[1]/section/div[2]/div/div/h3/span/text()"))
        year = year.replace("['\\n", "").replace("']", "")
        horoscope = str(tree.xpath(
            "//*[@id=\"main-wrapper\"]/div[4]/div/div[1]/section/div[2]/div/div/span/text()"))
        horoscope = horoscope.replace("[u'", "").replace("']", "").replace("\\xe2\\x80\\x99s", "")
        dict = {
            'year': year,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict
