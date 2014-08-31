import urllib2
from bs4 import BeautifulSoup
import re



####################################################################
# API
####################################################################

class Horoscope:
  @staticmethod
  def get_todays_horoscope (sunsign):
  	url = "http://www.ganeshaspeaks.com/" + sunsign + "/" + sunsign + "-daily-horoscope.action"
	html_doc = urllib2.urlopen (url)
	soup = BeautifulSoup (html_doc.read ())
	raw_data = str (soup.find_all (id="predData"))
	soup = BeautifulSoup (raw_data)
	date = soup.find_all('strong')[0].get_text ()
	soup = BeautifulSoup (raw_data)
	horoscope = soup.find_all(id="predData")[0].get_text ()
	horoscope = re.sub(r'\d+-\d+-\d+', r'', horoscope)
	horoscope = horoscope.replace ("\n", "")
	dict = {
		'date' : date,
		'horoscope' : horoscope,
		'sunsign' : sunsign
	}
	return dict
  
  @staticmethod
  def  know_all_about (sunsign) :
	url = "http://www.ganeshaspeaks.com/" + sunsign + ".action"
	html_doc = urllib2.urlopen (url)
	soup = BeautifulSoup (html_doc.read ())
	raw_data = str (soup.find_all ('p',{'class':'nrmltxt'}))
	soup = BeautifulSoup (raw_data)
	sanskrit_name = soup.find_all('em')[0].get_text ()
	meaning_of_name = soup.find_all('em')[1].get_text ()
	lord = soup.find_all('em')[3].get_text ()
	lucky_color = soup.find_all('em')[4].get_text ()
	lucky_day = soup.find_all('em')[5].get_text ()
	lucky_number = soup.find_all('em')[6].get_text ()
	dict = {
		'sanskrit_name' : sanskrit_name,
		'meaning_of_name' : meaning_of_name,
		'lord' : lord,
		'lucky_color' : lucky_color,
		'lucky_day' : lucky_day,
		'lucky_number' : lucky_number,
	}
	return dict
  
  @staticmethod
  def get_weekly_horoscope (sunsign) :
   	url = "http://www.ganeshaspeaks.com/" + sunsign + "/" + sunsign + "-weekly-horoscope.action" 
	html_doc = urllib2.urlopen (url)
	soup = BeautifulSoup (html_doc.read ())
	raw_data = str (soup.find_all (id="predData"))
	soup = BeautifulSoup (raw_data)
	week = soup.find_all('strong')[0].get_text ()
	soup = BeautifulSoup (raw_data)
	horoscope = soup.find_all(id="predData")[0].get_text ()
	horoscope = re.sub(r'.*\d+', r'', horoscope)
	horoscope = horoscope.replace ("\n", "")
	dict = {
		'week' : week,
		'horoscope' : horoscope,
		'sunsign' : sunsign
	}
	return dict

  @staticmethod
  def get_monthly_horoscope (sunsign) :
   	url = "http://www.ganeshaspeaks.com/" + sunsign + "/" + sunsign + "-monthly-horoscope.action" 
	html_doc = urllib2.urlopen (url)
	soup = BeautifulSoup (html_doc.read ())
	raw_data = str (soup.find_all (id="predData"))
	soup = BeautifulSoup (raw_data)
	month = soup.find_all('strong')[0].get_text ()
	soup = BeautifulSoup (raw_data)
	horoscope = soup.find_all(id="predData")[0].get_text ()
	horoscope = re.sub(r'[A-Za-z]+ \d+', r'', horoscope)
	horoscope = horoscope.replace ("\n", "")
	dict = {
		'month' : month,
		'horoscope' : horoscope,
		'sunsign' : sunsign
	}
	return dict

  @staticmethod
  def get_yearly_horoscope (sunsign) :
   	url = "http://www.ganeshaspeaks.com/" + sunsign + "/" + sunsign + "-yearly-horoscope.action" 
	html_doc = urllib2.urlopen (url)
	soup = BeautifulSoup (html_doc.read ())
	raw_data = str (soup.find_all (id="predData"))
	soup = BeautifulSoup (raw_data)
	year = soup.find_all('strong')[0].get_text ()
	soup = BeautifulSoup (raw_data)
	horoscope = soup.find_all(id="predData")[0].get_text ()
	horoscope = re.sub(r'\d+', r'', horoscope)
	horoscope = horoscope.replace ("\n", "")
	dict = {
		'year' : year,
		'horoscope' : horoscope,
		'sunsign' : sunsign
	}
	return dict

