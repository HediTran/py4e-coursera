# This program prompt the user for a search string (a location)
# call the Google geocoding API and extract information
# from the returned XML (in this exercise is the two-character country code)

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    tree = ET.fromstring(data)

    results = tree.findall('result')

    if 'country' in results[0].findall('address_component')[-1].findall('type'):
        country_code = results[0].findall('address_component')[-1].find('short_name').text
        print('Country code:', country_code)
    else:
        print('This location is not in any country! Cannot return country code.')
