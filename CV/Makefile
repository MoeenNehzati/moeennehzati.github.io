PROFILES := cv cv-ml cv-econ-ai cv-genetics cv-quant

.PHONY: all $(PROFILES)
all: $(PROFILES)

$(PROFILES):
	latexmk -pdf -outdir=_build -interaction=nonstopmode -halt-on-error $@.tex
