# ---------------------------------------------------------------------------- #
# paramorse.utils.render
# ---------------------------------------------------------------------------- #

import os
import logging
import textwrap
import difflib

from typing import Any 
from pprint import PrettyPrinter

from paramorse.utils.paths import get_data_dirs

# IPython is optional
# try to import and if unavailable, fall back at call sites

try:
    from IPython.display import Markdown as _IPy_Markdown
    from IPython.display import display as _IPy_display
    _HAS_IPYTHON = True
except Exception:
    _IPy_Markdown = None
    _IPy_display = None
    _HAS_IPYTHON = False


logger = logging.getLogger(__name__)

_DATADIRS: dict[str, dict]=get_data_dirs()

_pp = PrettyPrinter(
    indent=2,
    width=80,
    compact=True,
    # compact=False,
    # sort_dicts=True,
    sort_dicts=False,
)

_MAX_TABLE_WIDTH = 140

_MAX_PRINT_LEN = 650




# PRINT & FORMAT

def trunc_str(text: str, max_char: None | int=_MAX_PRINT_LEN):

    truncated = False
    
    if max_char is not None and len(text) > max_char:
        text = text[:max_char]
        truncated = True

    if truncated and text:
        text = text + " ..."

    return text


def pm_pformat(input: Any):
    return _pp.pformat(input)


def pm_pprint(input: Any):
    return _pp.pprint(input)




# TEXT COMPARE

def text_compare_html_diff(
        expected_string: str,
        actual_string: str,
        compare_filepath: str | None=None,
        test_data_subdir: str = "",
        test_compare_filename: str = 'text_compare.html',
    ) -> bool:

    # make into lists
    expected_lines = expected_string.splitlines()
    actual_lines = actual_string.splitlines()

    # compare
    # text_differ = difflib.Differ()
    # diff = text_differ.compare(expected_string, actual_string)
   
    html_diff = difflib.HtmlDiff(wrapcolumn=60).make_file(
        expected_lines,
        actual_lines
        )
    
    if(compare_filepath is not None):
        resolve_compare_path = os.path.abspath(compare_filepath)
    else:
        resolve_compare_path = f"{_DATADIRS['paths_string']['test']}/{test_data_subdir}/{test_compare_filename}"

    with open(f'{resolve_compare_path}', 'w') as f:        
        f.write(html_diff)

    if os.path.isfile(resolve_compare_path):
        return True
    else:
        return False




# MARKDOWN TABLES
# TODO types

