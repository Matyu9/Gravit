import os; os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"  # to hide the "Hello from the pygame community" message
import sys
import gravit

app = gravit.Launcher()
if len(sys.argv) > 1:
    if sys.argv[1] == "--simulation":
        app.askplay()
    else:
        app.mainloop()
else:
    app.mainloop()
