
# Import
import paralleldots
# Setting your API key
class API:

    def __init__(self):
            paralleldots.set_api_key("2NEj77DgFsoxg5AN7jLYwByaQaAKIXaPkocS6go2pUE")

    def sentiment_analysis(self,text):
            paralleldots.sentiment(text)
            return response
# Examples
