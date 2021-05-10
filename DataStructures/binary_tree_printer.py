#!/usr/bin/python3

import sys

# p̵̯̖̾̈́̏r̴͊̀ͅi̸̲̒n̵͔͕͑̈ͅt̶̹̹͗͝ ̷̙̋́á̸͎̻ ̵̳͕̼̆́b̷̨̯̉͜î̴̗͉̻̀͋n̵̖̮͊̈́a̸͍̒̐ṙ̶̰̗̪ỷ̸͉̰ ̸͙͆̚ṯ̸̡̒̈́͊r̷̞͠ẽ̴̟͂͜ȩ̵̡̣̂̿́ ̵̼͇͊͂͜ó̴̬n̷̘̽ ̵̤͓̪̊̆̈́ȧ̷̟̥ ̸̧̑̒c̴̛͔̃̃a̷͙̓͘n̶̡͍̍v̴̩̗͋͊͝a̶͇̅̽s̸̼̟͐̑̾

class Node:
    def __init__(self,value):
        self.key = value
        self.left = None
        self.right = None

class Canvas:
    def __init__(self,width):
        self.line_width = width
        self.canvas = []

    def put_char(self,x,y,c):
        if x < self.line_width:
            pos = y*self.line_width + x
            l = len(self.canvas)
            if pos < l:
                self.canvas[pos] = c
            else:
                self.canvas[l:] = [' ']*(pos - l)
                self.canvas.append(c)

    def print_out(self):
        i = 0
        for c in self.canvas:
            sys.stdout.write(c)
            i = i + 1
            if i % self.line_width == 0:
                sys.stdout.write('\n')
        if i % self.line_width != 0:
            sys.stdout.write('\n')

def print_binary_tree_r(t,x,y,canvas):
    max_y = y
    if t.left != None:
        x, max_y, lx, rx = print_binary_tree_r(t.left,x,y+2,canvas)
        x = x + 1
        for i in range(rx,x):
            canvas.put_char(i, y+1, '/')

    middle_l = x
    for c in str(t.key):
        canvas.put_char(x, y, c)
        x = x + 1
    middle_r = x

    if t.right != None:
        canvas.put_char(x, y+1, '\\')
        x = x + 1
        x0, max_y2, lx, rx = print_binary_tree_r(t.right,x,y+2,canvas)
        if max_y2 > max_y:
            max_y = max_y2
        for i in range(x,lx):
            canvas.put_char(i, y+1, '\\')
        x = x0

    return (x,max_y,middle_l,middle_r)

def print_tree(t):
    print_tree_w(t,80)

def print_tree_w(t,width):
    canvas = Canvas(width)
    print_binary_tree_r(t,0,0,canvas)
    canvas.print_out()

if __name__ == "__main__":
    def binary_tree_add(t,k):
        if t == None:
            return Node(k)

        if k <= t.key:
            t.left = binary_tree_add(t.left,k)
        else:
            t.right = binary_tree_add(t.right,k)

        return t

    if len(sys.argv) > 1:
        W = int(sys.argv[1])
    else:
        W = 80
    T = None
    for l in sys.stdin:
        for n in l.strip('\n').split(' '):
            T = binary_tree_add(T, int(n))

    print_tree_w(T,W)
