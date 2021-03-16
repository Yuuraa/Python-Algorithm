class Codec:
    url_ids = {"first": 2}
    characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    base = len(characters)
    char_ids = {char : i for i, char in enumerate(characters)}

    def encode(self, longUrl):
        if longUrl in self.url_ids:
            url_id = self.url_ids[longUrl]
        else:
            url_id = len(self.url_ids.items())
            self.url_ids[longUrl] = url_id
        

        encoded = []
        while url_id > 0:
            x = url_id % self.base
            encoded.append(self.characters[x])
            url_id //= self.base

        return "".join(encoded[::-1])


    def decode(self, shortUrl):
        decoded_id = 0
        mult = 1

        for char in shortUrl[::-1]:
            char_id = self.char_ids[char]
            decoded_id += char_id * mult
            mult *= self.base

        for url, url_id in self.url_ids.items():
            if url_id == decoded_id:
                return url


if __name__ == "__main__":
    codec = Codec()
    url = "https://leetcode.com/problems/design-tinyurl"
    shortend_url = codec.encode(url)
    print(shortend_url)
    decoded_url = codec.decode(shortend_url)
    assert(url == decoded_url)
    print("Example passed!")