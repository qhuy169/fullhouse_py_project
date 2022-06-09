import time

from automation import generate_driver

driver = generate_driver()

driver.get('https://www.youtube.com/watch?v=66DATYEbdb8')
time.sleep(100)
