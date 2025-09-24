# SPDX-FileCopyrightText: 2025-present Keisuke Magara <61485115+kei-mag@users.noreply.github.com>
#
# SPDX-License-Identifier: MIT
"""easy_modal.gui

Tkinterのfiledialog, messagebox, simpledialogをラップし、1行で実装できるようになっています。
使い方: https://github.com/kei-mag/python-easy-modal#使い方
"""

import re
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk
from typing import Any, List, Literal, Optional, Tuple, Union


# --- 内部関数 ---
def _create_root(toolwindow: bool = True) -> tk.Tk:
    """Tkinterのルートウィンドウを生成します。

    ウィンドウはユーザーに見えないように、サイズ0x0で画面外に配置されます。
    これにより、イベントループが安定して動作します。

    Args:
        toolwindow (bool, optional): ウィンドウがタスクバーに表示されないようにします（Windows向け）。デフォルトはTrueです。

    Returns:
        tk.Tk: Tkinterのルートウィンドウ。
    """
    root = tk.Tk()
    if toolwindow:
        # ウィンドウがタスクバーに表示されるのを防ぐ（Windows向け）
        root.wm_attributes("-toolwindow", True)
    # サイズ0x0で見えないようにし、画面の外へ移動させる
    root.geometry("0x0+9999+9999")
    root.attributes("-topmost", True)
    return root


# --- ファイル・フォルダ選択ダイアログ ---


def select_file(
    title: Optional[str] = None,
    initialdir: Optional[str] = None,
    filetypes: Optional[List[Tuple[str, str]]] = None,
    parent: Any = None,
) -> str:
    """単一のファイルを選択するダイアログを開きます。

    ユーザーがファイル選択をキャンセルした場合は、空文字列 '' を返します。

    Args:
        title (str, optional): ダイアログのウィンドウタイトル。
        initialdir (str, optional): ダイアログが最初に開くディレクトリ。
        filetypes (List[Tuple[str, str]], optional):
            選択可能なファイル種別のリスト。
            例: [('テキストファイル', '*.txt'), ('すべてのファイル', '*.*')]
        parent (Any, optional): このダイアログの親ウィンドウ。通常は指定不要です。

    Returns:
        str: 選択されたファイルのフルパス。キャンセルの場合は空文字列。
    """
    root = _create_root()
    # 一時的にルートウィンドウを表示可能状態にする（ただし画面外）
    root.deiconify()
    filepath = filedialog.askopenfilename(
        parent=parent or root, title=title, initialdir=initialdir, filetypes=filetypes
    )
    root.destroy()
    return filepath


def select_files(
    title: Optional[str] = None,
    initialdir: Optional[str] = None,
    filetypes: Optional[List[Tuple[str, str]]] = None,
    parent: Any = None,
) -> List[str]:
    """複数のファイルを選択するダイアログを開きます。

    ユーザーがファイル選択をキャンセルした場合は、空のリスト [] を返します。

    Args:
        title (str, optional): ダイアログのウィンドウタイトル。
        initialdir (str, optional): ダイアログが最初に開くディレクトリ。
        filetypes (List[Tuple[str, str]], optional):
            選択可能なファイル種別のリスト。
            例: [('画像ファイル', '*.jpg *.png'), ('すべてのファイル', '*.*')]
        parent (Any, optional): このダイアログの親ウィンドウ。通常は指定不要です。

    Returns:
        List[str]: 選択された全ファイルのフルパスのリスト。キャンセルの場合は空リスト。
    """
    root = _create_root()
    root.deiconify()
    filepaths = list(
        filedialog.askopenfilenames(parent=parent or root, title=title, initialdir=initialdir, filetypes=filetypes)
    )
    root.destroy()
    return filepaths


