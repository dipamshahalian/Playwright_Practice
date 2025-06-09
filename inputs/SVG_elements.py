from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Load an SVG demo page
        page.goto("https://www.w3schools.com/graphics/svg_circle.asp", timeout=60000)

        # Wait for SVG to load
        try:
            page.wait_for_selector("svg circle", timeout=5000)
        except Exception as e:
            print("❌ SVG circle not found:", e)
            browser.close()
            return

        # ✅ 1. Click SVG circle (if clickable)
        try:
            page.locator("svg circle").click()
            print("✅ Clicked SVG circle (if clickable)")
        except Exception as e:
            print("⚠️ Circle is not clickable, but exists.", e)

        # ✅ 2. Get text content inside SVG (if any)
        try:
            label = page.locator("svg text").text_content()
            print(f"📝 Text inside SVG: {label}")
        except Exception as e:
            print("⚠️ No text element found in SVG.", e)

        # ✅ 3. Get SVG attribute (like fill color)
        try:
            color = page.locator("svg circle").get_attribute("fill")
            print(f"🎨 Fill color of circle: {color}")
        except Exception as e:
            print("⚠️ Could not get fill attribute.", e)

        # ✅ 4. XPath example (alternate way)
        try:
            circle = page.locator("xpath=//*[name()='svg']//*[name()='circle']")
            print("✅ Found circle using XPath:", circle.count())
        except Exception as e:
            print("⚠️ Could not find circle using XPath.", e)

        browser.close()

if __name__ == "__main__":
    run()
