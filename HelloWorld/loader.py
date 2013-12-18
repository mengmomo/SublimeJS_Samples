import sublime

try:
	import SublimeJS.v8
except:
	sublime.error_message('This plugin was written in JavaScript.\n\nYour should install the SublimeJS plugin first.')