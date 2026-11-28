"""Identify qualifiers added to table cells and find their chapter schema evidence."""

from collections import defaultdict
import json
import re

from spec_source import load_json, objects

SUFFIX = re.compile(r"(.+?)\s*\(([^()]+)\)\s*$")
CONDITIONAL = re.compile(r"(?:조건부\s*(?:필수|Required)|(?:필수|Required)\s*\(조건부\))", re.I)
SCHEMA_FENCE = re.compile(r"^\s*(`{3,}|~{3,})\s*json\s*$", re.I)
BOUND = re.compile(r"([≥≤<>]|>=|<=)\s*(-?\d+(?:\.\d+)?)\s*(개)?$")
BOUND_NAMES = {"≥": "minimum", ">=": "minimum", "≤": "maximum", "<=": "maximum",
               ">": "exclusiveMinimum", "<": "exclusiveMaximum"}
SCHEMA_PATH_WORDS = {"properties", "patternProperties", "items", "$defs", "definitions", "allOf", "anyOf", "oneOf",
                     "if", "then", "else", "additionalProperties", "dependentSchemas"}


def requirements(qualifier):
    text = qualifier.strip()
    if text in {"enum", "oneOf", "anyOf", "allOf", "const"}:
        return {text: None}
    if text.startswith("enum:"):
        values = re.findall(r'"([^"\n]+)"', text)
        return {"enum": values} if values else {}
    for prefix, keyword in (("기본 ", "default"), ("const ", "const")):
        if text.startswith(prefix):
            try:
                return {keyword: json.loads(text[len(prefix):])}
            except ValueError:
                return {}
    if match := BOUND.fullmatch(text):
        symbol, value, count = match.groups()
        keyword = BOUND_NAMES[symbol]
        if count:
            keyword = {"minimum": "minItems", "maximum": "maxItems"}.get(keyword)
        return {keyword: json.loads(value)} if keyword else {}
    if match := re.fullmatch(r"길이 (\d+)", text):
        return {"minItems": int(match[1]), "maxItems": int(match[1])}
    if text.isdecimal():
        return {"minLength": int(text), "maxLength": int(text)}
    if match := re.fullmatch(r"(\d+)\s*~\s*(\d+)", text):
        return {"minimum": int(match[1]), "maximum": int(match[2])}
    if match := re.fullmatch(r"(\d+) 초과 (\d+) 이하", text):
        return {"exclusiveMinimum": int(match[1]), "maximum": int(match[2])}
    if text == "0 금지":
        return {"not": {"const": 0}}
    return {}


def schema_support(node, expected):
    for key, value in expected.items():
        if key not in node:
            return False
        if value is None:
            if not node[key] and key != "const":
                return False
        elif key == "enum":
            if set(map(str, node[key])) != set(value):
                return False
        elif isinstance(value, bool):
            if node[key] is not value:
                return False
        elif node[key] != value or isinstance(node[key], bool):
            return False
    return bool(expected)


class ChapterSchemas:
    def __init__(self, lines, scope):
        self.fields = defaultdict(list)
        for n, line in enumerate(lines):
            fence = SCHEMA_FENCE.match(line)
            if not fence or not n or scope[n - 1] is None:
                continue
            headings, _ = scope[n - 1]
            if (not any(level == 2 for level, _, _ in headings[:-1])
                    or not re.search(r"\bJSON Schema\b", lines[headings[-1][2]], re.I)):
                continue
            end = next((i for i in range(n + 1, len(lines)) if lines[i].strip() == fence[1]), len(lines))
            raw, _ = load_json("\n".join(lines[n + 1:end]))
            section = tuple(item[2] for item in headings[:-1])
            for path, obj in objects(raw):
                for key, node in obj.get("properties", {}).items():
                    if isinstance(node, dict):
                        direct = tuple(part for part in path if part not in SCHEMA_PATH_WORDS
                                       and re.fullmatch(r"[A-Za-z][\w-]*", part))
                        self.fields[key].append((section, n + 1, (*direct, key), node))

    def support(self, context, keys, qualifier):
        expected = requirements(qualifier)
        if not expected:
            return []
        section = tuple(item[2] for item in context[0])
        evidence = []
        for key in keys:
            path = tuple(key.split("."))
            candidates = [(scope, line, full, node) for scope, line, full, node in self.fields[path[-1]]
                          if section[:len(scope)] == scope and full[-len(path):] == path]
            depth = max((len(scope) for scope, _, _, _ in candidates), default=0)
            matches = [{"key": key, "line": line, "path": list(full),
                        "schema": {tag: node[tag] for tag in expected}}
                       for scope, line, full, node in candidates if len(scope) == depth and schema_support(node, expected)]
            if not matches:
                return []
            evidence.extend(matches)
        return evidence
