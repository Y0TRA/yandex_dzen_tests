from selenium import webdriver
from selenium.webdriver.common.by import By

import time


def test_search_input(driver):
    print("-------------------------")
    print("Ввод в поисковую строку: ")
    driver.get("https://zen.yandex.ru/")

    try:

        search = driver.find_element(By.CLASS_NAME, "zen-ui-search__input")
        search.send_keys("Вечерняя Москва")

        btn = driver.find_element(By.CLASS_NAME, "zen-ui-search__submit-button")

        if search.get_attribute("value") == "Вечерняя Москва" and btn != None:
            print("Успешно")
        else:
            print("Провалено")

    except BaseException:
        print("Провалено с ошибкой")


def test_video_page(driver):
    print("-------------------------")
    print("Переход на страницу видео: ")
    driver.get("https://zen.yandex.ru/")

    video = driver.find_elements(By.CLASS_NAME, "sidebar-item-view__title")

    video[1].click()

    try:
        btn = driver.find_element(By.CLASS_NAME, "video-add-button-view")

        page = driver.find_element(By.CLASS_NAME, "video-site-app__page")

        if btn != None and page != None:
            print("Успешно")
        else:
            print("Провалено")

    except BaseException:
        print("Провалено с ошибкой")


def test_like_video(driver):
    print("-------------------------")
    print("Лайк и появление кнопки \"подписаться\": ")
    driver.get("https://zen.yandex.ru/")

    video = driver.find_elements(By.CLASS_NAME, "sidebar-item-view__title")
    video[1].click()

    try:

        like = driver.find_elements(By.CLASS_NAME, "zen-ui-button2__text")
        like[1].click()

        subscribe = driver.find_elements(By.CLASS_NAME, "zen-ui-button2__text")

        if subscribe[0].text == "Subscribe" or subscribe[0].text == "Подписаться":
            print("Успешно")
        else:
            print("Провалено")

    except BaseException:
        print("Провалено с ошибкой")


def test_dislike_video(driver):
    print("-------------------------")
    print("Дизлайк и карточка с уведомлением, что контент скрыт: ")
    driver.get("https://zen.yandex.ru/")

    video = driver.find_elements(By.CLASS_NAME, "sidebar-item-view__title")
    video[1].click()

    try:

        dislike = driver.find_elements(By.CLASS_NAME, "zen-ui-button2__text")
        dislike[2].click()

        content = driver.find_element(By.CLASS_NAME, "card-layer-feedback-card-view__title")

        if content.text == "Content hidden" or content.text == "Публикация скрыта":
            print("Успешно")
        else:
            print("Провалено")

    except BaseException:
        print("Провалено с ошибкой")


def test_empty_notifier(driver):
    print("-------------------------")
    print("Уведомления: ")
    driver.get("https://zen.yandex.ru/")

    notifier = driver.find_element(By.CLASS_NAME, "notifier__box")
    notifier.click()

    time.sleep(4)

    # title = driver.execute_script("return document.getElementsByClassName('Title Title_level_1 Header-Title')")
    title = driver.find_elements(By.CLASS_NAME, "Application-Header")
    title_text = "Уведомления"
    print(title)
    notifier_message = driver.find_element(By.CLASS_NAME, "Notifications-MessageTitle")
    notifier_message_text = "Здесь будут ваши уведомления от сервисов Яндекса"

    if title.text == title_text and notifier_message.text == notifier_message_text:
        print("Успешно")
    else:
        print("Провалено")


def test_interests(driver):
    print("-------------------------")
    print("Интересы: ")
    driver.get("https://zen.yandex.ru/")

    count1 = len(driver.find_elements(By.CLASS_NAME, "sidebar-section-view__row"))

    btn = driver.find_element(By.CLASS_NAME, "button-unfold__icon")
    btn.click()

    count2 = len(driver.find_elements(By.CLASS_NAME, "sidebar-section-view__row"))

    if count2 > count1:
        print("Успешно")
    else:
        print("Провалено")


if __name__ == "__main__":
    driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
    test_search_input(driver)
    test_video_page(driver)
    test_like_video(driver)
    test_dislike_video(driver)
    test_interests(driver)
    # test_empty_notifier(driver)
