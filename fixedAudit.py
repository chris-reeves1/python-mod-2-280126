import argparse
import sys
from datetime import datetime, timezone
import re
import uuid
 
OUTPUT_FILE = "stage0_output.txt"
SYSTEM_NAME = "auth_service"
USER_ID_RE = re.compile(r"^user-\d+$")

 
def format_timestamp_utc_z() -> str:
    """UTC timestamp as an ISO-8601 string with Z (Zulu time)."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
 
def default_attempts() -> list[tuple[str, bool]]:
    return [
        ("user-100", True),
        ("user-200", False),
        ("user-100", False),
        ("user-999", True),
    ]
 
def parse_attempt_line(raw: str, line_no: int) -> tuple[str, bool]:
    # Require exactly 2 fields separated by a comma
    if "," not in raw:
        raise ValueError(
            f"Line {line_no}: missing comma (expected: user_id,true|false)"
        )

    user_id, success_raw = [p.strip() for p in raw.split(",", maxsplit=1)]

    if not user_id:
        raise ValueError(f"Line {line_no}: empty user_id")

    if not USER_ID_RE.fullmatch(user_id):
        raise ValueError(
            f"Line {line_no}: invalid user_id {user_id!r} (expected 'user-<digits>')"
        )

    v = success_raw.lower()
    if v not in {"true", "false"}:
        raise ValueError(
            f"Line {line_no}: invalid success value {success_raw!r} (expected true|false)"
        )

    return user_id, (v == "true")

def load_attempts(input_path: str | None) -> list[tuple[str, bool]]:
    """
    If --input is provided, read attempts from file.
    Expected line format: user_id,true|false
    Blank lines and lines starting with # are ignored.
    """
    if input_path is None:
        return default_attempts()
 
    attempts: list[tuple[str, bool]] = []
    errors: list[str] = []

    with open(input_path, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            raw = line.strip()
            if not raw or raw.startswith("#"):
                continue
 
            try:
                attempts.append(parse_attempt_line(raw, line_no))
            except ValueError as e:
                errors.append(str(e))

    if errors:
        raise ValueError("Invalid --input file:\n" + "\n".join(errors))

    return attempts
 
def is_known_user(user_id: str, known_users: set[str]) -> bool:
    return user_id in known_users
 
def build_event_line(user_id: str, success: bool, known: bool) -> str:
    ts = format_timestamp_utc_z()  # per-event timestamp
    outcome = "success" if success else "failure"
    user_status = "known" if known else "unknown"
    event_id = uuid.uuid4().hex
    return (
        f"id={event_id} time={ts} system={SYSTEM_NAME} user_id={user_id} "
        f"user_status={user_status} outcome={outcome}"
    )
 
def write_lines_append_only(path: str, lines: list[str]) -> None:
    # Append-only + context manager
    with open(path, "a", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")  # one event per line
 
def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Stage 0 audit log writer")
    parser.add_argument(
        "--input",
        default=None,
        help="Optional input file (lines: user_id,true|false). If omitted, defaults are used.",
    )
    return parser.parse_args(argv)
 
def next_event_id(path: str) -> int:
    try:
        with open(path, "r", encoding="utf-8") as f:
            return sum(1 for _ in f) + 1
    except FileNotFoundError:
        return 1
 
def main(argv: list[str]) -> None:
    args = parse_args(argv)
 
    known_users = {"user-100", "user-200", "user-300"}

    try:
        attempts = load_attempts(args.input)
    except ValueError as e:
        print(str(e), file=sys.stderr)
        sys.exit(2)

    # start_id = next_event_id(OUTPUT_FILE)
    lines: list[str] = []

    # for event_id, (user_id, success) in enumerate(attempts, start_id):
    for user_id, success in attempts:
        known = is_known_user(user_id, known_users)
        lines.append(build_event_line(user_id, success, known))
 
    write_lines_append_only(OUTPUT_FILE, lines)
    print(f"Wrote {len(lines)} lines to {OUTPUT_FILE}")
 
if __name__ == "__main__":
    main(sys.argv[1:])