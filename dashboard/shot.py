from playwright.sync_api import sync_playwright
import pathlib
u = pathlib.Path('index.html').resolve().as_uri()
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path='/opt/pw-browsers/chromium')
    p = b.new_page(viewport={'width':1180,'height':1400}, device_scale_factor=1)
    errs=[]
    p.on('console', lambda m: errs.append(m.type+': '+m.text) if m.type=='error' else None)
    p.on('pageerror', lambda e: errs.append('pageerror: '+str(e)))
    p.goto(u); p.wait_for_timeout(2500)
    p.screenshot(path='full.png', full_page=True)
    print('ERRORS:', errs or 'none')
    print('rows:', p.eval_on_selector_all('#rows tr','e=>e.length'))
    print('doc height:', p.evaluate('document.body.scrollHeight'))
    print('h-overflow:', p.evaluate('document.documentElement.scrollWidth > document.documentElement.clientWidth'))
    p.set_viewport_size({'width':390,'height':900}); p.wait_for_timeout(500)
    print('mobile h-overflow:', p.evaluate('document.documentElement.scrollWidth > document.documentElement.clientWidth'))
    b.close()
