"""
okf_convert — Core module for converting markdown directories to OKF bundles.
"""

import os
import re
from datetime import datetime, timezone

RESERVED = {'index.md', 'log.md'}
DEFAULT_EXCLUDES = {'.git', '.venv', '.pytest_cache', '__pycache__'}


def is_inside(path: str, parent: str) -> bool:
    """Return True when path is parent or a descendant of parent."""
    return os.path.commonpath([os.path.abspath(path), os.path.abspath(parent)]) == os.path.abspath(parent)


def scan_directory(root: str, output: str | None = None) -> list[str]:
    """Return sorted relative paths of all .md files under root."""
    root = os.path.abspath(root)
    output = os.path.abspath(output) if output else None
    md_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(
            d for d in dirnames
            if d not in DEFAULT_EXCLUDES
            and not (output and is_inside(os.path.join(dirpath, d), output))
        )
        for f in sorted(filenames):
            if f.endswith('.md'):
                rel = os.path.relpath(os.path.join(dirpath, f), root)
                md_files.append(rel)
    return md_files


def split_frontmatter(content: str) -> tuple[str | None, str, str]:
    """
    Split a markdown file into (frontmatter_text, frontmatter_body, markdown_body).

    frontmatter_text includes the --- delimiters, or None if no frontmatter.
    """
    content = content.lstrip()
    if not content.startswith('---'):
        return None, '', content

    # Find closing ---
    rest = content[3:]
    end = rest.find('\n---')
    if end == -1:
        return None, '', content

    fm_body = rest[:end].strip()
    md_body = rest[end + 4:].lstrip()
    fm_text = '---\n' + fm_body + '\n---'
    return fm_text, fm_body, md_body


def has_frontmatter_field(fm_body: str, field: str) -> bool:
    """Check if a frontmatter body has a non-empty value for the given field."""
    return bool(re.search(rf'^{field}:\s*\S', fm_body, re.MULTILINE))


def extract_frontmatter_value(fm_body: str, field: str) -> str | None:
    """Extract a simple scalar value from a frontmatter field."""
    m = re.search(rf'^{field}:\s*(.+?)\s*$', fm_body, re.MULTILINE)
    if m:
        val = m.group(1)
        # Strip quotes
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]
        return val
    return None


def filename_to_title(filename: str) -> str:
    """Derive a human-readable title from a filename."""
    name = filename.removesuffix('.md')
    name = re.sub(r'[-_]', ' ', name)
    return name.strip()


def process_file(content: str, filename: str) -> str:
    """
    Process file content for OKF conformance.
    Ensures frontmatter exists with a non-empty type field.
    """
    fm_text, fm_body, md_body = split_frontmatter(content)

    if fm_text and has_frontmatter_field(fm_body, 'type'):
        return content

    if fm_text:
        # Has frontmatter but no type — add it
        fm_body = fm_body.rstrip() + '\ntype: Document'
        fm_text = '---\n' + fm_body + '\n---'
        return fm_text + '\n' + md_body if md_body else fm_text + '\n'

    # No frontmatter — generate one
    title = filename_to_title(filename)
    fm = f'---\ntype: Document\ntitle: {title}\n---'
    return fm + '\n\n' + content.lstrip()


def get_concept_info(content: str, filename: str) -> tuple[str, str, str]:
    """Extract (type, title, description) from a concept file."""
    fm_text, fm_body, _ = split_frontmatter(content)
    concept_type = 'Document'
    title = filename_to_title(filename)
    description = ''

    if fm_body:
        ct = extract_frontmatter_value(fm_body, 'type')
        if ct:
            concept_type = ct
        t = extract_frontmatter_value(fm_body, 'title')
        if t:
            title = t
        d = extract_frontmatter_value(fm_body, 'description')
        if d:
            description = d

    return concept_type, title, description


def write_file(path: str, content: str, dry_run: bool, quiet: bool = False):
    """Write file if not dry_run; print preview if dry_run."""
    if dry_run:
        if not quiet:
            print(f'[dry-run] would write {path} ({len(content)} bytes)')
    else:
        os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
        with open(path, 'w') as f:
            f.write(content)


def build_index(dirname: str, entries: list[tuple[str, str, str]],
                output: str, dry_run: bool, quiet: bool = False):
    """
    Write index.md for a directory.
    entries: list of (concept_filename, title, description)
    """
    heading = os.path.basename(dirname.rstrip('/')) if dirname != '.' else 'Bundle Root'
    lines = [f'# {heading}', '']
    for fname, title, desc in entries:
        line = f'* [{title}]({fname})'
        if desc:
            line += f' - {desc}'
        lines.append(line)
    lines.append('')

    out_path = os.path.join(output, dirname, 'index.md') if dirname != '.' else os.path.join(output, 'index.md')
    write_file(out_path, '\n'.join(lines), dry_run, quiet)


def build_types(output: str, type_entries: dict[str, list[tuple[str, str]]],
                dry_run: bool, quiet: bool = False):
    """Write types.md at bundle root."""
    today = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    lines = [
        '---',
        'type: Concept Directory',
        'title: Types in this bundle',
        'description: Informational inventory of frontmatter type values found in this OKF bundle.',
        'tags: [okf, metadata]',
        f'timestamp: {today}',
        '---',
        '',
        '| Type | Count | Concepts |',
        '|------|-------|----------|',
    ]
    for concept_type, entries in sorted(type_entries.items()):
        links = ', '.join(f'[{title}]({path})' for path, title in sorted(entries))
        lines.append(f'| {concept_type} | {len(entries)} | {links} |')
    lines.append('')
    write_file(os.path.join(output, 'types.md'), '\n'.join(lines), dry_run, quiet)


def build_log(output: str, source: str, concepts: int, dry_run: bool, quiet: bool = False):
    """Write log.md at bundle root."""
    today = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    content = f"""# Bundle Update Log

## {today}
* **Creation**: Bundle created from `{source}` — {concepts} concepts.
"""
    write_file(os.path.join(output, 'log.md'), content, dry_run, quiet)


def build_bundle(source: str, output: str, dry_run: bool = False,
                 quiet: bool = False) -> dict:
    """
    Convert a directory of markdown files into an OKF knowledge bundle.

    Returns a summary dict with keys: concepts, directories, source, output.
    """
    source = os.path.abspath(source)
    output = os.path.abspath(output)
    md_files = scan_directory(source, output)

    dir_entries: dict[str, list[tuple[str, str, str]]] = {}
    type_entries: dict[str, list[tuple[str, str]]] = {}

    for rel_path in md_files:
        abs_path = os.path.join(source, rel_path)
        with open(abs_path) as f:
            content = f.read()

        processed = process_file(content, rel_path)
        filename = os.path.basename(rel_path)
        dirname = os.path.dirname(rel_path)

        if filename in RESERVED or (filename == 'types.md' and dirname == ''):
            filename = f'_{filename}'
        out_rel = os.path.join(dirname, filename) if dirname else filename

        out_abs = os.path.join(output, out_rel)
        write_file(out_abs, processed, dry_run, quiet)

        concept_type, title, desc = get_concept_info(processed, filename)
        group = dirname if dirname else '.'
        dir_entries.setdefault(group, []).append((filename, title, desc))
        type_entries.setdefault(concept_type, []).append((out_rel, title))

    for dirname, entries in sorted(dir_entries.items()):
        build_index(dirname, entries, output, dry_run, quiet)

    build_types(output, type_entries, dry_run, quiet)
    build_log(output, source, len(md_files), dry_run, quiet)

    return {
        'concepts': len(md_files),
        'directories': len(dir_entries),
        'source': source,
        'output': output,
    }
