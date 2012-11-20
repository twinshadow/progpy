ctlstr = 'one.two.three'
value = {'value':1, 'type':'uint'}
ctldict = {}
for f in ctlstr.split('.')[::-1]:
    hold = {}
    if value:
        hold[f] = value
        value = None
    else:     hold[f] = {}
    hold[f].update(ctldict)
    ctldict = hold

print ctldict
