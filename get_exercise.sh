#!/usr/bin/env bash

# folder containing all the *.html exercises
EXERCISES="./exercises"

# this function download and display the exercises
# .html is stored because it sucks to download the same file every time
get_exercise() {
  # is exercise is not dowloaded
  if [ ! -f "$EXERCISES/$1.html" ]; then
    # Download exercise
    printf "$1.html does not exist.\nDownloading...\n"
    curl https://projecteuler.net/minimal=$1 > "$EXERCISES/$1.html"
  fi

  # Display html in a more readable form
  clear && cat "$EXERCISES/$1.html" | w3m -dump -T text/html | cowsay | lolcat
}

# Check how many args were passed to the script
if [ "$#" -ne 1 ]; then
    printf "Illegal number of parameters. Be sure to pass 'arg1' as <exercise_number>\n"
else
  get_exercise $1
fi
