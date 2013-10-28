#/usr/bin/env python

# Requires pygeoip + GeoIP.dat from http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz
# pip install pygeoip

import pygeoip

geoip = pygeoip.GeoIP('GeoIP.dat')

ip = raw_input('IP Address to look up: ')

print '%s is in %s' % (ip, geoip.country_name_by_addr(ip))

