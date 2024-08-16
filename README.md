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
```
## Usage

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/game-automation-script.git
   ```
   2. **Edit the Script**
  
   Open the main.py script in your favorite text editor and adjust the constants at the top to suit your specific task,
   example:
# Constants
```
GAME_EXECUTABLE_PATH = r"C:\Path\To\Your\Game\game.exe"
IMAGE_PATHS = [
    "play.png",
    "ranked_solo.png",
    "confirm.png",
    "find_match.png",
]
TIMEOUT = 300  # Timeout for waiting for images in seconds
CONFIDENCE_LEVEL = 0.8  # Confidence level for image recognition
```
GAME_EXECUTABLE_PATH: The path to the game or application executable.
IMAGE_PATHS: A list of image filenames that the script will look for on the screen.
TIMEOUT: The maximum amount of time (in seconds) the script will wait for an image to appear.
CONFIDENCE_LEVEL: The confidence level for image detection (between 0 and 1).




## Customization

You can easily adapt this script for other games or applications by changing the image files and adjusting the constants. The script will work for any task where you need to automate clicking based on image detection.

## Troubleshooting

- **Image Not Found**: If the script fails to detect an image, try lowering the `CONFIDENCE_LEVEL` or ensure that the image files are clear and accurately represent what appears on the screen.
- **Timeout Issues**: If the script times out too quickly, consider increasing the `TIMEOUT` value.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

If you have suggestions for improvements or run into any issues, feel free to open an issue or submit a pull request.

---

This script was created to simplify repetitive tasks and improve efficiency when interacting with games or other applications.

