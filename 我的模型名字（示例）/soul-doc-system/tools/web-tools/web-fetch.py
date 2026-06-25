#!/usr/bin/env python3
"""网页内容提取
用法: python web-fetch.py <url>
输出: 提取的正文文本
需要: beautifulsoup4 (pip install beautifulsoup4)
"""
import sys, urllib.request
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []
        self.skip = False
        self.skip_tags = {"script", "style", "nav", "header", "footer"}
        self.depth = {tag: 0 for tag in self.skip_tags}

    def handle_starttag(self, tag, attrs):
        if tag in self.skip_tags:
            self.depth[tag] += 1
            if self.depth[tag] == 1:
                self.skip = True

    def handle_endtag(self, tag):
        if tag in self.skip_tags:
            self.depth[tag] = max(0, self.depth[tag] - 1)
            if self.depth[tag] == 0 and all(d == 0 for t, d in self.depth.items() if t != tag):
                self.skip = False

    def handle_data(self, data):
        if not self.skip:
            stripped = data.strip()
            if stripped:
                self.text.append(stripped)

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
    parser = TextExtractor()
    parser.feed(html)
    return "\n".join(parser.text[:200])  # first 200 text blocks

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python web-fetch.py <url>")
        sys.exit(1)
    print(fetch(sys.argv[1]))
