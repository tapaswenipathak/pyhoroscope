# horoscope

A Python module to fetch and parse data from GaneshaSpeaks.

### Projects built using pyhoroscope
* [`horoscope-api`](https://github.com/tapasweni-pathak/horoscope-api) – A REST API to get horscope from GaneshaSpeaks.


## Installation
You will need [Python 2](https://www.python.org/download/). [pip](http://pip.readthedocs.org/en/latest/installing.html) is recommended for installing dependencies.

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


### Todo
* More information about a sunsign
* Current month horoscope
* Current year horoscope
