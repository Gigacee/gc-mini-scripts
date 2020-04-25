################################################################################
# TSV を読み込んで、チェックされているツイートを削除します。
################################################################################

import csv
import json
import logging
import os
import tweepy
from modules import g_twitter

# 定数
PWD = os.path.dirname(os.path.abspath(__file__))
SRC_TSV_PATH = f"{PWD}/resources/delete.tsv"

# ロギング設定
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

# 設定をロード
with open(f"{PWD}/config.json", "r", encoding="utf_8") as f:
    config = json.load(f)

# API インスタンスを生成
g_twitter.construct_api(config)

with open(SRC_TSV_PATH, "r", encoding="utf_8") as src:
    for column in csv.DictReader(src, delimiter="\t"):
        if column["check"] == "TRUE":
            try:
                g_twitter.api.destroy_status(column["tweet_url"].split("/")[-1])
                logging.info(f"削除しました：{column['text']}")
            except tweepy.TweepError as e:
                response = json.loads(e.response.text)

                # ツイートが存在しない場合はスキップ
                if response["errors"][0]["code"] == 144:
                    logging.warning(f"ツイートが存在しません：{column['text']}")
                    continue

                logging.error(response)
                exit()

logging.info("チェックされたすべてのツイートの削除が完了しました。")
