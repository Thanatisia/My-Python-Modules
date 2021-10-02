"""
Program Name: PyQt5 Wrap
- A personal PyQt5 wrapper that aims to make usage of PyQt5 easier...hopefully

:: How to use?
	- Copy this into your project's module folder
	- Import this library/module
	- extlib.{class|function|variable}(<parameters>)
"""

import os
import sys

def importlib(self, mod_name=None):
	"""
	Import Module only when needed

	:: Params
		mod_name
			Type: String
			Description: Module Name
	"""
	module = None
	if not (mod_name == ""):
		module = import_module(mod_name)
	return module

''' 
Classes
'''
class Qt5():
	def __init__(self, qapp_params=None):
		"""
		Initialize Application

		:: Params
			qapp_params
				Data Type: List
				Description: Parameters for Application object
		"""
		global designers, widget_creator, app_ctrl

		# Initialize classes
		designers = self.Designers()
		widget_creator = designers.Create()
		app_ctrl = designers.App()

		# Initialize other variables
		self.app = self.create_app()

	def create_app(self, qapp_params=None):
		"""
		Create Application

		:: Params
			qapp_params
				Type: List
				Description: The Application parameters
		"""

		# Default
		if qapp_params == None:
			qapp_params = []

		# Create App
		app = QApplication(qapp_params)
		return app

	def show_widget(self, widget=None):
		"""
		Display Widget/Window in Application
		"""
		if not (widget == None):
			widget.show()

	def addwidgets(self, layout=None, widgets=None):
		"""
		Add multiple widgets at once
		:: Params
			widgets
				[1]
					Data Type: Dictionary
					Description: The Widget you wish to add to the layout and its parameters
					Syntax:
						widget-type: String; Your Widget's type {Label|Button}
						widget-n-id: String; Your Widget's Name
						widget-params: List; Your Widget's Parameters

						{
							"<widget-type>" : {
								"widget-n-id" : [<widget-params>],
							}
						}
					Examples:
						{
							"Button" : {
								"btn-1" : ["Top"],
								"btn-2" : ["Bottom"],
							}
						}
		:: Returns
			Type: List
				[0] : The Layout object itself
				[1] : A dictionary containing the widget_id mapped to the created widget according to its provided parameters
			Syntax:
				[
					<layout-object>,
					{
						"<widget-id>" : <widget-object>
					}
				]
		"""

		# --- Input
		widgets_added = {}

		# --- Processing
		for k,v in widgets.items():
			curr_widget_type = k
			curr_widget_object = v
			
			for curr_widget_id, curr_widget_param in curr_widget_object.items():
				checkstr = curr_widget_type.lower()
				if checkstr == "button":
					tmp_widget = QPushButton(*curr_widget_param)
					layout.addWidget(tmp_widget)
				elif checkstr == "label":
					tmp_widget = QLabel(*curr_widget_param)
					layout.addWidget(tmp_widget)

				# Archive added widgets and their ID
				widgets_added[curr_widget_id] = tmp_widget

		# --- Output
		return [layout, widgets_added]

	def set_layout(self, win=None, layout=None):
		"""
		Wrapper for window.setLayout()

		To set the designed QVBoxLayout() into the window (QWidget)
		"""
		if win == None:
			# Default Value
			win = QWidget()

		if not (layout == None):
			win.setLayout(layout)

		return win

	def exec_app(self, appl=None):
		"""
		Wrapper to execute application with just 1 function
		"""
		if not (appl == None):
			appl.exec()

	class Designers():
		"""
		Self-wrapped designer classes
		"""
		class Create():
			"""
			Create Widgets
			"""
			def labels(self, params=None):
				"""
				Design Labels
				"""
				lb_res = None
				if type(params) == type(list):
					lb_res = QLabel(*params)
				elif type(params) == type(dict):
					lb_res = QLabel(**params)
				else:
					lb_res = QLabel(params)
				return lb_res

			def buttons(self, params=None):
				"""
				Design Buttons
				"""
				btn_res = None
				if type(params) == type(list):
					btn_res = QPushButton(*params)
				elif type(params) == type(dict):
					btn_res = QPushButton(**params)
				else:
					btn_res = QPushButton(params)
				return btn_res
			
			def personal(self, widget_type=None, params=None):
				"""
				Design a Widget of your choice with a single function

				:: Params
					widget_type
						Type: String
						Description: The Widget you wish to use
							Window: QWidget()
							Button: QPushButton()
							Label: QLabel()

					params
						Type: Dictionary|List
						Description: Your Widget Parameters
				"""
				res = None

				# Default
				if params == None:
					params = {}

				target_widget_type = widget_type.lower()
				if target_widget_type == "window":
					if type(params) == type(dict):
						res = QWidget(**params)
					elif type(params) == type(list):
						res = QWidget(*params)
					else:
						res = QWidget(params)
				elif target_widget_type == "layout":
					if type(params) == type(dict):
						res = QVBoxLayout(**params)
					elif type(params) == type(list):
						res = QVBoxLayout(*params)
					else:
						res = QVBoxLayout(params)
				elif target_widget_type == "button":
					if type(params) == type(dict):
						res = QPushButton(**params)
					elif type(params) == type(list):
						res = QPushButton(*params)
					else:
						res = QPushButton(params)
				elif target_widget_type == "label":
					if type(params) == type(dict):
						res = QLabel(**params)
					elif type(params) == type(list):
						res = QLabel(*params)
					else:
						res = QLabel(params)
				return res

		class App():
			"""
			Design Application
			"""
			def style(self, app, style_params=None):
				"""
				Design application styles

				:: Params
					app
						Type: QApplication([])
						Description: Your Application object

					style_params
						Type: String
						Description: The application style
						Options: 'Fusion', 'Windows', 'WindowsVista', 'Macintosh'
				"""
				app.setStyle(style_params)

			def color(self, app, palette=None, color=None):
				"""
				Set application palette colorscheme
				:: Params
					palette
						Type: QPalette()
						Description: The palette widget to hold colours

					color
						Types: {List|Dictionary}
						Description: The parameters for setColor()
						[1] Dictionary
							keys: acg, acr, acolor, GlobalColor

						[2] List
							Syntax:
								Area to change color, Color
							Options: 
								QPalette.ButtonText --> Font color

				:: Returns
					Type: List
					Index
						[0]: Application Object after setting color
						[1]: Palette Widget
				"""
				if palette == None:
					palette = QPalette()

				if not(color == None):
					if type(color) == type(dict):
						palette.setColor(**color)
					elif type(color) == type(list):
						palette.setColor(*color)
				else:
					palette.setColor()
				
				app.setPalette(palette)
				return [app, palette]
	def default_app(self, app=None, window=None, layout=None, widgets=None, show=False):
		"""
		Create a default app setup + layout without running

		:: Params
			app
				Type: {QApplication|List|Dictionary}
				Description: 
					- The Application object
					- Provide QApplication parameters (List|Dictionary) if app object is not provided
				Syntax: 
					[0] : QApplication([]) object
					[1] : List object => [<params>]
					[2] : Dictionary object => { <params> }

			window
				Type: {QWidget|List|Dictionary}
				Description: 
					- The Window object to set the layout on
					- Provide QWidget parameters (List|Dictionary) if window object is not provided
				Syntax: 
					[0] : QWidget([]) object
					[1] : List object => [<params>]
					[2] : Dictionary object => { <params> }

			layout
				Type: {QVBoxLayout|List|Dictionary}
				Description: 
					- The Layout object to place on the window
					- Provide QVBoxLayout parameters (List|Dictionary) if layout object is not provided
				Syntax: 
					[0] : QVBoxLayout([]) object
					[1] : List object => [<params>]
					[2] : Dictionary object => { <params> }

			widgets
				Type: Dictionary
				Description:
					- The Widget you wish to add to the layout and its parameters
				Syntax:
					widget-type: String; Your Widget's type {Label|Button}
					widget-n-id: String; Your Widget's Name
					widget-params: List; Your Widget's Parameters

					{
						"<widget-type>" : {
							"widget-n-id" : [<widget-params>],
						}
					}
				Examples:
					{
						"Button" : {
							"btn-1" : ["Top"],
							"btn-2" : ["Bottom"],
						}
					}

		:: Returns
			app + layout object
				Type: QApplication object
		"""

		# --- Input
		## Defaults

		# Application object
		if type(app) == type(list):
			"""
			If is a list object => Application Parameters
			"""
			app = QApplication(*app)
		elif type(app) == type(dict):
			"""
			If is a dictionary object => Application Parameters
			"""
			app = QApplication(**app)
		else:
			"""
			Else (None value): Initialize empty widget
			"""
			app = QApplication([])

		# Window object
		if type(window) == type(list):
			"""
			If is a list object => Application Parameters
			"""
			window = QWidget(*window)
		elif type(window) == type(dict):
			"""
			If is a dictionary object => Application Parameters
			"""
			window = QWidget(**window)
		else:
			"""
			Else (None value): Initialize empty widget
			"""
			window = QWidget()

		# Layout object
		if type(layout) == type(list):
			"""
			If is a list object => Application Parameters
			"""
			layout = QVBoxLayout(*layout)
		elif type(window) == type(dict):
			"""
			If is a dictionary object => Application Parameters
			"""
			layout = QVBoxLayout(**layout)
		else:
			"""
			Else (None value): Initialize empty widget
			"""
			layout = QVBoxLayout()
	
		# --- Processing
		if not (widgets == None):
			"""
			Add Widgets into layout object if is not null
			"""
			# widgets = {
			# 	"button":
			# 		{
			# 			"btn-1" : ["Top"], 
			# 			"btn-2" : ["Middle"],
			# 			"btn-3" : ["Bottom"]
			# 		}
			# }
			# layout = self.addwidgets(layout, widgets)
			for k,v in widgets.items():
				curr_widget_type = k
				curr_widget_object = v
				
				for curr_widget_id, curr_widget_param in curr_widget_object.items():
					checkstr = curr_widget_type.lower()
					if checkstr == "button":
						if type(curr_widget_param) == type(list):
							tmp_widget = QPushButton(*curr_widget_param)
						elif type(curr_widget_param) == type(dict):
							tmp_widget = QPushButton(**curr_widget_param)
						else:
							tmp_widget = QPushButton(curr_widget_param)
					elif checkstr == "label":
						if type(curr_widget_param) == type(list):
							tmp_widget = QLabel(*curr_widget_param)
						elif type(curr_widget_param) == type(dict):
							tmp_widget = QLabel(**curr_widget_param)
						else:
							tmp_widget = QLabel(curr_widget_param)
					layout.addWidget(tmp_widget)

		# Place layout into window object
		window.setLayout(layout)
		
		# Enable & make window visible in Application
		if show == True:
			window.show()

		# --- Output
		return app


def init():
	"""
	Initialize on startup
	- Variables
	- Import modules
	"""
	print("Starting debug function...")

def setup():
	init()

def main():
	"""
	Debug function
	"""
	print("Initialized")
	qt5 = Qt5()
	default = qt5.default_app(show=True)
	default.exec() 

	
if __name__ == "__main__":
	# Import modules
	from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout
	from PyQt5.QtCore import Qt
	from PyQt5.QtGui import QPalette	# For Colorschemes
	from importlib import import_module
	import sqlite3 as db
	setup()
	main()