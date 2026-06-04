urls = {}

while True:
    long_url = input("Enter URL (or 'exit' to quit): ")

    if long_url.lower() == "exit":
        break

    short_code = f"url{len(urls) + 1}"

    urls[short_code] = long_url

    print("Short URL:", short_code)

print("\nStored URLs:")

for code, url in urls.items():
    print(f"{code} -> {url}")



Enter URL (or 'exit' to quit):  http://localhost:8888/notebooks/OneDrive/Desktop/Educational/My%20Courses/Daily/Untitled.ipynb?
Short URL: url1