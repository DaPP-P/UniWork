# Etude7: Where In The World CS

## Start Up

### Etude7.py File

To allow for the css file ('Etude7Maps') to interact with the geojson a local server must be implemented. I have used Live Server by Ritwick Dey which can be installed via Visual Studio Code.

platform allows the program to get information on the underlying operating system. Meaning the program works for both Windows and Mac OS
```
import platform
```
geojson allows for the program to interact with geojson files
```
import geojson
```
subprocess allows for the program to open other files
```
import subprocess
```
re allows for regex which is used to split up the inputted data
```
import re
```

### Etude7Maps.html File

My Etude7Maps.html file was implemented with help from the youtube channel "MapTiler" and more particularly their series on Leaflet starting with this video: https://www.youtube.com/watch?v=wVnimcQsuwk. The file uses Leaflet.


After turning on the local server via Visual Studio Code the code can be run by entering the following commands into console.
```
python Etude\ 7.py
```
This will read from stdn in and will either return an error or open up Etude7Maps.html with a pointer at the location of the entering coordinates.

## How The Program works

The program works by first reading in the input from the user, then splitting it via spaces and commas and passing the splits to a list. It then has three checks to make. The first checking if the input can be converted to standard form, the second check checking if it can be converted to degree minute second form and the final check, checking if it can be converted to degree decimal minute form. These checks are completed by passing through a list of if-else statements. If any of the checks are valid the output is dumped into a geojson file 'outputtedCoordinates.geojson', the Etude7Maps file is opened and the outputted coordinates are displayed on the map.

Link to the demonstration video:
https://www.youtube.com/watch?v=-evhaihKboU

## Testing

I have attached a test file that I have used to check if the valid inputs are displayed correctly.