def select_folder(
    title: Optional[str] = None, initialdir: Optional[str] = None, mustexist: bool = True, parent: Any = None
) -> str:
    """フォルダを選択するダイアログを開きます。

    ユーザーがフォルダ選択をキャンセルした場合は、空文字列 '' を返します。

    Args:
        title (str, optional): ダイアログのウィンドウタイトル。
        initialdir (str, optional): ダイアログが最初に開くディレクトリ。
        mustexist (bool, optional): 選択するフォルダが存在必須かどうか。デフォルトはTrueです。
        parent (Any, optional): このダイアログの親ウィンドウ。通常は指定不要です。

    Returns:
        str: 選択されたフォルダのフルパス。キャンセルの場合は空文字列。
    """
    root = _create_root()
    root.deiconify()
    folderpath = filedialog.askdirectory(
        parent=parent or root, title=title, initialdir=initialdir, mustexist=mustexist
    )
    root.destroy()
    return folderpath


def save_file(
    title: Optional[str] = None,
    initialdir: Optional[str] = None,
    initialfile: Optional[str] = None,
    filetypes: Optional[List[Tuple[str, str]]] = None,
    defaultextension: Optional[str] = None,
    parent: Any = None,
) -> str:
    """「名前を付けて保存」ダイアログを開きます。

    ユーザーが保存をキャンセルした場合は、空文字列 '' を返します。

    Args:
        title (str, optional): ダイアログのウィンドウタイトル。
        initialdir (str, optional): ダイアログが最初に開くディレクトリ。
        initialfile (str, optional): ファイル名の初期値。
        filetypes (List[Tuple[str, str]], optional):
            保存形式の選択肢リスト。
            例: [('テキストファイル', '*.txt'), ('すべてのファイル', '*.*')]
        defaultextension (str, optional): ユーザーが拡張子を省略した場合のデフォルト拡張子。
        parent (Any, optional): このダイアログの親ウィンドウ。通常は指定不要です。

    Returns:
        str: 保存先として指定されたファイルのフルパス。キャンセルの場合は空文字列。
    """
    root = _create_root()
    root.deiconify()
    filepath = filedialog.asksaveasfilename(
        parent=parent or root,
        title=title,
        initialdir=initialdir,
        initialfile=initialfile,
        filetypes=filetypes,
        defaultextension=defaultextension,
    )
    root.destroy()
    return filepath


# --- メッセージボックス ---


def show_info(title: str, message: str, parent: Any = None):
    """情報メッセージボックスを表示します。

    Args:
        title (str): メッセージボックスのタイトル。
        message (str): 表示するメッセージ本文。
        parent (Any, optional): このダイアログの親ウィンドウ。通常は指定不要です。
    """
    root = _create_root()
    root.deiconify()
    messagebox.showinfo(title, message, parent=parent or root)
    root.destroy()


def show_warning(title: str, message: str, parent: Any = None):
    """警告メッセージボックスを表示します。

    Args:
        title (str): メッセージボックスのタイトル。
        message (str): 表示するメッセージ本文。
        parent (Any, optional): このダイアログの親ウィンドウ。通常は指定不要です。
    """
    root = _create_root()
    root.deiconify()
    messagebox.showwarning(title, message, parent=parent or root)
    root.destroy()


def show_error(title: str, message: str, parent: Any = None):
    """エラーメッセージボックスを表示します。

    Args:
        title (str): メッセージボックスのタイトル。
        message (str): 表示するメッセージ本文。
        parent (Any, optional): このダイアログの親ウィンドウ。通常は指定不要です。
    """
    root = _create_root()
    root.deiconify()
    messagebox.showerror(title, message, parent=parent or root)
    root.destroy()


# --- ユーザー入力 ---


def ask_yesno(title: str, question: str, parent: Any = None) -> bool:
    """「はい/いいえ」を問う確認ダイアログを表示します。（OS標準）

    Args:
        title (str): ダイアログのタイトル。
        question (str): ユーザーへの質問文。
        parent (Any, optional): このダイアログの親ウィンドウ。通常は指定不要です。

    Returns:
        bool: 「はい」がクリックされた場合は True、「いいえ」の場合は False。
    """
    root = _create_root()
    root.deiconify()
    response = messagebox.askyesno(title, question, parent=parent or root)
    root.destroy()
    return response


