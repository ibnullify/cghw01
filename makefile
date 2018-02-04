all: imggen.py
	pyython imggen.py
	magick convert image.ppm image.png
