#Find Angle MBC
#https://www.hackerrank.com/challenges/find-angle/problem?h_r=next-challenge&h_v=zen

"""

so we know the length of BA
but let's just say we know the point of A = (0,BA)

and we know the length of BC
but let's just say we know the point C = (BC,0)

...of course B is (0,0)

this means the mid point or M is the average of A and C points.
M= (BC/2,BA/2)

know ...let's draw a new line from M to intersect with the X axis, in order to create a 90 degree angle


|
|     M
|     |
|     |
|_____|______

at the point at which it intersects we'll call i, for Intersect.
BI = BC/2
MI = BA/2

so we know the side Opposite from our angle, 
and the side Adjacent from our angle

so now we solve with atan(BI,MI)
and format correctly
"""

```python
import math

A = int(input())
C = int(input())

# print(A,C)
mPoint = [C/2,A/2]

print('{:.0f}°'.format(math.degrees(math.atan(mPoint[1]/mPoint[0]))))
```

