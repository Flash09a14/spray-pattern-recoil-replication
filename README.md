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

```python
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
```

#### this is a 4 round burst, then, just add a pygame rectangle with the coordinates of the next heat value (which is 4 here), and done!

# Pros
Simple yet effective, popular, balanced

# Cons
could be tedious to work with high magazines. Alot of the work is manual and isn't automated in the program

# How is it realistic?
When shooting an auto weapon in real life for a long time, the barrel heats up and the metal expands slightly which affects trajectory.
Newtons third law of motion is the main science of recoil patterns

A bullet gets shot, a backward force is sent to the gun to your direction, the center of rotation gets affected, the gun gets tilted, causing it to shoot higher. Plus the affected trajectory of the heated barrel, and the rotation being random depending your grip to the gun, this causes it to go in a random bullet pattern.

# Math
Law of Conservation of Momentum
Newton's Third Law states that every applied force has an equal and opposite reaction. An example commonly cited when explaining this law is that of a speeding car hitting a brick wall. The car exerts a force on the wall, and the wall exerts a reciprocal force on the car that crushes it. Mathematically, the incident force (FI) equals the force (FR) magnitude and acts in the opposite direction:
```
FI=−FR
```
Newton's Second Law defines force as mass time acceleration. Acceleration is change in velocity:
```
a = Δv/Δt
```
so net force can be expressed:
```
F=m•Δt/Δv
```
Calculating Recoil Velocity
In a typical recoil situation, the release of a body of smaller mass (body 1) has an impact on a larger body (body 2). If both bodies start from rest, the law of conservation of momentum states that m1v1 = -m2v2. The recoil velocity is typically the velocity of body 2 after the release of body 1. This velocity is
```
v2=−m1/m2•v1
```
Example
What is the recoil velocity of an 8-pound Winchester rifle after firing a 150-grain bullet with a speed of 2,820 feet/second?
Before solving this problem, it's necessary to express all quantities in consistent units. One grain is equal to 64.8 mg, so the bullet has a mass (mB) of 9,720 mg, or 9.72 grams. The rifle, on the other hand, has a mass (mR) of 3,632 grams, since there are 454 grams in a pound. It's now easy to calculate the recoil speed of the rifle (vR)in feet/second:
```
vR = mB/mR•vB = -9.72/332•2,820 = -7.55 ft
```
math research done on sciencing.com

# CS:GO Patterns on each weapon (that way you can replicate it in this code)
https://dmarket.com/blog/csgo-spray-patterns/
