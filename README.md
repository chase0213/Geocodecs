Geocodecs
---------

- Geocodecs provides a translator from addresses into geocodings.

Requirements
------------

- python3
  + simplejson

Installation
------------

1. clone this product into your working directory.
```
git clone git@github.com:chase0213/Geocodecs.git
```
2. install using setuptools
```
cd Geocodecs && python3 setup.py install
```

How to Use
----------

- import this class into your project:
```
import geocodecs.geocodecs as geo
```
- get url from address (addresses can be Kanji character)
```
url = geo.geocoding_from_address(address="Yokohama")
```
- get json object
```
json_obj = geo.request_with_url(url)
```