def ask_string(
    title: str,
    prompt: str,
    initialvalue: Optional[str] = None,
    pattern: Optional[str] = None,
    error_prompt: Optional[str] = None,
    parent: Any = None,
) -> Union[str, None]:
    """一行テキスト入力ダイアログを表示し、正規表現で入力を検証します。

    正規表現パターンに一致しない入力があった場合、エラーメッセージを表示し、
    再度入力を求めます。ユーザーがキャンセルした場合は None を返します。

    Args:
        title (str): ダイアログのタイトル。
        prompt (str): ユーザーへの指示文。
        initialvalue (str, optional): テキストボックスの初期値。
        pattern (str, optional):
            入力を検証するための正規表現パターン。
            例: r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$' (メールアドレス)
        error_prompt (str, optional):
            検証エラー時のカスタムメッセージ。指定しない場合はデフォルトメッセージが表示されます。
        parent (Any, optional): このダイアログの親ウィンドウ。通常は指定不要です。

    Returns:
        Union[str, None]: 検証を通過した入力文字列。キャンセルの場合は None。
    """
    while True:
        root = _create_root()
        root.deiconify()
        response = simpledialog.askstring(title, prompt, initialvalue=initialvalue, parent=parent or root)
        # simpledialogが閉じた後、rootを破棄
        if root.winfo_exists():
            root.destroy()

        if response is None:
            return None

        if pattern:
            if re.fullmatch(pattern, response):
                return response
            else:
                error_msg = error_prompt or f"入力が正規表現パターン '{pattern}' を満たしていません。"
                show_error("入力エラー", error_msg, parent=parent)
                initialvalue = response
        else:
            return response


def ask_int(
    title: str,
    prompt: str,
    initialvalue: Optional[int] = None,
    minvalue: Optional[int] = None,
    maxvalue: Optional[int] = None,
    parent: Any = None,
) -> Union[int, None]:
    """整数入力ダイアログを表示します。

    このダイアログはtkinterの機能により、整数以外や範囲外(minvalue/maxvalue)の
    値が入力されると自動でエラーを表示し、再入力を促します。
    ユーザーがキャンセルした場合は None を返します。

    Args:
        title (str): ダイアログのタイトル。
        prompt (str): ユーザーへの指示文。
        initialvalue (int, optional): 入力欄の初期値。
        minvalue (int, optional): 入力可能な最小値。
        maxvalue (int, optional): 入力可能な最大値。
        parent (Any, optional): このダイアログの親ウィンドウ。通常は指定不要です。

    Returns:
        Union[int, None]: 入力された整数。キャンセルの場合は None。
    """
    root = _create_root()
    root.deiconify()
    response = simpledialog.askinteger(
        title, prompt, initialvalue=initialvalue, minvalue=minvalue, maxvalue=maxvalue, parent=parent or root
    )
    if root.winfo_exists():
        root.destroy()
    return response


def ask_float(
    title: str,
    prompt: str,
    initialvalue: Optional[float] = None,
    minvalue: Optional[float] = None,
    maxvalue: Optional[float] = None,
    parent: Any = None,
) -> Union[float, None]:
    """小数入力ダイアログを表示します。

    このダイアログはtkinterの機能により、数値以外や範囲外(minvalue/maxvalue)の
    値が入力されると自動でエラーを表示し、再入力を促します。
    ユーザーがキャンセルした場合は None を返します。

    Args:
        title (str): ダイアログのタイトル。
        prompt (str): ユーザーへの指示文。
        initialvalue (float, optional): 入力欄の初期値。
        minvalue (float, optional): 入力可能な最小値。
        maxvalue (float, optional): 入力可能な最大値。
        parent (Any, optional): このダイアログの親ウィンドウ。通常は指定不要です。

    Returns:
        Union[float, None]: 入力された小数。キャンセルの場合は None。
    """
    root = _create_root()
    root.deiconify()
    response = simpledialog.askfloat(
        title, prompt, initialvalue=initialvalue, minvalue=minvalue, maxvalue=maxvalue, parent=parent or root
    )
    if root.winfo_exists():
        root.destroy()
    return response


