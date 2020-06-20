################################################################################
# 指定されたディレクトリにある画像の情報を調べ、CSV に出力します。
################################################################################

import csv
import glob
import logging
import os
from PIL import Image

# 定数
PWD = os.path.dirname(os.path.abspath(__file__))
IN_DIR_PATH = f"{PWD}/in"
OUT_CSV_PATH = f"{PWD}/out/table.csv"

# ロギング設定
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

with open(OUT_CSV_PATH, "w", encoding="utf_8") as file:
    writer = csv.writer(file, lineterminator='\n')
    for file in glob.glob(f"{IN_DIR_PATH}/*"):
        image = Image.open(file)
        writer.writerow([os.path.basename(file), image.size[0], image.size[1]])
