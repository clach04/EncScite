#!/usr/bin/env python
# -*- coding: us-ascii -*-
# vim:ts=4:sw=4:softtabstop=4:smarttab:expandtab
r"""Setup script to create exe and installer.

Added code from "extending" sample from py2exe (version 0.6.3)
http://www.py2exe.org/

Requires:
    http://www.py2exe.org/
    http://www.jrsoftware.org/isdl.php

To use simply issue:

    py2exe_setup.py py2exe



    cd C:\docs\python\puren_tonbo\puren_tonbo_main_20231211\puren_tonbo-main
    "C:\Portable Python 2.7.3.2\App\python" py2exe_setup.py py2exe

"""

import os
import sys
from distutils.core import setup

import py2exe
from py2exe.build_exe import py2exe



if len(sys.argv) <= 1:
    print("""
Suggested setup.py parameters:

    * py2exe

    python py2exe_setup.py py2exe
""")


icon_file = os.path.join("..", "tombo.ico")

hiddenimports = []
hiddenimports = ['Crypto', 'Crypto.Cipher', 'Crypto.Cipher._raw_ecb', ]
hidden_excludes = []  # FIXME tkinter
hidden_excludes = ['_tkinter', 'tkinter', 'Tkinter', ]  # FIXME tkinter
hidden_excludes = ['_tkinter', 'tkinter', 'Tkinter', 'chi_io', 'openssl_enc_compat', 'puren_tonbo.vimdecrypt']  # DEBUG for Crypto.Cipher._raw_ecb.pyd
dll_excludes = ['api-ms-win-crt-runtime-l1-1-0.dll', ]  # see code that auto-handles msvcr90.dll that is builtin to py2exe
cmc_program_name="puren_tonbo"
exe_dest_dir="prog"

zipfile = r"lib\shardlib"

options = {
    'py2exe': { 'includes': hiddenimports,
                'excludes': hidden_excludes,
                'dll_excludes': dll_excludes,
                "compressed": 1,
                "optimize": 1,  ## 1 and NOT 2 because I use the __doc__ string as the usage string (e.g. for ptig). 2 optimises out the doc strings
              }
       }

#C:\docs\python\puren_tonbo\puren_tonbo_main_20231211\puren_tonbo-main>copy puren_tonbo\tools\ptcipher.py .
tmp_program_name = 'ptcipher'
cmdexe_info = dict(
    script = tmp_program_name+".py",
    icon_resources = [(1, icon_file)],
    dest_base = exe_dest_dir + '/' + tmp_program_name)  # FIXME os.path.join()
    #dest_base = exe_dest_dir + '/' + tmp_program_name)

ptig_program = 'ptig'
ptig_info = dict(
    script = os.path.join('puren_tonbo', 'tools', ptig_program + '.py'),
    icon_resources = [(1, icon_file)],
    dest_base = os.path.join(exe_dest_dir, ptig_program))

console_exes = []
for console_name in ['ptcipher', 'ptig', 'ptconfig', 'ptgrep', 'pttkview']:
    temp_exe_info = dict(
        script = os.path.join('puren_tonbo', 'tools', console_name + '.py'),
        icon_resources = [(1, icon_file)],
        dest_base = os.path.join(exe_dest_dir, console_name))
    console_exes.append(temp_exe_info)

setup(
    # The lib directory contains everything except the executables and the python dll.
    zipfile = zipfile,
    #windows = [exe_info, exe_info2],
    #windows = [exe_info],

    name = cmc_program_name,
    version = "0.0.1",
    description = "Plain Text and Encrypted file tools; search, edit, encrypt, anddecrypt",
    url="https://github.com/clach04/puren_tonbo",
    author="Chris Clark",
    console = console_exes,  #[cmdexe_info, ptig_info],
    #console = ["ikpg.py"], ## doesn't work
    #data_files=[(exe_dest_dir, ["kpg.xrc", icon_file, 'mycolors.txt', 'template.html', 'template.txt'])],
    options = options
    )