def ask_choice(title: str, question: str, buttons: List[str], parent: Any = None) -> Union[str, None]:
    """カスタムボタンを持つ確認ダイアログを表示します。

    Args:
        title (str): ダイアログのタイトル。
        question (str): ユーザーへの質問文。
        buttons (List[str]): ボタンに表示するテキストのリスト。
        parent (Any, optional): このダイアログの親ウィンドウ。通常は指定不要です。

    Returns:
        Union[str, None]: クリックされたボタンのテキスト。ウィンドウが閉じられた場合は None。
    """
    root = _create_root()

    dialog = tk.Toplevel(parent or root)
    dialog.title(title)
    dialog.attributes("-topmost", True)
    dialog.resizable(False, False)

    dialog.update_idletasks()
    x = dialog.winfo_screenwidth() // 2 - dialog.winfo_reqwidth() // 2
    y = dialog.winfo_screenheight() // 2 - dialog.winfo_reqheight() // 2
    dialog.geometry(f"+{x}+{y}")

    label = tk.Label(dialog, text=question, padx=20, pady=20)
    label.pack()

    button_frame = tk.Frame(dialog, pady=10)
    button_frame.pack()

    choice = None

    def on_button_click(button_text):
        nonlocal choice
        choice = button_text
        dialog.destroy()

    for text in buttons:
        button = tk.Button(button_frame, text=text, command=lambda t=text: on_button_click(t), width=12)
        button.pack(side="left", padx=5, pady=5)

    def on_closing():
        nonlocal choice
        choice = None
        dialog.destroy()

    dialog.protocol("WM_DELETE_WINDOW", on_closing)
    dialog.transient(parent or root)
    dialog.grab_set()
    root.wait_window(dialog)
    root.destroy()
    return choice


def ask_item(
    title: str,
    question: str,
    items: List[str],
    widget_type: Union[Literal["radio"], Literal["dropdown"]] = "radio",
    parent: Any = None,
) -> Union[str, None]:
    """リストから単一の項目を選択させます。

    Args:
        title (str): ダイアログのタイトル。
        question (str): ユーザーへの指示文。
        items (List[str]): 選択肢のリスト。
        widget_type ("radio" or "dropdown", optional):
            使用するウィジェットの種類。'radio' (ラジオボタン) または
            'dropdown' (ドロップダウンリスト)。デフォルトは 'radio' です。
        parent (Any, optional): このダイアログの親ウィンドウ。通常は指定不要です。

    Returns:
        Union[str, None]: 選択された項目。キャンセルの場合は None。
    """
    root = _create_root()
    dialog = tk.Toplevel(parent or root)
    dialog.title(title)
    dialog.attributes("-topmost", True)
    dialog.resizable(False, False)

    label = tk.Label(dialog, text=question, padx=20, pady=10)
    label.pack()

    choice = tk.StringVar(root)
    if items:
        choice.set(items[0])

    widget_frame = tk.Frame(dialog)
    widget_frame.pack(padx=20, pady=5, anchor="w")

    if widget_type == "dropdown":
        combobox = ttk.Combobox(widget_frame, textvariable=choice, values=items, state="readonly")
        combobox.pack()
    else:
        for item in items:
            rb = tk.Radiobutton(widget_frame, text=item, variable=choice, value=item)
            rb.pack(anchor="w")

    result = None

    def on_ok():
        nonlocal result
        result = choice.get()
        dialog.destroy()

    def on_cancel():
        nonlocal result
        result = None
        dialog.destroy()

    dialog.update_idletasks()
    x = dialog.winfo_screenwidth() // 2 - dialog.winfo_reqwidth() // 2
    y = dialog.winfo_screenheight() // 2 - dialog.winfo_reqheight() // 2
    dialog.geometry(f"+{x}+{y}")

    button_frame = tk.Frame(dialog, pady=10)
    button_frame.pack()
    ok_button = tk.Button(button_frame, text="OK", command=on_ok, width=10)
    ok_button.pack(side="left", padx=10)
    cancel_button = tk.Button(button_frame, text="Cancel", command=on_cancel, width=10)
    cancel_button.pack(side="left", padx=10)

    dialog.protocol("WM_DELETE_WINDOW", on_cancel)
    dialog.transient(parent or root)
    dialog.grab_set()
    root.wait_window(dialog)
    root.destroy()
    return result


