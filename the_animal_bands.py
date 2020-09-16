import random
import tweepy
import emoji

animals = ["🐒", "🐔", "🐧", "🐦", "🐤", "🦆", "🦅", "🦇", "🐺", "🐗", "🐴", "🦄", "🐝", "🐛", "🐜", "🦟", "🦗", "🦂", "🐢", "🐍", "🦖", "🦕", "🦑", "🦐", "🐡", "🐠", "🐬", "🐋", "🦈", "🐅", "🐆", "🦓", "🦍", "🦧", "🐘", "🦛", "🦏", "🐪", "🐫", "🦒", "🦘", "🐃", "🐂", "🐄", "🐎", "🐖", "🐐", "🦜", "🦃", "🐇", "🐁", "🦥", "🦦"]
instruments = ["🎤", "🥁", "🎷", "🎺", "🎸", "🪕", "🎻", "🍺"]
band_name_1 = ["Jazz", "Fantastic", "Beach", "Forest", "Sky", "Wind", "Wing", "Flower", "Ocean", "Cool", "Earth", "Spring", "Summer", "Autumn", "Winter", "Space", "Petshop", "Spice", "Hibernating", "Night", "Flying", "Sunshine", "Moonlight", "Dead", "Berlin", "Beijing", "Imagined", "London", "New York", "Troubled", "Romanian", "Lost", "Rainbow", "Moon", "Chemical", "Baby", "Red", "Blue", 'Abrupt', 'Acidic', 'Adorable', 'Adventurous', 'Aggressive', 'Agitated', 'Alert', 'Aloof', 'Amiable', 'Amused', 'Annoyed', 'Antsy', 'Anxious', 'Appalling', 'Appetizing', 'Apprehensive', 'Arrogant', 'Ashamed', 'Astonishing', 'Attractive', 'Average', 'Batty', 'Beefy', 'Bewildered', 'Biting', 'Bitter', 'Bland', 'Blushing', 'Bored', 'Brave', 'Bright', 'Broad', 'Bulky', 'Burly', 'Charming', 'Cheeky', 'Cheerful', 'Chubby', 'Clean', 'Clear', 'Cloudy', 'Clueless', 'Clumsy', 'Colorful', 'Colossal', 'Combative', 'Comfortable', 'Condemned', 'Condescending', 'Confused', 'Contemplative', 'Convincing', 'Convoluted', 'Cooperative', 'Corny', 'Costly', 'Courageous', 'Crabby', 'Creepy', 'Crooked', 'Cruel', 'Cumbersome', 'Curved', 'Cynical', 'Dangerous', 'Dashing', 'Decayed', 'Deceitful', 'Deep', 'Defeated', 'Defiant', 'Delicious', 'Delightful', 'Depraved', 'Depressed', 'Despicable', 'Determined', 'Dilapidated', 'Diminutive', 'Disgusted', 'Distinct', 'Distraught', 'Distressed', 'Disturbed', 'Dizzy', 'Drab', 'Drained', 'Dull', 'Eager', 'Ecstatic', 'Elated', 'Elegant', 'Emaciated', 'Embarrassed', 'Enchanting', 'Encouraging', 'Energetic', 'Enormous', 'Enthusiastic', 'Envious', 'Exasperated', 'Excited', 'Exhilarated', 'Extensive', 'Exuberant', 'Fancy', 'Fantastic', 'Fierce', 'Filthy', 'Flat', 'Floppy', 'Fluttering', 'Foolish', 'Frantic', 'Fresh', 'Friendly', 'Frightened', 'Frothy', 'Frustrating', 'Funny', 'Fuzzy', 'Gaudy', 'Gentle', 'Ghastly', 'Giddy', 'Gigantic', 'Glamorous', 'Gleaming', 'Glorious', 'Gorgeous', 'Graceful', 'Greasy', 'Grieving', 'Gritty', 'Grotesque', 'Grubby', 'Grumpy', 'Handsome', 'Happy', 'Harebrained', 'Healthy', 'Helpful', 'Helpless', 'High', 'Hollow', 'Homely', 'Horrific', 'Huge', 'Hungry', 'Hurt', 'Icy', 'Ideal', 'Immense', 'Impressionable', 'Intrigued', 'Irate', 'Irritable', 'Itchy', 'Jealous', 'Jittery', 'Jolly', 'Joyous', 'Filthy', 'Flat', 'Floppy', 'Fluttering', 'Foolish', 'Frantic', 'Fresh', 'Friendly', 'Frightened', 'Frothy', 'Frustrating', 'Funny', 'Fuzzy', 'Gaudy', 'Gentle', 'Ghastly', 'Giddy', 'Gigantic', 'Glamorous', 'Gleaming', 'Glorious', 'Gorgeous', 'Graceful', 'Greasy', 'Grieving', 'Gritty', 'Grotesque', 'Grubby', 'Grumpy', 'Handsome', 'Happy', 'Harebrained', 'Healthy', 'Helpful', 'Helpless', 'High', 'Hollow', 'Homely', 'Horrific', 'Huge', 'Hungry', 'Hurt', 'Icy', 'Ideal', 'Immense', 'Impressionable', 'Intrigued', 'Irate', 'Irritable', 'Itchy', 'Jealous', 'Jittery', 'Jolly', 'Joyous', 'Juicy', 'Jumpy', 'Kind', 'Lackadaisical', 'Large', 'Lazy', 'Lethal', 'Little', 'Lively', 'Livid', 'Lonely', 'Loose', 'Lovely', 'Lucky', 'Ludicrous', 'Macho', 'Magnificent', 'Mammoth', 'Maniacal', 'Massive', 'Melancholy', 'Melted', 'Miniature', 'Minute', 'Mistaken', 'Misty', 'Moody', 'Mortified', 'Motionless', 'Muddy', 'Mysterious', 'Narrow', 'Nasty', 'Naughty', 'Nervous', 'Nonchalant', 'Nonsensical', 'Nutritious', 'Nutty', 'Obedient', 'Oblivious', 'Obnoxious', 'Odd', 'Old-Fashioned', 'Outrageous', 'Panicky', 'Perfect', 'Perplexed', 'Petite', 'Petty', 'Plain', 'Pleasant', 'Poised', 'Pompous', 'Precious', 'Prickly', 'Proud', 'Pungent', 'Puny', 'Quaint', 'Quizzical', 'Ratty', 'Reassured', 'Relieved', 'Repulsive', 'Responsive', 'Ripe', 'Robust', 'Rotten', 'Rotund', 'Rough', 'Round', 'Salty', 'Sarcastic', 'Scant', 'Scary', 'Scattered', 'Scrawny', 'Selfish', 'Shaggy', 'Shaky', 'Shallow', 'Sharp', 'Shiny', 'Short', 'Silky', 'Silly', 'Skinny', 'Slimy', 'Slippery', 'Small', 'Smarmy', 'Smiling', 'Smoggy', 'Smooth', 'Smug', 'Soggy', 'Solid', 'Sore', 'Sour', 'Sparkling', 'Spicy', 'Splendid', 'Spotless', 'Square', 'Stale', 'Steady', 'Steep', 'Responsive', 'Sticky', 'Stormy', 'Stout', 'Straight', 'Strange', 'Strong', 'Stunning', 'Substantial', 'Successful', 'Succulent', 'Superficial', 'Superior', 'Swanky', 'Sweet', 'Tart', 'Tasty', 'Teeny', 'Tender', 'Tense', 'Terrible', 'Testy', 'Thankful', 'Thick', 'Thoughtful', 'Thoughtless', 'Tight', 'Timely', 'Tricky', 'Trite', 'Troubled', 'Twitter', 'Pated', 'Uneven', 'Unsightly', 'Upset', 'Uptight', 'Vast', 'Vexed', 'Victorious', 'Virtuous', 'Vivacious', 'Vivid', 'Wacky', 'Weary', 'Whimsical', 'Whopping', 'Wicked', 'Witty', 'Wobbly', 'Wonderful', 'Worried', 'Yummy', 'Zany', 'Zealous', 'Zippy']
band_name_2 = ["Beasts", "Birds", "Walkers", "Roamers", "Surfers", "Boys", "Girls", "Sounds", "Cats", "Rebels", "Rangers", "Power", "Blues", "Gems", "Crawlers", "Poets", "Herbivores", "Babes", "Hunters", "Humans", "Chasers", "Carnivores", "Pistols", "Chorus", "Dishwashers", "Chefs", "Church", "Spree", "Shadows", "Lips", "Things", "Hearts", 'Statistics', 'Chefs', 'Yaks', 'Riders', 'Users', 'Rubric', 'Mecca', 'Tenor', 'Halt', 'Revenant', 'Pupa', 'Identification', 'Honesty', 'Affiliate', 'Curtain', 'Riding', 'Vignette', 'Mover', 'Invasion', 'Passbook', 'Brook', 'Silk', 'Conservative', 'Step-Uncle', 'Capitulation', 'Sauce', 'Torte', 'Waterfall', 'Latitude', 'Evening-Wear', 'Performance', 'Wisdom', 'Retrospect', 'Dishwasher', 'Metabolite', 'Read', 'Level', 'Fry', 'Spelling', 'Living', 'Dick', 'Artist', 'Admin', 'Mayonnaise', 'Muscle', 'Encirclement', 'Roster', 'Threat', 'Wardrobe', 'Favorite', 'Pathogenesis', 'Scotch', 'Yeast', 'Most', 'Media', 'Lab', 'Skyscraper', 'Ramen', 'Inn', 'Affinity', 'Clover', 'Quartz', 'Friendship', 'Hardhat', 'Shaw', 'Facelift', 'Vibe', 'Broccoli', 'Cord', 'Success', 'Stripe', 'Skiing', 'Pomelo', 'Tablecloth', 'Male', 'Rubbish', 'Girl', 'Termite', 'Ex-Wife', 'Aperitif', 'Canvas', 'Steeple', 'Singing', 'Cheddar', 'Leadership', 'Tensor', 'Crash', 'Dipstick', 'Buy', 'Card', 'Conversation', 'Cranky', 'Eyeballs', 'Hallways', 'Trustees', 'Metronomes', 'Pences', 'Adapters', 'Moons']



#odd

def publictweet(tweet):
	consumer_key = "cQkb9fyBoblzT5sFsin8rrJMp"
	consumer_secret = "UJfaXMs960YNExD3yGpgwjjqAgvUoOi9pR9Iyhuie9AjGjLxSQ"
	access_token = "1251862586120863746-FAGWtXltNWBY7JKQyznfVtOxjOwkXM"
	access_token_secret = "4Sv4ZVgasOdktgQFgLa9UeKQ4btfPFhEbKmrshI9gmrdC"
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)
	api.update_status(tweet)
	print(tweet)
# test
def talent_scout():
    the_boys = ""
    the_band_name = "\n              The " + random.choice(band_name_1) + " " + random.choice(band_name_2)
    bandmates = random.randrange(2, 6)
    bandassemble = []
    global the_boys
    while bandmates > 0:
        instrument_emoji = emoji.emojize(random.choice(instruments), use_aliases=True)
        animal_emoji = emoji.emojize(random.choice(animals), use_aliases=True)
        bandassemble.append(instrument_emoji)
        bandassemble.append(animal_emoji)
        bandassemble.append("  ")
        bandmates-=1
    the_boys = ''.join(bandassemble)
    tweet = the_boys + the_band_name
    publictweet(tweet)