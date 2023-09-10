import keyboard

class KeyboardHandler:
    def __init__(self) -> None:
        self.k = keyboard
        self.key_actions = {}

    def register_key_action(self, key, action):
        self.key_actions[key] = action

    def start_listening(self):
        self.k.hook(self.on_key_event)

    def stop_listening(self):
        self.k.unhook_all()

    def on_key_event(self, e):
        key = e.name
        if key in self.key_actions:
            self.key_actions[key]()
        else:
            print("key not registed Dx")

