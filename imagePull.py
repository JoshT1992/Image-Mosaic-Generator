#This program pulls a large amount of image data from a specific website to create an image library used for the mosaic program.

import urllib
import os.path


numCards = 4965

#also 398405 - 398681

#numCards = 30
print
for i in range(0, numCards):
	#print ('%d//%d pictures downloaded.' % i, numCards),
	fileLoc = 'Library/%d.jpg' % i
	if (os.path.isfile(fileLoc)==False):
		urllib.urlretrieve('http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=%d&type=card' % i, fileLoc)
	#else:
		#print 'File %s already exists.' % fileLoc
		