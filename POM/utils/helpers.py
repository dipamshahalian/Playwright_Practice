import time

def take_screenshot(page, name="screenshot"):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    page.screenshot(path=f"screenshots/{name}-{timestamp}.png", full_page=True)
