import allure
from pages.practice_form_page import PracticeFormPage


@allure.title("Заполнение формы Practice Form (Allure screenshot/video)")
def test_practice_form(setup_browser):
    driver = setup_browser
    form = PracticeFormPage(driver)

    with allure.step("Открыть форму"):
        form.open()

    with allure.step("Заполнить имя"):
        form.fill_first_name("Daria")

    with allure.step("Заполнить фамилию"):
        form.fill_last_name("Belevtseva")

    with allure.step("Заполнить email"):
        form.fill_email("test@example.com")

    with allure.step("Выбрать пол"):
        form.fill_gender_female()

    with allure.step("Заполнить мобильный номер"):
        form.fill_mobile("1234567890")

    with allure.step("Отправить форму"):
        form.submit()
