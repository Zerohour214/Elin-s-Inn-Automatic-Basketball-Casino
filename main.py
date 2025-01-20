import tkinter as tk
import pyautogui
import time
import threading
import keyboard
import win32api

cancel_flag = False

def left_click_and_hold(x, y, duration, repetitions):
    global cancel_flag
    for _ in range(repetitions):
        if cancel_flag:
            break
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown(button='left')
        time.sleep(duration)
        pyautogui.mouseUp(button='left')
        time.sleep(0.1)  # Small delay between repetitions

def get_mouse_position():
    x, y = win32api.GetCursorPos()
    x_entry.delete(0, tk.END)
    x_entry.insert(0, str(x))
    y_entry.delete(0, tk.END)
    y_entry.insert(0, str(y))

def start_click_and_hold():
    x = int(x_entry.get())
    y = int(y_entry.get())
    duration = float(duration_entry.get())
    repetitions = int(repetitions_entry.get())
    threading.Thread(target=left_click_and_hold, args=(x, y, duration, repetitions)).start()

def cancel_click_and_hold():
    global cancel_flag
    cancel_flag = True

# Create the root window
root = tk.Tk()
root.title("Mouse Click and Hold")
root.geometry("300x300")

# Create labels and entry fields
tk.Label(root, text="Enter X coordinate:").pack()
x_entry = tk.Entry(root)
x_entry.pack()

tk.Label(root, text="Enter Y coordinate:").pack()
y_entry = tk.Entry(root)
y_entry.pack()

tk.Label(root, text="Enter duration (seconds):").pack()
duration_entry = tk.Entry(root)
duration_entry.pack()
duration_entry.insert(0, "0.55") #Default duration for the basketball game

tk.Label(root, text="Enter number of repetitions:").pack()
repetitions_entry = tk.Entry(root)
repetitions_entry.pack()
repetitions_entry.insert(0, "1")

# Create a button to get the current mouse position
position_button = tk.Button(root, text="Get Mouse Position(F5)", command=get_mouse_position)
position_button.pack()

# Create a button to start the click and hold action
start_button = tk.Button(root, text="Start(F6)", command=start_click_and_hold)
start_button.pack()

# Create a button to cancel the click and hold action
cancel_button = tk.Button(root, text="Stop(F7)", command=cancel_click_and_hold)
cancel_button.pack()

# Bind the F5 key to get the current mouse position
root.bind('<F5>', lambda event: get_mouse_position())
# Bind the F6 key to start the click and hold action
root.bind('<F6>', lambda event: start_click_and_hold())
# Bind the F7 key to cancel the click and hold action
root.bind('<F7>', lambda event: cancel_click_and_hold())

# Register global hotkeys
keyboard.add_hotkey('F5', get_mouse_position)
keyboard.add_hotkey('F6', start_click_and_hold)
keyboard.add_hotkey('F7', cancel_click_and_hold)

# Start the GUI event loop
root.mainloop()