# mycheckpkg/checker.py
#!/usr/bin/env python3
import json
import re
from typing import Any, Tuple
import argparse
import sys

def traverse_path(data: Any, path_segments: list) -> Tuple[bool, Any]:
    # (তোমার একই ফাংশন এখানে রাখো)
    cur = data
    for seg in path_segments:
        if isinstance(cur, dict):
            if seg in cur:
                cur = cur[seg]; continue
            if seg.isdigit() and seg in cur:
                cur = cur[seg]; continue
            return False, cur
        elif isinstance(cur, list):
            if re.fullmatch(r"-?\d+", seg):
                idx = int(seg)
                if -len(cur) <= idx < len(cur):
                    cur = cur[idx]; continue
                else:
                    return False, cur
            else:
                found = False
                for item in cur:
                    if isinstance(item, dict) and seg in item:
                        cur = item[seg]; found = True; break
                if found:
                    continue
                else:
                    return False, cur
        else:
            return False, cur
    return True, cur

def check(json_path: str, key_path: str, password: str) -> int:
    # (তোমার একই check ফাংশন, কিন্তু print শেষে exit কোড রিটার্ন করো)
    try:
        with open(json_path, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File not found: {json_path}")
        return 2

    try:
        data = json.loads(content)
    except json.JSONDecodeError:
        data = None

    path_segments = [seg for seg in key_path.split("/") if seg != ""]

    if data is not None:
        ok, value = traverse_path(data, path_segments)
        if ok:
            if isinstance(value, (dict, list)):
                print(f"Path found but final node is a {type(value).__name__}.")
                print("Final node (repr):", repr(value))
                print("Cannot directly compare to password string.")
                return 1
            else:
                if str(value) == password:
                    print("MATCH: provided password matches the value at the given path.")
                    return 0
                else:
                    print("NO MATCH: value at path does not equal provided password.")
                    print("Value at path (repr):", repr(value))
                    return 1

    last_seg = path_segments[-1] if path_segments else ""
    esc_pw = re.escape(password)
    pattern_key_value = re.compile(r'["\']?' + re.escape(last_seg) + r'["\']?\s*[:=]\s*["\']?' + esc_pw + r'["\']?', re.IGNORECASE)
    if pattern_key_value.search(content):
        print("MATCH (fallback): found key+value pattern in file text for last path segment.")
        return 0
    if key_path in content and esc_pw in content:
        print("POSSIBLE MATCH (fallback): both path string and password string occur in file text.")
        return 0
    if re.search(esc_pw, content):
        print("PASSWORD FOUND IN FILE (fallback): the password string appears somewhere in the file,")
        print("but the exact structured path could not be traversed (malformed JSON or path missing).")
        return 0

    print("NOT FOUND: password not found at the given path nor in the file.")
    return 1

def main(argv=None):
    p = argparse.ArgumentParser(prog="mycheck", description="Check password at JSON path")
    p.add_argument("json_path", help="Path to JSON/text file")
    p.add_argument("key_path", help="Slash-separated key path, e.g. 'a/b/0/c'")
    p.add_argument("password", help="Password string to check")
    args = p.parse_args(argv)
    rc = check(args.json_path, args.key_path, args.password)
    sys.exit(rc)

if __name__ == "__main__":
    main()
