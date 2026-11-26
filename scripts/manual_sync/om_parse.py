"""Parse the official article HTML: the Specifications table as rows. No AI, no network."""
import html
import re

_NO = re.compile(r"^(?:\d+(?:\.\d+)*\.?|\(\d+\)|[ivxIVX]+\.|[a-z]\.?|\([a-z]+\))$")


def cell_text(fragment):
    fragment = re.sub(r"<br\s*/?>", "\n", fragment)
    fragment = re.sub(r"</(p|li|div)>", "\n", fragment)
    return html.unescape(re.sub(r"<[^>]+>", "", fragment)).replace("\xa0", " ").replace("​", "")


def _one_line(lines):
    text = " ".join(x.strip() for x in lines if x.strip())
    text = re.sub(r"\s*•\s*", " · ", text).replace("◦", "/")
    return re.sub(r"\s+", " ", text).strip(" ·")


def spec_rows(body):
    """Rows of the Specifications table as dicts: no, desc, keys, type, default, required, group.

    A row with fewer than five cells is a group heading ("When X is true") and is attached to the
    rows that follow it as ``group``.
    """
    body = re.sub(r"<script.*?</script>|<style.*?</style>", "", body or "", flags=re.S)
    starts = [m.start() for m in re.finditer(r"<h3[^>]*>(?:(?!</h3>).)*?Specifications", body, re.S)]
    if not starts:
        return []
    out, group = [], ""
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", body[starts[-1]:], re.S):
        cells = [[x for x in cell_text(c).split("\n")] for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S)]
        if len(cells) < 5:
            text = _one_line([x for c in cells for x in c])
            if text:
                group = text
            continue
        if _one_line(cells[-4]) == "Key":
            group = ""
            continue
        key_text = _one_line(cells[-4])
        keys = re.findall(r'"\s*([A-Za-z_][A-Za-z0-9_\-]*)\s*"', key_text)
        head = [_one_line(c) for c in cells[:-4]]
        head = [h for h in head if h]
        no = ""
        if head and _NO.match(head[0]) and len(head) > 1:
            no, head = head[0], head[1:]
        elif head and re.match(r"^(\d+\.\d+[\d.]*|[ivx]+\.|\(\d+\))\s", head[0]):
            m = re.match(r"^(\S+)\s+(.*)$", head[0])
            no, head = m.group(1), [m.group(2)] + head[1:]
        out.append({
            "no": no, "desc": " ".join(head), "keys": keys, "key_text": key_text,
            "type": _one_line(cells[-3]), "default": _one_line(cells[-2]), "required": _one_line(cells[-1]),
            "group": group,
        })
    return out


def md_escape(text):
    return text.replace("|", "\\|")
