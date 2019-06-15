################################################################################
# CSV に入力された名前のディレクトリを生成します。
################################################################################

import csv
import os

# 作業ディレクトリのパスを取得
WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))

csv_path = f"{WORKING_DIRECTORY_PATH}\\table.csv"

if not os.path.exists(csv_path):
    print("Error: table.csv does not exist.")
    exit()

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.reader(f)

    for row in reader:
        d = f"{WORKING_DIRECTORY_PATH}\\{row[0]}"

        if not os.path.exists(d):
            print(f"Make: {d}")
            os.makedirs(d)
