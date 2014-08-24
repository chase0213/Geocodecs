#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib.parse
import urllib.request
import simplejson
import codecs

BASE_URL = "https://maps.googleapis.com/maps/api/geocode/"


class Geocodecs():
    """
    Geocodecs provides translator from address/geocoding into geocoding/address
    using Google Maps API v3.
    """

    def geocoding_from_address(self, output='json', address='', sensor=False, filter=''):
        if address == '':
            return False

        sensor = 'true' if (sensor == True or sensor == 'true') else 'false'

        address = urllib.parse.quote(address)
        url = BASE_URL + output + '?' + 'address=' + address + '&sensor=' + sensor
        if filter != '':
            url += '&components=' + filter

        return url

    def request_with_url(self, url):
        try:
            r = urllib.request.urlopen(url)
            json_obj = simplejson.loads(r.read())
        except:
            print('Error: cannot open %s or is not json format' % url)
            exit(1)

        if json_obj["status"] != "OK":
            print('Warning: status code is %s' % json_obj['status'])
            return False
        return json_obj

    def get_location(self, json_obj):
        return json_obj['results']['geometry']['location']

    def get_formatted_address(self, json_obj):
        return json_obj['results']['formatted_address']


def sample():
    geo = Geocodecs()
    address = "群馬県伊勢崎市"
    url = geo.geocoding_from_address(address=address)
    json_obj = geo.request_with_url(url)
    print(json_obj)


def main():
    sample()


if __name__ == '__main__':
    main()
