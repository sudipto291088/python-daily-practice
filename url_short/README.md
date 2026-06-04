# URL Shortener Simulator in Python

## Overview

This program simulates a basic URL shortening service.

Users can:
- Enter long URLs
- Generate short URL codes
- Store URL mappings
- View all stored URLs

The project demonstrates dictionaries, loops, user input handling, and key-value data storage.

---

## Code

```python
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
```

---

## How It Works

1. An empty dictionary stores URL mappings
2. The user enters a long URL
3. A unique short code is generated
4. The URL is stored using the short code as the key
5. The process repeats until the user exits
6. All stored mappings are displayed

---

## Example Run

### Input

```text
Enter URL: https://google.com
Enter URL: https://github.com
Enter URL: exit
```

### Output

```text
Short URL: url1
Short URL: url2

Stored URLs:
url1 -> https://google.com
url2 -> https://github.com
```

---

## Concepts Covered

- Dictionaries
- Loops
- String formatting
- User input handling
- Key-value mapping

---

## Why This Program?

This project introduces:

- URL shortening concepts
- Mapping systems
- Identifier generation
- Data lookup operations

These concepts are commonly used in:

- URL shorteners
- Database indexing
- Caching systems
- Web applications

---

## Possible Improvements

- Generate random short codes
- Search URLs by code
- Delete URLs
- Save mappings to a file
- Track click counts

---

## Author

Daily Python Practice  
URL Shortener Simulator
