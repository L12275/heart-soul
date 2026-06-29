#!/usr/bin/env python3
"""CLI-Anything: 网页截图工具
用法: python browser-screenshot.py <url> [output.png]
需要: playwright (pip install playwright && playwright install chromium)
"""
import sys
import asyncio

async def screenshot(url: str, output: str = "screenshot.png"):
    from playwright.async_api import async_playwright
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1280, "height": 800})
        await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        await page.screenshot(path=output, full_page=True)
        await browser.close()
        print(f"screenshot saved: {output}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("usage: python browser-screenshot.py <url> [output.png]")
        sys.exit(1)
    url = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else "screenshot.png"
    asyncio.run(screenshot(url, output))
