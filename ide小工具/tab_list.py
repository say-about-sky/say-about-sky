from idlelib.multicall import MultiCallCreator
#追踪autocomplete查看事件流程
import idlelib.autocomplete as aut
#模拟官方idle的窗口结构
class root_dang:
    def __init__(self,*v,**k):
        #本来想用locals 但是默认是只读不好改
        los=globals()
        los.update(k)
        self.text=text
        self.indentwidth = 4
        self.tabwidth=8
        self.prompt_last_line=''
        self.num_context_lines=50, 500, 5000000
        self.color = None
        self.code_context = None
        self.line_numbers = None
        #新建菜单
        self.menubar =tk.Menu(root)
        #self.top = window.ListedToplevel(root, menu=self.menubar)
        #self.createmenubar()
        #self.apply_bindings()
    def _build_char_in_string_func(self, startindex):
        def inner(offset, _startindex=startindex,
                _icis=self.is_char_in_string):
            return _icis(_startindex + "+%dc" % offset)
        return inner
    def is_char_in_string(self, text_index):
        if self.color:
            # Return true iff colorizer hasn't (re)gotten this far
            # yet, or the character is tagged as being in a string
            return self.text.tag_prevrange("TODO", text_index) or \
                   "STRING" in self.text.tag_names(text_index)
        else:
            # The colorizer is missing: assume the worst
            return 1
    def newline_and_indent_event(self, event):
        """Insert a newline and indentation after Enter keypress event.

        Properly position the cursor on the new line based on information
        from the current line.  This takes into account if the current line
        is a shell prompt, is empty, has selected text, contains a block
        opener, contains a block closer, is a continuation line, or
        is inside a string.
        """
        text = self.text
        first, last = self.get_selection_indices()
        text.undo_block_start()
        try:  # Close undo block and expose new line in finally clause.
            if first and last:
                text.delete(first, last)
                text.mark_set("insert", first)
            line = text.get("insert linestart", "insert")

            # Count leading whitespace for indent size.
            i, n = 0, len(line)
            while i < n and line[i] in " \t":
                i += 1
            if i == n:
                # The cursor is in or at leading indentation in a continuation
                # line; just inject an empty line at the start.
                text.insert("insert linestart", '\n',
                            self.user_input_insert_tags)
                return "break"
            indent = line[:i]

            # Strip whitespace before insert point unless it's in the prompt.
            i = 0
            while line and line[-1] in " \t":
                line = line[:-1]
                i += 1
            if i:
                text.delete("insert - %d chars" % i, "insert")

            # Strip whitespace after insert point.
            while text.get("insert") in " \t":
                text.delete("insert")

            # Insert new line.
            text.insert("insert", '\n', self.user_input_insert_tags)

            # Adjust indentation for continuations and block open/close.
            # First need to find the last statement.
            lno = index2line(text.index('insert'))
            y = pyparse.Parser(self.indentwidth, self.tabwidth)
            if not self.prompt_last_line:
                for context in self.num_context_lines:
                    startat = max(lno - context, 1)
                    startatindex = repr(startat) + ".0"
                    rawtext = text.get(startatindex, "insert")
                    y.set_code(rawtext)
                    bod = y.find_good_parse_start(
                            self._build_char_in_string_func(startatindex))
                    if bod is not None or startat == 1:
                        break
                y.set_lo(bod or 0)
            else:
                r = text.tag_prevrange("console", "insert")
                if r:
                    startatindex = r[1]
                else:
                    startatindex = "1.0"
                rawtext = text.get(startatindex, "insert")
                y.set_code(rawtext)
                y.set_lo(0)

            c = y.get_continuation_type()
            if c != pyparse.C_NONE:
                # The current statement hasn't ended yet.
                if c == pyparse.C_STRING_FIRST_LINE:
                    # After the first line of a string do not indent at all.
                    pass
                elif c == pyparse.C_STRING_NEXT_LINES:
                    # Inside a string which started before this line;
                    # just mimic the current indent.
                    text.insert("insert", indent, self.user_input_insert_tags)
                elif c == pyparse.C_BRACKET:
                    # Line up with the first (if any) element of the
                    # last open bracket structure; else indent one
                    # level beyond the indent of the line with the
                    # last open bracket.
                    self.reindent_to(y.compute_bracket_indent())
                elif c == pyparse.C_BACKSLASH:
                    # If more than one line in this statement already, just
                    # mimic the current indent; else if initial line
                    # has a start on an assignment stmt, indent to
                    # beyond leftmost =; else to beyond first chunk of
                    # non-whitespace on initial line.
                    if y.get_num_lines_in_stmt() > 1:
                        text.insert("insert", indent,
                                    self.user_input_insert_tags)
                    else:
                        self.reindent_to(y.compute_backslash_indent())
                else:
                    assert 0, "bogus continuation type %r" % (c,)
                return "break"

            # This line starts a brand new statement; indent relative to
            # indentation of initial line of closest preceding
            # interesting statement.
            indent = y.get_base_indent_string()
            text.insert("insert", indent, self.user_input_insert_tags)
            if y.is_block_opener():
                self.smart_indent_event(event)
            elif indent and y.is_block_closer():
                self.smart_backspace_event(event)
            return "break"
        finally:
            text.see("insert")
            text.undo_block_stop()
            
def printaf(event=None):
    return af.autocomplete_event(event)
#测试
def test():
    global rden,text,tk,root,af
    import tkinter as tk
    root=tk.Tk()
    root.title('自动补偿窗口测试')
    text=MultiCallCreator(tk.Text)(root,font=('宋体',25),tabs=4)
    #实例化部件对象
    rden=root_dang()
    #加工使用对象(补全)
    af=aut.AutoComplete(rden)
    text.event_add('<<autocomplete>>', '<Key-Tab>')
    text.bind('<Shift_L>',printaf)
    text.bind('<Tab>',printaf)
    text.bind("<<autocomplete>>", af.autocomplete_event)
    text.pack(fill=tk.BOTH)
    
if __name__=="__main__":
    test()