def md_table_build(
    rows,
    columns,
    justify=None,
    # *,
    col_min_widths=None,
    table_max_width : None | int=_MAX_TABLE_WIDTH,
    target="terminal",  # "terminal" or "notebook"
):
    """
    Build a Markdown table string (pipes).

    Parameters
    ----------
    rows : list[dict|sequence]
        - Preferred (concise): list of sequences, each aligned by position to `columns`.
          Example: rows = [['config', config], ['cover', cover]]
        - Back-compat: list of dicts mapping column -> value.
    columns : list[str]
        Column headers (order defines column order).
    justify : list[str] | None
        One per column in {'left','center','right'} (or 'l','c','r'). Defaults to all 'left'.
    col_min_widths : None | int | list[int] | dict[str,int]
        Minimum content width per column (hard lower bound). If dict, keys are headers.
    table_max_width : int | None
        If int, maximum overall row width (including pipes/spaces). Cells are **wrapped** to fit.
        If None, no cap is enforced.
    target : "notebook" | "terminal"
        - notebook: HTML-escaped, line breaks become <br>
        - terminal: raw Markdown, wrapped cells emit **additional table rows**, padded to width
    """

    # ---------------- helpers (target-agnostic) ----------------
    def _norm_justify(just):
        if just is None:
            return ["unspec"] * len(columns)
        if len(just) != len(columns):
            raise ValueError("justify must have the same length as columns")
        out = []
        for j in just:
            jj = str(j).lower()
            if jj in ("u","unspec","unspecified"): out.append("unspec")
            elif jj in ("l","left"): out.append("left")
            elif jj in ("c","center","centre","middle"): out.append("center")
            elif jj in ("r","right"): out.append("right")
            else:
                raise ValueError(f"invalid justify value: {j!r}; use unspec/left/center/right")
        return out

    def _norm_min_widths(mcw):
        if mcw is None:
            return [0] * len(columns)
        if isinstance(mcw, int):
            return [max(0, mcw)] * len(columns)
        if isinstance(mcw, list):
            if len(mcw) != len(columns):
                raise ValueError("col_min_widths list must match len(columns)")
            return [max(0, int(v)) for v in mcw]
        if isinstance(mcw, dict):
            return [max(0, int(mcw.get(c, 0))) for c in columns]
        raise ValueError("col_min_widths must be None, int, list[int], or dict[str,int]")

    def _wrap_text(raw, width):
        """Wrap raw text to width; returns '\\n'-joined lines (no escaping)."""
        if width <= 0:
            return ""
        s = "" if raw is None else str(raw)
        s = s.replace("\r\n", "\n").replace("\r", "\n")
        out = []
        for part in s.split("\n"):
            wrapped = textwrap.wrap(
                part,
                width=width,
                break_long_words=True,
                break_on_hyphens=True,
                replace_whitespace=False,
                drop_whitespace=False,
            )
            if not wrapped:
                out.append("")
            else:
                out.extend(wrapped)
        return "\n".join(out)

    # Normalize rows to a list-of-lists aligned with columns (backward compatible)
    def _normalize_rows(rows, columns):
        norm = []
        for r_idx, row in enumerate(rows):
            if isinstance(row, dict):
                norm.append([row.get(c, "") for c in columns])
            else:
                try:
                    seq = list(row)
                except TypeError:
                    raise ValueError(f"Row {r_idx} is neither dict nor sequence")
                if len(seq) < len(columns):
                    seq = seq + [""] * (len(columns) - len(seq))
                elif len(seq) > len(columns):
                    # Stricter here to avoid silent misalignment
                    raise ValueError(
                        f"Row {r_idx} has {len(seq)} cells; expected {len(columns)}"
                    )
                norm.append(seq)
        return norm

    # ---------------- target-specific helpers ----------------
    tgt = str(target).lower()
    if tgt not in ("notebook", "terminal"):
        raise ValueError("target must be 'notebook' or 'terminal'")

    def _visible_len_notebook(x):
        s = "" if x is None else str(x)
        return len(s.replace("\n", " "))

    def _visible_len_terminal(x):
        s = "" if x is None else str(x)
        s = s.replace("|", "\\|")
        return len(s.replace("\n", " "))

    def _escape_for_notebook(s):
        # Escape &, <, >; escape '|'; newline -> <br>
        s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        s = s.replace("|", "\\|")
        return s.replace("\n", "<br>")

    def _escape_for_terminal(s):
        # Only escape pipes; keep real newlines
        return s.replace("|", "\\|")

    def _align_token(j):
        return {"unspec": "---", "left": ":---", "center": ":---:", "right": "---:"}[j]

    def _sep_token_terminal(width, j):
        w = max(3, int(width))
        if j == "unspec":
            return "-" + "-"*(w-1)
        if j == "left":
            return ":" + "-"*(w-1)
        elif j == "right":
            return "-"*(w-1) + ":"
        else:
            return ":" + "-"*max(1, w-2) + ":"

    def _pad_align(s, width, j):
        n = len(s)
        if n >= width:
            return s
        if j == "right":
            return " "*(width - n) + s
        if j == "center":
            left = (width - n) // 2
            right = width - n - left
            return " "*left + s + " "*right
        return s + " "*(width - n)

    # ---------------- normalize inputs ----------------
    N = len(columns)
    justify = _norm_justify(justify)
    min_widths = [max(1, w) for w in _norm_min_widths(col_min_widths)]  # >=1

    # Normalize rows to matrix (list of lists)
    rows_mat = _normalize_rows(rows, columns)

    # choose vlen based on target
    vlen = _visible_len_notebook if tgt == "notebook" else _visible_len_terminal

    # measure content
    header_vis = [vlen(h) for h in columns]
    body_max = [0] * N
    for row in rows_mat:
        for i in range(N):
            body_max[i] = max(body_max[i], vlen(row[i]))

    # initial widths
    widths = [max(header_vis[i], body_max[i], min_widths[i]) for i in range(N)]

    # enforce overall cap if set
    if table_max_width is not None:
        non_content_extra = 3 * N + 1  # "| " + " | ".join(cells) + " |"
        content_budget = max(0, table_max_width - non_content_extra)
        # terminal: don't shrink below header_vis (single-line header)
        low_bounds = (
            min_widths[:] if tgt == "notebook"
            else [max(min_widths[i], header_vis[i]) for i in range(N)]
        )
        over = sum(widths) - content_budget
        if over > 0 and N > 0:
            while over > 0:
                reducible = [i for i in range(N) if widths[i] > low_bounds[i]]
                if not reducible:
                    break
                share = max(1, over // len(reducible))
                changed = False
                for i in reducible:
                    dec = min(share, widths[i] - low_bounds[i])
                    if dec > 0:
                        widths[i] -= dec
                        over -= dec
                        changed = True
                    if over <= 0:
                        break
                if not changed:
                    for i in reducible:
                        if widths[i] > low_bounds[i] and over > 0:
                            widths[i] -= 1
                            over -= 1
                    if over > 0 and all(widths[i] == low_bounds[i] for i in range(N)):
                        break

    # ---------------- build ----------------
    if tgt == "notebook":
        # Header (wrapped; HTML-escaped; <br> for newlines)
        hdr_cells = []
        for i, c in enumerate(columns):
            wrapped = _wrap_text(c, widths[i])
            hdr_cells.append(_escape_for_notebook(wrapped))
        header = "| " + " | ".join(hdr_cells) + " |"

        # Alignment row
        sep = "| " + " | ".join(_align_token(j) for j in justify) + " |"

        # Body
        body_lines = []
        for r in rows_mat:
            cells = []
            for i in range(N):
                wrapped = _wrap_text(r[i], widths[i])
                cells.append(_escape_for_notebook(wrapped))
            body_lines.append("| " + " | ".join(cells) + " |")
            # body_lines.append("| ```" + "``` | ```".join(cells) + "``` |")

        return "\n".join([header, sep] + body_lines)

    # ----- terminal path -----
    # Single-line header (replace header newlines with spaces)
    term_hdr_cells = []
    for i, c in enumerate(columns):
        raw = "" if c is None else str(c)
        raw = raw.replace("\r\n", "\n").replace("\r", "\n").replace("\n", " ")
        cell = _escape_for_terminal(raw)
        term_hdr_cells.append(_pad_align(cell, widths[i], justify[i]))
    header = "| " + " | ".join(term_hdr_cells) + " |"

    # Alignment row sized to final widths
    sep = "| " + " | ".join(_sep_token_terminal(widths[i], justify[i]) for i in range(N)) + " |"

    # Body rows: wrap each cell to width; emit as multiple physical rows; pad each segment
    body_lines = []
    for r in rows_mat:
        col_lines = []
        max_h = 0
        for i in range(N):
            esc = _escape_for_terminal("" if r[i] is None else str(r[i]))
            wrapped = _wrap_text(esc, widths[i])
            lines = wrapped.split("\n") if wrapped else [""]
            max_h = max(max_h, len(lines))
            col_lines.append(lines)

        for k in range(max_h):
            row_cells = []
            for i in range(N):
                seg = col_lines[i][k] if k < len(col_lines[i]) else ""
                row_cells.append(_pad_align(seg, widths[i], justify[i]))
            body_lines.append("| " + " | ".join(row_cells) + " |")

    return "\n".join([header, sep] + body_lines)


def md_table(
    rows,
    columns = ['Item', 'Value'],
    justify = ['left', 'left'],
    # *,
    col_min_widths = [13, 13],
    table_max_width : None | int=_MAX_TABLE_WIDTH,
):
    
    if not _HAS_IPYTHON:
        # Fallback: produce terminal/raw Markdown string
        return md_table_str(
            rows=rows, columns=columns, justify=justify,
            col_min_widths=col_min_widths,
            table_max_width=table_max_width,
        )
    
    # IPython present: build notebook-flavored table and wrap in Markdown
    if _IPy_Markdown is not None:
        """Notebook-friendly: returns IPython.display.Markdown"""
        return _IPy_Markdown(md_table_build(
            rows=rows, columns=columns, justify=justify,
            col_min_widths=col_min_widths,
            table_max_width=table_max_width,
            target="notebook",
        ))


def md_table_str(
    rows,
    columns = ['Item', 'Value'],
    justify = ['unspec', 'unspec'],
    # *,
    col_min_widths = [13, 13],
    table_max_width : None | int=_MAX_TABLE_WIDTH,
):
    """Terminal/raw: returns a Markdown string suitable for printing"""
    return md_table_build(
        rows, columns, justify,
        col_min_widths=col_min_widths,
        table_max_width=table_max_width,
        target="terminal",
    )


def display_md_table(
    rows,
    columns = ['Item', 'Value'],
    justify = ['left', 'left'],
    # *,
    col_min_widths = [13, 13],
    table_max_width : None | int=_MAX_TABLE_WIDTH,
):
    if not _HAS_IPYTHON:
        # Fallback: print the terminal-friendly Markdown string
        return print_md_table_str(
            rows=rows, columns=columns, justify=justify,
            col_min_widths=col_min_widths,
            table_max_width=table_max_width,
        )
    # IPython present
    if _IPy_display is not None:
        return _IPy_display(md_table(
            rows=rows, columns=columns, justify=justify,
            col_min_widths=col_min_widths,
            table_max_width=table_max_width,
        ))


def print_md_table_str(
        rows,
        columns = ['Item', 'Value'],
        justify = ['unspec', 'unspec'],
        # *,
        col_min_widths = [13, 13],
        table_max_width : None | int=_MAX_TABLE_WIDTH,
    ):

    return print(md_table_str(
        rows=rows, columns=columns, justify=justify,
        col_min_widths=col_min_widths,
        table_max_width=table_max_width,
    ))