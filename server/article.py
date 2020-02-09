class Article:
    sentimentScore = 0
    magnitude = 0
    
    def __init__(self, title, url, body):
        self.title = title
        self.url = url
        self.body = body
        
    def setSentimentScore(self, ss):
        self.sentimentScore = ss

    def setMagnitude(self, m):
        self.magnitude = m

    def __str__(self):
        return self.title + '\n' + self.url + '\n' + self.body + '\nSentiment Score: ' + str(self.sentimentScore) + '\nMagnitude: ' + str(self.magnitude) + '\n'
