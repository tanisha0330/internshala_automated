from playwright.sync_api import sync_playwright
import time
import config

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        #LOGIN 
        print("🔑 Logging in...")
        page.goto("https://internshala.com/login")
        page.fill("#email", config.EMAIL)
        page.fill("#password", config.PASSWORD)
        page.click("#login_submit")
        
       

         # Change this URL to whatever category you want (Web Dev, Data Science, etc.)

        page.goto("https://internshala.com/internships/work-from-home-web-development-internships/stipend-2000/")

        print("target page has been loaded") 

      


       

if __name__ == "__main__":
    run()
