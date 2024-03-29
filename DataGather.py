import tweepy
from pandas import DataFrame as df

#API keys will not be provided for security purposes
consumer_key = "******************"
consumer_secret = "***********************"
access_key = "*************-******************"
access_secret = "********************"


# Function to extract tweets
def get_tweets(username):
    # Authorization to consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Access to user's access key and access secret
    auth.set_access_token(access_key, access_secret)

    # Calling api
    api = tweepy.API(auth)

    #200 is max number of tweets per call
    number_of_tweets = 200
    tweets = api.user_timeline(screen_name=username, count=number_of_tweets, tweet_mode="extended")

    # Empty Array
    tmp = []

    #Creates array of full length tweets
    full_tweets = [[tweet.full_text] for tweet in tweets]
    space = ""
    
    #Remove non-ascii characters
    def remove_emoji(inputStr):
        return inputStr.encode('ascii', 'ignore').decode('ascii')
    
    #To clean each tweet by candidates
    for j in full_tweets:
        without_link = j[0][:j[0].rfind("http")]
        without_at = without_link.replace("@", space)
        without_hash = without_at.replace("#", space)
        without_emoji = remove_emoji(without_hash)
        without_and = without_emoji.replace("&", space)
        without_quote = without_and.replace("\"", space)
        without_dollar = without_quote.replace("$", space)
        without_percent = without_dollar.replace("%", space)
        without_lpar = without_percent.replace("(", space)
        without_rpar = without_lpar.replace(")", space)
        without_star = without_rpar.replace("*", space)
        without_carat = without_star.replace("^", space)
        without_plus = without_carat.replace("+", space)
        without_minus = without_plus.replace("-", space)
        without_equals = without_minus.replace("=", space)
        final_tweet = without_equals
        retweet = False
        if j[0][0] == 'R' and j[0][1] == 'T' and j[0][2] == ' ':
            retweet = True
        if not retweet:
            tmp.append(final_tweet)
    file = df(data=tmp)
    file.to_excel(username + '.xlsx', header=False, index=False)


candidates = ["AmyKlobuchar", "AndrewYang", "BernieSanders", "BetoORourke", "CoryBooker", "EricSwalwell", "EWarren",
              "GovBillWeld", "Hickenlooper", "JayInslee", "JoeBiden", "JohnDelaney", "JulianCastro", "KamalaHarris",
              "MarWilliamson", "PeteButtigieg", "RealDonaldTrump", "SenGillibrand", "TimRyan", "TulsiGabbard",
              "WayneMessam"]

# Driver code
if __name__ == '__main__':
    
    for candidate in candidates:
        get_tweets(candidate)
 
