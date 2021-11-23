#!/usr/bin/env bash

# folder containing all the *.html exercises
EXERCISES="./exercises"

# this function download and display the exercises
# .html is stored because it sucks to download the same file every time
get_exercise() {
  # is exercise is not dowloaded
  if [ ! -f "$EXERCISES/$2.html" ]; then
    # Download exercise
    printf "$1.html does not exist.\nDownloading...\n"
    curl https://projecteuler.net/minimal=$1 > "$EXERCISES/$2.html"
  fi

  # Display html in a more readable form
  clear && cat "$EXERCISES/$2.html" | w3m -dump -T text/html | lolcat
}

# Check how many args were passed to the script
if [ "$#" -ne 1 ]; then
    printf "Illegal number of parameters. Be sure to pass 'arg1' as <exercise_number>\n"
else
  if (( $1 < 1)) || (( $1 > 763 )); then
      echo "Exercises must be whithin (1:763) range"
      exit 1
  elif (( $1 < 10 )); then
      FILENAME="00$1"
  elif (( $1 < 100 )); then
      FILENAME="0$1"
  elif (( $1 < 1000 )); then
      FILENAME="$1"
  fi
  get_exercise $1 $FILENAME
  echo "https://projecteuler.net/problem=$1"
fi
