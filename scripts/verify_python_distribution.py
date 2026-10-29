"""Verify Python distribution payloads against the selected library source."""
import argparse
import ast
from email.parser import BytesParser
from pathlib import Path, PurePosixPath
import stat
import tarfile
import tomllib
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def expected(root):
    assignments = ast.parse((root / 'setup.py').read_text()).body
    assets = next(ast.literal_eval(node.value) for node in assignments
                  if isinstance(node, ast.Assign) and any(
                      isinstance(target, ast.Name) and target.id == 'ASSETS' for target in node.targets))
    files = {}
    for path in (root / 'qspquest_models').iterdir():
        if path.suffix in ('.py', '.json'):
            files['qspquest_models/' + path.name] = path
    for name in assets:
        source = root / name
        for path in sorted(source.rglob('*')) if source.is_dir() else [source]:
            require(not path.is_symlink(), 'Distribution inputs must be regular files')
            if path.is_file() and path.name != '.DS_Store' and '__pycache__' not in path.parts:
                files['qspquest_models/_library/' + path.relative_to(root).as_posix()] = path
    return files


def safe_names(names):
    require(len(names) == len(set(names)) and 0 < len(names) < 10000, 'Invalid archive inventory')
    for name in names:
        parts = PurePosixPath(name).parts
        require(not name.startswith('/') and '\\' not in name and ':' not in name
                and '..' not in parts and str(PurePosixPath(name)) == name.rstrip('/'),
                'Unsafe archive path')


def metadata(raw, version, root):
    message = BytesParser().parsebytes(raw)
    require(not message.defects and message.get_all('Name') == ['qspquest-models']
            and message.get_all('Version') == [version], 'Distribution metadata identity differs')
    description = message.get_payload(decode=True).decode('utf-8').replace('\r\n', '\n')
    require(description.strip() == (root / 'PACKAGE_README.md').read_text().strip(),
            'Distribution description differs from the selected package guide')


def verify(directory, root=ROOT):
    project = tomllib.loads((root / 'pyproject.toml').read_text())['project']
    version = project['version']
    package = 'qspquest_models-' + version
    wheel = directory / (package + '-py3-none-any.whl')
    source = directory / (package + '.tar.gz')
    require(wheel.is_file() and source.is_file(), 'The selected wheel and source archive are required')
    payload = expected(root)
    with zipfile.ZipFile(wheel) as archive:
        members = archive.infolist()
        safe_names([member.filename for member in members])
        require(sum(member.file_size for member in members) < 400_000_000
                and all(member.file_size < 100_000_000 and not member.flag_bits & 1
                        and not stat.S_ISLNK(member.external_attr >> 16) for member in members),
                'Unsafe wheel member')
        names = set(archive.namelist())
        prefix = package + '.dist-info/'
        auxiliary = {prefix + name for name in ('METADATA', 'WHEEL', 'RECORD', 'entry_points.txt', 'top_level.txt')}
        licenses = {prefix + 'licenses/' + name: root / name for name in project['license-files']}
        require(set(payload) | set(licenses) <= names <= set(payload) | set(licenses) | auxiliary,
                'Wheel includes missing or unselected files')
        for name, path in {**payload, **licenses}.items():
            require(archive.read(name) == path.read_bytes(), 'Wheel differs from selected source: ' + name)
        metadata(archive.read(prefix + 'METADATA'), version, root)
    selected = {path.relative_to(root).as_posix(): path for path in payload.values()}
    for name in ('pyproject.toml', 'setup.py', 'MANIFEST.in', 'PACKAGE_README.md'):
        selected[name] = root / name
    with tarfile.open(source) as archive:
        members = archive.getmembers()
        safe_names([member.name for member in members])
        require(sum(member.size for member in members) < 400_000_000
                and all(member.isfile() or member.isdir() for member in members), 'Unsafe source member')
        files = {}
        for member in members:
            require(member.name == package or member.name.startswith(package + '/'), 'Unexpected source wrapper')
            if member.isfile():
                files[member.name[len(package) + 1:]] = archive.extractfile(member).read()
        for name, path in selected.items():
            require(files.get(name) == path.read_bytes(), 'Source archive differs: ' + name)
        allowed = {'PKG-INFO', 'setup.cfg', 'README.md'} | {
            'qspquest_models.egg-info/' + name for name in
            ('PKG-INFO', 'SOURCES.txt', 'dependency_links.txt', 'entry_points.txt', 'top_level.txt')}
        require(set(files) <= set(selected) | allowed, 'Unselected files in source archive')
        if 'README.md' in files:
            require(files['README.md'] == (root / 'README.md').read_bytes(), 'Source README differs')
        metadata(files['PKG-INFO'], version, root)
    return {'status': 'passed', 'version': version, 'wheel_payload_files': len(payload)}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('directory', type=Path)
    args = parser.parse_args()
    import json
    print(json.dumps(verify(args.directory), sort_keys=True))
