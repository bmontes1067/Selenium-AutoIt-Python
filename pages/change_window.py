
def change_window_focus(driver):
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    return driver


def close_new_window(driver):
    driver.close()


def go_back_first_window(driver):
    first_window = driver.window_handles[0]
    driver.switch_to.window(first_window)
