Week 7 Materials  
################

:date: 2015-01-26
:summary: Making the connection  between position, velocity, and acceleration.  What causes acceleration?
:category: lessons
:tags: acceleration, velocity, graphs, motion maps, pressure


=====
Day 1
=====

 1. Download the Gas Properties simulation at: http://phet.colorado.edu/en/simulation/gas-properties

 2. Explore the behavior of the simulation and find as many ways as possible to increase the pressure inside the chamber.

 3. In your notes: what are all the things you can do that increase the pressure inside the chamber?  Why does each of those affect the pressure?

 4. What are all  the things you can do that decrease the pressure inside the chamber?  Why does each of these affect the pressure?



===========
Day 2 and 3
===========

 1. This `Desmos graph <https://www.desmos.com/calculator/hs3cl7los4>`_  shows the velocity of an object over time.  Use it to figure out how *far* the object involved travelled.


This is harder than other ones we've done, isn't it?  What is different?

The issue is that the speed is changing.  If the speed is constant, it's easy:

Distance travelled equals Speed times Time.

:math:`meters = \frac{meters}{second} \cdot seconds`

which suggests that we should try:

:math:`\frac{30 meters}{second} \cdot 10 seconds = 300 meters`

but that is much too big, because it uses the *final* speed of the object.  It doesn't get to 30 meters per second until the very last instant, so it is always travelling slower than that, so it shouldn't get as far as 300 meters.

So how do we handle this situation where the speed is changing?


 2. Notice that when the speed is constant, the speed vs. time  graph is always a horizontal line.  Take a look at the `following graph <https://www.desmos.com/calculator/zy4mrufuzm>`_.  You can click on the folder icon next to the description to see how the graph is made.  If you move the time slider back and forth, you will see the line showing the speed at each moment advance, and a rectangle is formed underneath the line.  The rectangle gets bigger as the time advances forward, smaller as the time decreases.

**If you put the time at 5 seconds, how far has the object travelled?**

Well the speed of 2meters per second, for a time of 5 seconds gives a distance of 10 meters.

The interesting thing is that *10* is also the area of that rectangle.

The base is **5** -- that's the time.

The height is **2** -- that's the speed.

**Does that always work?**

Open up the folder in the graph and change the speed to some number other than 2, and then move the time slider back and forth.  Notice that you always get a rectangle.  And notice that the distance travelled is *always* the base of that rectangle times the height,or the *time* times *the speed*.

 3. How do we apply this idea to the case where the speed is changing?  Well the calculation we were doing with the base and height is really finding the *area* of the rectangle.  So maybe when the speed is changing, we should be finding the *area* again -- except now it doesn't form a rectangle, it forms a `triangle <https://www.desmos.com/calculator/5p9xtroxeb>`_.






=====
Day 4
=====

 1. We are trying to figure out the relationship between force and acceleration. Do a systematic investigation using the PhET simulation, http://phet.colorado.edu/en/simulation/forces-and-...

Using the "Motion" tab

Choose a mass to put on the skateboard, and push it at a force of 100N.

Time how long it takes for the skateboard to get from rest (Zero speed) to the "maximum" speed when the pusher falls over

The acceleration is a measure of how quickly the speed changes -- so the change in speed divided by the time it takes for the speed to change.

On this simulation, we don't have units for the speedometer, but as long as we are consistent, we can use whatever units are available -- so the speedometer dial has 20 divisions on it, so let's say that the change in speed is +20 -- an increase of 20 speed units.

Repeat the measurements using 5 different force levels (100 through 500 Newtons)

Then repeat using 3 different masses (100kg, 200kg, 300kg) 

 2. We will discuss the results on Monday.

   
