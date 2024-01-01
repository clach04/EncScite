# EncScite

SciTE with encryption/decryption support

WORK IN PROGRESS

## Build

NOTE assumes Python (virtualenv / venv) already setup. Something like:

    call c:\Pythons\pp2717venv\Scripts\activate.bat

pip install of py2exe is NOT possible, i.e. `python -m pip install py2exe==0.6.9` fails
Running exe https://sourceforge.net/projects/py2exe/files/py2exe/0.6.9/py2exe-0.6.9.win32-py2.7.exe/download
also does not work.

BUT can extract contents of `PLATLIB` dir (inside archive, use 7z to view/extract) into `site-packages`.

With virtualenv, may need to manuall set tcl and tk lib paths, e.g.:

    set TCL_LIBRARY=C:\Pythons\PortablePython-2.7.17\App\Python\tcl\tcl8.5
    set TK_LIBRARY=C:\Pythons\PortablePython-2.7.17\App\Python\tcl\tk8.5

This avoids error, `_tkinter.TclError: Can't find a usable init.tcl in the following directories:`.

Get required pieces

    setup.bat
    cd puren_tonbo
    python -m pip install -r requirements.txt
    python -m pip install -r requirements_optional.txt
    python -m pip install -e .
    python -m pip install git+https://github.com/clach04/easydialogs-windows.git
    # Manually install easydialogs-windows

    # HACK - workaround py2exe pywin32 hook problem https://github.com/clach04/EncScite/issues/3
    delete virtualenv\\Lib\site-packages\pythonwin\pywin\Demo

    # FIXME
    # https://github.com/clach04/EncScite/issues/2
    pip uninstall pycryptodome
    echo manually install https://web.archive.org/web/20200427093214/http://www.voidspace.org.uk/python/modules.shtml#pycrypto

### Sanity check / test

    python -m puren_tonbo.tools.ptcipher --password-prompt=gui --decrypt puren_tonbo\tests\data\aesop.chi
    python -m puren_tonbo.tools.ptcipher --password password --decrypt puren_tonbo\tests\data\aesop_linux_7z.aes256stored.zip
    python -m puren_tonbo.tools.ptcipher --password password --decrypt puren_tonbo\tests\data\aesop_win.openssl_aes256cbc_pbkdf2_10k
    python -m puren_tonbo.tools.ptcipher --password password --decrypt puren_tonbo\tests\data\aesop_win_ccrypt.cpt
    python -m puren_tonbo.tools.ptcipher --password password --decrypt puren_tonbo\tests\data\aesop_win_ccrypt.cpt


### Build exes

Assuming in `puren_tonbo` directory from previous steps.

    python ..\py2exe_setup.py py2exe
    copy ..\sc1.exe dist\prog


post Build test

    dist\prog\ptcipher.exe --list-formats
    dist\prog\ptcipher.exe --password password --decrypt puren_tonbo\tests\data\aesop_win.openssl_aes256cbc_pbkdf2_10k
    dist\prog\ptcipher.exe --password-prompt=gui puren_tonbo\tests\data\aesop_win.openssl_aes256cbc_pbkdf2_10k

Should have ~11-12Mb dist directory without Tkinter, with tk/tcl will be ~18Mb dist directory.
**May** need to copy mfc and msvcrt 90 dlls from virtualenv AND also the base Python path the virtual env is based on.


  * TODO scite config
  * TODO scite lua
  * TODO wrapper batch file
