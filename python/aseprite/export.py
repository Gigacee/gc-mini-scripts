################################################################################
# asperite ファイルを読み込んで、レイヤー別に書き出します。
################################################################################

import json
import logging
import os
import subprocess

# 定数
PWD = os.path.dirname(os.path.abspath(__file__))
ASEPRITE_PATH = f"{PWD}/avatar_siena.aseprite"

# ロギング設定
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

# 設定をロード
with open(f"{PWD}/config.json", "r", encoding="utf_8") as f:
    config = json.load(f)

# 書き出し先のディレクトリが存在していなければ作成
if not os.path.exists(config["dest_dir_path"]):
    os.makedirs(config["dest_dir_path"])

command = [
    config["aseprite_path"],
    "--batch",
    "--split-layers",
    config["src_file_path"],
    "--trim",
    "--save-as",
    config["dest_dir_path"] + "/{layer}.png",
]

subprocess.call(command)

logging.info("書き出しが完了しました。")
