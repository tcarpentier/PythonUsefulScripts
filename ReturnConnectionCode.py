import urllib2


def getCode(urls):
    """
	>>> getCode(['http://www.google.fr'])
	http://www.google.fr : 200
	>>> getCode(['http://www.google.fr', 'http://yahoo.fr', 'http://www.python.org'])
	http://www.google.fr : 200
	http://yahoo.fr : 200
	http://www.python.org : 200
	>>> getCode(['http://www.iamnotabletoconnecttothissite.com'])
	Server not available
	http://www.iamnotabletoconnecttothissite.com : [Errno 11004] getaddrinfo failed
	"""
    for url in urls:
        try:
            connection = urllib2.urlopen(url)
            print url + " : " + str(connection.getcode())
            connection.close()
        except urllib2.HTTPError, e:
            print url + " : " + str(e.getcode())
        except urllib2.URLError, e:
            print 'Server not available'
            print url + " : " + str(e.reason)

if __name__ == "__main__":
    import doctest
    doctest.testmod()