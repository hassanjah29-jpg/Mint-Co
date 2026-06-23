from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("logo_preview.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={"width":700,"height":340})
    pg.goto(url);pg.wait_for_timeout(1200);pg.screenshot(path="logo_preview.png");b.close()
print("ok")
