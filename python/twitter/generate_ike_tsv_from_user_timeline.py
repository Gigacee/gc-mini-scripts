################################################################################
# 自分のユーザータイムラインを読み込み、いいねの一覧を TSV 形式で書き出します。
################################################################################

import json
import logging
import os
import tweepy
from modules import g_twitter, g_tsv

# 定数
PWD = os.path.dirname(os.path.abspath(__file__))
DEST_TSV_PATH = f"{PWD}/out/like.tsv"

# ロギング設定
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")

# 設定をロード
with open(f"{PWD}/config.json", "r", encoding="utf_8") as f:
    config = json.load(f)

# API インスタンスを生成
g_twitter.construct_api(config)

g_tsv.init(DEST_TSV_PATH)

with open(DEST_TSV_PATH, "a", encoding="utf_8", newline="") as dest:
    writer = g_tsv.get_writer(dest)
    tweet_info = {}

    for i, status in enumerate(
        tweepy.Cursor(g_twitter.api.favorites, tweet_mode="extended").items()
    ):
        # DEBUG ============================================================
        # if i > 10:
        #     exit()
        # ==================================================================

        # ツイートがすでに書き込まれていたらスキップ
        if g_tsv.is_written(status.id):
            continue

        # ツイート情報の辞書を作成
        tweet_info.clear()
        tweet_info["favorited"] = status.favorited
        tweet_info["tweet_url"] = g_tsv.construct_tweet_url(status)
        tweet_info["created_at"] = g_tsv.construct_jst_date(status)
        tweet_info.update(g_tsv.construct_image_functions(status))
        tweet_info.update(g_tsv.extract_url(status))

        text = ""

        # リプライ文を追加。だたしリプライ先が自分自身の場合はスキップ
        if (
            True
            and status.in_reply_to_status_id is not None
            and status.in_reply_to_screen_name != status.user.screen_name
        ):
            # 名前があったら追加
            if status.in_reply_to_screen_name is not None:
                text += f"> [{status.in_reply_to_screen_name}]\n> "

            # リプライを取得し、存在していたらリプライ文と空行を追加
            reply_status = g_twitter.get_reply_status(status.in_reply_to_status_id)
            if reply_status is not None:
                text += g_tsv.construct_reply_text(reply_status) + "\n\n"

        text += g_tsv.remove_url(status.full_text)

        # テキストを追加
        tweet_info["text"] = text

        # ツイート情報を TSV に書き出し
        writer.writerow(tweet_info)
        logging.info(f"書き込みました：{tweet_info}")

logging.info("すべてのツイート情報の書き込みが完了しました。")
