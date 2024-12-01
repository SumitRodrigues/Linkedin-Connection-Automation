from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

# LinkedIn login credentials
email = "sumitrod11@gmail.com"
password = "rodlinkedin@11"

# Message to include with the connection request
note = """Hi, I came across your profile and found your experience really inspiring. 
I’m currently seeking summer 2025 full-time opportunities and would be grateful if you could share advice on the application process and give insights to increase my chances of getting an interview at Intuit.
Thank you!"""

# Setting up the browser
driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in your PATH
driver.get("https://www.linkedin.com/login")

# Login to LinkedIn
driver.find_element(By.ID, "username").send_keys(email)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.ID, "password").send_keys(Keys.RETURN)

# Pause to allow page to load
time.sleep(5)

# Navigate to search results page (replace this URL with your target search)
driver.get("https://www.linkedin.com/search/results/people/?currentCompany=%5B%221666%22%5D&geoUrn=%5B%22102448103%22%5D&heroEntityKey=urn%3Ali%3Aorganization%3A1666&keywords=intuit&origin=FACETED_SEARCH&page=2&position=0&searchId=7cd9cb17-27de-485d-80ec-3b65ee828a5e&sid=%40lO")

# Wait for the page to load
time.sleep(5)

# Loop to scroll and process "Connect" buttons
while True:
    try:
        # Find all "Connect" buttons currently visible on the page
        connect_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Connect')]")
        
        for button in connect_buttons:
            try:
                # Scroll to the button to make it visible
                ActionChains(driver).move_to_element(button).perform()
                time.sleep(1)
                button.click()  # Click the "Connect" button
                time.sleep(2)

                # Add a note if prompted
                try:
                    add_note = driver.find_element(By.XPATH, "//button[contains(text(), 'Add a note')]")
                    add_note.click()
                    time.sleep(1)

                    # Enter the note
                    note_box = driver.find_element(By.XPATH, "//textarea[@name='message']")
                    note_box.send_keys(note)

                    # Send the connection request
                    send_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Send')]")
                    send_button.click()
                    time.sleep(2)
                except Exception as e:
                    print("Note window not found, skipping:", e)

            except Exception as e:
                print(f"Error processing button: {e}")
                # Close any pop-up if encountered
                try:
                    dismiss_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Dismiss')]")
                    dismiss_button.click()
                except:
                    pass
                continue

        # Scroll down to load more results
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(3)

        # Check if there are any more "Connect" buttons
        new_connect_buttons = driver.find_elements(By.XPATH, "//button[contains(text(), 'Connect')]")
        if not new_connect_buttons:
            print("No more connections to process.")
            break

    except Exception as e:
        print(f"Error in main loop: {e}")
        break

# Close the browser
driver.quit()