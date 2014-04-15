import sublime, sublime_plugin

def dedupe(seq):
    present = set()
    present_add = present.add
    return [i for i in seq if i not in present and not present_add(i)]

class FormatFile(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        region = Region(0L, view.size())
        original = StringIO(view.substr(region))
        new = StringIO() + ",,"
        view.replace(edit, region, new.getvalue())
