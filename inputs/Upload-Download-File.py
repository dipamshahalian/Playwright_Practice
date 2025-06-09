# # This script uses Playwright to automate file upload on a web page.

# from playwright.sync_api import sync_playwright
# import os

# def run():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)  # Set headless=True to run without UI
#         context = browser.new_context()
#         page = context.new_page()

#         # Navigate to the test file upload site
#         page.goto("https://the-internet.herokuapp.com/upload", timeout=60000)

#         # Wait for the file input to be visible
#         page.wait_for_selector("input#file-upload", timeout=10000)

#         # Replace this path with the full path to your file
#         file_path = r"inputs\sf25_LH.jpg"  # Use raw string for Windows paths

#         # Check if file exists before uploading
#         if not os.path.isfile(file_path):
#             print(f"❌ File not found: {file_path}")
#             browser.close()
#             return

#         # Upload the file
#         page.set_input_files("input#file-upload", file_path)

#         # Click the 'Upload' button
#         page.click("input#file-submit")

#         # Optional: wait for upload result
#         page.wait_for_selector("h3")  # "File Uploaded!" heading

#         print("✅ File uploaded successfully!")

#         # Close browser
#         input("Press Enter to close the browser...")
#         browser.close()

# if __name__ == "__main__":
#     run()


# Now let's create a script to download a file using Playwright.

from playwright.sync_api import sync_playwright
import os

def run():
    download_dir = os.path.join(os.getcwd(), "downloads")
    os.makedirs(download_dir, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()

        # Go to a page with a downloadable CSV file
        page.goto("https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html")

        # Wait for the download link to be visible
        page.wait_for_selector('a[href="airtravel.csv"]')

        # Start waiting for the download
        with page.expect_download() as download_info:
            page.click('a[href="airtravel.csv"]')
        download = download_info.value

        # Save the downloaded file to the downloads directory
        save_path = os.path.join(download_dir, download.suggested_filename)
        download.save_as(save_path)
        print(f"✅ File downloaded to: {save_path}")

        input("Press Enter to close the browser...")
        browser.close()

if __name__ == "__main__":
    run()