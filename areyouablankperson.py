import random
import pytumblr
from wordnik import *

apiUrl = "http://api.wordnik.com/v4"
apiKey = "61b5d9cdfaf70bbcfd0060dda6906f55536bf6b9e2a23fd67"
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
    return a is "a" or a is "e" or a is "i" or a is "o" or a is "u"

def are_you_a():
    items = []
    level = default_level

    while len(items) is not 2:
        items = get_related_words(get_random_noun(level))
        level += 1

    first_vowel = begins_with_vowel(items[0])
    second_vowel = begins_with_vowel(items[1])

    text = "Are you a"
    if first_vowel:
        text += "n "
    else:
        text += " "
    text += items[0]

    text += " person or a"

    if second_vowel:
        text += "n "
    else:
        text += " "
    text += items[1] + " person...  "

    return text

consumer_key = "kQg24WSBiK7laCxHizvmvayPSzQrjYi0Te8gfAaOQ0G3WAM5zq"
consumer_secret = "pO0vvdIRaK5WdVlxzZxyviAtoujLGhtrxGxnwC7GUnSOjbkF7m"
oauth_token = "kkrZDZ5YRuC18m22fWx63gArzzIFIJvf0SQuW9L2TaQZBIa5o7"
oauth_token_secret = "6mQ83xXxhd75DXB46Tgkzw0AxvfsCMwyfzgN870nXM0rb4Lo8U"

client = pytumblr.TumblrRestClient(
    consumer_key,
    consumer_secret,
    oauth_token,
    oauth_token_secret
)

text = are_you_a() + are_you_a() + are_you_a()

client.create_text("testybotty", state="published", body=text)
