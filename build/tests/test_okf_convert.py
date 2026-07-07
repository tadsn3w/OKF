import json
import os
import subprocess
import sys
import tempfile
from okf_convert import (
    build_bundle,
    split_frontmatter,
    has_frontmatter_field,
    process_file,
    scan_directory,
)


def write_file(path: str, content: str):
    os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)


def test_scan_empty_directory():
    with tempfile.TemporaryDirectory() as tmp:
        result = scan_directory(tmp)
        assert result == []


def test_scan_with_md_files():
    with tempfile.TemporaryDirectory() as tmp:
        write_file(os.path.join(tmp, 'a.md'), '# A')
        write_file(os.path.join(tmp, 'sub', 'b.md'), '# B')
        write_file(os.path.join(tmp, 'not.txt'), 'nope')
        result = scan_directory(tmp)
        assert sorted(result) == ['a.md', 'sub/b.md']


def test_scan_skips_default_excludes():
    with tempfile.TemporaryDirectory() as tmp:
        write_file(os.path.join(tmp, 'keep.md'), '# Keep')
        write_file(os.path.join(tmp, '.venv', 'skip.md'), '# Skip')
        write_file(os.path.join(tmp, '.git', 'skip.md'), '# Skip')
        write_file(os.path.join(tmp, '.pytest_cache', 'skip.md'), '# Skip')
        write_file(os.path.join(tmp, '__pycache__', 'skip.md'), '# Skip')
        result = scan_directory(tmp)
        assert result == ['keep.md']


def test_scan_skips_output_directory_inside_source():
    with tempfile.TemporaryDirectory() as tmp:
        output = os.path.join(tmp, 'knowledge')
        write_file(os.path.join(tmp, 'keep.md'), '# Keep')
        write_file(os.path.join(output, 'skip.md'), '# Skip')
        result = scan_directory(tmp, output)
        assert result == ['keep.md']


class TestSplitFrontmatter:
    def test_no_frontmatter(self):
        text, body, md = split_frontmatter('# Plain file')
        assert text is None
        assert '# Plain file' in md

    def test_with_frontmatter(self):
        content = '---\ntype: Doc\n---\n\n# Body'
        text, body, md = split_frontmatter(content)
        assert text is not None
        assert 'type: Doc' in body
        assert '# Body' in md

    def test_empty_frontmatter(self):
        content = '---\n---\n\n# Body'
        text, body, md = split_frontmatter(content)
        assert text is not None
        assert body == ''
        assert '# Body' in md

    def test_malformed_frontmatter(self):
        content = '---\ntype: Doc\n# Body'
        text, body, md = split_frontmatter(content)
        assert text is None  # no closing ---


class TestHasFrontmatterField:
    def test_has_field(self):
        assert has_frontmatter_field('type: Doc\ntitle: X', 'type')
        assert has_frontmatter_field('type: Doc', 'type')

    def test_missing_field(self):
        assert not has_frontmatter_field('title: X', 'type')

    def test_empty_field(self):
        assert not has_frontmatter_field('type: \n', 'type')
        assert not has_frontmatter_field('type:', 'type')


class TestProcessFile:
    def test_has_type_preserved(self):
        content = '---\ntype: Doc\ntitle: My\n---\n\n# Body'
        result = process_file(content, 'file.md')
        assert 'type: Doc' in result
        assert 'title: My' in result
        assert '# Body' in result

    def test_has_frontmatter_no_type_adds_type(self):
        content = '---\ntitle: My\n---\n\n# Body'
        result = process_file(content, 'file.md')
        assert 'type: Document' in result
        assert 'title: My' in result
        assert '# Body' in result

    def test_no_frontmatter_generates(self):
        content = '# Just markdown'
        result = process_file(content, 'my-file.md')
        assert 'type: Document' in result
        assert 'title: my file' in result
        assert '# Just markdown' in result


