import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, long_url):
        # Use hashlib to create a unique hash for the long URL
        url_hash = hashlib.sha256(long_url.encode()).hexdigest()[:8]

        # Generate the shortened URL
        short_url = f"http://short.url/{url_hash}"

        # Store the mapping in the dictionary
        self.url_mapping[short_url] = long_url

        return short_url

    def expand_url(self, short_url):
        # Retrieve the original long URL from the dictionary
        return self.url_mapping.get(short_url, "URL not found")

# Example usage:
url_shortener = URLShortener()

long_url = input()
short_url = url_shortener.shorten_url(long_url)
print(f"Shortened URL: {short_url}")

original_url = url_shortener.expand_url(short_url)
print(f"Original URL: {original_url}")
