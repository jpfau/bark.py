#!/usr/bin/env python
import sys

# Add your own breed!
dogs = {
# This is the default
'puppy': '''
     __
    (,'`-;  @@
    / ,-` 
   /  |
(\/_)_\_''',
# And because this meme just will not die, and people would add it anyway, I've
# added this in advance
'shiba': '''   ,    ,
  _|\__/ | 
 /     ` (
/ o,,o  \ \  @@
|,#*     )|
 >^-'   ' \ 
|`---      `'''
}

def bark(dog, message):
    template = dogs[dog].split('\n')
    message = message.split('\n')
    rowLength = max([len(l) // 2 for l in message])
    rows = []
    rows.append('  \\\'{}/'.format(''.join(['v\''] * rowLength)))
    for line in message:
        rows.append(' <{{: ^{}}}>'.format(rowLength * 2 + 3).format(line))
    rows.append('_=^,{}\\'.format(''.join(['^,'] * rowLength)))
    output = []
    start = -1
    # Reverse everything so that we construct the message from the bottom first
    template.reverse()
    for line in template:
        if start < 0:
            start = line.find('@@')
        if start >= 0 and rows:
            line = '{{: <{}}}'.format(start).format(line)
            line = line[:start] + rows.pop()
        output.append(line)
    rows.reverse()
    # If we have something left over after the message, put that on the top
    for line in rows:
        output.append('{{: >{}}}'.format(start + len(line)).format(line))
    output.reverse()
    return '\n'.join(output)

if __name__ == '__main__':
    dog = 'puppy'
    if len(sys.argv) > 1:
        if sys.argv[1] == '-d' and len(sys.argv) > 2:
            dog = 'shiba'
            message = ' '.join(sys.argv[2:])
        else:
            message = ' '.join(sys.argv[1:])
    else:
        message = 'Bark!'
    print(bark(dog, message))
