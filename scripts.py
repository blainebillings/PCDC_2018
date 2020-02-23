import os, time
def fs(l):
    a = l[l.rfind(' ')+1:-1]
    return a[a.rfind('/')+1:]
ls = lambda l, i: l.split()[i]
cm = lambda c : os.popen(c).readlines()
ps = lambda : cm('sudo ps -aux')[1:]
sv = lambda : cm('sudo systemctl -a --plain')
pw = lambda : cm('(sudo cat /etc/passwd | awk \'{print "PWD: " $0}\' && sudo cat /etc/shadow | awk \'{print "SHD: " $0}\')')
nl = lambda o : o[:o.index("\n")]
p_s = [fs(l)[fs(l).rfind('/')+1:] for l in cm('sudo cat /etc/shells')[1:]]
r_r = [ls(l, 1) for l in ps() if fs(l) in p_s]
c_s = {ls(l, 0): ls(l, 2) for l in nl(sv())}
i_p = pw()
while True:
    time.sleep(0.1)
    r_r = [len(r_r) + 1] + r_r + [l for l in ps() if fs(l) in p_s]
    print(''.join('NEW SHL: shell=' + fs(l) + ', pid=' + ls(l, 1) + '|' + l[:-1] + "\n" for l in r_r[r_r[0]:] if ls(l, 1) not in r_r[:r_r[0]]), end='')
    r_r = [ls(l, 1) for l in r_r[r_r[0]:]]
    o_l = nl(sv())
    print(''.join('SRV ' + ('ADD: ' if ls(l, 0) not in c_s.keys() else 'CHN: ') + ls(l, 0) + ':' + ls(l, 2) + str(c_s.update({ls(l, 0): ls(l, 2)})) * 0 + '\n' for l in o_l if ls(l, 0) not in c_s.keys() or c_s[ls(l, 0)] != ls(l, 2)), end='')
    print(''.join('SRV DEL: ' + c_s.pop(l) + "\n" for l in list(c_s.keys()) if l not in [ls(k, 0) for k in o_l]), end='')
    print(''.join(('DEL ' + i_p.pop(i_p.index(l))[:-1] if l in i_p else 'ADD ' + (l[:-1] + str(i_p.append(l)) * 0)) + "\n" for l in set(i_p)^set(pw())), end='')
