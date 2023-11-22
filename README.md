# LaTeX Template
Template for making IEEEish style engineering reports
- `main` branch: IEEE LaTeX template files.
- `Example-PH2019` branch: an example use case

## Features
- Automatic document outline for easy navigation
- Contents page hyperlinking
- Ability to render 2d/3d graphics in latex as opposed to screenshotting a premade one (though it is a pain, and screenshotting ends up being easier)

## TODO
- Automated solution for displaying tables by including a path to a `.csv` file
- Configure referencing
- Use `.sty` for header file which is currently `.tex`
- Make use of `\usepackage{cleverref}` to automate figure referencing
- Change from `\input` to `\include` for subsections to make use of `\includeonly{}` function in header to reduce compiling times by excluding files not being edited
- Code chunks with [syntax highlighting](https://www.overleaf.com/learn/latex/Code_Highlighting_with_minted#Including_code_from_a_file)
- Remove automatic paragraph indenting with either `\setlength{\parindent}{0pt}` or `\parskip`
