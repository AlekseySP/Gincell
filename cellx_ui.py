#from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel
#from kivymd.uix.button import MDRectangleFlatButton
import os


KV = '''
BoxLayout:
	orientation: "vertical"
	path_label: path_label
	
	BoxLayout:
		orientation: "horizontal"
		padding: 20, 0, 20, 0
		size_hint: 1.0, None
		#pos_hint: {"right": 0.5}
		
		MDLabel:
			id: path_label
			text: "path/to/file/xlsx"
			theme_text_color: "Secondary"
			font_size: "20sp"
			font_name: "Ubuntu-M"
			
		MDRectangleFlatButton:
			text: "Open file"
			font_name: "Ubuntu-L"
			on_release: app.file_manager_open()
	
	BoxLayout:
		orientation: "horizontal"
		padding: 20, 0, 10, 20
		spacing: 20
		size_hint: 1, None
			
		MDRectangleFlatButton:
			text: "Create staks"
			font_name: "Ubuntu-L"
			on_release: app.confirm_text()
			
		MDRectangleFlatButton:
			text: "Exit"
			font_name: "Ubuntu-L"
			on_release: app.stop()
'''




class GincellApp(MDApp):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		Window.bind(on_keyboard=self.events)
		self.manager_open = False
		self.file_manager = MDFileManager(exit_manager=self.exit_manager, select_path=self.load, preview=False,
        )
	
	def confirm_text(self):
			toast("Staks in progress...")
		
	def file_manager_open(self):
		self.file_manager.show('/data/media/0')
		self.manager_open = True
		
	def load(self, path):
			self.t = path
			toast(self.t)
			#self.path_label.text = self.t
			
	def exit_manager(self, *args):
		self.manager_open = False
		self.file_manager.close()
		
	def events(self, instance, keyboard, keycode, text, modifiers):
		if keyboard in (1001, 27):
			if self.manager_open:
				self.file_manager.back()
		return True
	
	def build(self):
		self.theme_cls.theme_style = "Dark"
		self.theme_cls.primary_palette = "Orange"

		screen = Builder.load_string(KV)
		return screen

if __name__ == '__main__':
	GincellApp().run()