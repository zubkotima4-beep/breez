from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote
import re

ROOT = Path(__file__).resolve().parent.parent
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class Checker(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.path = path
        self.stack = []
        self.errors = []
        self.ids = []
        self.links = []
        self.images = []
        self.copy_targets = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "a" and attrs.get("href"):
            self.links.append(attrs["href"])
        if tag == "img" and attrs.get("src"):
            self.images.append(attrs["src"])
        if attrs.get("data-copy", "").startswith("#"):
            self.copy_targets.append(attrs["data-copy"][1:])
        if tag not in VOID:
            self.stack.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append(f"extra </{tag}> at {self.getpos()}")
            return
        if self.stack[-1][0] == tag:
            self.stack.pop()
        else:
            self.errors.append(f"mismatch </{tag}> at {self.getpos()}, open {self.stack[-1]}")
            # try to recover
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    del self.stack[i:]
                    break


def local_path(value):
    if not value or value.startswith(("http://", "https://", "mailto:", "tel:", "#", "javascript:")):
        return None
    value = value.split("#")[0].split("?")[0]
    if not value:
        return None
    return ROOT / unquote(value)


def main():
    problems = 0
    for path in sorted(ROOT.glob("*.html")):
        text = path.read_text(encoding="utf-8")
        checker = Checker(path)
        checker.feed(text)
        if checker.stack:
            checker.errors.append(f"unclosed: {checker.stack[-4:]}")
        if checker.errors:
            problems += len(checker.errors)
            print(f"\n{path.name}:")
            for err in checker.errors:
                print("  ", err)
        if len(checker.ids) != len(set(checker.ids)):
            dupes = sorted({x for x in checker.ids if checker.ids.count(x) > 1})
            problems += len(dupes)
            print(f"\n{path.name}: duplicate ids {dupes}")
        for target in checker.copy_targets:
            if target not in checker.ids:
                problems += 1
                print(f"{path.name}: missing copy target #{target}")
        for link in checker.links:
            p = local_path(link)
            if p and not p.exists():
                problems += 1
                print(f"{path.name}: broken link {link}")
        for image in checker.images:
            p = local_path(image)
            if p and not p.exists():
                problems += 1
                print(f"{path.name}: missing image {image}")
    print(f"\nChecked {len(list(ROOT.glob('*.html')))} pages, problems: {problems}")


if __name__ == "__main__":
    main()
