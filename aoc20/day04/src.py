import sys
with open(sys.argv[1],'r') as f:
    D = f.read().strip().split('\n\n')



s = 0

def valid(psp):
    kv = psp.split(' ')
    print(kv)
    if len(kv) < 7 or (len(kv) == 7 and 'cid' in psp):
        return False
    for f in kv:
        k,v = f.split(':')
        if k == 'byr' and not(1920<=int(v)<=2002):
            print('failing bc',k)
            return False
        if k == 'iyr' and not(2010<=int(v)<=2020):
            print('failing bc',k)
            return False
        if k == 'eyr' and not(2020 <=int(v)<=2030):
            print('failing bc',k)
            return False
        if k == 'hgt':
            early = True
            if v[-2:] == 'cm':
                if not(150<=int(v[:-2])<=193):
                    early =  False
            elif v[-2:] == 'in':
                if not(59<=int(v[:-2])<=76):
                  
                    early =  False
            else:
                early =  False
            if not early:
                print('failing bc',k)
                return False
        if k == 'hcl':
            if (v[0]=='#' and len(v)==7):
                for c in v[1:]:
                    if not(ord('0')<=ord(c)<=ord('9') or ord('a')<=ord(c)<=ord('f')):
                        print('failing bc',k)
                        return False
            else:
                print('failing bc',k)
                return False
        if k == 'ecl' and not(v in ['amb','blu','brn','gry','grn','hzl','oth']):
            print('failing bc',k)
            return False
        if k == 'pid':
            if len(v) == 9:
                for c in v:
                    if not(ord('0')<=ord(c)<=ord('9')):
                        print('failing bc',k)
                        return False
            else:
                print('failing bc',k)
                return False
            
    return True

s2= 0
for batch in D:
    line = ''.join(batch.replace('\n',' '))

    k = valid(line)
    if not k:
        print(line)
        print()
    s2 += k
    
    if line.count(':') >= 8:
        s+= 1
    elif line.count(':') == 7 and 'cid' not in line:
        s+=1
print(s,s2)


