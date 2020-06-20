################################################################################
# CSV の 1 列目に記載されたファイル・ディレクトリ名を、2 列目の名称にリネームします。
################################################################################

import csv
import logging
import os
import pathlib

# 定数
PWD = os.path.dirname(os.path.abspath(__file__))
TABLE_PATH = f"{PWD}/in/table.csv"

# ロギング設定
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

if not os.path.exists(TABLE_PATH):
    logging.error("リネームテーブルが存在していません。")
    exit()

with open(TABLE_PATH, "r", encoding="utf_8") as file:
    for row in csv.reader(file):
        before_name = row[0]
        after_name = row[1]

        if not pathlib.Path.is_absolute(pathlib.Path(row[0])):
            before_name = f"{PWD}/{before_name}"

        if not pathlib.Path.is_absolute(pathlib.Path(row[0])):
            after_name = f"{PWD}/{after_name}"

        if not os.path.exists(before_name):
            logging.error(f"ファイルまたはディレクトリが存在していません：{before_name}")
            continue

        os.rename(before_name, after_name)
