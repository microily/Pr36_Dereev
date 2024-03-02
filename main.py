from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class RainbowColorApp(App):
    def build(self):
        # Определяем цвета и соответствующие им коды
        rainbow_colors = {
            'Красный': '#ff0000',
            'Оранжевый': '#ff8800',
            'Желтый': '#ffff00',
            'Зеленый': '#00ff00',
            'Голубой': '#00ffff',
            'Синий': '#0000ff',
            'Фиолетовый': '#ff00ff',
        }

        # Основной макет приложения
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Текстовое поле для отображения кода цвета (сверху)
        color_code_input = TextInput(text="", readonly=True, font_size=20, multiline=False, background_color=(1, 1, 1, 1))
        layout.add_widget(color_code_input)

        # Метка для отображения названия цвета
        color_label = Label(text="Выберите цвет", font_size=20)
        layout.add_widget(color_label)

        # Создаем кнопки для каждого цвета с различными цветами фона
        for color, code in rainbow_colors.items():
            btn = Button(text=color, background_color=self.hex_to_rgba(code), on_press=self.update_color_info)
            btn.color_code = code  # Сохраняем код цвета в свойстве кнопки
            layout.add_widget(btn)

        return layout

    def update_color_info(self, instance):
        # Обновляем текстовое поле и метку при нажатии на кнопку
        self.root.children[0].text = instance.color_code
        self.root.children[1].text = instance.text

    def hex_to_rgba(self, hex_code):
        # Преобразование шестнадцатеричного кода в RGBA
        return [int(hex_code[i:i + 2], 16) / 255.0 for i in (1, 3, 5)] + [1.0]

if __name__ == '__main__':
    RainbowColorApp().run()
