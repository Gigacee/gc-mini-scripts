import json
import logging
import tweepy

api = None


# API インスタンスを生成
def construct_api(config):
    # Twitter API を取得
    auth = tweepy.OAuthHandler(config["consumer_key"], config["consumer_secret"])
    auth.set_access_token(config["access_token"], config["access_token_secret"])

    global api
    api = tweepy.API(auth)


# リプライ文を取得
def get_reply_status(status_id):
    reply_status = None

    try:
        reply_status = api.get_status(status_id, tweet_mode="extended")
    except tweepy.RateLimitError as e:
        response = json.loads(e.response.text)
        if response["errors"][0]["code"] == 88:
            logging.error("アクセス制限に達しました。")
            exit()
    except tweepy.TweepError as e:
        response = json.loads(e.response.text)
        if (
            True
            and response["errors"][0]["code"] != 144
            and response["errors"][0]["code"] != 179
        ):
            logging.error(response)
            exit()

    return reply_status
