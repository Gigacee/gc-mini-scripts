import csv
import datetime
import logging
import os
import re

# 定数
JST = datetime.timezone(datetime.timedelta(hours=+9))
URL_PATTERN = r"https?://[\w/:%#\$&\?\(\)~\.=\+\-]+"
HEADER = [
    "created_at",
    "text",
    "favorited",
    "check",
    "media1",
    "media2",
    "media3",
    "media4",
    "tweet_url",
    "url1",
    "url2",
    "url3",
]

written_ids = []


# 指定されたパスを元に、TSV を初期化する
def init(path):
    # 書き出し先のディレクトリが存在していなければ作成
    dest_dir_path = os.path.dirname(path)
    if not os.path.exists(dest_dir_path):
        os.makedirs(dest_dir_path)

    # 書き出し先のファイルが存在していなければ作成し、何も書き込まれていなければヘッダーを書き込み
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        with open(path, "w", encoding="utf_8", newline="") as dest:
            csv.writer(dest, delimiter="\t").writerow(HEADER)

    # 書き込み済みのツイート ID のリストを作成
    with open(path, "r", encoding="utf_8") as dest:
        for column in csv.DictReader(dest, delimiter="\t"):
            written_ids.append(column["tweet_url"].split("/")[-1])


# 指定されたファイルから、TSV をヘッダー込みで読み込んで返す
def get_writer(f):
    return csv.DictWriter(f, HEADER, delimiter="\t")


# 指定された ID が TSV に書き込み済みかどうかを返す
def is_written(status_id):
    res = str(status_id) in written_ids

    if res:
        logging.info(f"書き込み済みのツイートです：{status_id}")

    return res


# URL を除去して返す
def remove_url(text):
    return re.sub(URL_PATTERN, "", text).strip()


# Status オブジェクトからツイート ID をを取り出し、URL を構築して返す
def construct_tweet_url(status):
    return f"https://twitter.com/{status.user.screen_name}/status/{status.id}"


# Status オブジェクトから日時を取り出し、JST に変換して返す
def construct_jst_date(status):
    time_utc = status.created_at.replace(tzinfo=datetime.timezone.utc)
    return time_utc.astimezone(JST).strftime("%Y/%m/%d %H:%M:%S")


# Status オブジェクトからリプライ文を取り出して返す
def construct_reply_text(status):
    return re.sub("\n", "\n> ", remove_url(status.full_text))


# Status オブジェクトから画像の URL を取り出し、IMAGE 関数を構成して返す
def construct_image_functions(status):
    fns = {}

    if (
        True
        and "extended_entities" in status._json
        and "media" in status._json["extended_entities"]
    ):
        for i, media in enumerate(status._json["extended_entities"]["media"]):
            # jpg, png 以外だったらエラー
            if (
                True
                and media["media_url_https"].split(".")[-1] != "jpg"
                and media["media_url_https"].split(".")[-1] != "png"
            ):
                logging.error(f"メディアが画像ではありません：{status.id}")
                exit()

            fns["media" + str(i + 1)] = f"=IMAGE(\"{media['media_url_https']}\")"

    return fns


# Status オブジェクトからツイート文を取り出し、URL を抽出して返す
def extract_url(status):
    urls = {}

    # ツイート文に含まれている URL を追加
    for i, url in enumerate(re.findall(URL_PATTERN, status.full_text)):
        # URL の数が 3 つを超えていたらエラー
        if i > 3:
            logging.error(f"ツイート文に含まれる URL が 3 つを超えています：{status.id}")
            exit()

        urls["url" + str(i + 1)] = url

    return urls
