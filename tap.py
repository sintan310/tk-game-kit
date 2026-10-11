# tap.py - マウス入力管理モジュール

x = 0
y = 0
clicked = False

def _on_motion(e):
    global x, y
    x = e.x
    y = e.y

def _on_click(e):
    global clicked
    clicked = True

def _on_release(e):
    global clicked
    clicked = False

def bind_events(widget):
    widget.bind("<Motion>", _on_motion)
    widget.bind("<ButtonPress-1>", _on_click)
    widget.bind("<ButtonRelease-1>", _on_release)
