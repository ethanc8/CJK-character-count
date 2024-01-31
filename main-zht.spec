# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['main-zht.py'],
    pathex=[],
    binaries=[],
    datas=[("*-han.txt","."), ("readme.txt","."), ("LICENSE","."), ("appicon.png","."), ("GenYoGothicTW-R.ttf","."), ("cjk-char-bold.ttf",".")],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='main-zht',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    icon="appicon.ico",
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='main-zht',
)
app = BUNDLE(exe,
         name='main-zht.app',
         icon=None,
         bundle_identifier=None,
         info_plist={
            'NSPrincipalClass': 'NSApplication',
            'NSAppleScriptEnabled': False,
            },
         )