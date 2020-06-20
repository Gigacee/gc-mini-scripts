################################################################################
# ClickUp のすべてのビューの情報を出力します。
################################################################################

import json
import os
from pyclickup import ClickUp

# 作業ディレクトリのパス
WORKING_DIRECTORY_PATH = os.path.dirname(os.path.abspath(__file__))

# 設定をロード
config = json.load(open(f"{WORKING_DIRECTORY_PATH}/config.json", "rt"))

# 出力先のディレクトリが無ければ作成
dest_dir_path = f"{WORKING_DIRECTORY_PATH}/dest"
if not os.path.exists(dest_dir_path):
    os.makedirs(dest_dir_path)

# ClickUp オブジェクトを作成
clickup = ClickUp(config["api_token"])

text = ""

for cu_workspace in clickup.teams:
    for cu_space in cu_workspace.spaces:
        for cu_folder in cu_space.projects:
            text += cu_folder.name + "\n"
            response = ClickUp.get(
                clickup, f"https://api.clickup.com/api/v2/folder/{cu_folder.id}"
            )
            text += str(response) + "\n\n"
            # for cu_list in cu_folder.lists:
            #     response = ClickUp.get(
            #         clickup, f"https://api.clickup.com/api/v2/list/{cu_list.id}/view"
            #     )
            #     text += str(response) + "\n\n"

with open(f"{dest_dir_path}/res.txt", "wt", encoding="utf_8") as file:
    file.write(text)
