import os
import pyautogui
import time

# Constants
GAME_EXECUTABLE_PATH = r"C:\Users\xxosa\Desktop\YourGame.exe"
IMAGE_PATHS = [
    "play.png",
    "ranked_solo.png",
    "confirm.png",
    "find_match.png",
]
TIMEOUT = 300  # Timeout for waiting for images in seconds
CONFIDENCE_LEVEL = 0.8  # Confidence level for image recognition

def open_game(executable_path):
    """Opens the game using the given executable path."""
    try:
        os.startfile(executable_path)
        print("Game opened successfully.")
    except FileNotFoundError as e:
        print(f"Failed to open the game: {e}")

def wait_for_any_image_to_load(image_paths, timeout=TIMEOUT):
    """Waits for any specified image to load on the screen within a timeout."""
    start_time = time.time()
    while True:
        for image_path in image_paths:
            try:
                location = pyautogui.locateOnScreen(image_path, confidence=CONFIDENCE_LEVEL)
                if location:
                    print(f"Image {image_path} found on the screen.")
                    return image_path, location
            except pyautogui.ImageNotFoundException:
                continue  # If image not found, continue with the next image

        if time.time() - start_time > timeout:
            print("Timed out waiting for images to appear.")
            return None, None
        time.sleep(1)  # wait a bit before trying again to not overload the CPU

def click_image(location):
    """Clicks at the given location."""
    if location:
        x, y = pyautogui.center(location)
        pyautogui.moveTo(x, y)
        time.sleep(0.1)  # Adding a slight delay to ensure the mouse has time to move
        pyautogui.click()
        print("Clicked on the image.")

def main():
    # open_game(GAME_EXECUTABLE_PATH)
    images = IMAGE_PATHS.copy()  # Copy the list to avoid modifying the original

    while images:
        found_image_path, location = wait_for_any_image_to_load(images)
        if found_image_path:
            click_image(location)
            # Remove the found image and previous ones from the list
            images = images[images.index(found_image_path)+1:]
        else:
            print("No more images found or timed out.")
            break

if __name__ == "__main__":
    main()
