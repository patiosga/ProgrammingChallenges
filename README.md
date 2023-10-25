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
Input:  
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


2. Find Lakes problem  
  
The task is to find the number of the lakes as well as the surface area of each one of them. The encoded image is given as  
a 2D array of tiles that can be either a ground tile or a water tile. Each tile in the image corresponds to one square meter of area. Given a  
single water tile, a lake is defined to cover all the water tiles that are reachable from the initial tile by performing an arbitrary sequence  
of up/down/left or right moves on water tiles (not diagonally). You can assume that the border tiles found at the edge of the image are always  
ground tiles  
  
Input:  
  
The first two lines of the input contain two integers N and M. These define an N x M 2D array  
of tiles. The next N lines of the input are strings of exactly M characters, which are a combination of to mark a ground tile and 1 to mark a water tile.  
OR  
You can select a randomly generated matrix.  

Warning!! In order for the user input to work all positions that are at the borders of the matrix must be equal to 0 (ground tiles).  
  
Output:  
  
The first line of the output should be a single integer K that is the number of distinct lakes found in the data. The second line should have K  
space separated integers that are the sizes in square meters of each lake. The integers in the second line (lake sizes) must be in sorted order,  
from the smallest to the largest.  

e.g. (of user input)  
Input:  
00000  
01100  
01010  
01010  
00000  
  
Output:  
Number of lakes 2  
Sorted by size:  2, 4  
  
  
3. Spies Phone Number problem  
  
  
The NIS spy network has decided to change the phone number from its headquarters every day as an extra security measure. To inform the  
spies about the new number, a sequence of words is given only to the spies (a total of 10 words), which they must then compare to a sequence  
of words from a newspaper, word by word. The comparison of words is done by finding the minimum number of operations required to make the  
first word identical to the second word. The possible operations that can be performed on the first word are the following 
    
Operation 1 (INSERT) Insert any character before or after any index of str1  
Operation 2 (REMOVE): Remove a character from str1  
Operation 3 (REPLACE): Replace a character at any index of str1 with some other character.  
  
Input:  
The first line contains the number (N) of words in the newspaper paragraph that will be used The second line contains the 10 positions  
from the words that must be used from the given paragraph. The third line contains the 10 initial wards of the secret phrase. The   
fourth line provides the N words of the paragraph.  
  
Output:  
The phone numbers.

Example:

Sample Input  
1 3 2 5 6 8 15 10 11 12  
hello i cannot wait to start coding for this problem  
amidst the tranquil forest a cascade of colors painted the trees in a mesmerizing dance
  
Sample Output 1  
6 8 6 3 7 5 5 3 3 7  




  
