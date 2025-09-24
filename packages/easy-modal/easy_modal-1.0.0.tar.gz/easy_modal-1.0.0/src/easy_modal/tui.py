# SPDX-FileCopyrightText: 2025-present Keisuke Magara <61485115+kei-mag@users.noreply.github.com>
#
# SPDX-License-Identifier: MIT
"""easy_modal.tui

easy_modal.guiのask_item(s), ask_yesno, ask_choice相当のモーダルをASCII文字列でシェル上に表示できます。
使い方: https://github.com/kei-mag/python-easy-modal#使い方
"""

import os
import sys
from typing import List, Optional, Set, Union

# --- 内部関数 ---


def _get_terminal_width() -> int:
    """ターミナルの幅を取得します。"""
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 80  # 取得できない場合はデフォルト値


def _display_dialog(
    question: str,
    items: List[str],
    title: Optional[str] = None,
    selections: Optional[Set[int]] = None,
    error_msg: Optional[str] = None,
):
    """
    CUIでダイアログ風の表示を描画します。
    """
    # 全体の幅を計算
    max_len = 0

    # 全角文字を2文字としてカウントするヘルパー関数
    def get_char_width(text: str) -> int:
        return sum(2 if ord(c) > 255 else 1 for c in text)

    if title:
        max_len = max(max_len, get_char_width(title))

    if question:
        max_len = max(max_len, get_char_width(question))
    for item in items:
        max_len = max(max_len, get_char_width(item) + 5)  # 番号分 "[x] " を考慮

    width = min(max_len + 4, _get_terminal_width() - 2)

    # パディングを計算してテキストを配置するヘルパー関数
    def print_padded_line(text: str):
        padding = width - 4 - get_char_width(text)
        padding = max(0, padding)  # 負のパディングを防ぐ
        print(f"| {text}{' ' * padding} |")

    # 中央揃えでテキストを配置するヘルパー関数
    def print_centered_line(text: str):
        padding_total = width - 4 - get_char_width(text)
        padding_total = max(0, padding_total)
        pad_left = padding_total // 2
        pad_right = padding_total - pad_left
        print(f"| {' ' * pad_left}{text}{' ' * pad_right} |")

    # 上辺
    print(f"+{'-' * (width - 2)}+")
    # タイトル（指定されている場合のみ表示）
    if title:
        print_centered_line(title)
        print(f"+{'-' * (width - 2)}+")
    # 質問
    if question:
        print_padded_line(question)
        print(f"|{' ' * (width - 2)}|")

    # 選択肢
    for i, item in enumerate(items):
        if selections is not None:  # ask_itemsの場合
            mark = "x" if i in selections else " "
            line_base = f"[{mark}] {i + 1}. {item}"
        else:  # ask_itemの場合
            line_base = f"  {i + 1}. {item}"

        print_padded_line(line_base)

    # エラーメッセージ
    if error_msg:
        print(f"|{' ' * (width - 2)}|")
        print_padded_line(error_msg)

    # 下辺
    print(f"+{'-' * (width - 2)}+")


# --- 公開関数 ---


def ask_item(question: str, items: List[str], title: Optional[str] = None) -> Union[str, None]:
    """リストから単一の項目を数字で選択させます。

    Args:
        question (str): ユーザーへの指示文。
        items (List[str]): 選択肢のリスト。
        title (str, optional): ダイアログのタイトル。省略可能です。

    Returns:
        Union[str, None]: 選択された項目。Ctrl+Cなどで中断した場合はNone。
    """
    error_msg = None
    while True:
        print("\n")  # 履歴が見えるように空行を挿入
        _display_dialog(question, items, title=title, error_msg=error_msg)

        try:
            choice_str = input("選択してください (番号): ")
            if not choice_str.isdigit():
                error_msg = "エラー: 数字で入力してください。"
                continue

            choice_idx = int(choice_str) - 1
            if 0 <= choice_idx < len(items):
                return items[choice_idx]
            else:
                error_msg = f"エラー: 1 から {len(items)} の間で選択してください。"

        except (KeyboardInterrupt, EOFError):
            print("\nキャンセルされました。")
            return None


