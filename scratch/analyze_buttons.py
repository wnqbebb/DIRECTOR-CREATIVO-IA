import html.parser

class Parser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        
    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        classes = attr_dict.get('class', '').split()
        self.stack.append((tag, attr_dict, classes))
        if tag == 'button':
            ancestors = []
            for ptag, pattr, pclasses in reversed(self.stack[:-1]):
                ancestors.append(f"{ptag}." + ".".join(pclasses))
            print(f"Button: {classes} | Ancestors: {' -> '.join(ancestors)}")
            
    def handle_endtag(self, tag):
        if self.stack:
            self.stack.pop()

parser = Parser()
with open('biblioteca-de-prompts.html', 'r', encoding='utf-8') as f:
    parser.feed(f.read())
