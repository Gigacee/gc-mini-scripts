################################################################################
# GitKraken Glo のカードの一覧を CSV に出力します。
################################################################################

import csv
import json
import os
import py_glo_boards_api

# 作業ディレクトリのパス
WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))

# 設定をロード
config = json.load(open(f"{WORKING_DIRECTORY_PATH}/config.json", "rt"))

# 各ボード、カードから取得するフィールド
board_fields = ["name", "columns"]
card_fields = ["name", "description", "column_id", "labels"]

# 出力先のディレクトリが無ければ作成
dest_dir_path = f"{WORKING_DIRECTORY_PATH}/dest"
if not os.path.exists(dest_dir_path):
    os.makedirs(dest_dir_path)

# GloBoard オブジェクトを取得
globoard = py_glo_boards_api.GloBoard(config["personal_access_token"])

# 各ボードに対して処理を行う
for board in globoard.get_boards(board_fields):
    # カラムの ID がキー、名前が値の辞書を作成
    columns = {}
    for column in board.columns:
        columns[column.id] = column.name

    # 全カードのリストを作成
    cards = []
    for card in globoard.get_cards(board.id, card_fields, per_page=300):
        row = {}
        row["name"] = card.name
        if card.description is not None:
            row["description"] = card.description["text"].replace("\n", "\\n")
        row["column"] = columns[card.column_id]
        row["label"] = ""
        if card.labels is not None:
            for label in card.labels:
                row["label"] += label.name
        cards.append(row)

    # 全カードのリストを CSV に出力
    with open(f"{dest_dir_path}/{board.name}.csv", "wt", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, ["name", "description", "column", "label"])
        writer.writeheader()
        writer.writerows(cards)
