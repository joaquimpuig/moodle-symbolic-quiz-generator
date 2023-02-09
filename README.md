# moodle-symbolic-quiz-generator
Generating Moodle Question Banks using Python and Sympy


Over the years I have developed some scripts for generating banks of questions for Moodle so that students can challenge themselves and check their answers. Sometimes I have been dealing with hundreds of students so an automated procedure is needed.

After checking with colleagues from my [department at UPC](www.mat.upc.edu) and many hours of trial and error, I finally ended with the following solution, which works for GNU/Linux systems (although I guess that also works for other systems).

## Requirements

The process needs the following components:

-   A Python install (Python3).

-   The [SymPy Python library for symbolic mathematics](www.sympy.org). Check the website for install and docs.

-   [Lualatex](https://www.luatex.org/), an extended version of [pdfTeX](http://www.pdftex.org)
    using [Lua](http://www.lua.org) as an embedded scripting language. For Ubuntu/Debian distributions, it can be found under the 'texlive-lualatex' systems. Pdflatex did not work for me because of UTF-8 encoding.

-   [The moodle package for LaTeX.](http://tug.ctan.org/tex-archive/macros/latex/contrib/moodle/) For Ubuntu/Debian systems, this package is included in 'texlive-latex-extra'.

- The Python and TeX files you will find in this repository.

## Steps

1.   Update 'sample-quiz-generator.py' to tailor your wishes.

2.   Execute this file using Python, for instance, in bash,
    
          python ./sample-quiz-generator.py
        
This will generate a TeX file 'chunks-moodle.tex' which contains the different questions and is included within the main file 'template-python-moodle.tex'

3.   Run LuaLaTex to compile the file:

          lualatex template-python-moodle.tex

4.   This will create a PDF with solutions to preview and an XML to upload to Moodle.

5.  Upload the XML file to the platform of your choice.
