from playwright.sync_api import Page, expect
import pytest

testdata = [[10,''],[11,''],[12,'']]


@pytest.mark.parametrize('testdata', testdata)
def test_example(page: Page, testdata) -> None:
    page.goto("https://forms.yandex.ru/cloud/61087018ddb03890a6b000b2/")
    page.get_by_role("row", name="* Хочу").get_by_label("Выбрать").click()
    page.locator("#uniq16693733178634").get_by_text("Продление дедлайна").click()
    page.get_by_role("row", name="* Школа").get_by_label("Выбрать").click()
    page.locator("#uniq16693733178637").get_by_text("SkillFactory").click()
    page.get_by_role("row", name="* Курс Coding").get_by_label("Выбрать").click()
    page.locator("#uniq166937331786324").get_by_text("DEVOPS (DevOps-инженер)").click()
    page.locator("input[name=\"answer_non_profile_email_71480\"]").click()
    page.locator("input[name=\"answer_non_profile_email_71480\"]").fill("mulyarchik.rk@yandex.ru")
    page.get_by_role("button", name="Далее").click()
    page.locator("input[name=\"answer_number_11015573\"]").click()
    page.locator("input[name=\"answer_number_11015573\"]").fill("30")
    page.locator("input[name=\"answer_short_text_9389221\"]").click()
    page.locator("input[name=\"answer_short_text_9389221\"]").fill("B11")
    page.locator("#uniq16691154758992126753").click()
    page.get_by_role("cell", name="42 29").click()
    page.locator("textarea[name=\"answer_long_text_71488\"]").click()
    page.locator("textarea[name=\"answer_long_text_71488\"]").fill("Выгорел. Пришлось сделать перерыв. ")
    page.locator("textarea[name=\"answer_long_text_71488\"]").press("Meta+a")
    page.locator("textarea[name=\"answer_long_text_71488\"]").fill("Нагоняю упущенное.")
    page.locator("input[name=\"answer_short_text_9389221\"]").click()
    page.locator("input[name=\"answer_short_text_9389221\"]").fill("B9")
    page.locator("input[name=\"answer_url_9464989\"]").click()
    page.locator("input[name=\"answer_url_9464989\"]").click()
    page.locator("input[name=\"answer_url_9464989\"]").fill("https://lms.skillfactory.ru/courses/course-v1:SkillFactory+DEVOPS-3.0+2021/courseware/1818f1e4a2fa4e2aace76827bb5ed460/e56399ed48e144a089408ca517c75175/")
    page.get_by_role("button", name="Отправить").click()
    expect(page).to_have_url("https://forms.yandex.ru/cloud/61087018ddb03890a6b000b2/success/?akey=6d851d763711826f6510a76817e87abdb878621b")
