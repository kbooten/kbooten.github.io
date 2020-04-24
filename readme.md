Porting personal website from expensive hosting site.

A simple site (index page + <5 others), rarely updated, so I'm just using pandoc locally to convert `.md` to `.html` files.


A bash script automatically converts local `.md` files, injects links to the stylesheet, converts `map.md` (a navigation bar) to html, and adds this html to the top of each page. 

To do:
* sometimes the centering between pages is a few pixels off, making the nav bar jump slightly between clicks.  maybe something about how `{margin:auto}` works?
* link to old domain

Favicon made with imagemagick's `plasma:` command.