def ask_items(title: str, question: str, items: List[str], parent: Any = None) -> List[str]:
    """リストから複数の項目を選択させます。

    Args:
        title (str): ダイアログのタイトル。
        question (str): ユーザーへの指示文。
        items (List[str]): 選択肢のリスト。
        parent (Any, optional): このダイアログの親ウィンドウ。通常は指定不要です。

    Returns:
        List[str]: 選択された項目のリスト。キャンセルの場合は空リスト。
    """
    root = _create_root()
    dialog = tk.Toplevel(parent or root)
    dialog.title(title)
    dialog.attributes("-topmost", True)

    dialog.update_idletasks()
    x = dialog.winfo_screenwidth() // 2 - dialog.winfo_reqwidth() // 2
    y = dialog.winfo_screenheight() // 2 - dialog.winfo_reqheight() // 2
    dialog.geometry(f"+{x}+{y}")

    label = tk.Label(dialog, text=question, padx=20, pady=10)
    label.pack()

    frame = tk.Frame(dialog)
    frame.pack(padx=20, pady=5, fill="both", expand=True)

    listbox = tk.Listbox(frame, selectmode="extended", exportselection=False)
    for item in items:
        listbox.insert("end", item)

    scrollbar = tk.Scrollbar(frame, orient="vertical", command=listbox.yview)
    listbox["yscrollcommand"] = scrollbar.set
    listbox.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    result = []

    def on_ok():
        nonlocal result
        selected_indices = listbox.curselection()
        result = [items[i] for i in selected_indices]
        dialog.destroy()

    def on_cancel():
        nonlocal result
        result = []
        dialog.destroy()

    button_frame = tk.Frame(dialog, pady=10)
    button_frame.pack()
    ok_button = tk.Button(button_frame, text="OK", command=on_ok, width=10)
    ok_button.pack(side="left", padx=10)
    cancel_button = tk.Button(button_frame, text="Cancel", command=on_cancel, width=10)
    cancel_button.pack(side="left", padx=10)

    dialog.protocol("WM_DELETE_WINDOW", on_cancel)
    dialog.transient(parent or root)
    dialog.grab_set()
    root.wait_window(dialog)
    root.destroy()
    return result


# --- このファイルが直接実行された場合のサンプルコード ---
if __name__ == "__main__":
    show_info("サンプル開始", "easy_modal(gui)のデモを開始します。")

    departments = ["営業部", "開発部", "人事部", "総務部"]

    # 1. ask_itemのラジオボタン形式（デフォルト）のサンプル
    department_radio = ask_item(
        title="部署選択 (ラジオボタン)", question="あなたの所属部署を選択してください:", items=departments
    )
    if department_radio:
        show_info("選択結果", f"選択された部署: {department_radio}")
    else:
        show_warning("キャンセル", "部署選択がキャンセルされました。")

    # 2. ask_itemのドロップダウン形式のサンプル
    department_dropdown = ask_item(
        title="部署選択 (ドロップダウン)",
        question="あなたの所属部署を選択してください:",
        items=departments,
        widget_type="dropdown",
    )
    if department_dropdown:
        show_info("選択結果", f"選択された部署: {department_dropdown}")
    else:
        show_warning("キャンセル", "部署選択がキャンセルされました。")

    show_info("サンプル終了", "全てのデモが完了しました。使用するにはeasy_modal.guiをインポートしてください。")
