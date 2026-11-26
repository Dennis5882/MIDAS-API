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


def spec_rows(body, *, scoped_groups=False):
    """Rows of the Specifications table as dicts: no, desc, keys, type, default, required, group.

    A row with fewer than five cells is a group heading ("When X is true") and is attached to the
    rows that follow it as ``group``. With scoped_groups, nested headings end at the
    enclosing rowspan and keys starting with a digit are also recognized.
    """
    body = re.sub(r"<script.*?</script>|<style.*?</style>", "", body or "", flags=re.S)
    starts = [m.start() for m in re.finditer(r"<h3[^>]*>(?:(?!</h3>).)*?Specifications", body, re.S)]
    if not starts:
        return []
    out, group = [], ""
    groups, active_spans = {}, []
    # from the first Specifications heading on, so an article with two tables (e.g. Static Earth
    # Pressure) yields the rows of both
    for index, tr in enumerate(re.findall(r"<tr[^>]*>(.*?)</tr>", body[starts[0]:], re.S)):
        raw_cells = re.findall(r"<t[dh]\b([^>]*)>(.*?)</t[dh]>", tr, re.S)
        cells = [cell_text(c).split("\n") for _, c in raw_cells]
        if scoped_groups:
            active_spans = [end for end in active_spans if end > index]
            groups = {end: label for end, label in groups.items() if end is None or end > index}
        if len(cells) < 5:
            text = _one_line([x for c in cells for x in c])
            if text:
                group = text
                if scoped_groups:
                    scope = min(active_spans, default=None)
                    groups[scope] = text
            continue
        if _one_line(cells[-4]) == "Key":
            group = ""
            groups.clear()
            active_spans.clear()
            continue
        key_text = _one_line(cells[-4])
        key_start = "[A-Za-z0-9_]" if scoped_groups else "[A-Za-z_]"
        keys = re.findall(r'"\s*(' + key_start + r'[A-Za-z0-9_\-]*)\s*"', key_text)
        head = [_one_line(c) for c in cells[:-4]]
        head = [h for h in head if h]
        no = ""
        if head and _NO.match(head[0]) and len(head) > 1:
            no, head = head[0], head[1:]
        elif head and re.match(r"^(\d+\.\d+[\d.]*|[ivx]+\.|\(\d+\))\s", head[0]):
            m = re.match(r"^(\S+)\s+(.*)$", head[0])
            no, head = m.group(1), [m.group(2)] + head[1:]
        if scoped_groups:
            scope = min((end for end in groups if end is not None), default=None)
            group = groups.get(scope, "")
            first_cell_span = re.search(r"""\browspan\s*=\s*["']?(\d+)""", raw_cells[0][0])
            if first_cell_span and len(cells) >= 6 and no:
                end = index + int(first_cell_span.group(1))
                if end > index + 1:
                    active_spans.append(end)
                    # A condition immediately before a merged object covers that object.
                    if not active_spans[:-1] and scope is None and group.startswith("When "):
                        groups.pop(None)
                        groups[end] = group
        out.append({
            "no": no, "desc": " ".join(head), "keys": keys, "key_text": key_text,
            "type": _one_line(cells[-3]), "default": _one_line(cells[-2]), "required": _one_line(cells[-1]),
            "group": group,
        })
    return out


def md_escape(text):
    return text.replace("|", "\\|")
