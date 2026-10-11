# wlib.py - 描画・アニメーション・数学関数モジュール
import tkinter
import math
import random


canvas = None

def set_canvas(cvs):
    global canvas
    canvas = cvs



# 数学関数 ---------------------------------------------
# 三角関数：引数は角度 0 から 360（ラジアンでなくて良い）    
def sin(deg):
    return math.sin(math.radians(deg))

def cos(deg):
    return math.cos(math.radians(deg))

def rnd(max_val):
    return random.randint(0, max_val)

def get_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)



    
# 図形の描画など -----------------------------------------------------
# 線：(x1, y1) - (x2, y2)
def draw_line(x1,y1, x2,y2, outline="white", width=1):
    canvas.create_line(x1,y1, x2,y2, fill=outline, width=width)
    

# 丸：(x,y) を中心に半径rの円    
def draw_circle(x, y, r, outline="white", width=1, fill=""):
    canvas.create_oval(x - r, y - r, x + r, y + r,
                       fill=fill, outline=outline, width=width)



# 多角形: pos_list には各頂点を [x1,y1, x2,y2, x3,y3, ...] と格納する
def draw_poly(pos_list, outline="white", width=1, fill=""):
    canvas.create_polygon(pos_list,
                       fill=fill, outline=outline, width=width)


# 正三角形 (x,y) を中心に頂点までの距離を r とする
def draw_tri(x, y, r, angle=0, outline="white", width=1, fill=""):
    pos = [x+cos(270+angle)*r, y+sin(270+angle)*r,
           x+cos(30+angle)*r,  y+sin(30+angle)*r,
           x+cos(150+angle)*r, y+sin(150+angle)*r]
    draw_poly(pos, outline, width, fill)
    


# 四角形： (x1,y1) - (x2,y2) の長方形を描画    
def draw_rect(x1, y1, x2, y2, outline="white", width=1, fill=""):
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill, outline=outline, width=width)


# 四角形： (x,y) を中心とした幅 w、高さ h の長方形を描画    
def draw_rect_cpos(x, y, w, h, outline="white", width=1, fill=""):
    w_half = w/2
    h_half = h/2
    canvas.create_rectangle(x-w_half, y-h_half, x+w_half, y+h_half,
                            fill=fill, outline=outline, width=width)
    

# 四角形： (x1,y1) を中心にして、幅 w、高さ h の長方形。回転角度は angle で指定
def draw_rect_angle(x,y, w, h, angle=0, outline="white", width=1, fill=""):
    points = [
        (-w / 2, -h / 2),
        ( w / 2, -h / 2),
        ( w / 2,  h / 2),
        (-w / 2,  h / 2)
    ]

    pos_list = []

    for px, py in points:
        rx = x + px * cos(angle) - py * sin(angle)
        ry = y + px * sin(angle) + py * cos(angle)

        pos_list.extend([int(rx), int(ry)])


    draw_poly(
        pos_list,
        outline=outline,
        width=width,
        fill=fill
    )
        

# 角丸四角形：(x1,y1) - (x2,y2) の角丸四角形。四隅の丸の半径は r で指定。
def draw_roundrect(x1, y1, x2, y2, r, fill="blue"):
    r2=r*2

    # 四隅の 1/4円
    canvas.create_arc(x1,y1, x1+r2, y1+r2, fill=fill, outline="",
                   start=90, extent=90, width=0)
    canvas.create_arc(x2-r2, y1, x2, y1+r2, fill=fill, outline="", 
                   start=0, extent=90, width=0)
    canvas.create_arc(x2-r2, y2-r2, x2, y2, fill=fill, outline="", 
                   start=270, extent=90, width=0)
    canvas.create_arc(x1, y2-r2, x1+r2, y2, fill=fill, outline="", 
                   start=180, extent=90, width=0)
    
    # 塗りつぶせていないところを長方形で塗る
    draw_rect(x1+r, y1, x2-r, y2, fill=fill, outline="", width=0)
    draw_rect(x1, y1+r, x2+2, y2-r, fill=fill, outline="", width=0)

    
# テキスト
def ftext(text, x, y, font="Times New Roman", size=20, color="red", align="center"):
    align_str = {
        "center": "center",
        "left": "nw",
        "right": "ne"
    }
    canvas.create_text(x, y, text=text, anchor=align_str[align], font=(font, size), fill=color)


# 画像
MAX_IMG_NUM = 256
img = [None] * MAX_IMG_NUM 

def load_img(id_num, filename):
    if id_num < 0 or id_num >= MAX_IMG_NUM:
        raise ValueError(
            "ERROR: load_img の id_num は 0 から {}までを指定してください: id_num={}".format(
                MAX_IMG_NUM-1, id_num))

    img[id_num] = tkinter.PhotoImage(file=filename)

    
def draw_imgc(id_num, x, y):
    if img[id_num] != None:
        canvas.create_image(x,y, image=img[id_num])

        
        
# イージング -------------------------------------------------------
# しり上がりで上昇
def ease_in(t):   
    return t*t

def ease_in4(t):
    return t*t*t*t

def ease_in6(t):
    return t*t*t*t*t*t

def ease_in8(t):
    return t*t*t*t*t*t*t*t



# 一気に上昇してジワジワ1へ（参考： https://easings.net/ja ）
def ease_out(t):  
    return t*(2-t)     #  1 - (1-x) * (1-x)

def ease_out4(t):
    return 1 - (1-t)**4

def ease_out6(t):
    return 1 - (1-t)**6
