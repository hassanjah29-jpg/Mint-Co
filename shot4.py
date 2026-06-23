from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("index.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={"width":1280,"height":860})
    pg.goto(url);pg.wait_for_timeout(700);pg.screenshot(path="b_closed.png")
    pg.evaluate("document.getElementById('box3d').classList.add('opening')");pg.wait_for_timeout(1100);pg.screenshot(path="b_open.png")
    pg2=b.new_page(viewport={"width":390,"height":840})
    pg2.goto(url);pg2.wait_for_timeout(700);pg2.screenshot(path="b_m_closed.png")
    b.close()
print("ok")
