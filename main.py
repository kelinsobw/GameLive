import random
from datetime import datetime
from time import sleep

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Rectangle, Line, Ellipse)
from kivy.config import Config

class Setting():
    weight = 1280
    height = 920
    start_elements = 2000
    size_point = 10
    elements = []


Config.set("graphics", "resizable", 0)
Config.set("graphics", "width", Setting.weight)
Config.set("graphics", "height", Setting.height)


def create_elements():
    elements = []
    for i in range(Setting.start_elements):
        elements.append((random.randrange(0, Setting.weight, Setting.size_point), (random.randrange(0, Setting.height, Setting.size_point))))
    return elements


def logic(elements):
    size_point = Setting.size_point
    height = Setting.height
    weight = Setting.weight
    dead_elements = []
    new_elements = []
    for i in range(len(elements)):
        cout = 0
        if (elements[i][0]+size_point, elements[i][1]) in elements:
            cout = cout+1
        if (elements[i][0], elements[i][1]+size_point) in elements:
            cout = cout+1
        if (elements[i][0]-size_point, elements[i][1]) in elements:
            cout = cout+1
        if (elements[i][0], elements[i][1]-size_point) in elements:
            cout = cout+1
        if (elements[i][0]-size_point, elements[i][1]-size_point) in elements:
            cout = cout+1
        if (elements[i][0]+size_point, elements[i][1]+size_point) in elements:
            cout = cout+1
        if (elements[i][0]-size_point, elements[i][1]+size_point) in elements:
            cout = cout+1
        if (elements[i][0]+size_point, elements[i][1]-size_point) in elements:
            cout = cout+1
        if cout>3 or cout<2:
            dead_elements.append(elements[i])
    for h in range(0, height, size_point):
        start_time = datetime.now()
        for w in range(0, weight, size_point):
            if (w,h) is not elements:
                cout_2 = 0
                if (w, h+size_point) in elements:
                    cout_2 = cout_2+1
                if (w, h-size_point) in elements:
                    cout_2 = cout_2+1
                if (w+size_point, h) in elements:
                    cout_2 = cout_2+1
                if (w-size_point, h) in elements:
                    cout_2 = cout_2+1
                if (w+size_point, h+size_point) in elements:
                    cout_2 = cout_2+1
                if (w-size_point, h-size_point) in elements:
                    cout_2 = cout_2+1
                if (w+size_point, h-size_point) in elements:
                    cout_2 = cout_2+1
                if (w-size_point, h+size_point) in elements:
                    cout_2 = cout_2+1
                if cout_2==3:
                    new_elements.append((w, h))
        print(datetime.now() - start_time)
    for i in range(0, len(new_elements)):
        elements.append(new_elements[i])
    for elem in dead_elements:
        elements.remove(elem)

    return elements


class Screen(Widget):
    if Setting.elements == []:
        Setting.elements = create_elements()
    def on_touch_down(self, touch):
        with self.canvas:
            Color(0,1,0,1)
            if Setting.elements!=[]:
                self.canvas.clear()
                for i in range(len(Setting.elements)):
                    Color(0, 1, 0, 1)
                    self.canvas.add(Rectangle(pos = (int(Setting.elements[i][0]), int(Setting.elements[i][1])), size = (Setting.size_point,Setting.size_point)))
            else:
                print("lose")
                touch.ud['line'] = Line(pos=(1,1,25,25))
        Setting.elements = logic(Setting.elements)


class LiveApp(App):
    def build(self):
        parent = Widget()
        self.painter = Screen()
        parent.add_widget(self.painter)
        return parent


if __name__ == "__main__":
    LiveApp().run()
