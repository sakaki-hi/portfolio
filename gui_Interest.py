"""
ポートフォリオ用作品
定期預金向けの利息計算アプリを開発する。
"""

import tkinter as tk
t = ("Yu Gothic UI",16)

period = None

def my_f(num):
    global period

    try:
        #テキストボックスから金額を取ってくる
        principal = int(box1.get()) # Entry型が待っているメソッド
        int_rate = float(box2.get()) / 100
        error_label.config(text="")
    except ValueError:
        print("数字を入力してください")
        error_label.config(text="数字を入力してください")
        return

    tax_rate = 0.20315
    match num:
        case 1:
            years = 3/12
            period = "3か月"
        case 2:
            years = 6/12
            period = "6か月"
        case 3:
            years = 1
            period = "1年"
        case 4:
            years = 3
            period = "3年"
        case 5:
            years = 5
            period = "5年"
    net_int = principal * int_rate * years * (1 - tax_rate) 
  
    box3.delete(0, tk.END)
    box3.insert(tk.END,f"{round(net_int):,}") 

def my_f2():
    #CSVファイルに保存する
    principal = int(box1.get()) # Entry型が待っているメソッド
    int_rate = float(box2.get()) 
    net_int = box3.get()
    remarks = box4.get()
    # 保存用作文 \nで改行
    out_str = f'{principal},{int_rate},{period},"{net_int}",{remarks}\n'

    # ファイルを開いて保存する
    with open("interest_record.csv","a",encoding="utf-8") as fp:

        # ファイルが空ならヘッダーを書く
        if fp.tell() == 0:
            fp.write("元本,利率,期間,税引き後利息,備考\n")
            fp.write(out_str)

        else:
            fp.write(out_str)

    # ボックスをクリアする
    clear_box()

def clear_box():
    global period
    period = None
    error_label.config(text="")

    # ボックスの中を消す
    box1.delete(0, tk.END)
    box2.delete(0, tk.END)
    box3.delete(0, tk.END)
    box4.delete(0, tk.END)





# ==================================================

# メイン画面
# Tkinterのメインウィンドウを作って、それをrootという名前で呼ぶ
root = tk.Tk()
root.geometry("600x550")
root.title("利息計算アプリ")
root.configure(bg="#E7EAFF")

# タイトル
title = tk.Label(
    root,
    text="利息計算アプリ",
    font=("Yu Gothic UI", 22, "bold"),
    fg="#2C3E50",
    bg="#E7EAFF"
)

# 元本
text1 = tk.Label(
    root,
    text="元本",
    font=("Yu Gothic UI", 12),
    fg="#677B93",
    bg="#E7EAFF"
)

box1 = tk.Entry(
    root,
    font=("Yu Gothic UI", 16),
    width=20
)

# 利率
text2 = tk.Label(
    root,
    text="利率（％）",
    font=("Yu Gothic UI", 12),
    fg="#677B93",
    bg="#E7EAFF"
)

box2 = tk.Entry(
    root,
    font=("Yu Gothic UI", 16),
    width=10
)

# エラーメッセージ
error_label = tk.Label(
    root,
    text="",
    font=("Yu Gothic UI", 10),
    fg="red",
    bg="#E7EAFF"
)

# 期間
text3 = tk.Label(
    root,
    text="期間",
    font=("Yu Gothic UI", 12),
    fg="#677B93",
    bg="#E7EAFF"
)

# ボタン専用のFrameを作る
button_frame = tk.Frame(
    root,
    bg="#E7EAFF"
)

# ボタンはbutton_frameを親にする
bt1 = tk.Button(
    button_frame,
    text="3か月",
    command=lambda:my_f(1),
    font=("Yu Gothic UI", 11),
    fg="white",
    bg="#D99A3D",
    width=7
)

bt2 = tk.Button(
    button_frame,
    text="6か月",
    command=lambda:my_f(2),
    font=("Yu Gothic UI", 11),
    fg="white",
    bg="#D99A3D",
    width=7
)

bt3 = tk.Button(
    button_frame,
    text="1年",
    command=lambda:my_f(3),
    font=("Yu Gothic UI", 11),
    fg="white",
    bg="#D99A3D",
    width=7
)

