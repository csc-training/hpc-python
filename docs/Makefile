SOURCES=$(wildcard *.md)
TARGETS=$(patsubst %.md,%.html,$(SOURCES))
PDFS=$(patsubst %.md,%.pdf,$(SOURCES))

SINGULARITY=singularity
SARGS=run
SIMAGE=../../../slide-template/slidefactory.simg

all: $(TARGETS)

pdfs: $(PDFS)

%.html: %.md
	$(SINGULARITY) $(SARGS) $(SIMAGE) $<

%.pdf: %.html
	chromium-browser --headless --print-to-pdf=$@ file://`pwd`/$(<)?print-pdf

.PHONY: clean
clean:
	-/bin/rm -f *.html *.pdf *~

book:
	jupyter-book build .

serve:
	python -m http.server --directory _build/html
