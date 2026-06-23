from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("index.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={"width":1280,"height":860})
    pg.goto(url);pg.wait_for_timeout(500)
    pg.evaluate("document.getElementById('intro').classList.add('gone');document.body.classList.remove('lock');document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in'))")
    pg.wait_for_timeout(500)
    for sec in ["home","about","services","gallery","giveaways","contact"]:
        pg.evaluate(f"document.getElementById('{sec}').scrollIntoView()")
        pg.wait_for_timeout(600)
        pg.screenshot(path=f"w_{sec}.png")
    # mobile
    pg2=b.new_page(viewport={"width":390,"height":840})
    pg2.goto(url);pg2.wait_for_timeout(500)
    pg2.screenshot(path="m_intro.png")
    pg2.evaluate("document.getElementById('intro').classList.add('gone');document.body.classList.remove('lock');document.querySelectorAll('.reveal').forEach(e=>e.classList.add('in'))")
    pg2.wait_for_timeout(400);pg2.screenshot(path="m_hero.png")
    b.close()
print("ok")