def ask_items(question: str, items: List[str], title: Optional[str] = None) -> List[str]:
    """リストから複数の項目を数字で選択させます。

    Args:
        question (str): ユーザーへの指示文。
        items (List[str]): 選択肢のリスト。
        title (str, optional): ダイアログのタイトル。省略可能です。

    Returns:
        List[str]: 選択された項目のリスト。キャンセルの場合は空リスト。
    """
    selections: Set[int] = set()
    error_msg = None

    while True:
        print("\n")  # 履歴が見えるように空行を挿入
        _display_dialog(
            question + " (スペース区切りで複数入力可)", items, title=title, selections=selections, error_msg=error_msg
        )
        error_msg = None  # エラーメッセージをリセット

        try:
            choice_str = input(f"選択/解除する番号を入力してください (0で確定): ")

            choices = choice_str.split()
            if not choices:
                error_msg = "エラー: 番号を入力してください。"
                continue

            # 確定(0)が含まれているか先にチェック
            if "0" in choices:
                # 0以外の有効な番号も処理する
                for choice in choices:
                    if choice.isdigit() and choice != "0":
                        choice_idx = int(choice) - 1
                        if 0 <= choice_idx < len(items):
                            if choice_idx in selections:
                                selections.remove(choice_idx)
                            else:
                                selections.add(choice_idx)
                return [items[i] for i in sorted(list(selections))]

            # 確定以外の番号を処理
            for choice in choices:
                if not choice.isdigit():
                    error_msg = f"エラー: '{choice}' は数字ではありません。"
                    continue

                choice_num = int(choice)
                choice_idx = choice_num - 1

                if 0 <= choice_idx < len(items):
                    if choice_idx in selections:
                        selections.remove(choice_idx)
                    else:
                        selections.add(choice_idx)
                else:
                    # 範囲外の番号は無視
                    pass

        except (KeyboardInterrupt, EOFError):
            print("\nキャンセルされました。")
            return []


def ask_yesno(question: str, title: str = "確認") -> bool:
    """「はい/いいえ」を問う確認ダイアログを表示します。

    Args:
        question (str): ユーザーへの質問文。
        title (str, optional): ダイアログのタイトル。デフォルトは「確認」です。

    Returns:
        bool: 「はい」が選択された場合は True、「いいえ」の場合は False。
    """
    choice = ask_item(question, ["はい", "いいえ"], title=title)
    return choice == "はい"


def ask_choice(question: str, buttons: List[str], title: Optional[str] = None) -> Union[str, None]:
    """カスタムボタン（選択肢）を持つ確認ダイアログを表示します。

    Args:
        question (str): ユーザーへの質問文。
        buttons (List[str]): 選択肢のテキストのリスト。
        title (str, optional): ダイアログのタイトル。省略可能です。

    Returns:
        Union[str, None]: 選択された選択肢のテキスト。中断した場合はNone。
    """
    return ask_item(question, buttons, title=title)


# --- このファイルが直接実行された場合のサンプルコード ---
if __name__ == "__main__":
    print("--- easy_modal(tui)のデモ ---")

    # 1. ask_yesno のサンプル (タイトル付き)
    if not ask_yesno("デモを開始しますか？", title="実行確認"):
        print("デモを終了しました。")
        sys.exit()

    # 2. ask_item (単一選択) のサンプル (タイトル付き)
    departments = ["営業部", "開発部", "人事部", "総務部"]
    department = ask_item("あなたの所属部署を選択してください:", items=departments, title="部署選択")
    if department:
        print(f"\n=> 選択された部署: {department}")
    else:
        print("\n処理が中断されました。")
        sys.exit()

    # 3. ask_items (複数選択) のサンプル (タイトルなし)
    skills = ["Python", "Excel", "PowerPoint", "データ分析", "コミュニケーション"]
    selected_skills = ask_items("保有スキルを全て選択してください:", items=skills)
    if selected_skills:
        print(f"\n=> 選択されたスキル: {', '.join(selected_skills)}")
    else:
        print("\nスキルは選択されなかったか、処理が中断されました。")

    print("\n--- デモ終了 ---\n使用するにはeasy_modal.tuiをインポートしてください。")
