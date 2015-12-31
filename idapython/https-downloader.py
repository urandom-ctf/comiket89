import re
import idaapi

PAT_TITLE   = re.compile(r' *<title>[^<]*</title> *')
NEWTITLE    = '<title>mikudayo-</title>'

def bpt_fwrite():
    # (3)
    RefreshDebuggerMemory()
    size = Dword(cpu.esp + 0x04)    # cpu.edx
    ptr = Dword(cpu.esp + 0x00)     # cpu.eax
    text = DbgRead(ptr, size)

    # (4)
    matchobj = next(PAT_TITLE.finditer(text))
    mstart, mend = matchobj.start(0), matchobj.end(0)
    titlelen = mend - mstart

    # (5)
    if titlelen < len(NEWTITLE):
        return True
    else:
        newtitle = ' ' * (titlelen - len(NEWTITLE)) + NEWTITLE 
        DbgWrite(ptr + mstart, newtitle)
        return False

# (1)
fwrite_call = next(CodeRefsTo(
    next(CodeRefsTo(
        LocByName("fwrite"),
        False
    )),
    False
))

# (2)
idaapi.enable_extlang_python(True)
AddBpt(fwrite_call)
SetBptCnd(fwrite_call, "return bpt_fwrite();")