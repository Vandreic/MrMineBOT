"""
MrMine BOT v1.0

A small program written in Python for the game named Mr. Mine.

Functions:
- Sell all your ores
- Forge gem [Missing yellow gem]

The program is made for a 1920x1080 resolution
"""

# TO-DO:
# 1) Create info text for user (What is the bot currently doing...)
# 2) Create info text for user (Total amount of ores sold etc)
# - Start & Stop button on one side, and 2x info text on other side.
# - BOT Info Text = Scroll Text
# 3) Create popup box for when activating all functions at once
# - Add function to forge yellow gem

from functools import partial
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.clock import Clock
from kivy.core.window import Window
from sell_ores import sell_all_ores
from sell_ores import sell_all_ores_count
from forge_gems import forge_gem


class MainWidget(Widget):

    # Object properties [Used for linking with .kv file]
    btn_sell_all_ores = ObjectProperty(None)        # Sell all ores
    btn_forge_gem = ObjectProperty(None)            # Forge gem
    btn_forge_gem_color = ObjectProperty(None)      # Choose gem color
    btn_start_bot = ObjectProperty(None)            # Start BOT
    btn_stop_bot = ObjectProperty(None)             # Stop BOT
    label_info_for_user = ObjectProperty(None)      # Label for information

    sell_all_ores_timer = 60*30    # Timer for capacity to reach 100% (In seconds) | Set to 30 min

    # Time to forge a gem (In seconds)        Default forge time:
    red_gem_forge_time = 60*10                # 10 min
    blue_gem_forge_time = 60*30               # 30 min
    green_gem_forge_time = (60*60) * 4        # 4 hours
    purple_gem_forge_time = (60*60) * 16      # 16 hours
    yellow_gem_forge_time = (60*60) * 48      # 48 hours


    # Used for getting keyboard input
    def __init__(self, **kwargs):
        super(MainWidget, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    # If "Numpad 0" is pressed, stop bot
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == "numpad0":
            self.btn_click_stop_bot()

    # Button: Forge gem
    def btn_click_forge_gem(self):
        # Reset text for gem-color button
        if self.btn_forge_gem.state == "normal":
            self.btn_forge_gem_color.text = "Gem color?"

    # Button: Start BOT
    def btn_click_start_bot(self):
        # Switch activation state for buttons
        self.btn_start_bot.disabled = True
        self.btn_stop_bot.disabled = False
        self.btn_sell_all_ores.disabled = True
        self.btn_forge_gem.disabled = True
        self.btn_forge_gem_color.disabled = True

        # Check if "Sell all ores" is selected
        if self.btn_sell_all_ores.state == "down" and self.btn_forge_gem.state == "normal":
            print("Sell all ores\t Active")
            self.func_sell_all_ores = Clock.schedule_interval(sell_all_ores, self.sell_all_ores_timer) # Start function using Kivy Clock Module
            self.label_info_for_user.text = "All ores were sold " + str(sell_all_ores_count) + " times"

        elif self.btn_sell_all_ores.state == "normal":
            print("Sell all ores\t Deactive")

        # Check if "Forge gem" is selected
        if self.btn_forge_gem.state == "down" and self.btn_sell_all_ores.state == "normal":
            if self.btn_forge_gem_color.text == "Red":
                print("Forge red gem\t Active")
                self.func_forge_gem = Clock.schedule_interval(partial(forge_gem, "red"), self.red_gem_forge_time)
            if self.btn_forge_gem_color.text == "Blue":
                print("Forge blue gem\t Active")
                self.func_forge_gem = Clock.schedule_interval(partial(forge_gem, "blue"), self.blue_gem_forge_time)
            if self.btn_forge_gem_color.text == "Green":
                print("Forge green gem\t Active")
                self.func_forge_gem = Clock.schedule_interval(partial(forge_gem, "green"), self.green_gem_forge_time)
            if self.btn_forge_gem_color.text == "Purple":
                print("Forge purple gem\t Active")
                self.func_forge_gem = Clock.schedule_interval(partial(forge_gem, "purple"), self.purple_gem_forge_time)
            if self.btn_forge_gem_color.text == "Yellow":
                print("Forge yellow gem\t Active")
            if self.btn_forge_gem_color.text == "Gem color?":
                print("Forge gem\t Choose a gem color!")
        elif self.btn_forge_gem.state == "normal":
            print("Forge gem\t Deactive")

        # Check if everything is selected [W.I.P]
        if self.btn_sell_all_ores.state == "down" and self.btn_forge_gem.state == "down":
            print("\nThis function is not available at the moment.")

    # Button: Stop BOT
    def btn_click_stop_bot(self):
        # Switch activation state for buttons
        self.btn_start_bot.disabled = False
        self.btn_stop_bot.disabled = True
        self.btn_sell_all_ores.disabled = False
        self.btn_forge_gem.disabled = False
        self.btn_forge_gem_color.disabled = False

        # Stop active functions
        if self.btn_sell_all_ores.state == "down":
            self.func_sell_all_ores.cancel()
            self.btn_sell_all_ores.state = "normal"
            self.label_info_for_user.text = ""
        if self.btn_forge_gem.state == "down" and self.btn_forge_gem_color.text != "Gem color?" and self.btn_forge_gem_color.text != "Yellow": # W.I.P
            self.func_forge_gem.cancel()
            self.btn_forge_gem.state = "normal"


class MainApp(App):
    def build(self):
        self.title = "MrMine BOT v1.0" # Set title bar

MainApp().run() # Run app