# Spray-pattern-recoil-replication

adds a CS:GO and Valorant (and a few other games) recoil pattern replication using python pygame and random

video about it:
https://www.youtube.com/watch?v=WJp8e3oOUBw

inspired by garbaj:
https://www.youtube.com/c/Garbaj


# How It works and what it is

A spray pattern recoil is a realistic (usually hitscan) type recoil system found in games like CS:GO and Valorant.
The system uses a list of different x and y values that use the term to define them as "heat" (not the temperature term, but pretty similiar scientifically).
In Burst or Auto weapons (also works with single fire, but less effectively), the "heat" value increases by one (usually) per shot. If you shoot without stopping in between the fire rate, the heat value increases more and more. When the heat value increases, the bullet spray increases usually by the Y and X values, making it harder to control the more you shoot. This works by making an array or list of heat (float numbers, these numbers are the x and y positions of the bullet) values, and then using a loop that increases the heat per shot (in this case, per 0.3 seconds as that's the fire rate) and then depending on the heat value, it keeps going kn the list in an order of the heat values which have coordinates of the bullet. In order to randomize the coordinates, we use a random number generator that changes the values slightly from it's original, making the spray patter more random.

# How to change the amount of rounds of this recoil simulation

simple. just make more lists with a number of x and y coordinates, then use said lists to draw a new rect in pygame using these coordinates

may sound confusing, but here is an example:


from random import randint

heatValuesX2 = [970, 950, 940, 980]
heatValuesY2 = [450, 440, 430, 435]
heatValuesX3 = [975, 955, 950, 970]
heatValuesY3 = [370, 390, 350, 340]
heatValuesX4 = [980, 970, 965, 990]
heatValuesY4 = [290, 270, 310, 260]
number1Y = heatValuesY1
number1X = heatValuesX1
number2X = heatValuesX2[randint(0,3)]
number2Y = heatValuesY2[randint(0,3)]
number3X = heatValuesX3[randint(0,3)]
number3Y = heatValuesY3[randint(0,3)]
number4X = heatValuesX4[randint(0,3)]
number4Y = heatValuesY4[randint(0,3)]

# this is a 4 round burst, then, just add a pygame rectangle with the coordinates of the next heat value (which is 4 here), and done!

# Pros
Simple yet effective, popular, balanced

# Cons
could be tedious to work with high magazines. Alot of the work is manual and isn't automated in the program

# How is it realistic?
When shooting an auto weapon in real life for a long time, the barrel heats up and the metal expands slightly which affects trajectory.
Newtons third law of motion is the main science of recoil patterns

A bullet gets shot, a backward force is sent to the gun to your direction, the center of rotation gets affected, the gun gets tilted, causing it to shoot higher. Plus the affected trajectory of the heated barrel, and the rotation being random depending your grip to the gun, this causes it to go in a random bullet pattern.

if "VF" is the force of velocity, and "P" is position then the equation goes like this:

VF (Force of velocity of the bullet) - 0 (Position of the gun, assuming the force is pushed the exact same amount as the velocity) = P (The final position of the gun, after the shot)

I couldn't bother calculating the rotation, I'm too lazy

Have fun modifying
