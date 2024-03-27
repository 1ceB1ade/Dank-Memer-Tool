import json
import keyboard
import time
import random
import pyautogui
import os
import cv2
import numpy as np

def read_config_file(file_name):
    try:
        with open(file_name, 'r') as file:
            config_data = json.load(file)
        return config_data
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: File '{file_name}' is not a valid JSON file.")
        return None
    except Exception as e:
        print(f"Error occurred while reading '{file_name}': {e}")
        return None

def type_content(content):
    try:
        pyautogui.write(content)
        pyautogui.press('enter')
    except Exception as e:
        print(f"Error occurred while typing '{content}': {e}")

def click_on_button(button_images):
    try:
        if os.path.exists("images"):
            for button_image in button_images:
                button_path = os.path.join("images", button_image)
                template = cv2.imread(button_path, cv2.IMREAD_GRAYSCALE)
                if template is not None:
                    screen = pyautogui.screenshot(region=(0, 0, 1920, 1080))  # Adjust region as per your screen resolution
                    screen = np.array(screen)
                    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                    result = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)
                    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
                    if max_val > 0.8:
                        button_location = (max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2)
                        time.sleep(0.5)
                        pyautogui.click(button_location)
                        print(f"Clicked on button: {button_image}")
                        return
            print("Button images found but none are visible on the screen.")
        else:
            print("Error: 'images' folder not found.")
    except Exception as e:
        print(f"Error occurred while clicking on button: {e}")

def main():
    config_file_name = "config.json"
    enabled = False
    print("[DISABLED]")

    while True:
        config_data = read_config_file(config_file_name)
        if config_data:
            beg_text = config_data.get("beg_text", "")
            hunt_text = config_data.get("hunt_text", "")
            crime_text = config_data.get("crime_text", "")
            deposit_text = config_data.get("deposit_text", "")

            toggle_keybind = config_data.get("toggle_keybind", "F1")
            
            if os.path.exists("images"):
                button_images = [file for file in os.listdir("images") if file.endswith(".png")]
            else:
                button_images = []

            if keyboard.is_pressed(toggle_keybind):
                enabled = not enabled
                if enabled:
                    print("[ENABLED]")
                else:
                    print("[DISABLED]")
                time.sleep(0.2)

            if keyboard.is_pressed('F2'):
                print("Exiting...")
                break

            if enabled:
                print("\nTyping /beg")
                type_content(beg_text)
                time.sleep(random.randint(40, 80))
                print("\nTyping /hunt")
                type_content(hunt_text)
                time.sleep(random.randint(40, 80))
                print("\nTyping /crime and clicking on button")
                type_content(crime_text)
                click_on_button(button_images)
                print("\n/deposit amount:max")
                type_content(deposit_text)
                time.sleep(7)

if __name__ == "__main__":
    main()
