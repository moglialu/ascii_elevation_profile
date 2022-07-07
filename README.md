# ascii_elevation_profile

This is WIP!

It is code to create a very simplified elevation profile out of a gpx-file. It only uses ascii charackters in one line.
Each symbol represents roughly 250m in distance. A bigger symbol stands for higher elevation.
It is not supposed to be exact but to give you a very rough idea of the ups and downs of a trail. 


For example:

1. ..:::iiIIÎÎÎÎIiiiiiiiiiIÎÎIIIii::::::.................... 
 * (https://www.outdooractive.com/de/route/wanderung/midi-pyrenees/pyrenees2018tag61/127256744/) 
2. ........................:::::::::::iiIIIIIIÎÎÎIIIIii:iiiiIIIIIIIIIIIÎÎÎÎÎÎIÎÎÎIIIIIIiiiiii:::::::i:::....... 
 * (https://www.outdooractive.com/de/route/mountainbike/schwarzwald/mountainbike-tour-auf-den-totenkopf-im-kaiserstuhl/6409788/)


The code is written in python. It uses minidom, pandas and the math module.

To use it you have to place your gpx-file in the same directory as main.py. Run the script and enter the name of your gpx-file.


For better and more beautiful elevation profiles I recommend outdooractive or komoot. Both are very good applications for planing a tour!


 
  


 

