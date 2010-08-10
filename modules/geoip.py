"""Adds the 'geoip' command, which attempts to resolve a location for an IP or hostname."""

import urllib2
import xml.dom.minidom as dom

__info__ = {
	"Author": "Wil Hall",
	"Version": "1.0",
	"Dependencies": []
}

def onLoad():
	@command('geoip', 1)
	def geoip_cmd(ctx, cmd, arg, *args):
		ip = args[0]
		fornick = ''
		if '.' not in ip:
			ctx.reply(u'geoip by Nick not currently supported.', 'geoip')
			return

		response = urllib2.urlopen('http://ipinfodb.com/ip_query2.php?ip=%s&timezone=false' % ip)

		xml = dom.parse(response)

		ip = xml.getElementsByTagName("Ip")[0].firstChild.data
		status = xml.getElementsByTagName("Status")[0].firstChild.data
		cc = xml.getElementsByTagName("CountryCode")[0].firstChild.data
		country = xml.getElementsByTagName("CountryName")[0].firstChild.data
		region = xml.getElementsByTagName("RegionName")[0].firstChild.data
		city = xml.getElementsByTagName("City")[0].firstChild.data
		zip = xml.getElementsByTagName("ZipPostalCode")[0].firstChild.data
		lat = xml.getElementsByTagName("Latitude")[0].firstChild.data
		lon = xml.getElementsByTagName("Longitude")[0].firstChild.data

		xml.unlink() # Phew! Release all the xml tree data now, since we just spent the code pulling it into vars. :)


		lon = lon.replace('\n', '').replace('\\n', '')
		ctx.reply(u"The IP Address `B%s`B %s traces to `B%s`B, `B%s`B, `B%s`B(`B%s`B) `B%s`B (`B%s`B, `B%s`B)." % (ip, fornick, city, region, country, cc, zip, lat, lon), 'geoip')
