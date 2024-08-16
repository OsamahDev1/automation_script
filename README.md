# Game Automation Script

This Python script automates the process of interacting with a game by detecting specific images on the screen and clicking on them. It is designed to be flexible and easily configurable for various tasks by modifying the constants defined at the beginning of the script.

## Features

- Opens a game or application using a specified executable path.
- Waits for specified images to appear on the screen.
- Clicks on the detected images in sequence.
- Configurable timeout and confidence level for image detection.
- Easy to adapt for different tasks by modifying the constants.

## Prerequisites

- Python 3.x
- [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) library

You can install the required library using pip:

```bash
pip install pyautogui
