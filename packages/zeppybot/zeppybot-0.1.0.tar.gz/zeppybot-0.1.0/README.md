# zeppybot

`zeppybot` is a threaded Selenium helper that automates chatting on [Zeppy](https://zep.us/).

## Features
- wraps Selenium Chrome webdriver with sensible defaults
- polls public chat, exposes new messages, and lets you override `Bot.update()`
- supports optional whisper functionality when running on Windows profiles

## Installation
```bash
pip install zeppybot
```
## Quick start
```python
from zeppybot import Bot

class HelloBot(Bot):
    def __init__(self,number):
        super().__init__(f"HelloBot {number}","https://zep.us/play/Example",login=True)
    def update(self):
        for chat in self.new_chat:
            if chat.text == "Hello":
                self.public_chat(f"Hello, {chat.name}")
                self.whisper(chat.name,"I'm zeppy bot")
                self.press_key("z")

bot = HelloBot()
bot.start()
```

## Development
1. Create a virtual environment and install the project in editable mode:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install --upgrade pip
   pip install -e .
   ```
2. Install build tooling:
   ```bash
   pip install build twine
   ```
3. Build artifacts for distribution:
   ```bash
   python -m build
   ```
4. Upload to PyPI (replace with TestPyPI first if needed):
   ```bash
   python -m twine upload dist/*
   ```
