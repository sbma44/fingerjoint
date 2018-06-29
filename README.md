fingerjoint
===========
Convenience class to create finger joint panels for lasercut boxes. 

See http://en.wikipedia.org/wiki/Finger_joint for a good discussion of what these are.

I published a blog post explaining this project's rationale and showing off some early results here:

http://tomlee.wtf/2013/05/31/lasercut-fingerjoint-enclosures-pictures-code/

I use Ponoko.com to make these, but there are a variety of other sites that do this (Big Blue Saw, eMachineshop, etc.). Your local hackerspace might also have a laser cutter.

Why bother with this code? A few reasons:

* I'm not very good at fiddling around in vector drawing programs.
* It's difficult to remember to account for things like kerf (the width of the laser beam).
* Doing a bunch of test prints gets slow and expensive.
* My original finger joint project was an octagonal box (I hope to eventually expand this library's capabilities to non-rectilinear geometries). This involved a lot of graph paper and head scratching -- I'm not great at visualizing things in three dimensions. I'd prefer to solve these problems once, then ask a script to repeat the lessons I learned.


Suggested Values
----------------
Check the specs of whatever materials you intend to use, and whatever documentation of kerf is available. For Ponoko wood materials, thickness variance tends to be 10% and kerf can be set to 0.2mm.


Example Code
------------
The light_box.py script generates SVGs that can subsequently be used to construct a box. A sample EPS file is provided that reflects what I submitted to Ponoko to successfully print the design. Note that there are differences between the SVG and the EPS -- the script is not yet intended to produce ready-to-print vector output.


Known Issues / TODO
-------------------
* there is some path doubling on fingers aligned with bottom edges; this produces double-cutting
* default kerf value may be slightly too large
* would like to add support for complete box construction, both for rectilinear and other geometries


Requirements
------------
* numpy


Credits
-------
Tom Lee <thomas.j.lee@gmail.com>


License
-------
See the LICENSE file. Do what you want / please don't sue me! Pull requests welcome.
