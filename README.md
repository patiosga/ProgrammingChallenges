# ProgrammingChallenges
In this repository I upload every prorgamming problem I find interesting and solve.


1. Equations Problem

Let x1, x2, ..., xn be variables.<br>
You are given an ordered list of contraints (equations) in the form of xi = xj or xi = - xj. The constraints are transitive.<br>
Then for each contraint between two variables xi and xj, you must mark it with:<br>
  a. The letter N if it is a new contraint<br>
  b. The letter E if it is an existing contraint (the constraint existed either directly or transitively)<br>
  c. The letter C if it is a contradicting constraint, meaning that it is impossible to fullfill the constraint given the previous ones.<br>
Input:<br>
The first two lines of the input are the number of variables (N) and the number of equations (M). After the second line there are M more<br>
lines, each with two integers I and J seperated with a whitespace character (where I and J represent two variables not necessarily different).<br>
If J < 0 the it represents the contraint xi = - xj, otherwise xi = xj.<br>
<br>
The program stop when a contradicting constraint is given.<br>
<br>
e.g <br>
4<br>
7<br>
1 2<br>
3 -4<br>
1 -4<br>
1 3<br>
2 -4<br>
2 -3<br>
1 -4<br>
<br>
Output:<br>
N<br>
N<br>
N<br>
E<br>
E<br>
C<br>

