from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scatter import Scatter
from kivy.graphics import Color

class RainbowApp(App):
    def build(self):
        # Создание основного контейнера
        layout = BoxLayout(orientation='vertical')

        # Создание текстового поля
        text_input = TextInput(hint_text='Код цвета', multiline=False, readonly=True)
        layout.add_widget(text_input)

        # Создание метки для отображения названия цвета
        color_label = Label(text='', font_size=20)
        layout.add_widget(color_label)

        # Создание контейнера для кнопок
        buttons_container = BoxLayout(orientation='horizontal')

        # Список цветов в формате (название, код)
        rainbow_colors = [
            ('Красный', '#ff0000'),
            ('Оранжевый', '#ff8800'),
            ('Желтый', '#ffff00'),
            ('Зеленый', '#00ff00'),
            ('Голубой', '#00ffff'),
            ('Синий', '#0000ff'),
            ('Фиолетовый', '#ff00ff')
        ]

        # Создание кнопок для каждого цвета
        for color_name, color_code in rainbow_colors:
            btn = Button(text=color_name, background_color=Color(hex=color_code).rgba)
            btn.bind(on_press=self.on_button_press)
            buttons_container.add_widget(btn)

        layout.add_widget(buttons_container)

        return layout

    def on_button_press(self, instance):
        # Получение цвета кнопки
        button_color = instance.background_color
        # Преобразование цвета в формат #RRGGBB
        color_code = '#{0:02X}{1:02X}{2:02X}'.format(int(button_color[0] * 255), int(button_color[1] * 255), int(button_color[2] * 255))
        # Установка значения в текстовое поле
        self.root.children[0].text = color_code
        # Установка значения в метку
        self.root.children[1].text = instance.text

if __name__ == "__main__":
    RainbowApp().run()
