##
##Adding support for Python3 ;-)
##
try:
  import urllib2
except ImportError:
  import urllib.request as urllib2
##


from bs4 import BeautifulSoup
import re



####################################################################
# API
####################################################################





ERROR_MESSAGE="Couldn't retrieve data, We are working to fix this."
THRESH=35


CLASS_NAME="g5-box-25 first daily-hor sunsign-bx50"
DATE_TAG="soup.a"
#############################
#These variables has to be mantained as per wishes of ganeshaspeaks.com
#It is the smallest tag (innermost) under which the date and horoscope is to be found
##############################


class Horoscope:


  @staticmethod
  def get_todays_horoscope (sunsign):
      url = "http://www.ganeshaspeaks.com/" + sunsign + "/" + sunsign + "-daily-horoscope.action"
      html_doc = urllib2.urlopen (url)
      soup = BeautifulSoup (html_doc.read (),"html.parser")
      raw_data = str (soup.find_all ("div",CLASS_NAME))
      ############################
      #In case class_name becomes invalid when site data updates/changes
      #=>return some error message
      #Foolish assumption: horoscope will always be greater than THRESH number of letters
      ###########################

      
      soup = BeautifulSoup (raw_data,"html.parser")
      
      ##initializing
      horoscope=ERROR_MESSAGE
      date=""
      ##############
      if soup:
        date=eval(DATE_TAG).string[2:-1]
        for string in soup.stripped_strings:
            if len(string)>THRESH:
                horoscope=string
                break

      
          
      
      
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
      soup = BeautifulSoup (html_doc.read (),"html.parser")
      raw_data = str (soup.find_all ("div",CLASS_NAME))
      soup = BeautifulSoup (raw_data,"html.parser")
      horoscope=ERROR_MESSAGE
      week=""
      if soup:
          week=eval(DATE_TAG).string[2:-1]
          for string in soup.stripped_strings:
              if len(string)>THRESH:
                  horoscope=string
                  break
          
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
      soup = BeautifulSoup (html_doc.read (),"html.parser")
      raw_data = str (soup.find_all ("div",CLASS_NAME))
      soup = BeautifulSoup (raw_data,"html.parser")
      horoscope=ERROR_MESSAGE
      month=""
      if soup:
          month=eval(DATE_TAG).string[2:-1]
          for string in soup.stripped_strings:
              if len(string)>THRESH:
                  horoscope=string
                  break

          
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
      soup = BeautifulSoup (html_doc.read (),"html.parser")
      raw_data = str (soup.find_all ("div",CLASS_NAME))
      soup = BeautifulSoup (raw_data,"html.parser")
      horoscope=ERROR_MESSAGE
      year=""
      if soup:
          year=eval(DATE_TAG).string[2:-1]
          for string in soup.stripped_strings:
              if len(string)>THRESH:
                  horoscope=string
                  break

      dict = {
              'year' : year,
              'horoscope' : horoscope,
              'sunsign' : sunsign
      }
      return dict

