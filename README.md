# horoscope

A Python module to fetch and parse data from GaneshaSpeaks.

### Projects built using pyhoroscope
* [`horoscope-api`](https://github.com/tapasweni-pathak/horoscope-api) – A REST API to get horscope from GaneshaSpeaks.


## Installation
* You will need [Python 2](https://www.python.org/download/). 
* [pip](http://pip.readthedocs.org/en/latest/installing.html) is recommended for installing dependencies.

Install using pip:

    pip install horoscope

## Usage

```python

from horoscope import Horoscope

your_horoscope = Horoscope.get_todays_horoscope ('Libra')
    
#do stuff with the parsed data
your_horoscope['date']
your_horoscope['sunsign']
your_horoscope['horoscope']

```

## Features
### Currently implemented
* Today's Horscope 
* Weekly Horoscope
* Monthly Horoscope
* Yearly Horoscope


### Todo
* Personality Profile 
* Facts About a Sunsign
* Practical Side of a Sunsign
* Astrological Perspective of a Sunsign

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/tapasweni-pathak/pyhoroscope/trend.png)](https://bitdeli.com/free "Bitdeli Badge")



