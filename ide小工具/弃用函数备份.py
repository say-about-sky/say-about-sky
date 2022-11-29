
# 剪贴
def cutJob():
    try:
        # 调用下面的copyJoy方法
        copyJob()
        # 删除所选取的文字
        text.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)
    except tkinter.TclError:
        pass

# 复制
def copyJob():
    try:
        # 清除剪贴板
        text.clipboard_clear()
        # 复制选取内容
        copyText = text.get(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        # 写入剪贴板
        text.clipboard_append(copyText)
    except tkinter.TclError:
        print('没有选取')


# 粘贴
def pasteJob():
    try:
        # 读取剪贴板内容
        copyText = text.selection_get(selection='CLIPBOARD')
        # 插入内容
        text.insert(tkinter.INSERT, copyText)
    except tkinter.TclError:
        print('剪贴板没有内容')
