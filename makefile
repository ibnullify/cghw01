all: imggen.py
	python imggen.py
	convert image.ppm image.png
