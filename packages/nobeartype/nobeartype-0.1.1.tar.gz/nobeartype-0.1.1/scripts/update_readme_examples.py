from __future__ import annotations

import ast
import re
from pathlib import Path

SRC_FILE = Path("src/nobeartype/__init__.py")
README_FILE = Path("README.md")
CLASS_NAME = "NoBearType"

BEGIN_MARK = "<!-- BEGIN:NOBEARTYPE-EXAMPLES -->"
END_MARK = "<!-- END:NOBEARTYPE-EXAMPLES -->"


def read_docstring(path: Path, class_name: str) -> str | None:
    src = path.read_text(encoding="utf-8")
    mod = ast.parse(src, filename=str(path))
    for node in ast.walk(mod):
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            return ast.get_docstring(node)
    return None


def extract_pycon_blocks(doc: str) -> list[str]:
    pattern = re.compile(r"```pycon\s*(.*?)\s*```", re.DOTALL | re.IGNORECASE)
    return [m.group(1).strip() for m in pattern.finditer(doc or "")]


def build_readme_section(blocks: list[str]) -> str:
    if not blocks:
        return "*No examples found in the docstring.*"
    if len(blocks) == 1:
        return f"```pycon\n{blocks[0]}\n```"
    parts = []
    for i, b in enumerate(blocks, 1):
        parts.append(f"```pycon\n{b}\n```")
        if i < len(blocks):
            parts.append("\n---\n")
    return "\n".join(parts)


def replace_between_markers(text: str, payload: str) -> str:
    begin_idx = text.find(BEGIN_MARK)
    end_idx = text.find(END_MARK)
    if begin_idx == -1 or end_idx == -1 or end_idx < begin_idx:
        raise SystemExit(
            f"Could not find proper markers '{BEGIN_MARK}' and '{END_MARK}' in {README_FILE}."
        )

    before = text[: begin_idx + len(BEGIN_MARK)]
    after = text[end_idx:]
    middle = f"\n<!-- Auto-generated from {CLASS_NAME} docstring. Do not edit by hand. -->\n\n{payload}\n"
    return before + "\n" + middle + "\n" + after


def main() -> int:
    doc = read_docstring(SRC_FILE, CLASS_NAME)
    if not doc:
        raise SystemExit(
            f"Could not find docstring for class '{CLASS_NAME}' in {SRC_FILE}."
        )

    blocks = extract_pycon_blocks(doc)
    payload = build_readme_section(blocks)

    readme_text = README_FILE.read_text(encoding="utf-8")
    new_text = replace_between_markers(readme_text, payload)

    if new_text != readme_text:
        _ = README_FILE.write_text(new_text, encoding="utf-8")
        print(f"Updated {README_FILE} from {SRC_FILE}:{CLASS_NAME} docstring.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
