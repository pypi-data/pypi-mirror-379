"""Utilities for automating Zeppy chat interactions via Selenium."""

from __future__ import annotations

import sys
import time
from threading import Thread
from typing import List

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

__all__ = ["MSG", "Bot"]
__version__ = "0.1.0"


class MSG:
    """Simple container for chat messages."""

    def __init__(self, name: str = "None", text: str = "None") -> None:
        self.name = name
        self.text = text


class Bot(Thread):
    """Threaded selenium bot that polls Zeppy chat and reacts via hooks."""

    def __init__(
        self,
        bot_name: str,
        target_url: str,
        update_time: float = 0.3,
        login: bool = False,
    ) -> None:
        super().__init__()
        options = Options()
        if sys.platform.startswith("win"):
            options.add_argument("--user-data-dir=C:/selenium/ChromeProfile")
            options.add_argument("--profile-directory=Default")
        else:
            login = False
        self.login = login
        self.seen = []
        self.target_url = target_url
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.name = bot_name
        self.update_time = update_time
        self.running = True
        self.prev_username = ""
        self.new_chat: List[MSG] = []

    def public_chat(self, msg: str) -> None:
        time.sleep(0.51)
        self.driver.find_element(By.CSS_SELECTOR, "body").send_keys(f"\n {msg} \n")

    def press_key(self, key: str) -> None:
        self.driver.find_element(By.CSS_SELECTOR, "body").send_keys(key)

    def update(self) -> None:
        pass

    def whisper(self, name: str, text: str) -> None:
        if not self.login:
            return

        texts = text.split("@n")
        self.driver.find_element(
            By.XPATH,
            f"//div[@type='button'][.//span[contains(text(), '{name}')]]",
        ).click()
        time.sleep(0.05)
        self.driver.find_element(By.CSS_SELECTOR, "button.bg-primaryBg.text-primary").click()
        self.driver.find_element(By.CSS_SELECTOR, ".DirectMessage_panel__pxW3y")
        time.sleep(0.05)
        textarea = self.driver.find_element(
            By.XPATH,
            "//div[contains(@class,'DirectMessage_direct_message_container__4omwe')]"
            f"[.//span[@class='DirectMessage_chat_user_name__QBR_6' "
            f"and normalize-space(text())='{name}']]"
            "//textarea",
        )
        for message in texts:
            textarea.send_keys(message)
            textarea.send_keys(Keys.ENTER)

    def get_chats(self) -> List[MSG]:
        self.new_chat = []
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        loaded_chats = soup.select(".relative .peer")
        new_chats = [msg for msg in loaded_chats if msg not in self.seen]
        for chat in new_chats:
            self.seen.append(chat)
            if chat.select_one(".flex .text-body-2"):
                username = chat.select_one(".flex .text-body-2").text
                self.prev_username = username
                print(username)
            else:
                username = self.prev_username
                print(username)
            if chat.select_one(".relative .text-body-1"):
                message = chat.select_one(".relative .text-body-1").text
                print(message)
            else:
                message = ""
            self.new_chat.append(MSG(username, message))
        return self.new_chat

    def close(self) -> None:
        self.running = False

    def run(self) -> None:
        self.driver.get(self.target_url)
        time.sleep(2)
        for _ in range(50):
            self.driver.find_element(
                By.CSS_SELECTOR, ".Input_input__NwYso input"
            ).send_keys(Keys.BACK_SPACE)
        self.driver.find_element(By.CSS_SELECTOR, ".Input_input__NwYso input").send_keys(
            f"{self.name} \n"
        )
        self.driver.find_element(
            By.CSS_SELECTOR,
            ".PlayerCount_player_count_wrapper__cJhdr .Tooltip_trigger__nNDnu button",
        ).click()
        self.press_key("v")
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        loaded_chats = soup.select(".relative .peer")

        for chat in loaded_chats:
            self.seen.append(chat)

        while self.running:
            self.get_chats()
            self.update()
            time.sleep(self.update_time)
