from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton




class GincellApp(MDApp):
	def build(self):
		screen = Screen()
		screen.add_widget(MDRectangleFlatButton(
			text="Create stacks",
			pos_hint={"center_x": 0.5, "center_y": 0.5},))
		screen.add_widget(MDRectangleFlatButton(
			text="Exit",
			pos_hint={"center_x": 0.5, "center_y": 0.6},
			command=self.App.stop())
			)
		return screen


if __name__ == '__main__':
	GincellApp().run()