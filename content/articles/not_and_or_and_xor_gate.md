Title: Not And Or and Xor gate
Author: Abdur-Rahmaan Janhangeer
Date: 2019-04-15 21:00
Category: blogging
Tags: gates, assembly-lang
Slug: not-and-or-and-xor-gate

## On binary and electricity

binary means of two states. electricity can flow or not. current can be on or off. current on represents true. current off represents false. or current on represents 1 and current off represents 0. it could have been apple and pears

## The Transistor as foundation 

a transistor is an electronic component. it acts as switch. but the difference is that it is controlled by electricity. so, it can be switched on and off quickly

```
    ----- metal piece
●——-      |——-●
    -/-/-/  here acts as magnet

```

if you did physics, you might remember that magnetic fields are formed around any wire carrying current and coiling the wires acts as a magnet so when current is applied, the magnet is activated, attracting the metal piece, closing the switch, and current flows from the two ends ● ●
summary : a transistor is used as a switch
—

Logic gates logic gates form the foundation of computers, a gate is no wizardry. just arrangement of switches

the 3 basic gates are : AND OR and NOT gates

## AND gate 

an AND gate checks if both conditions are true for outputting true just like if x==4 and y==2 do …. it is constructed by placing 2 transistors in series
```
     1             2
     a●———-●__●———●b
      |           |
```
current will only flow from a to b if transistor / switch 1 and switch 2 is closed

## OR gate 

an or gate gives out true if one condition is true it is constructed by using 2 transistors in parallel
```
       | 1 
    ●————-●
   a|     |b
    ●————-● 
       | 2
```
transistor 1 and 2 

if both open -> current flows 

if one open one close -> current flows 

if both closed -> no current

## NOT gate 

a not gate just outputs the opposite of the input
```
    output
       |
       |
current ——●————–●—–ground
                | input
```
when input is on / current flows, it opens the switch and current flows to ground i.e if input 1 -> no output and so 0 

if no input so the switch is closed, and current deviates to output input 0 output 1 such is the NOT gate

## XOR gate 

a xor gate is as follows where a and b are inputs

```
a  b  output
1  1    0
1  0    1
0  1    1
0  0    0
```

it is constructed as follows

![py love]({static}/img/xor1.jpg)

testing the first case of 1 1

![py love]({static}/img/xor2.jpg)

see a XOR gate is nice !

try as an exercise the other inputs

the symbol of a XOR gate is

![py love]({static}/img/xor2.jpg)

besides these gates, there are more !

## On the naming of gates

they are called gates as they control current flow just like real gates control crowd flow