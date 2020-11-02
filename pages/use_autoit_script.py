import os
import time


def use_autoit_script(driver):
    driver.find_element_by_id("id_button_click").click()
    time.sleep(1)
    os.system(r'"..\executables\upload_icon.exe')
    time.sleep(1)
