'''
Given a text and a subText that might be in the text, return the maximum distance from the subText to any side of the text. If the subText is not in the text, return -1. The distance is the number of characters from the subText to any of the text sides.

Example 1:

Input:

    text = abcdefghi
    subText = de

Output: 4

Explanation:

The minimum distance is the one on the right side (fghi).

Example 2:

Input:

    text = abcdefgci
    subText = c

Output: 7

Explanation:

The maximum distance is on the left side to the second c.

Constraints:

    1 <= text.length <= 2147483647
    1 <= subText.length <= text.length

Text and subText contain only English lowercase letters
'''

#text = input('Digita la cadena de texto: ') 
subtext = input('Digita el texto a buscar: ')

file = open('temp.txt', 'w')
file.write(input('Texto: '))
file.close()

#first=(open('temp.txt', 'r').read().find(subtext))

with open('temp.txt') as f:
    if subtext in f.read():
        answer = 0 
    else:
        print(-1)

 

