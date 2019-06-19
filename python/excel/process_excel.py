################################################################################
# Excel ファイルを扱うテストです。
################################################################################

import glob
import openpyxl
import os

# 作業ディレクトリのパス
WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))

# 作業ディレクトリと同階層にあるすべての xlsx ファイルに対して処理を行う
for xlsx_file in glob.glob(f"{WORKING_DIRECTORY_PATH}\\*.xlsx"):
    # xlsx ファイルをロード
    book = openpyxl.load_workbook(xlsx_file)
    print(f"{xlsx_file} loaded.")

    # 処理

    # xlsx ファイルをセーブ
    book.save(xlsx_file)
    print(f"{xlsx_file} saved.")
