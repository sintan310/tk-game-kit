# TK Game Kit

白鴎大学 佐藤ゼミで「TK Game Project」として使用してきた、 Python・Tkinter用のゲーム制作ライブラリです。

マウス・キーボード入力、図形や画像の描画、画面更新などの定型処理を簡略化し、ゲームの仕組みやキャラクターの動きの実装に集中できるようにしています。

このREADMEでは、利用できる変数、定数、関数を一覧で説明します。

> このライブラリは、廣瀬豪さんの書籍『7大ゲームの作り方を完全マスター！ ゲームアルゴリズムまるごと図鑑』（技術評論社、2022年）で紹介されている考え方を参考に、Tkinter向けに実装した学習用ラッパーです。

## 準備

このリポジトリをダウンロードまたはクローンし、次のファイルを同じフォルダーに置いてください。

```text
README.md
main.py
wlib.py
tap.py
kbd.py
```

`main.py`がゲーム記述用のメインファイルです。このファイルにゲームの内容を書いていきます。

## 実行方法

ターミナルまたはコマンドプロンプトで、ファイルのあるフォルダーへ移動して実行します。

```bash
python main.py
```

環境によっては、次のように実行します。

```bash
python3 main.py
```

## main.pyの構成

ゲーム開始時に一度だけ行う初期化は、`setup()`に記述します。

キャラクターの移動、当たり判定、画面描画など、毎フレーム行う処理は`main()`に記述します。`main()`は約30fpsで繰り返し呼び出されます。

主に編集する場所は次の3か所です。

1. キャラクターの変数・関数を書く場所
2. ゲーム全体の初期化を書く`setup()`
3. 毎フレーム実行する処理を書く`main()`

## マウス操作

`tap`モジュールから現在のマウス状態を取得できます。

- `tap.x`: マウスポインターのx座標
- `tap.y`: マウスポインターのy座標
- `tap.clicked`: マウスの左ボタンを押している間は`True`、離すと`False`

## キーボード操作

`kbd.key[キーコード]`で、キーの押下状態を取得できます。

- `0`: 押されていない
- `1`: 押した直後
- `2`以上: 押し続けている

次のキーコードが定義されています。

- `kbd.ENTER`
- `kbd.SPACE`
- `kbd.LEFT`
- `kbd.UP`
- `kbd.RIGHT`
- `kbd.DOWN`
- `kbd.ESC`
- `kbd.A`
- `kbd.Z`

次の関数が定義されています。

```python
kbd.keycls()
# キーボードの押下状態を初期化します。通常はsetup()の中で呼び出します。
```

## 図形の描画

色は`"red"`や`"white"`などの色名、または`"#ff0000"`などの形式で指定します。

主な描画オプションは次のとおりです。

- `outline`: 線の色
- `width`: 線の太さ
- `fill`: 塗りつぶし色

次の関数が定義されています。

```python
draw_line(x1, y1, x2, y2, outline="white", width=1)
# (x1, y1)から(x2, y2)まで線を描画します。
```

```python
draw_circle(x, y, r, outline="white", width=1, fill="")
# (x, y)を中心として、半径rの円を描画します。
```

```python
draw_poly(pos_list, outline="white", width=1, fill="")
# 多角形を描画します。
# pos_listには各頂点を[x1, y1, x2, y2, x3, y3, ...]の形式で指定します。
```

```python
draw_tri(x, y, r, angle=0, outline="white", width=1, fill="")
# (x, y)を中心として正三角形を描画します。
# rは中心から頂点までの距離、angleは回転角度です。
```

```python
draw_rect(x1, y1, x2, y2, outline="white", width=1, fill="")
# (x1, y1)と(x2, y2)を対角とする長方形を描画します。
```

```python
draw_rect_cpos(x, y, w, h, outline="white", width=1, fill="")
# (x, y)を中心として、幅w、高さhの長方形を描画します。
```

```python
draw_rect_angle(x, y, w, h, angle=0, outline="white", width=1, fill="")
# (x, y)を中心として、幅w、高さhの長方形を描画します。
# angleには回転角度を度数で指定します。
```

```python
draw_roundrect(x1, y1, x2, y2, r, fill="blue")
# (x1, y1)と(x2, y2)を対角とする角丸長方形を描画します。
# rは四隅の丸みの半径です。
```

## 文字の描画

次の関数が定義されています。

```python
ftext(text, x, y, font="Times New Roman", size=20, color="red", align="center")
# 座標(x, y)に文字列を描画します。
```

- `text`: 描画する文字列
- `font`: フォント名
- `size`: 文字サイズ
- `color`: 文字色
- `align`: 文字揃え

`align`には次の値を指定できます。

- `"left"`: 左揃え
- `"center"`: 中央揃え
- `"right"`: 右揃え

## 画像の描画

次の関数が定義されています。

```python
load_img(id_num, filename)
# 画像ファイルを読み込み、画像IDを付けて登録します。
```

- `id_num`: `0`から`255`までの画像ID
- `filename`: 読み込む画像のファイル名

通常は`setup()`の中で呼び出します。

```python
draw_imgc(id_num, x, y)
# load_img()で登録した画像を描画します。
# 画像IDをid_numで指定し、画像の中心を座標(x, y)に合わせます。
```

## 数学関数

次の関数が定義されています。

```python
sin(deg)
# 角度degの正弦を返します。角度はラジアンではなく度数で指定します。
```

```python
cos(deg)
# 角度degの余弦を返します。角度はラジアンではなく度数で指定します。
```

```python
rnd(max_val)
# 0以上max_val以下のランダムな整数を返します。
```

```python
get_distance(x1, y1, x2, y2)
# 2点(x1, y1)と(x2, y2)の距離を返します。
```

## イージング関数

引数`t`には、通常は`0`から`1`までの値を指定します。

### イーズイン

ゆっくり始まり、次第に変化が大きくなります。

```python
ease_in(t)   # 2次のイーズイン
ease_in4(t)  # 4次のイーズイン
ease_in6(t)  # 6次のイーズイン
ease_in8(t)  # 8次のイーズイン
```

### イーズアウト

大きく変化してから、次第に変化が小さくなります。

```python
ease_out(t)   # 2次のイーズアウト
ease_out4(t)  # 4次のイーズアウト
ease_out6(t)  # 6次のイーズアウト
```

## ライブラリ準備用の関数

次の関数は`main.py`の準備部分で使用します。通常、ゲーム内容を記述するときに直接呼び出す必要はありません。

```python
set_canvas(cvs)
# wlib.pyが描画に使用するTkinterのCanvasを登録します。
```

```python
tap.bind_events(widget)
# マウスイベントを登録します。
```

```python
kbd.bind_events(widget)
# キーボードイベントを登録します。
```

## 参考文献

廣瀬豪『7大ゲームの作り方を完全マスター！ ゲームアルゴリズムまるごと図鑑』技術評論社、2022年。

## 利用について

本リポジトリは、ゼミにおけるPythonゲーム制作の学習用教材として作成しています。

公開、再配布、改変などの条件は、リポジトリに掲載するライセンスに従ってください。



## ライセンス

本リポジトリに含まれるPythonプログラムは、 MIT Licenseのもとで公開しています。 詳しくは`LICENSE`を参照してください。
