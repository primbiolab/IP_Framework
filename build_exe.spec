# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec para generar el ejecutable de IPFramework.

Uso:
    venv\\Scripts\\python.exe -m PyInstaller build_exe.spec --noconfirm --clean
"""

import os
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# --- Recoleccionar datos y dependencias ---

# Incluir la carpeta Files/ del proyecto
datas = []
datas += collect_data_files('.', subdir='Files') if os.path.isdir('Files') else []

# Hidden imports: módulos que PyInstaller no detecta automáticamente
hiddenimports = []
hiddenimports += collect_submodules('torch')
hiddenimports += collect_submodules('PyQt5')
hiddenimports += collect_submodules('pyqtgraph')

# Recoger datos de PyQt5, pyqtgraph y matplotlib
datas += collect_data_files('PyQt5', subdir='Qt')
datas += collect_data_files('pyqtgraph')
datas += collect_data_files('matplotlib')

# --- Análisis ---
a = Analysis(
    ['main_GUI.py'],
    pathex=['.'],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='IPFramework',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
    onefile=True,
)
