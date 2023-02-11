import random
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Rectangle, Line, Ellipse)


def create_elements():
    elements = []
    for i in range(250):
        elements.append((random.randrange(0, 490, 10), (random.randrange(0, 490, 10))))
    return elements


def logic(elements):
    dead_elements = []
    new_elements = []
    for i in range(len(elements)):
        cout = 0
        if (elements[i][0]+10, elements[i][1]) in elements:
            cout = cout+1
        if (elements[i][0], elements[i][1]+10) in elements:
            cout = cout+1
        if (elements[i][0]-10, elements[i][1]) in elements:
            cout = cout+1
        if (elements[i][0], elements[i][1]-10) in elements:
            cout = cout+1
        if (elements[i][0]-10, elements[i][1]-10) in elements:
            cout = cout+1
        if (elements[i][0]+10, elements[i][1]+10) in elements:
            cout = cout+1
        if (elements[i][0]-10, elements[i][1]+10) in elements:
            cout = cout+1
        if (elements[i][0]+10, elements[i][1]-10) in elements:
            cout = cout+1
        if cout>3 or cout<2:
            dead_elements.append(elements[i])
    for elem in dead_elements:
        elements.remove(elem)
    return elements



class Screen(Widget):
    elements = []
    if elements == []:
        elements = create_elements()
    def on_touch_down(self, touch):
        with self.canvas:
            Color(0,1,0,1)
            for i in range(len(Screen.elements)):
                Color(0, 1, 0, 1)
                touch.ud['rectangle'] = Rectangle(pos = (int(Screen.elements[i][0]), int(Screen.elements[i][1])), size = (10,10))
        print(len(Screen.elements))
        Screen.elements = logic(Screen.elements)

        print(len(Screen.elements))




class LiveApp(App):
    def build(self):
        parent = Widget()
        self.painter = Screen()
        parent.add_widget(self.painter)
        parent.add_widget(Button(text = "След. шаг", on_press = self.clear_canvas, pos = (400,400)))
        return parent

    def clear_canvas(self, instance):
        self.painter.canvas.clear()


if __name__ == "__main__":
    LiveApp().run()
