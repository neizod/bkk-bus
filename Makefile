SHELL = /bin/bash

main:
	./parser.py > metro-map.tex
	pdflatex metro-map.tex

clean:
	rm -f metro-map.{aux,log,tex,pdf}
