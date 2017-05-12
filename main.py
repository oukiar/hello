from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget

class Hello(FloatLayout):
    pass

if __name__ == "__main__":
    from kivy.app import App
    
    class HelloApp(App):
        def build(self):
            return Hello()

    HelloApp().run()
