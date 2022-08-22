'''
Given a rectangular matrix of integers m, consider all the paths starting from the top right to the bottom left corner and return the maximum sum of numbers among all paths.

You can only move in two directions: left or down.

Example 1

Input:

m = [[0,0,0],[0,1,1], [0,1,1]]

Output:

3

Explanation:

The sum of the elements in the following path, which is 3, is the maximum.

            0   0   0   < start here
                    ▼
            0   1   1
                    ▼
End here >  0 ◀ 1 ◀ 1

Also, the following path gets the same result:

             0   0   0 	< start here
                     ▼
             0   1 ◀ 1
                 ▼
End here >   0 ◀ 1   1

Example 2

Input:

m = [[1,2], [3,4], [6,-10]]

Output:

15

Explanation:

The sum of the elements in the following path, which is 15, is the maximum.

            1   2     < start here
                ▼
            3 ◀ 4
            ▼
End here >  6 -10
'''
