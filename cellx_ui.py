#from kivy.uix.screenmanager import Screen

from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.toast import toast
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty
#from kivymd.uix.label import MDLabel
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
			font_size: "20sp"
			font_name: "Ubuntu-M"
			
		MDRectangleFlatButton:
			text: "Open file"
			font_name: "Ubuntu-L"
			on_release: app.show_load()
	
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
			
<LoadDialog>:
	BoxLayout:
		size: root.size
        pos: root.pos
        orientation: "vertical"
        FileChooserIconView:
            id: filechooser

        BoxLayout:
            size_hint_y: None
            height: 30
            Button:
                text: "Cancel"
                on_release: root.cancel()

            Button:
                text: "Load"
                on_release: app.load(filechooser.path, filechooser.selection)		
'''

class LoadDialog(FloatLayout):
	load = ObjectProperty(None)
	cancel = ObjectProperty(None)


class GincellApp(MDApp):
	
	loadfile = ObjectProperty(None)
	path_label = ObjectProperty(None)
	
	def confirm_text(self):
			toast("Staks in progress...")
			
	def dismiss_popup(self):
		self._popup.dismiss()
		
	def show_load(self):
		content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
		self._popup = Popup(title="Load file", content=content, size_hint=(0.9, 0.9))
		self._popup.open()
		
	def load(self, path, filename):
			self.t = filename
			self.path_label.text = self.t
			self.dismiss_popup()
	
	def build(self):
		screen = Builder.load_string(KV)
		return screen


Factory.register('Root', cls=GincellApp)
Factory.register('LoadDialog', cls=LoadDialog)

if __name__ == '__main__':
	GincellApp().run()