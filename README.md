fingerjoint
===========
Convenience class to create finger joint panels for lasercut boxes. 

See http://en.wikipedia.org/wiki/Finger_joint for a good discussion of what these are.

I use Ponoko.com to make these, but there are a variety of other sites that do this (Big Blue Saw, eMachineshop, etc.). Your local hackerspace might also have a laser cutter.

Why bother with this code? A few reasons:

* I'm not very good at fiddling around in vector drawing programs.
* It's difficult to remember to account for things like kerf (the width of the laser beam).
* Doing a bunch of test prints gets slow and expensive.
* My original finger joint project was an octagonal box (I hope to eventually expand this library's capabilities to non-rectilinear geometries). This involved a lot of graph paper and head scratching -- I'm not great at visualizing things in three dimensions. I'd prefer to solve these problems once, then ask a script to repeat the lessons I learned.


Suggested Values
----------------
Check the specs of whatever materials you intend to use, and whatever documentation of kerf is available. For Ponoko wood materials, thickness variance tends to be 10% and kerf can be set to 0.2mm.


Requirements
------------
* numpy


Credits
-------
Tom Lee <thomas.j.lee@gmail.com>


License
-------
See the LICENSE file. Do what you want / please don't sue me! Pull requests welcome.
