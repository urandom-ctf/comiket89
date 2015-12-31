SEARCH_DIST = 5

# (3)
def search_pushval(ea, left):
    if left == 0:
        return []

    val = [DecodeInstruction(ea).Op1.value] \
        if GetMnem(ea) == 'push'            \
        else []

    return sum((
            search_pushval(r, left-1) for r in CodeRefsTo(ea, True)
        ),
        val
    )

# (4)
def decrypt_string(s, k):
    decs = ''
    while Byte(s):
        decs += chr(Byte(s) ^ k)
        s += 1
    return decs

# (1)
decstr = LocByName("decrypt_string")

# (2)
args = tuple(
    search_pushval(r, SEARCH_DIST) for r in CodeRefsTo(decstr, False)
)

# (4)
for a in args:
    s, k = a[:2]
    decs = decrypt_string(s, k)
    for r in DataRefsTo(s):
        MakeRptCmt(r, 'Decrypted: "%s"' % decs)
