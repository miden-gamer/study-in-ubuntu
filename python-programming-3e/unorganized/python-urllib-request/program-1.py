from urllib import request
# import urllib.request

# List built-in functions from "urllib.request" module
# print(dir(request))

# Print help text for urlopen function
# print(help(request.urlopen))

url = "https://www.google.com"  # we are going to make a request to Google's homepage
# when we don't give any specific path, it looks for homepage of particular website

res = request.urlopen(url) # opens the given url, and returns http response from website
print(res, type(res))

# check functions of returned http response
# print(dir(res))

# closed attribute tells either the request has been closed or not
print("\nResponse Closed?", res.closed)
# False, means http connection is still open to website

# http uses response code to verify if the response was success or failure, 
# we can check response code using code attribute on this response "res" object
print("\nResponse Code =", res.code)

# look at initial part of response using peek() method of response object
print("\nInitial Part Of Response:")
print(res.peek())  # returns binary object

# look at headers
print("\nHeaders:")
print(res.getheaders()) # returns a list with header and its value as tuple

# get a particular header detail
print("\nContent-Type Header:")
print(res.getheader('Content-Type')) # pass header key as argument to .getheader()

# Close response
res.close()
print("\nResponse Closed?", res.closed)