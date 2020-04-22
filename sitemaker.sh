#!/bin/sh


## first convert to html
## extension of https://gist.github.com/hugorodgerbrown/5317616
FILES=*.md
for f in $FILES
do
  if [ "$f" != "readme.md" ] &&  [ "$f" != "map.md" ] ; then
    filename="${f%.*}"
    echo "Converting $f to $filename.html"
    cat map.md $f > temp.md
    ## make current page special
    sed -i.back "s#]($filename.html#*]($filename.html#g" temp.md
    pandoc temp.md -s -o $filename.html
  fi
done
rm temp.md



## now add the html
PAGES=*.html
for p in $PAGES
do
  echo "Adding resources, viewport meta, div to $p, adding viewport meta, divs"
  sed -i.bak 's/\<head\>/\<head\>\<link rel="stylesheet" type="text\/css" href="style.css"\>/g' $p
  #sed -i.bak 's/\<head\>/\<head\>\<link href="https:\/\/fonts.googleapis.com\/css2?family=Roboto:wght@100\&display=swap" rel="stylesheet"\>/g' $p
  sed -i.bak 's/\<body\>/\<body\>\<div\>/g' $p
  sed -i.bak 's/\<\/body\>/\<\/div\>\<\/body\>/g' $p
  sed -i.bak 's/\<head\>/\<head\>\<meta name="viewport" content="width=device-width, initial-scale=1.0"\>/g' $p
done

## delete .bak
rm *bak

