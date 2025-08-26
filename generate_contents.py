import os
import json
import fnmatch

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(ROOT_DIR, "CONTENTS.md")

DEFAULT_IGNORES = {".git", ".idea", ".vscode", "__pycache__", ".venv"}

def load_gitignore(root_dir):
    gitignore_path = os.path.join(root_dir, ".gitignore")
    patterns = []
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    patterns.append(line)
    return patterns

def is_ignored(path, ignore_patterns):
    parts = path.split(os.sep)
    for part in parts:
        if part in DEFAULT_IGNORES:
            return True
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(path, pattern) or fnmatch.fnmatch(os.path.basename(path), pattern):
            return True
    return False

def get_category_name(folder):
    meta_path = os.path.join(folder, "_category.json")
    if os.path.exists(meta_path):
        with open(meta_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
                return data.get("title", os.path.basename(folder))
            except json.JSONDecodeError:
                return os.path.basename(folder)
    return os.path.basename(folder)

def get_markdown_title(file_path):
    """Берёт первый # заголовок из .md файла"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip().startswith("# "):
                    return line.strip("# ").strip()
    except Exception:
        pass
    return os.path.splitext(os.path.basename(file_path))[0]

def build_contents(base_dir, ignore_patterns, depth=0):
    entries = []
    items = sorted(os.listdir(base_dir))
    for item in items:
        path = os.path.join(base_dir, item)
        if is_ignored(path, ignore_patterns):
            continue

        if os.path.isdir(path):
            section_title = get_category_name(path)
            subsection = build_contents(path, ignore_patterns, depth + 1)
            if subsection:
                entries.append("  " * depth + f"- **{section_title}**")
                entries.extend(subsection)
        elif item.endswith(".md") and item != os.path.basename(OUTPUT_FILE):
            rel_path = os.path.relpath(path, ROOT_DIR).replace("\\", "/")
            title = get_markdown_title(path)
            entries.append("  " * depth + f"- [{title}]({rel_path})")

    return entries

def main():
    ignore_patterns = load_gitignore(ROOT_DIR)

    contents = ["# 📚 Содержание\n"]
    contents.extend(build_contents(ROOT_DIR, ignore_patterns))

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(contents))

    print(f"✅ Файл {OUTPUT_FILE} обновлён!")

if __name__ == "__main__":
    main()
