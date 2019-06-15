################################################################################
# このディレクトリ以下のすべての Excel ファイルを編集します。
################################################################################

import glob
import openpyxl
import os

# 作業ディレクトリのパス
WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))

for xlsx_file in glob.glob(f"{WORKING_DIRECTORY_PATH}\\**\\*.xlsx", recursive=True):
    # xlsx ファイルをロードする
    book = openpyxl.load_workbook(xlsx_file)
    print(f"{xlsx_file} is loaded.")

    # 処理

    # セーブする際の名前
    path_and_ext = os.path.splitext(xlsx_file)
    dest = f"{path_and_ext[0]}_edited{path_and_ext[1]}"

    # xlsx ファイルをセーブする
    book.save(dest)
    print("Completed.\n")
