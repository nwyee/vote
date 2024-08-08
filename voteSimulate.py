import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode if you don't need to see the browser

# Specify the path to your chromedriver if it's not in your PATH
chrome_driver_path = 'PATH-TO-CHROME-DRIVER-IN-COMPUTER'


# Function to perform the voting process
def vote():
    # Create a new Chrome session
    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:

        # Navigate to the poll page
        driver.get("https://poll.fm/14165530/embed")

        # Wait for the radio button to be present
        wait = WebDriverWait(driver, 300)
        radio_button = wait.until(EC.presence_of_element_located((By.ID, "PDI_answer63080042")))

        # Select the "Blank: The Series" radio button
        radio_button.click()

        # Click the vote button
        vote_button = driver.find_element(By.ID, "pd-vote-button14165530")
        vote_button.click()
        print("Voted successfully!")

        # Wait for the next page to load (adjust the time as needed)
        wait.until(EC.presence_of_element_located((By.ID, "captcha_14165530")))

        print("wait .. for math")

        # Handle the math CAPTCHA
        question_element = driver.find_element(By.XPATH, "//div[@id='captcha_14165530']//p")
        question_text = question_element.text.strip()

        # Extract numbers from the question text
        numbers = [int(s) for s in question_text.split() if s.isdigit()]
        print(f"math: {numbers}")
        if "+" in question_text:
            answer = sum(numbers)
        elif "-" in question_text:
            answer = numbers[0] - numbers[1]

        # Input the answer into the text field
        answer_input = driver.find_element(By.ID, "answer_14165530")
        answer_input.send_keys(str(answer))

        # Submit the form by clicking the Vote button again
        vote_button = driver.find_element(By.ID, "pd-vote-button14165530")
        vote_button.click()

        print(f"Voted successfully, including solving the CAPTCHA! ->  {answer}")

        # Optionally print the page source or further interact with the page
        # print(driver.page_source)

    except Exception as e:
        print(f"Error during voting: {e}")

    finally:
        # Close the browser
        driver.quit()



# Run the voting process 100 times
for i in range(5):
    print(f"Running iteration {i+1}")
    vote()
    time.sleep(2) 
