################################################################################
# 同階層にあるディレクトリの一覧を CSV へ出力します。
################################################################################

import glob
import os

# 作業ディレクトリのパスを取得
WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))

csv_path = f"{WORKING_DIRECTORY_PATH}\\dir_list.csv"

with open(csv_path, "w", encoding="utf-8") as file:
    for path in glob.glob(f"{WORKING_DIRECTORY_PATH}\\*"):
        if os.path.isdir(path):
            file.write(f"{os.path.basename(path)}\n")