bt4 = tk.Button(
    button_frame,
    text="3年",
    command=lambda:my_f(4),
    font=("Yu Gothic UI", 11),
    fg="white",
    bg="#D99A3D",
    width=7
)

bt5 = tk.Button(
    button_frame,
    text="5年",
    command=lambda:my_f(5),
    font=("Yu Gothic UI", 11),
    fg="white",
    bg="#D99A3D",
    width=7
)

# 利息
text4 = tk.Label(
    root,
    text="利息\n（税引き後）",
    font=("Yu Gothic UI", 12),
    fg="#677B93",
    bg="#E7EAFF"
)

box3 = tk.Entry(
    root,
    font=("Yu Gothic UI", 16),
    width=20
)

# 備考
text5 = tk.Label(
    root,
    text="備考",
    font=("Yu Gothic UI", 10),
    fg="#677B93",
    bg="#E7EAFF"
)

box4 = tk.Entry(
    root,
    font=("Yu Gothic UI", 16),
    width=24
)

# 保存ボタン
save_button = tk.Button(
    root,
    command=my_f2,
    text="保存",
    font=("Yu Gothic UI", 11, "bold"),
    bg="#5B8C5A",
    fg="white",
    width=8
)

# クリアボタン
clear_button = tk.Button(
    root,
    command=clear_box,
    text="クリア",
    font=("Yu Gothic UI", 11, "bold"),
    fg="white",
    bg="#A8A29A",
    width=8
)

note_label = tk.Label(
    root,
    text="※税引き後利息は概算値です。税率20.315%で計算しています。",
    font=("Yu Gothic UI", 9),
    fg="#5B8C5A",
    bg="#E7EAFF"
)

# ==================================================
# 配置

# タイトル
title.grid(
    row=0,
    column=0,
    columnspan=2,
    pady=(20, 20)
)

# 元本
text1.grid(
    row=1,
    column=0,
    padx=(80, 20),
    pady=10,
    sticky="e"
)

box1.grid(
    row=1,
    column=1,
    padx=(0, 80),
    pady=10,
    sticky="w"
)

# 利率
text2.grid(
    row=2,
    column=0,
    padx=(80, 20),
    pady=10,
    sticky="e"
)

box2.grid(
    row=2,
    column=1,
    padx=(0, 80),
    pady=10,
    sticky="w"
)

# エラーメッセージ
error_label.grid(
    row=3,
    column=1,
    sticky="w",
    padx=(0, 80)
)

# 期間
text3.grid(
    row=4,
    column=0,
    padx=(80, 20),
    pady=10,
    sticky="e"
)

button_frame.grid(
    row=4,
    column=1,
    padx=(0, 40),
    pady=10,
    sticky="w"
)

# ボタンを2段に配置
bt1.grid(row=0, column=0, padx=3, pady=3)
bt2.grid(row=0, column=1, padx=3, pady=3)
bt3.grid(row=0, column=2, padx=3, pady=3)
bt4.grid(row=1, column=0, padx=3, pady=3)
bt5.grid(row=1, column=1, padx=3, pady=3)

# 利息
text4.grid(
    row=5,
    column=0,
    padx=(80, 20),
    pady=(10, 10),
    sticky="e"
)

box3.grid(
    row=5,
    column=1,
    padx=(0, 80),
    pady=(10, 10),
    sticky="w"
)

# 備考
text5.grid(
    row=6,
    column=0,
    padx=(80, 20),
    pady=10,
    sticky="e"
)

box4.grid(
    row=6,
    column=1,
    padx=(0, 80),
    pady=10,
    sticky="w"
)

# 保存ボタン
save_button.grid(
    row=7,
    column=0,
    columnspan=2,
    pady=(30, 20),
)

# クリアボタン
clear_button.grid(
    row=7,
    column=1,
    padx=(40, 20),
    pady=(30, 20),
)

note_label.grid(
    row=8,
    column=1,
    columnspan=2,
    padx=(50, 0),
    pady=(0, 10)
)

# 消えないおまじない
root.mainloop()
