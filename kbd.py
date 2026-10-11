# kbd.py - キーボード入力管理モジュール

inkey = 0
key = [0] * 256

def keycls():
    global key, inkey
    key = [0] * 256
    inkey = 0

def keyup(e):
    global key, inkey
    key[e.keycode] = 0
    inkey = 0

def keydown(e):
    global key, inkey
    key[e.keycode] += 1
    inkey = e.keycode

def bind_events(widget):
    widget.bind("<KeyPress>", keydown)
    widget.bind("<KeyRelease>", keyup)

# キーコード定数
ENTER = 13
SPACE = 32
LEFT  = 37
UP    = 38
RIGHT = 39
DOWN  = 40
ESC   = 27
A     = 65
Z     = 90
