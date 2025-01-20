import tkinter as tk
from tkinter import ttk
import pyautogui
import time
import threading
import keyboard
import win32api

cancel_flag = False
get_position_flag = False

# Define key binding variables
get_position_key = 'a'
start_key = 'b'
stop_key = 'c'

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
    global get_position_flag
    if not get_position_flag:
        get_position_flag = True
        x, y = win32api.GetCursorPos()
        x_entry.delete(0, tk.END)
        x_entry.insert(0, str(x))
        y_entry.delete(0, tk.END)
        y_entry.insert(0, str(y))
        get_position_flag = False

def start_click_and_hold():
    global cancel_flag
    cancel_flag = False  # Reset the cancel flag
    x = int(x_entry.get())
    y = int(y_entry.get())
    duration = float(duration_entry.get())
    repetitions = int(repetitions_entry.get())
    threading.Thread(target=left_click_and_hold, args=(x, y, duration, repetitions)).start()

def cancel_click_and_hold():
    global cancel_flag
    cancel_flag = True

def set_keybind(label, var_name):
    def on_key_event(event):
        key = event.name
        label.config(text=f"Get Mouse Position: {key}")
        globals()[var_name] = key
        keyboard.unhook_all()

        # Update the text of the buttons and labels on the main tab
        position_button.config(text=f"Get Mouse Position({get_position_key})")
        start_button.config(text=f"Start({start_key})")
        cancel_button.config(text=f"Stop({stop_key})")

        # Rebind all keys
        root.bind(f'<{get_position_key}>', lambda event: get_mouse_position())
        root.bind(f'<{start_key}>', lambda event: start_click_and_hold())
        root.bind(f'<{stop_key}>', lambda event: cancel_click_and_hold())

        # Register global hotkeys
        keyboard.add_hotkey(get_position_key, get_mouse_position)
        keyboard.add_hotkey(start_key, start_click_and_hold)
        keyboard.add_hotkey(stop_key, cancel_click_and_hold)

    label.config(text="Press any key...")
    keyboard.hook(on_key_event)

def validate_numeric_input(P):
    if P.isdigit() or P == "":
        return True
    else:
        return False

# Create the root window
root = tk.Tk()
root.title("Mouse Click and Hold")
root.geometry("300x300")

vcmd = (root.register(validate_numeric_input), '%P')

# Create a Notebook widget
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both')

# Create frames for each tab
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)

# Add frames to the notebook
notebook.add(tab1, text='Main')
notebook.add(tab2, text='Settings')

# Add widgets to the first tab
tk.Label(tab1, text="Enter X coordinate:").pack()
x_entry = tk.Entry(tab1, validate='key', validatecommand=vcmd)
x_entry.pack()

tk.Label(tab1, text="Enter Y coordinate:").pack()
y_entry = tk.Entry(tab1, validate='key', validatecommand=vcmd)
y_entry.pack()

tk.Label(tab1, text="Enter duration (seconds):").pack()
duration_entry = tk.Entry(tab1)
duration_entry.pack()
duration_entry.insert(0, "0.55") # Default duration for the basketball game

tk.Label(tab1, text="Enter number of repetitions:").pack()
repetitions_entry = tk.Entry(tab1, validate='key', validatecommand=vcmd)
repetitions_entry.pack()
repetitions_entry.insert(0, "1")

# Create a button to get the current mouse position
position_button = tk.Button(tab1, text=f"Get Mouse Position({get_position_key})", command=get_mouse_position)
position_button.pack()

# Create a button to start the click and hold action
start_button = tk.Button(tab1, text=f"Start({start_key})", command=start_click_and_hold)
start_button.pack()

# Create a button to cancel the click and hold action
cancel_button = tk.Button(tab1, text=f"Stop({stop_key})", command=cancel_click_and_hold)
cancel_button.pack()

# Add widgets to the second tab (Settings)
get_mouse_keybinding_label = tk.Label(tab2, text=f"Get Mouse Position Key: {get_position_key}")
get_mouse_keybinding_label.pack()
get_mouse_keybinding_button = tk.Button(tab2, text="Set Keybind", command=lambda: set_keybind(get_mouse_keybinding_label, 'get_position_key'))
get_mouse_keybinding_button.pack()

start_keybinding_label = tk.Label(tab2, text=f"Start Key: {start_key}")
start_keybinding_label.pack()
start_keybinding_button = tk.Button(tab2, text="Set Keybind", command=lambda: set_keybind(start_keybinding_label, 'start_key'))
start_keybinding_button.pack()

stop_keybinding_label = tk.Label(tab2, text=f"Stop Key: {stop_key}")
stop_keybinding_label.pack()
stop_keybinding_button = tk.Button(tab2, text="Set Keybind", command=lambda: set_keybind(stop_keybinding_label, 'stop_key'))
stop_keybinding_button.pack()

# Bind the keys to their respective functions
root.bind(f'<{get_position_key}>', lambda event: get_mouse_position())
root.bind(f'<{start_key}>', lambda event: start_click_and_hold())
root.bind(f'<{stop_key}>', lambda event: cancel_click_and_hold())

# Register global hotkeys
keyboard.add_hotkey(get_position_key, get_mouse_position)
keyboard.add_hotkey(start_key, start_click_and_hold)
keyboard.add_hotkey(stop_key, cancel_click_and_hold)

# Start the GUI event loop
root.mainloop()