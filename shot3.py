from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("index.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={"width":1280,"height":860})
    pg.goto(url);pg.wait_for_timeout(900)
    pg.screenshot(path="r_intro.png")
    pg.evaluate("document.getElementById('intro').classList.add('gone');document.body.classList.remove('lock');document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in'))")
    pg.wait_for_timeout(500)
    for sec in ["home","collections","gallery"]:
        pg.evaluate(f"document.getElementById('{sec}').scrollIntoView()");pg.wait_for_timeout(700);pg.screenshot(path=f"r_{sec}.png")
    b.close()
print("ok")
