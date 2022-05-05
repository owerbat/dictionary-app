from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import ObjectProperty


kv = '''
Screen:
    ScreenManager:
        id: screen_manager
        canvas:
            Color:
                rgba: 0.1, 0.1, 0.1, 1
            Rectangle:
                pos: self.pos
                size: self.size

        Screen:
            name: "main_screen"

            MDLabel:
                text: "[b]en-ru dictionary[/b]"
                font_style: "H4"
                text_size: self.size
                halign: "center"
                valign: "top"
                markup: True
                theme_text_color: "Custom"
                text_color: 0.9, 0.9, 0.9, 1

            MDIconButton:
                id: play_button
                icon: "play"
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                theme_text_color: "Custom"
                text_color: 0.1, 0.1, 0.1, 1
                md_bg_color: 0.9, 0.9, 0.9, 1
                on_press:
                    screen_manager.current = "play_screen"

            MDIconButton:
                icon: "star"
                pos_hint: {'center_x': 0.75, 'center_y': 0.5}
                theme_text_color: "Custom"
                text_color: 0.1, 0.1, 0.1, 1
                md_bg_color: 0.9, 0.9, 0.9, 1

            MDIconButton:
                icon: "cog-outline"
                pos_hint: {'center_x': 0.25, 'center_y': 0.5}
                theme_text_color: "Custom"
                text_color: 0.1, 0.1, 0.1, 1
                md_bg_color: 0.9, 0.9, 0.9, 1

        Screen:
            name: "play_screen"

            MDIconButton:
                icon: "arrow-left"
                pos_hint: {'center_x': 0.05, 'center_y': 0.95}
                theme_text_color: "Custom"
                text_color: 0.9, 0.9, 0.9, 1
                on_press:
                    screen_manager.current = "main_screen"

            Label:
                text: "word"
                pos_hint: {'center_x': 0.5, 'center_y': 0.6}
                markup: True
                theme_text_color: "Custom"
                text_color: 0.9, 0.9, 0.9, 1

            MDTextField:
                hint_text: 'Enter the translation'
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: None
                width: 300
                color_mode: "custom"
                line_color_normal: 0.9, 0.9, 0.9, 1
                line_color_focus: 0.9, 0.9, 0.9, 1
                icon_right: "arrow-right"
                icon_right_color: 0.9, 0.9, 0.9, 1
                theme_text_color: "Custom"
                text_color: 0.9, 0.9, 0.9, 1
                current_hint_text_color: 0.9, 0.9, 0.9, 1
'''


class Main(MDApp):
    def build(self):
        return Builder.load_string(kv)


Main().run()
