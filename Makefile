.PHONY: all thesis slides-thesis slides-conference clean cleanall

THESIS_MAIN       = thesis_lanconelli
SLIDES_TH_MAIN    = slides_lanconelli
SLIDES_CONF_MAIN  = slides_conference

all: thesis slides-thesis slides-conference

# --- thesis ---------------------------------------------------------------
thesis:
	cd thesis && \
	pdflatex -interaction=nonstopmode $(THESIS_MAIN).tex && \
	bibtex $(THESIS_MAIN) && \
	pdflatex -interaction=nonstopmode $(THESIS_MAIN).tex && \
	pdflatex -interaction=nonstopmode $(THESIS_MAIN).tex

# --- thesis defence slides ------------------------------------------------
slides-thesis:
	cd slides-thesis/main && \
	pdflatex -interaction=nonstopmode $(SLIDES_TH_MAIN).tex && \
	pdflatex -interaction=nonstopmode $(SLIDES_TH_MAIN).tex

# --- conference presentation ----------------------------------------------
slides-conference:
	cd slides-conference/main && \
	pdflatex -interaction=nonstopmode $(SLIDES_CONF_MAIN).tex && \
	pdflatex -interaction=nonstopmode $(SLIDES_CONF_MAIN).tex

# --- clean ----------------------------------------------------------------
clean:
	find thesis slides-thesis slides-conference \
	  \( -name "*.aux" -o -name "*.log" -o -name "*.toc" -o -name "*.lof" \
	     -o -name "*.lot" -o -name "*.bbl" -o -name "*.blg" -o -name "*.out" \
	     -o -name "*.nav" -o -name "*.snm" -o -name "*.vrb" -o -name "*.synctex.gz" \
	     -o -name "*.fls" -o -name "*.fdb_latexmk" -o -name "*.auxlock" \) \
	  -delete

cleanall: clean
	rm -f thesis/$(THESIS_MAIN).pdf \
	      slides-thesis/main/$(SLIDES_TH_MAIN).pdf \
	      slides-conference/main/$(SLIDES_CONF_MAIN).pdf
