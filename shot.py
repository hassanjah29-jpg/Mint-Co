from playwright.sync_api import sync_playwright
import pathlib
url="file://"+str(pathlib.Path("index.html").resolve())
with sync_playwright() as p:
    b=p.chromium.launch()
    pg=b.new_page(viewport={"width":1280,"height":860})
    pg.goto(url)
    pg.wait_for_timeout(700)
    pg.screenshot(path="v_intro_closed.png")          # box closed
    pg.evaluate("document.getElementById('box3d').classList.add('opening')")
    pg.wait_for_timeout(900)
    pg.screenshot(path="v_intro_open.png")             # doors opening
    pg.wait_for_timeout(2200)
    pg.evaluate("window.scrollTo(0,0)")
    pg.wait_for_timeout(300)
    pg.screenshot(path="v_hero.png")
    pg.evaluate("document.getElementById('about').scrollIntoView()");pg.wait_for_timeout(700);pg.screenshot(path="v_about.png")
    pg.evaluate("document.getElementById('services').scrollIntoView()");pg.wait_for_timeout(700);pg.screenshot(path="v_services.png")
    pg.evaluate("document.getElementById('gallery').scrollIntoView()");pg.wait_for_timeout(700);pg.screenshot(path="v_gallery.png")
    pg.evaluate("document.getElementById('giveaways').scrollIntoView()");pg.wait_for_timeout(700);pg.screenshot(path="v_give.png")
    pg.evaluate("document.getElementById('contact').scrollIntoView()");pg.wait_for_timeout(700);pg.screenshot(path="v_contact.png")
    b.close()
print("ok")
