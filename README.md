# ProgrammingChallenges
In this repository I upload every prorgamming problem I find interesting and solve.


1. Equations Problem

Let x1, x2, ..., xn be variables.
You are given an ordered list of contraints (equations) in the form of xi = xj or xi = - xj. The constraints are transitive.
Then for each contraint between two variables xi and xj, you must mark it with:
  a. The letter N if it is a new contraint
  b. The letter E if it is an existing contraint (the constraint existed either directly or transitively)
  c. The letter C if it is a contradicting constraint, meaning that it is impossible to fullfill the constraint given the previous ones.
Input:
The first two lines of the input are the number of variables (N) and the number of equations (M). After the second line there are M more
lines, each with two integers I and J seperated with a whitespace character (where I and J represent two variables not necessarily different).
If J < 0 the it represents the contraint xi = - xj, otherwise xi = xj.

The program stop when a contradicting constraint is given.

e.g 
4
7
1 2
3 -4
1 -4
1 3
2 -4
2 -3
1 -4

Output:
N
N
N
E
E
C

