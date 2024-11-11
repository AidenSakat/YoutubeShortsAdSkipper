# Youtube shorts auto skipper
# run with "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
url = "https://www.google.com"

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(options=chrome_options)
driver.get(url)
actions = ActionChains(driver)

# func to get time left in short by getting an element that constantly updates
def get_time_left_in_shorts():
  shorts = driver.find_elements(By.CLASS_NAME, 'YtPlayerProgressBarDragContainer')

  for short in shorts:
    # element that updates % of video done
    time_left = short.get_attribute('aria-valuenow')
    if time_left:
      return float(time_left)
  return 0

# func to check if you are viewing a short to begin the program
def monitor_shorts():
    while True:
      # finds progress bar in shorts video
        shorts_section = driver.find_elements(By.CLASS_NAME, 'YtPlayerProgressBarDragContainer')
        
        if shorts_section:
            time_left = get_time_left_in_shorts()
            print(time_left)

            if time_left > 93:
              print("Scrolling")
              actions.send_keys(Keys.PAGE_DOWN).perform()
              time.sleep(3)
        time.sleep(0.2)

monitor_shorts()
