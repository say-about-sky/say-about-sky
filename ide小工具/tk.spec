# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['C:/Users/saysky/Desktop/pyLi/基础/ide小工具/tk.py'],
    pathex=[],
    binaries=[],
    datas=[('C:/Users/saysky/Desktop/pyLi/基础/ide小工具/global.log', '.'), ('C:/Users/saysky/Desktop/pyLi/基础/ide小工具/help.help', '.'), ('D:\\Python\\Python310\\Lib\\site-packages\\PIL', 'PIL/'), ('D:/Python/Python310/Lib/site-packages/pyautogui', 'pyautogui/'), ('D:/Python/Python310/Lib/site-packages/pymsgbox', 'pymsgbox/'), ('D:/Python/Python310/Lib/site-packages/pyscreeze', 'pyscreeze/'), ('D:/Python/Python310/Lib/site-packages/mouseinfo', 'mouseinfo/'), ('D:/Python/Python310/Lib/site-packages/pygetwindow', 'pygetwindow/'), ('D:/Python/Python310/Lib/site-packages/pytweening', 'pytweening/'), ('D:/Python/Python310/Lib/site-packages/pyrect', 'pyrect/'), ('D:/Python/Python310/Lib/site-packages/pyperclip', 'pyperclip/'), ('C:/Users/saysky/Desktop/pyLi/基础/ide小工具/T/tk.txt', '.'), ('C:/Users/saysky/Desktop/pyLi/基础/ide小工具/T/设置环境变量(如果需要也可以重新设置).bat', '.'), ('C:/Users/saysky/Desktop/pyLi/基础/ide小工具/account.json', '.'), ('C:/Users/saysky/Desktop/pyLi/基础/ide小工具/logo', 'logo/')],
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
    name='tk',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\saysky\\Desktop\\Ms.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='tk',
)
