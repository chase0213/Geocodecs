#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import urllib.parse
import urllib.request
import simplejson


def geocoding_from_address(output='json', address='', sensor=False, filter=''):
    if address == '':
        return False

    sensor = 'true' if (sensor == True or sensor == 'true') else 'false'

    address = urllib.parse.quote(address)
    BASE_URL = "https://maps.googleapis.com/maps/api/geocode/"
    url = BASE_URL + output + '?' + 'address=' + address + '&sensor=' + sensor
    if filter != '':
        url += '&components=' + filter

    return url


def request_with_url(url):
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


def get_location(json_obj):
    return json_obj['results']['geometry']['location']


def get_formatted_address(json_obj):
    return json_obj['results']['formatted_address']
