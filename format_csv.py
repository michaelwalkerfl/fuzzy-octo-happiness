import sublime, sublime_plugin

def dedupe(seq):
    present = set()
    present_add = present.add
    return [i for i in seq if i not in present and not present_add(i)]

class FormatFile(sublime_plugin.TextCommand):
    def read_line(self, row):
        view = self.view
        text = view.text(row, 0)
        line = view.line(text)
        return view.substr(line)
