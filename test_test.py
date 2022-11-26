import os
from typing import Generator

import pytest
from playwright.sync_api import Page, expect, APIRequestContext




def test_example(page: Page) -> None:
    page.goto("https://mail.ru/")
    page.get_by_text("Спецоперация").click()

    page.get_by_test_id("enter-mail-primary").click()

    page.frame_locator(".ag-popup__frame__layout__iframe").get_by_placeholder("Имя аккаунта").click()

    page.frame_locator(".ag-popup__frame__layout__iframe").get_by_placeholder("Имя аккаунта").fill("roman.mulyarchik")

    page.frame_locator(".ag-popup__frame__layout__iframe").locator(
        "[data-test-id=\"domain-select-value\\:mail\\.ru\"]").click()

    page.frame_locator(".ag-popup__frame__layout__iframe").locator(
        "[data-test-id=\"select-value\\:mail\\.ru\"]").get_by_text("@mail.ru").click()

    page.frame_locator(".ag-popup__frame__layout__iframe").locator("[data-test-id=\"next-button\"]").click()

    page.frame_locator(".ag-popup__frame__layout__iframe").locator("[data-test-id=\"accountNotRegistered\"]").click()
