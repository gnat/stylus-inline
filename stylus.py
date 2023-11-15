#!/bin/python3
"""
Stylus to CSS
	Usage: ./stylus.py
	Test:  ./stylus.py test

Order files by names or MOVE_TO_START
"""
OUTPUT_FILE = 'main.css'
EXTENSION = 'styl'
MOVE_TO_START = ['styl/reset.styl', 'styl/globals.styl', 'styl/colors.styl', 'styl/fonts.styl']

def stylus_to_css(string=''):

	# Remove excess indentation (dedent).
	cursor=0
	indent=''
	while cursor < len(string):
		if string[cursor] == "\n": # Line.
			cursor += 1 # Skip
			continue
		if string[cursor] == "\t" or string[cursor] == " ":
			indent += string[cursor]
			cursor += 1 # Skip
			continue

		string = string.replace("\n"+indent, "\n") # Remove.
		string = string.lstrip("\n").lstrip(indent) # Clean up start.
		break

	# Remove repeat newlines.
	cursor=0
	while cursor < (end := len(string)):
		if string[cursor:cursor+2] == "\n\n":
			cursor_2 = cursor
			while cursor_2 < end and string[cursor_2] == "\n":
				cursor_2 += 1 # Skip
			string = string[0:cursor+1] + string[cursor_2:]
		cursor += 1 # Skip

	# Skip over strings.
	def skip_string(string, cursor, c='"'):
		end = len(string)
		if string[cursor:cursor+1] == c: # Skip string.
			cursor += 1 # Skip
			while cursor < end and (string[cursor] != c or (string[cursor] == c and string[cursor-1] == "\\")):
				cursor += 1 # Skip
		return string, cursor

	# Remove comments /* ... */
	cursor=0
	while cursor < len(string):
		# Skip comments in strings.
		string, cursor = skip_string(string, cursor, "'")
		string, cursor = skip_string(string, cursor, '"')
		if string[cursor:cursor+2] == "/*": # Comment. Remove until newline.
			cursor_2 = cursor+2
			while cursor_2 < (end := len(string)):
				if string[cursor_2:cursor_2+2] == '*/' or cursor_2 > end-2: # Stop comment.
					string = string[0:cursor] + string[cursor_2+2:]
					break
				cursor_2 += 1
		cursor += 1 # Skip

	# Remove comments //
	cursor=0
	while cursor < len(string):
		# Skip comments in strings.
		string, cursor = skip_string(string, cursor, "'")
		string, cursor = skip_string(string, cursor, '"')
		if string[cursor:cursor+2] == "//": # Comment. Remove until newline.
			cursor_2 = cursor+2
			while cursor_2 < len(string):
				if string[cursor_2] == "\n": # Stop comment.
					string = string[0:cursor] + string[cursor_2:]
					break
				cursor_2 += 1
		cursor += 1 # Skip

	# Add curly braces.
	cursor=0
	level_from=0
	level_to=0

	while cursor < len(string):
		if string[cursor] == "\n": # Line.
			level_to = 0
			cursor += 1 # Skip
			continue
		if string[cursor] == "\t": # Indent.
			level_to += 1
			cursor += 1 # Skip
			continue
		while level_to > level_from: # Real start.
			level_from += 1

			# Cursor #2 finds last real character for the insert.
			cursor_2 = cursor-1
			while cursor_2 > 0 and (string[cursor_2] in ["\n", "\t", " "]):
				cursor_2 -= 1
			cursor_2 += 1

			string = string[0:cursor_2] +' { '+ string[cursor_2:]
			cursor += 3 # Skip ' {'
			continue
		while level_from > level_to: # Real start.
			level_from -= 1

			# Cursor #2 finds last real character for the insert.
			cursor_2 = cursor-1
			while cursor_2 > 0 and (string[cursor_2] in ["\n", "\t", " "]):
				cursor_2 -= 1
			cursor_2 += 1

			string = string[0:cursor_2] +' } '+ string[cursor_2:]
			cursor += 3 # Skip '} '
			continue
		cursor += 1 # Skip

	# End of file. Close remaining levels.
	while level_from > 0:
		string += '}'
		level_from -= 1

	def alphanum(c):
		return c.isalpha() or c.isdigit()
		#	return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')

	# Add semicolons.
	cursor=0
	while cursor < len(string):
		if cursor > 3 and string[cursor] == "\n": # Line.
			cursor_2 = cursor-1
			while cursor_2 > 2:
				# Rewind until applicable character.
				if string[cursor_2] == ' ' or string[cursor_2] == "\t" or string[cursor_2] == "}":
					cursor_2 -= 1
					continue
				c = string[cursor_2]
				if c != '{' and c != '}' and c != ';' and (c == "\'" or c == '"' or c == ')' or c == '%' or c == '-' or c == '_' or alphanum(c)):
					string = string[0:cursor_2+1] +';'+ string[cursor_2+1:]
					cursor += 1
				break
		cursor += 1 # Next.

	return string

import sys
if 'test' in sys.argv:
	# Run self test.
	string = """
	/* Account menu */
	.layout
		.account_menu
			color: hsl(0, 0%, 73%)
			text-align: left
			margin-bottom: 20px
		.account_menu_header
			padding: 0px 20px
			font-size: 16px
			margin: 3px 0
			line-height: 40px
			background: hsl(0, 0%, 12%)
			&:first-child
				margin: 0 0 3px 0
		.account_menu_options
			border-radius: 10px
			background: hsl(0, 0%, 9%)
			box-shadow: var(--box_shadow_inset)
		.account_menu_options a
			&:first-child
				border-radius: 10px 10px 0 0
				padding-top: 5px
			&:last-child
				border-radius: 0 0 10px 10px
				padding-bottom: 5px
			&:first-child:last-child
				border-radius: 10px
		.account_menu_options a
			font-size: 14px
			padding: 3px 20px 3px 12px
			line-height: 30px
			display: block
			/*background hsl(0, 0%, 9%) */
			&.active
				color: var(--color_primary)
			&:hover
				color: var(--color_primary)_highlight
			&.default_icon:before
				font-family: var(--font_awesome)
				content: "\f35a"
				display: inline-block
				padding: 0 10px 2px 0
				font-weight: 900
			&.account_menu_games
				&:before
					content: "\f11b"
"""
	print(f"Running test.")
	print(f"{stylus_to_css(string)}")
else:
	#file_out = open(OUTPUT_FILE, 'w')
	#file_out.write('/* Generated by '+sys.argv[0]+' */\n')
	#import atexit; atexit.register(lambda: file_out.close())

	# Sort by directory first, then by filename
	import glob, os
	def sort_by_directory(path):
		directory, filename = os.path.split(path)
		return (directory, filename)
	stylus_files = sorted(list(glob.glob('**/*.'+EXTENSION, recursive=True)), key=sort_by_directory)

	# Move to start of CSS.
	move_to_start = MOVE_TO_START
	for e in list(move_to_start):
		if e in stylus_files:
			stylus_files.remove(e)
		else:
			move_to_start.remove(e)
			print(f"File not found: {e}")
	stylus_files = move_to_start + stylus_files

	# CSS
	for stylus_file in stylus_files:
		print(f"Adding: {stylus_file}")
		file_out = open(str(f"{stylus_file}").replace('.styl', '.css'), 'w')
		file_in = open(f"{stylus_file}", "r")
		string = file_in.read()
		string = stylus_to_css(string)
		file_out.write(f"/* {stylus_file} */\n{string}\n")
		file_in.close()
		file_out.close()

	print("Generated: "+OUTPUT_FILE)
