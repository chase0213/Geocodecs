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

How to Use
----------

- import this class into your project:
```
import Geocodecs
```
- create Geocodecs instance
```
geo = Geocodecs()
```
- get url from address
```
url = geo.geocoding_from_address(address="Yokohama")
```
- get json object
```
json_obj = geo.request_with_url(url)
```

