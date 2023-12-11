# LaTeX Temple Example - See [Here](main.pdf)
Template for making IEEEish style engineering reports.
Until this point, I've been using Rmarkdown, which is pretty much a jankier implementation of pure LaTeX. I saw some [Youtube videos](https://www.youtube.com/playlist?list=PLHXZ9OQGMqxcWWkx2DMnQmj5os2X5ZR73) and thought it would probably be best if I just swap over from Rmarkdown, since it produces similar results and ends up being easier.
You can copy and paste this template into Overleaf and save it as a template, or clone the repo locally to edit in a LaTeX editor of your choice. I use Visual Studio Code with the Latex workshop extension - to my knowledge, it has all the features of overleaf premium for free - though overleaf is still super super nice and all on the browser.

## Repository Outline
- `main` branch: The template itself
- `Example-PH2019` branch: an example use case
- `Example-general` branch: a more generalised use case that demos many of the features

## Features
- Files are segmented by section, each having their own `.tex` file, which is super nice and stops you from being lost if you have a large document
- Automatic document outline inside pdf readers
- Contents page hyperlinking
- Ability to render 2d/3d graphics in latex as opposed to screenshotting a premade one (though it is a pain, and screenshotting ends up being easier)

## To Do
- Look into implementing 2 column format? Is this really required?
- Generalise and simplify csv file implementation (currently super finneky)
    - Round numbers
    - Figure out header names
    - Is there some kind of library i'm missing?
- Configure referencing
    - There appear to be many libraries to do this     








