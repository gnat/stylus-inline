string = """
			html
				font-family: Noto Sans, sans-serif
			h1, h2, h3
				font-size: 3rem
				margin: 10px
			.me
				border: none
				color: black
				font-family: Noto Sans, sans-serif
				background: hsl(100 20% 70%)
				border: none
				border-radius: 12px
				box-shadow: 2px 2px 5px #00000044
				padding: 10px 20px
				color: #222
				margin: 20px
				animation: bounce 4s ease-in-out infinite
				& span
					background: hsl(200 50% 70%)
					padding: 12px
					border-radius: 4px
					color: #fff
				& ::before
					content:'🔮'
					padding: 0 4px 0 0
				.me
					li
						list-style: disc
						padding: 4px
						border-radius: 12px
						margin: 4px 20px
			@keyframes bounce
				0%
					transform: translateY(0px)
				50%
					transform: translateY(20px)
				100%
					transform: translateY(0px)
"""


cursor=0

# Remove excess indentation (dedent).
indent=''
while cursor < len(string):
	if string[cursor] == "\n": # Line.
		cursor += 1 # Next.
		continue
	if string[cursor] == "\t" or string[cursor] == " ":
		indent += string[cursor]
		cursor += 1 # Next.
		continue
	string = string.replace("\n"+indent, "\n") # Remove.
	break

# Add curly braces.
level_from=0
level_to=0

while cursor < len(string):
	if string[cursor] == "\n": # Line.
		level_to = 0
		cursor += 1 # Next.
		continue
	if string[cursor] == "\t": # Indent.
		level_to += 1
		cursor += 1 # Next.
		continue
	while level_to > level_from: # Real start.
		level_from += 1

		# Cursor #2 finds last real character for the insert.
		cursor_2 = cursor-1
		while cursor_2 > 0 and (string[cursor_2] in ["\n", "\t", " "]):
			cursor_2 -= 1
		cursor_2 += 1

		string = string[0:cursor_2] +' {'+ string[cursor_2:]
		cursor += 2 # Skip ' {'
		#cursor += 1 # Next.
		continue
	while level_from > level_to: # Real start.
		level_from -= 1

		# Cursor #2 finds last real character for the insert.
		cursor_2 = cursor-1
		while cursor_2 > 0 and (string[cursor_2] in ["\n", "\t", " "]):
			cursor_2 -= 1
		cursor_2 += 1

		string = string[0:cursor_2] +'} '+ string[cursor_2:]
		cursor += 2 # Skip '} '
		#cursor += 1 # Next.
		continue
	cursor += 1 # Next.

# End of file. Close remaining levels.
while level_from > 0:
	string += '}'
	level_from -= 1

#def alphanum(c)
#	return (c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z') || (c >= '0' && c <= '9')

# Add semicolons.
cursor=0
while cursor < len(string):
	if string[cursor] == "\n": # Line.
		if cursor > 2: # Should we add a semicolon?
			c = string[cursor-1]
			if c != '{' and c != '}' and (c == "\'" or c == '"' or c == ')' or c == '-' or c == '_' or c.isalnum()):
				string = string[0:cursor] +';'+ string[cursor:]
	cursor += 1 # Next.

print(string)
