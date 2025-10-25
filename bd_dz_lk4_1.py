import wx
import os


class MainWindow(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Приветствие", size=(450, 500))
        self.initializeUI()

    def initializeUI(self):
        """Настройте графический интерфейс приложения."""
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.setUpMainWindow(panel, vbox)

        panel.SetSizer(vbox)
        self.Centre()
        self.Show()

    def setUpMainWindow(self, panel, sizer):
        """Создайте элементы для отображения в главном окне."""
        # Текст приветствия
        hello_label = wx.StaticText(panel, label="привет")
        hello_font = wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        hello_label.SetFont(hello_font)
        sizer.Add(hello_label, 0, wx.ALIGN_CENTER | wx.TOP, 15)

        # Изображение
        image_path = r"c:\Users\dmitry\Downloads\эээ.jfif"
        if os.path.exists(image_path):
            try:
                image = wx.Image(image_path, wx.BITMAP_TYPE_ANY)
                if image.IsOk():
                    image_bitmap = wx.StaticBitmap(panel, bitmap=wx.Bitmap(image))
                    sizer.Add(image_bitmap, 0, wx.ALL, 10)
                else:
                    print("Ошибка загрузки изображения")
            except Exception as error:
                print(f"Image not found.\nError: {error}")
        else:
            print(f"Файл {image_path} не найден")


class ProfileWindow(wx.Frame):
    def __init__(self):
        super().__init__(None, title="Профиль пользователя", size=(400, 700), pos=(550, 100))
        self.initializeUI()

    def initializeUI(self):
        """Настройте графический интерфейс для второго окна."""
        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.setUpMainWindow(panel, vbox)

        panel.SetSizer(vbox)
        self.Show()

    def createImageLabels(self, panel, sizer):
        """Создаёт метки изображений."""
        images = [
            r"c:\Users\dmitry\Downloads\лега230.jfif"
        ]

        image_sizer = wx.BoxSizer(wx.HORIZONTAL)

        for image_path in images:
            if os.path.exists(image_path):
                try:
                    image = wx.Image(image_path, wx.BITMAP_TYPE_ANY)
                    if image.IsOk():
                        # Масштабируем изображение если нужно
                        image = image.Scale(100, 120, wx.IMAGE_QUALITY_HIGH)
                        image_bitmap = wx.StaticBitmap(panel, bitmap=wx.Bitmap(image))
                        image_sizer.Add(image_bitmap, 0, wx.ALL, 5)
                    else:
                        print(f"Ошибка загрузки изображения {image_path}")
                except Exception as e:
                    print(f"Ошибка при загрузке изображения {image_path}: {e}")
            else:
                print(f"Файл {image_path} не найден")

        sizer.Add(image_sizer, 0, wx.ALIGN_CENTER | wx.TOP, 10)

    def setUpMainWindow(self, panel, sizer):
        """Создайте метки, которые будут отображаться в окне."""
        # Изображения
        self.createImageLabels(panel, sizer)

        # Имя пользователя
        user_label = wx.StaticText(panel, label="Киров Дима")
        user_font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        user_label.SetFont(user_font)
        sizer.Add(user_label, 0, wx.ALIGN_CENTER | wx.TOP, 20)

        # Биография
        bio_label = wx.StaticText(panel, label="Информация")
        bio_font = wx.Font(17, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        bio_label.SetFont(bio_font)
        sizer.Add(bio_label, 0, wx.LEFT | wx.TOP, 15)

        about_label = wx.StaticText(panel, label="Я студент 2 курса")
        about_label.Wrap(350)  # Перенос текста
        sizer.Add(about_label, 0, wx.LEFT | wx.TOP, 5)

        # Навыки
        skills_label = wx.StaticText(panel, label="Mellstroy.game")
        skills_label.SetFont(bio_font)
        sizer.Add(skills_label, 0, wx.LEFT | wx.TOP, 15)

        languages_label = wx.StaticText(panel, label="open the door")
        sizer.Add(languages_label, 0, wx.LEFT | wx.TOP, 5)
class App(wx.App):
    def OnInit(self):
        # Создаем оба окна
        main_window = MainWindow()
        profile_window = ProfileWindow()
        return True
# Запуск приложения
if __name__ == "__main__":
    app = App()
    app.MainLoop()