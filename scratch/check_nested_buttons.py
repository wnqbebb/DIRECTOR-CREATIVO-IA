import html.parser

class Parser(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.targets = []
        
    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        classes = attr_dict.get('class', '').split()
        is_target = tag in ['pre', 'code'] or any(c in ['prompt-text', 'copy-target'] for c in classes)
        self.stack.append((tag, attr_dict, classes, is_target))
        
    def handle_endtag(self, tag):
        if self.stack:
            tag, attr_dict, classes, is_target = self.stack.pop()
            if is_target:
                # We finished a target element. Check if we found a button inside it.
                # Since we parse sequentially, if a button starts while is_target is active on stack, we would know.
                pass

# Let's do a simpler traversal with html.parser
class NestedButtonChecker(html.parser.HTMLParser):
    def __init__(self):
        super().__init__()
        self.active_targets = []
        
    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        classes = attr_dict.get('class', '').split()
        
        # Check if we are starting a button inside an active target
        if tag == 'button' or 'copy-btn' in classes:
            if self.active_targets:
                print(f"CRITICAL: Found button {tag} with classes {classes} inside target(s): {self.active_targets}")
                
        is_target = tag in ['pre', 'code'] or any(c in ['prompt-text', 'copy-target'] for c in classes)
        if is_target:
            self.active_targets.append((tag, classes))
            
    def handle_endtag(self, tag):
        # Remove from active targets if we are ending a target
        # Since tags are nested, if the ended tag is a target, it should match the last one in active_targets
        if self.active_targets:
            last_tag, last_classes = self.active_targets[-1]
            if last_tag == tag:
                self.active_targets.pop()

checker = NestedButtonChecker()
with open('biblioteca-de-prompts.html', 'r', encoding='utf-8') as f:
    checker.feed(f.read())
print("Nested button check complete.")
