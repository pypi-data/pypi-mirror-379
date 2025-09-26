#!/usr/bin/env python3
import sys
import re
from typing import List, Tuple, Optional

# ---------- Forward-decl parsing & sorting ----------

DECL_RE = re.compile(
    r"""
    ^(?P<indent>[ \t]*)                     # leading indentation
    (?P<kind>class|struct|enum\s+class)     # kind
    \s+
    (?P<name>[A-Za-z_]\w*(?:::[A-Za-z_]\w*)*) # qualified identifier
    \s*;                                    # semicolon
    (?P<after>\s*(?://[^\r\n]*)?)           # optional trailing comment/whitespace
    (?P<eol>\r?\n|\r)?$                     # original line ending
    """,
    re.VERBOSE,
)

KindRank = {"class": 0, "struct": 1, "enum class": 2}


def parse_decl_line(line: str):
    m = DECL_RE.match(line)
    if not m:
        return None
    d = m.groupdict()
    return {
        "indent": d["indent"] or "",
        "kind": d["kind"],
        "name": d["name"],
        "after": d["after"] or "",
        "eol": d["eol"] if d["eol"] is not None else "",
        "orig": line,
    }


def render_decl(indent: str, kind: str, name: str, after: str, eol: str) -> str:
    return f"{indent}{kind} {name};{after}{eol}"


def sort_block(decls: List[dict], indent_for_block: str) -> List[str]:
    if indent_for_block is None and decls:
        indent_for_block = decls[0]["indent"]

    def key(d):
        return (KindRank.get(d["kind"], 99), d["name"].casefold(), d["name"])

    decls_sorted = sorted(decls, key=key)
    return [
        render_decl(indent_for_block, d["kind"], d["name"], d["after"], d["eol"])
        for d in decls_sorted
    ]


def process_full_text(text: str) -> str:
    """Sort all contiguous forward-decl blocks in the entire text."""
    lines = text.splitlines(keepends=True)
    out: List[str] = []
    i = 0
    n = len(lines)

    while i < n:
        parsed = parse_decl_line(lines[i])
        if not parsed:
            out.append(lines[i])
            i += 1
            continue

        # Collect contiguous decl lines until a blank or non-decl
        j = i
        decls: List[dict] = []
        while j < n:
            line = lines[j]
            if line.strip() == "":
                break
            p = parse_decl_line(line)
            if p:
                decls.append(p)
                j += 1
                continue
            break

        out.extend(
            sort_block(decls, indent_for_block=decls[0]["indent"] if decls else "")
        )
        i = j

        # Preserve a single blank line right after the block (if present)
        if i < n and lines[i].strip() == "":
            out.append(lines[i])
            i += 1

    return "".join(out)


# ---------- Offset/length handling (byte-based, UTF-8 safe) ----------


def parse_selection_ranges(argv: List[str]) -> List[Tuple[int, int]]:
    """
    Parse --offset / --length pairs (supports --offset=N --length=M or --offset N --length M).
    Returns a list of (byte_offset, byte_length). Ignores extra args.
    """
    ranges: List[Tuple[int, int]] = []
    i = 0
    pending_offset: Optional[int] = None
    pending_length: Optional[int] = None

    def maybe_emit():
        nonlocal pending_offset, pending_length
        if pending_offset is not None and pending_length is not None:
            ranges.append((pending_offset, pending_length))
            pending_offset = None
            pending_length = None

    while i < len(argv):
        a = argv[i]
        if a.startswith("--offset="):
            pending_offset = int(a.split("=", 1)[1])
        elif a == "--offset" and i + 1 < len(argv):
            i += 1
            pending_offset = int(argv[i])
        elif a.startswith("--length="):
            pending_length = int(a.split("=", 1)[1])
        elif a == "--length" and i + 1 < len(argv):
            i += 1
            pending_length = int(argv[i])
        # else: ignore other args
        maybe_emit()
        i += 1

    # In case offset/length appear at the very end
    maybe_emit()
    return ranges


def byte_to_char_index(text: str, byte_pos: int) -> int:
    """
    Map a byte offset (UTF-8) to a character index in 'text'.
    We decode only complete chars up to byte_pos, ignoring a partial trailing char if present.
    """
    b = text.encode("utf-8", errors="surrogatepass")
    if byte_pos <= 0:
        return 0
    if byte_pos >= len(b):
        return len(text)
    return len(b[:byte_pos].decode("utf-8", errors="ignore"))


def char_span_from_byte_span(text: str, b_off: int, b_len: int) -> Tuple[int, int]:
    start_c = byte_to_char_index(text, b_off)
    end_c = byte_to_char_index(text, b_off + b_len)
    return start_c, end_c


def expand_to_full_lines(text: str, start_c: int, end_c: int) -> Tuple[int, int]:
    """Expand [start_c, end_c) to encompass whole lines (for clean declaration sorting)."""
    # Move start to previous newline+1
    ls = text.rfind("\n", 0, start_c)
    if ls == -1:
        start_c2 = 0
    else:
        start_c2 = ls + 1

    # Move end to next newline end (include newline if present)
    le = text.find("\n", end_c)
    if le == -1:
        end_c2 = len(text)
    else:
        end_c2 = le + 1
    return start_c2, end_c2


def process_with_ranges(text: str, ranges_bytes: List[Tuple[int, int]]) -> str:
    """Apply sorting only inside the given byte ranges (each expanded to full lines)."""
    if not ranges_bytes:
        return process_full_text(text)

    # Process right-to-left so earlier indices remain valid
    result = text
    for b_off, b_len in sorted(ranges_bytes, key=lambda t: t[0], reverse=True):
        start_c, end_c = char_span_from_byte_span(result, b_off, b_len)
        start_c, end_c = expand_to_full_lines(result, start_c, end_c)

        segment = result[start_c:end_c]
        processed = process_full_text(segment)
        result = result[:start_c] + processed + result[end_c:]
    return result


# ---------- Main ----------


def main():
    data = sys.stdin.buffer.read()

    # Decode as UTF-8 (most C++ codebases).
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        text = data.decode("utf-8", errors="surrogatepass")

    ranges = parse_selection_ranges(sys.argv[1:])
    out_text = process_with_ranges(text, ranges)

    sys.stdout.buffer.write(out_text.encode("utf-8"))


if __name__ == "__main__":
    main()
