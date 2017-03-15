# Note: this file should be placed in /cgi-bin/
# To start a builtin CGI server: 'python -m http.server 8000 --cgi'

import os
import cgi

print("Content-type: text/html")
print()

print("<h3>Input</h3>")
form = cgi.FieldStorage()
for f in form:
    print("<b>{}</b>: {}</br>".format(f, form.getvalue(f)))

print("<h3>Environment</h3>")
for param in os.environ.keys():
    print("<b>{}</b>: {}</br>".format(param, os.environ[param]))
