################################################################################
# wav ファイルを mp3 にエンコードします。
################################################################################

import glob
import json
import os
import subprocess

# 作業ディレクトリのパス
WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))

# 設定をロード
settings = json.load(open(f"{WORKING_DIRECTORY_PATH}\\settings.json", "r"))

# 設定された引数を配列に変換
lame_args = settings["lame_arg"].split()

# 作業ディレクトリと同階層にあるすべての wav ファイルに対して処理を行う
for wav in glob.glob(f"{WORKING_DIRECTORY_PATH}\\*.wav"):
    dest = f"{os.path.splitext(wav)[0]}.mp3"

    command = []
    command.append(settings["lame_path"])
    command.extend(lame_args)
    command.append(wav)
    command.append(dest)

    subprocess.call(command)
