# H17I Github Actions Ghost Build System - https://github.com/H17I/Ghost

# Imports.
from sys import exit as sys_exit

from platform import system

from os.path import exists

from subprocess import run, CalledProcessError

from xml.etree.ElementTree import parse, Element, ParseError


# Utilities.
def ghost_fail(strrepr: str, code: int) -> None:
    print(f'Ghost Building Error: {strrepr} [{code}]')

    sys_exit(code)

def xml_el_not_none(cfg: Element, tag: str, eid: int) -> str:
    element = cfg.find(tag)

    if element == None: ghost_fail(f'[CONFIG] Missing `{tag}` element in <GhostBuild>', eid)

    return element.text

# Starting messages.
print('[Ghost] Starting Ghost building process...')

print('[CONFIG] Parsing build config...')

# Parse XML file.
if not exists('ghost-build/ghost-build.xml'): ghost_fail('[CONFIG] Can\'t find Ghost Build Config.', 1)

try:
    build_cfg = parse('ghost-build/ghost-build.xml').getroot()
except ParseError:
    ghost_fail('[CONFIG] Can\'t parse build config: invalid syntax/missing root element (<GhostBuild>).', 2)

# XML: Compiler.
build_compiler = build_cfg.get('Compiler')

if not build_compiler: ghost_fail('[CONFIG] Missing `Compiler` attribute in <GhostBuild>', 3)

if build_compiler == 'NULL': ghost_fail('[CONFIG] Compiler is NULL. Please modify the config.', -1)

if build_compiler not in ['GNU', 'Clang']: ghost_fail('[CONFIG] Invalid compiler: expected `GNU` or `Clang`.', 4)

# XML: CType.
ctype = build_cfg.get('CType')

if not ctype: ghost_fail('[CONFIG] Missing `CType` attribute in <GhostBuild>', 5)

if ctype not in ['C', 'C++']: ghost_fail('[CONFIG] Invalid CType: Expected `C` or `C++`.', 6)

# XML: BuildName.
build_name = xml_el_not_none(build_cfg, 'BuildName', 7)

# XML: CMainFile
main_file = xml_el_not_none(build_cfg, 'CMainFile', 8)

# XML: CFlags(Windows/Linux)
cf_win = xml_el_not_none(build_cfg, 'CFlagsWindows', 9); cf_win = '' if cf_win in ['' , 'NULL'] else ' ' + cf_win
cf_linux = xml_el_not_none(build_cfg, 'CFlagsLinux', 10); cf_linux = '' if cf_linux in ['' , 'NULL'] else ' ' + cf_linux

# XML: (Windows/Linux)Auxiliary
win_aux = xml_el_not_none(build_cfg, 'WindowsAuxiliary', 11); win_aux = None if win_aux in ['' , 'NULL'] else win_aux
linux_aux = xml_el_not_none(build_cfg, 'LinuxAuxiliary', 12); linux_aux = None if linux_aux in ['' , 'NULL'] else linux_aux

_repr_waux, _repr_laux = win_aux, linux_aux

if win_aux: win_aux = "ghost-build/" + win_aux + ".py" if not win_aux.endswith(".py") else ""
if linux_aux: linux_aux = "ghost-build/" + linux_aux + ".py" if not linux_aux.endswith(".py") else ""

# Check CMakeFile for existence.
if not exists(main_file): ghost_fail('[CONFIG] Error: CMainFile is non-existent.', 13)

# Get running system & validate it.
gh_sys = system()[0]

if gh_sys not in ['W', 'L']: ghost_fail('[BUILD] Invalid gh_sys.', 14)

# Define compiler for future build.
build_compiler_cmd = ('gcc' if ctype == 'C' else 'g++') \
    if build_compiler == 'GNU' else ('clang' if ctype == 'C' else 'clang++')

if gh_sys == 'W' and build_compiler == 'Clang':
    print('[BUILD] [WINDOWS]: Switching to GNU because Ghost does not support Clang compiler for Windows.')

    build_compiler_cmd = build_compiler_cmd.replace('clang++', 'g++').replace('clang', 'gcc')

# Building command.
build_cmd = f'{build_compiler_cmd} {main_file} -o {"ghost-build-" + ("windows.exe" if gh_sys == "W" else "linux")}{cf_win if gh_sys == "W" else cf_linux}'

# Auxiliary files: Windows.
if win_aux and gh_sys == 'W':
    print('[BUILD-AUXILIARY] Running Windows auxiliary file...')

    if not exists(win_aux): ghost_fail('[CONFIG&BUILD] Invalid Windows auxiliary file.', 15)

    try:
        run(f'python {win_aux}', shell=True, check=True)
    except CalledProcessError:
        ghost_fail('[BUILD-AUXILIARY] Windows auxiliary file crash: can\'t proceed.', 16)

else:
    print('[BUILD-AUXILIARY] Windows auxiliary file is not specified.')

# Auxiliary files: Linux.
if linux_aux and gh_sys == 'L':
    print('[BUILD-AUXILIARY] Running Linux auxiliary file...')

    if not exists(linux_aux): ghost_fail('[CONFIG&BUILD] Invalid Linux auxiliary file.', 17)

    try:
        run(f'python3 {linux_aux}', shell=True, check=True)
    except CalledProcessError:
        ghost_fail('[BUILD-AUXILIARY] Linux auxiliary file crash: can\'t proceed.', 18)

else:
    print('[BUILD-AUXILIARY] Linux auxiliary file is not specified.')

# Log message.
_tab = ' ' * 13

print(\
f'[BUILD-INFO] Running Platform: \
{"Windows" if gh_sys == "W" else "Linux"}\n{_tab}\
Compiler: {build_compiler}{"? (Fallback to GNU)" if gh_sys == "W" and build_compiler == "Clang" else ""} \
({build_compiler_cmd})\n{_tab}C Type: {ctype}\n{_tab}Build name: {build_name}\n{_tab}\
Main file: {main_file}\n{_tab}Windows Flags: {"None" if not cf_win else cf_win[1:]}\n{_tab}\
Linux Flags: {"None" if not cf_linux else cf_linux[1:]}\n{_tab}\
Windows Auxiliary: {_repr_waux}\n{_tab}Linux Auxiliary: {_repr_laux}')

# Start the build process.
print(f'[BUILD] Starting the build process...')

try:
    run(build_cmd, shell=True, check=True)
except CalledProcessError:
    ghost_fail('[BUILD] Build failed.', 19)

# Finish the build process.
print('[BUILD] Build finished without any errors.')

print('[Ghost] Build process finished.')

sys_exit(0)
