#!/usr/bin/env python3
"""CLI-Anything: HTTP fetch 工具
用法: python fetch.py <url> [--method POST] [--data '{"key":"value"}']
"""
import sys
import json
import urllib.request
import urllib.error

def fetch(url: str, method: str = "GET", data: str = None):
    headers = {"User-Agent": "CLI-Anything/1.0"}
    body = None
    if data:
        body = data.encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            content = resp.read().decode("utf-8")
            print(content)
    except urllib.error.HTTPError as e:
        print(f"HTTP {e.code}: {e.read().decode()}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python fetch.py <url> [--method POST] [--data '{}']")
        sys.exit(1)
    url = sys.argv[1]
    method = "GET"
    data = None
    args = sys.argv[2:]
    for i, a in enumerate(args):
        if a == "--method" and i + 1 < len(args):
            method = args[i + 1]
        elif a == "--data" and i + 1 < len(args):
            data = args[i + 1]
    fetch(url, method, data)
