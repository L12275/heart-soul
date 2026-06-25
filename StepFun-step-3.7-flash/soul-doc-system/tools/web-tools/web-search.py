#!/usr/bin/env python3
"""网页搜索（通过 DuckDuckGo HTML）
用法: python web-search.py <query> [max_results]
输出: JSON 结果列表 [{title, url, snippet}]
需要: beautifulsoup4 (pip install beautifulsoup4)
"""
import sys, json, urllib.parse, urllib.request
from html.parser import HTMLParser

class DDGParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.results = []
        self.in_result = False
        self.current = {}
        self._tags = []

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        cls = attrs_dict.get("class", "")
        if tag == "a" and "result__a" in cls:
            self.in_result = True
            self.current["url"] = attrs_dict.get("href", "")
        elif tag == "a" and "result__snippet" in cls:
            self.in_result = True
        elif tag == "h2" and "result__title" in cls:
            self._tags.append("title")

    def handle_endtag(self, tag):
        if tag in self._tags:
            self._tags.remove(tag)
        if self.in_result and tag == "a" and self.current.get("text"):
            self.results.append(self.current)
            self.current = {}
            self.in_result = False

    def handle_data(self, data):
        if self.in_result:
            stripped = data.strip()
            if stripped:
                if "title" in self._tags and "title" not in self.current:
                    self.current["title"] = stripped
                elif "snippet" in self._tags or self.current.get("url"):
                    self.current.setdefault("snippet", "")
                    self.current["snippet"] += stripped + " "

def search(query, max_results=5):
    url = "https://html.duckduckgo.com/html/?q=" + urllib.parse.quote(query)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        html = resp.read().decode("utf-8", errors="ignore")
    parser = DDGParser()
    parser.feed(html)
    return parser.results[:max_results]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python web-search.py <query> [max_results]")
        sys.exit(1)
    query = sys.argv[1]
    max_r = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    results = search(query, max_r)
    print(json.dumps(results, ensure_ascii=False, indent=2))
