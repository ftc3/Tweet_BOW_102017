# Tweet_BOW_102017
This project is a bag of words text analysis: frequency, classification, sentiment analysis

# false_match_word_creator.py
using previously compiled list of match words the mined sentiment words ("cat" and "cats", "cat" and "category"), this file creates a list of false positive strings to be excluded if the potential match fits inside it ("category" should be excluded in future runs), once the match program is rerun.

# tweet_download_api.py
downloads max number of tweets (~3200) from a specified user, all data available from each tweet.
