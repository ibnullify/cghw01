all: imggen.py
	python imggen.py
	magick convert image.ppm image.png
