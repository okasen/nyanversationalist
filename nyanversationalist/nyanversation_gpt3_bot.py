import openai
import re
import os
from typing import List, Tuple
import time

import tweepy

openai.api_key = os.getenv("OPENAI_API_KEY")

consumer_key=os.getenv("CONSUMER_TWITTER")
consumer_secret=os.getenv("CONSUMER_SECRET")
access_token_key=os.getenv("TWITTER_TOKEN")
access_token_secret=os.getenv("TWITTER_SECRET")

auth = tweepy.OAuth1UserHandler(
    consumer_key,
    consumer_secret,
    access_token_key,
    access_token_secret
)

api = tweepy.API(auth)


def scrub_completion(completion: dict) -> str:
    text = completion["choices"][0]["text"]
    text = re.sub("#", "", text)
    text = re.sub("@", "", text)
    text = re.sub(" -> ", "", text)
    text_lines = text.split("\n")
    actual_text_lines = [line for line in text_lines if len(line) > 0]
    text = " ".join(actual_text_lines)
    return text


def check_for_conversations(api, since_id, converser) -> str:
    new_since_id = since_id
    checking = True
    failed_checks = 0
    while checking:
        conversing_user_tweets = api.user_timeline(user_id=converser.id, count=100)
        for tweet in conversing_user_tweets:
            new_since_id = max(tweet.id, new_since_id)
            if tweet.user == converser:
                if not "bye bye" in tweet.text.lower():
                    response = openai.Completion.create(
                        model="davinci:ft-personal-2022-08-09-17-26-53",
                        prompt=tweet.text
                    )
                    api.update_status(
                        status=f"@{converser.screen_name} Nyan: {scrub_completion(response)}",
                        in_reply_to_status_id=tweet.id
                    )
                    return True
                else:
                    return False
            else:
                failed_checks += 1
        if failed_checks > 9:
            checking = False
            return False


def new_conversation_getter(api, since_id) -> Tuple[str, bool]:
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline, since_id=new_since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if "hello nyan" in tweet.text.lower():
            response = openai.Completion.create(
                model="davinci:ft-personal-2022-08-09-17-26-53",
                prompt=tweet.text
            )
            api.update_status(
                status=f"@{tweet.user.screen_name} Nyan: {scrub_completion(response)}",
                in_reply_to_status_id=tweet.id
            )
            return tweet.user, True
    return "", False


def converse() -> None:
    in_conversation = False
    since_id = 1
    conversing_user = ""
    wait_counter = 0
    while conversing:
        if in_conversation and conversing_user:
            in_conversation = check_for_conversations(api, since_id, conversing_user)
            print(f"talking to {conversing_user}")
        else:
            conversing_user, in_conversation = new_conversation_getter(api, since_id)
        print("waiting before checking")
        time.sleep(60)


print("should we start up Nyan?")
should_converse = input()
if should_converse == "Y":
    conversing = True
else:
    conversing = False

converse()
