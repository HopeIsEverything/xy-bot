import random
import pytumblr
from wordnik import *

keys = [line.rstrip("\n") for line in open("keys.txt")]

apiUrl = "http://api.wordnik.com/v4"
apiKey = keys[0]
client = swagger.ApiClient(apiKey, apiUrl)
wordApi = WordApi.WordApi(client)
wordsApi = WordsApi.WordsApi(client)

default_level = 60

def get_random_noun(level=default_level):
    return wordsApi.getRandomWord(includePartOfSpeech="noun", minDictionaryCount=level).word

def get_related_words(word):
    related = wordApi.getRelatedWords(word, relationshipTypes="same-context")[0].words

    word_one = random.choice(related)
    word_two = word_one

    while word_one is word_two:
        word_two = random.choice(related)

    return (word_one, word_two)

def begins_with_vowel(word):
    a = word[0]
    return (a == "a") or (a == "e") or (a == "i") or (a == "o") or (a == "u")

def are_you_a():
    items = []
    level = default_level

    while len(items) is not 2:
        items = get_related_words(get_random_noun(level))
        level += 1

    first_vowel = begins_with_vowel(items[0].strip())
    second_vowel = begins_with_vowel(items[1].strip())

    text = "Are you a"
    if first_vowel:
        text += "n "
    else:
        text += " "
    text += items[0]

    text += " or a"

    if second_vowel:
        text += "n "
    else:
        text += " "
    text += items[1] + " person...  "

    return text

consumer_key = keys[1]
consumer_secret = keys[2]
oauth_token = keys[3]
oauth_token_secret = keys[4]

client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_token,
    oauth_token_secret
)

text = are_you_a() + are_you_a() + are_you_a()

client.create_text("xy-bot", state="published", body=text, tags=["are you a x or a y person", "x or y", "x or y person meme"])
