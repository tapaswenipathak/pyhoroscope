sunsign = ["aries", "taurus", "gemini", "cancer", "leo", "virgo",
           "libra", "scorpio", "stagittarius", "capricorn", "aquarius", "pisces"]
typ = ["todays", "weekly", "yearly", "monthly"]
from pyhoroscope import Horoscope as horo
from pprint import pprint
for i in sunsign:
    for j in typ:
        d = eval("horo.get_" + j + "_horoscope(i)")
        d['horoscope'] = d['horoscope'][:35]
        pprint(d)
