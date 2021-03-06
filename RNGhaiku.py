import random
import tweepy
from words import words
import creds

def syllable_count(word):
	word = word.lower()
	count = 0
	vowels = "aeiouy"
	if word[0] in vowels:
		count += 1
	for index in range(1, len(word)):
		if word[index] in vowels and word[index - 1] not in vowels:
			count += 1
	if word.endswith("e"):
		count -= 1
	if count == 0:
		count += 1
	return count

completed_haiku = ""


def make_haiku(allowed_syllables):
	haiku = ""
	count = 0
	while count < allowed_syllables:
		chosen_word = random.choice(words)
		if syllable_count(chosen_word) > allowed_syllables or (count + syllable_count(chosen_word) > allowed_syllables ):
			continue
		else:
			haiku += " " + chosen_word
			count += syllable_count(chosen_word)
	return haiku

def tweet_haiku():

	first_line = make_haiku(5)
	second_line = make_haiku(7)
	third_line = make_haiku(5)

	completed_haiku = first_line + "\n    " + second_line + "\n" + third_line

	print(completed_haiku)

	consumer_key = creds.consumer_key
	consumer_secret = creds.consumer_secret
	access_token = creds.access_token
	access_token_secret = creds.access_token_secret
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
# test
	try:
	    api.verify_credentials()
	    print("Authentication OK")
	except:
	    print("Error during authentication")

	def publictweet():

	    api.update_status(completed_haiku)

	publictweet()
