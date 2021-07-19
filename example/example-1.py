import transparentwindow as tw

tw.SetProcessDpiAwarenessContext()
tw.show(callback=lambda key: print(key, chr(key)))
