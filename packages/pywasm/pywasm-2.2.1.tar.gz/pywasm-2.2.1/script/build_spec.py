import contextlib
import glob
import os
import subprocess
import typing


def call(cmd: str) -> subprocess.CompletedProcess[bytes]:
    print(f'$ {cmd}')
    return subprocess.run(cmd, shell=True, check=True)


@contextlib.contextmanager
def cd(dst: str) -> typing.Generator[None, typing.Any, None]:
    cwd = os.getcwd()
    os.chdir(dst)
    yield
    os.chdir(cwd)


root = os.path.dirname(os.path.dirname(__file__))
os.chdir(root)

with cd('res'):
    if not os.path.exists('spec'):
        call('git clone https://github.com/WebAssembly/spec')
with cd('res/spec'):
    call('git checkout main')
    call('git pull origin main')
    # When update spectest, we can increase the commit id in small steps.
    # Use: git log --reverse fffc6e12fa454e475455a7b58d3b5dc343980c10.. -- test/core
    call('git checkout fffc6e12fa454e475455a7b58d3b5dc343980c10')
with cd('res/spec/test/core'):
    for e in sorted(glob.glob('*.wast')):
        call(f'{root}/res/wabt/bin/wast2json {e}')
with cd('res/spec/test/core/simd'):
    for e in sorted(glob.glob('*.wast')):
        call(f'{root}/res/wabt/bin/wast2json {e}')
