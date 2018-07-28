# Image-Mosaic-Generator
A project I did for my computer vision class. Me and my partner chose to build a program that could create a large image out of many smaller images. Essentially, a program to make image mosaics. It uses a very simple method of calculating pixel values based on the average of all pixel values in an image, assigns this number to the file, and then uses those numbers to decide where each image should go. We found the larger the image database, the more accurate of an image it can create. My partner decided to write a program to pull a large amount of image files from a website that we used to create an image library. Our program however can still work with custom image libraries, but this saved us a lot of time trying to find over 5000 images on our hard drives combined, plus whatever we could siphon from the internet.

At very high resolutions the program will run slower, and at higher resolutions, some images will be too big to load on some machines. I recommend caution with very large settings, we have accidentally crashed computers before when we made the file too big. The settings that the program is currently set to should be safe for most computer.

Also note that if you change the pixel resolutions, both the image and the "pixels" must have the same X : Y ratio and be a multiple of each other. For example, if the resolution of a pixel is 100 x 50, the output image resolution could be 1000 x 500, but not 1000 x 1000. Unintended results may occur if you do. This program was not written with error checking in mind, we were being marked based on whether it worked or not, not if the user puts bad input.

The program will search for images in any subfolder called Library, and it's target is any jpg image called Target.jpg. The project was created in python.


Note: Image Pull was not my work, that was my partner's job. My job was getting the other pieces of code to work.
