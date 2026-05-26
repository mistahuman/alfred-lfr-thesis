#!/usr/bin/env bash
set -e

# Installs the LaTeX packages needed to compile this thesis.
# Tested on Ubuntu/Debian. On other distros adapt the package manager.

if ! command -v apt-get >/dev/null 2>&1; then
    echo "This script requires apt-get (Ubuntu/Debian). Install the packages manually:"
    echo "  texlive-latex-base texlive-latex-extra texlive-lang-italian"
    echo "  texlive-science texlive-fonts-recommended texlive-pictures"
    echo "  latexmk biber"
    exit 1
fi

echo "Installing LaTeX dependencies..."
sudo apt-get update -qq
sudo apt-get install -y \
    texlive-latex-base \
    texlive-latex-extra \
    texlive-lang-italian \
    texlive-science \
    texlive-fonts-recommended \
    texlive-fonts-extra \
    texlive-pictures \
    latexmk

echo "Done. Run 'bash build.sh' to compile the thesis."
