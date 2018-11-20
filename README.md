# TypeBolt
TypeBolt is a program written in python 3 that tests your typing skills using [TypingBolt](https://www.typingbolt.com/). Results are saved on a .csv file, which can later are used by grapher.py to show a line graph with your score. Check how fast you type!

# Usage
Run TypeBolt.py, which will open your selected browser. Once finished typing, close the browser and then run grapher.py to see your results!

# Requirements
- Selenium(Browser Interaction)  ```pip install -U selenium```
- Matplotlib(graphing)  ```pip install matplotlib```
- [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/)(chrome) or [geckodriver](https://github.com/mozilla/geckodriver/releases)(firefox)

# Supported Browsers
- Chrome
- Firefox

# Config
All the information needed for the program is in config.ini file.

# Q&A
Q: Failed to change window state to maximized (macOS 10.12.6 and Chrome v70)
A: Remove line 56 in TypeBolt.py

Q: IndexError: list index out of range
A: This happens when it tries to get the score, but the keyboard didn't load.
