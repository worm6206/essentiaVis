import sys
import fileinput
import re

from os import walk

for (dirpath, dirnames, filenames) in walk("streaming/"):
	for name in filenames:
		file=""
		with open(dirpath+name) as f:
			file=f.read()

			sys.stdout.write("<tr>\n")
			sys.stdout.write("<th scope=\"row\" class=\"col-xs-1\">\n")

			p = re.compile(ur'<h1 class="title">(.*?)</h1>')
			m = re.search(p, file)
			if m:
				title = m.group(1)
				sys.stdout.write(title)
				sys.stdout.write("<br>[streaming]\n")
			sys.stdout.write("\n</th><td class=\"col-xs-2\">\n")

			p = re.compile(ur'<h2>Inputs</h2>\n<blockquote>\n<ul class="simple">\n((.|\n)*?)\n</ul>')
			m = re.search(p, file)
			if m:
				input_text = m.group(1)
				sys.stdout.write(input_text)
			sys.stdout.write("\n</td><td class=\"col-xs-2\">\n")

			p = re.compile(ur'<h2>Outputs</h2>\n<blockquote>\n<ul class="simple">\n((.|\n)*?)\n</ul>')
			m = re.search(p, file)
			if m:
				output_text = m.group(1)
				sys.stdout.write(output_text)
			sys.stdout.write("\n</td><td class=\"col-xs-2\">\n")

			p = re.compile(ur'<h2>Parameters</h2>\n<blockquote>\n<ul>\n((.|\n)*?)\n</ul>')
			m = re.search(p, file)
			if m:
				param_text = m.group(1)
				sys.stdout.write(param_text)
			sys.stdout.write("\n</td><td class=\"col-xs-5\">\n")

			p = re.compile(ur'<div class="section" id="description">\n<h2>Description</h2>\n((.|\n)*?)\n</div>')
			m = re.search(p, file)
			if m:
				descript_text = m.group(1)
				sys.stdout.write(descript_text)
			sys.stdout.write("\n</td></tr>\n")