class TestBuildBundle:
    def test_empty_source(self):
        with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as out:
            result = build_bundle(src, out)
            assert result['concepts'] == 0
            assert result['directories'] == 0
            assert os.path.isfile(os.path.join(out, 'log.md'))

    def test_single_file(self):
        with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as out:
            write_file(os.path.join(src, 'doc.md'), '---\ntype: Note\n---\n\n# Hi')
            result = build_bundle(src, out)
            assert result['concepts'] == 1
            assert result['directories'] == 1
            assert os.path.isfile(os.path.join(out, 'doc.md'))
            assert os.path.isfile(os.path.join(out, 'index.md'))
            assert os.path.isfile(os.path.join(out, 'log.md'))

    def test_file_without_frontmatter(self):
        with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as out:
            write_file(os.path.join(src, 'notes.md'), '# Notes\n\nSome text')
            result = build_bundle(src, out)
            assert result['concepts'] == 1
            with open(os.path.join(out, 'notes.md')) as f:
                content = f.read()
            assert 'type: Document' in content
            assert 'title: notes' in content
            assert '# Notes' in content

    def test_subdirectory_structure(self):
        with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as out:
            write_file(os.path.join(src, 'a.md'), '---\ntype: One\n---\n\n# A')
            write_file(os.path.join(src, 'sub', 'b.md'), '---\ntype: Two\n---\n\n# B')
            result = build_bundle(src, out)
            assert result['concepts'] == 2
            assert result['directories'] >= 1
            assert os.path.isfile(os.path.join(out, 'index.md'))
            assert os.path.isfile(os.path.join(out, 'a.md'))
            assert os.path.isfile(os.path.join(out, 'sub', 'b.md'))

    def test_reserved_filenames_renamed(self):
        with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as out:
            write_file(os.path.join(src, 'index.md'), '---\ntype: Original\n---\n\n# I')
            write_file(os.path.join(src, 'log.md'), '---\ntype: Original\n---\n\n# L')
            result = build_bundle(src, out)
            assert result['concepts'] == 2
            assert os.path.isfile(os.path.join(out, '_index.md'))
            assert os.path.isfile(os.path.join(out, '_log.md'))
            # Bundle's own index.md should also exist
            assert os.path.isfile(os.path.join(out, 'index.md'))

    def test_root_types_file_renamed_for_generated_inventory(self):
        with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as out:
            write_file(os.path.join(src, 'types.md'), '---\ntype: Source Types\n---\n\n# T')
            build_bundle(src, out)
            assert os.path.isfile(os.path.join(out, '_types.md'))
            assert os.path.isfile(os.path.join(out, 'types.md'))
            with open(os.path.join(out, 'types.md')) as f:
                content = f.read()
            assert 'type: Concept Directory' in content
            assert '| Source Types | 1 | [types](_types.md) |' in content

    def test_subdirectory_types_file_preserved(self):
        with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as out:
            write_file(os.path.join(src, 'sub', 'types.md'), '---\ntype: Local Types\n---\n\n# T')
            build_bundle(src, out)
            assert os.path.isfile(os.path.join(out, 'sub', 'types.md'))

    def test_dry_run_writes_nothing(self):
        with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as out:
            write_file(os.path.join(src, 'doc.md'), '---\ntype: X\n---\n\n# Hi')
            result = build_bundle(src, out, dry_run=True)
            assert result['concepts'] == 1
            assert not os.path.isfile(os.path.join(out, 'doc.md'))
            assert not os.path.isfile(os.path.join(out, 'index.md'))
            assert not os.path.isfile(os.path.join(out, 'log.md'))

    def test_non_md_files_skipped(self):
        with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as out:
            write_file(os.path.join(src, 'a.md'), '---\ntype: X\n---\n\n# A')
            write_file(os.path.join(src, 'b.txt'), 'not markdown')
            write_file(os.path.join(src, 'c.py'), 'print("hi")')
            result = build_bundle(src, out)
            assert result['concepts'] == 1
            assert not os.path.exists(os.path.join(out, 'b.txt'))
            assert not os.path.exists(os.path.join(out, 'c.py'))

    def test_index_includes_descriptions(self):
        with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as out:
            write_file(os.path.join(src, 'doc.md'),
                       '---\ntype: Note\ntitle: My Doc\ndescription: A test doc\n---\n\n# Body')
            build_bundle(src, out)
            with open(os.path.join(out, 'index.md')) as f:
                index = f.read()
            assert '[My Doc](doc.md)' in index
            assert 'A test doc' in index

    def test_types_inventory_groups_concepts_by_type(self):
        with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as out:
            write_file(os.path.join(src, 'a.md'), '---\ntype: Note\ntitle: A\n---\n\n# A')
            write_file(os.path.join(src, 'b.md'), '---\ntype: Note\ntitle: B\n---\n\n# B')
            write_file(os.path.join(src, 'c.md'), '---\ntype: Task\ntitle: C\n---\n\n# C')
            build_bundle(src, out)
            with open(os.path.join(out, 'types.md')) as f:
                content = f.read()
            assert '| Note | 2 | [A](a.md), [B](b.md) |' in content
            assert '| Task | 1 | [C](c.md) |' in content


def test_cli_stdout_is_clean_json():
    script = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'okf-convert')
    with tempfile.TemporaryDirectory() as src, tempfile.TemporaryDirectory() as out:
        write_file(os.path.join(src, 'doc.md'), '---\ntype: Note\n---\n\n# Hi')
        result = subprocess.run(
            [sys.executable, script, src, '--output', out, '--stdout'],
            check=True,
            capture_output=True,
            text=True,
        )
        parsed = json.loads(result.stdout)
        assert parsed['concepts'] == 1
        assert result.stderr == ''
