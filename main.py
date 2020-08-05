import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import sys
import gravit

app = gravit.Launcher()
try:
    if sys.argv[1] == "--simulation":
        app.askplay()
    else:
        app.mainloop()
except IndexError:
    app.mainloop()
