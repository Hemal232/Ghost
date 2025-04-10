# H17I Github Actions Ghost Build System - https://github.com/Highway-17-Interactive/Ghost

from sys import exit as sys_exit

from platform import system

from os.path import exists

from subprocess import run, CalledProcessError

from json import load


def ghost_fail(code: int) -> None:
    print(f'Ghost Building Error: {code}')

    sys_exit(code)

print('[Ghost] Parsing build config...')

if not exists('ghost-build/ghost-build.json'): ghost_fail(1)

with open('ghost-build/ghost-build.json', 'r') as gb: gbc: dict = load(gb)

if 'CMainFile' not in gbc: ghost_fail(2)
if 'CType' not in gbc: ghost_fail(3)
if 'CFlagsWindows' not in gbc: ghost_fail(4)
if 'CFlagsLinux' not in gbc: ghost_fail(5)

cmf = gbc['CMainFile']

if not cmf or not exists(cmf): ghost_fail(6)

ct = gbc['CType']

if not ct or ct not in ['C', 'C++']: ghost_fail(7)

cfw = gbc['CFlagsWindows']; cfw = '' if not cfw else ' ' + cfw
cfl = gbc['CFlagsLinux']; cfl = '' if not cfl else ' ' + cfl

sys = system()

compiler = 'gcc' if ct == 'C' else 'g++'

if sys == 'Windows':
    cmd = f'{compiler} {cmf} -o ghost-build-windows.exe{cfw}'

elif sys == 'Linux':
    cmd = f'{compiler} {cmf} -o ghost-build-linux{cfl}'

else:
    ghost_fail(8)

print('[Ghost] Building...')

try:
    run(cmd, shell=True, check=True)
except CalledProcessError:
    ghost_fail(9)

print('[Ghost] Success!')

sys_exit(0)
