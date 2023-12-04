class Codec:
    
    def __init_(self):
        self.urls = {}
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if not hasattr(self,"urls"):
            self.urls = {}
        url = longUrl.split("/")[-1]
        hash_value = hash(url)
        self.urls[str(hash_value)]=longUrl
        return "http://tinyurl.com/"+str(hash_value)
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        if not hasattr(self,"urls"):
            self.urls = {}
        hash_value = shortUrl.split("/")[-1]
        if hash_value not in self.urls:
            return self.urls[hash_value]
        return self.urls[hash_value]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))