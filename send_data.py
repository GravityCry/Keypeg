import subprocess, pexpect

host = 'alucard.csc.depauw.edu'
dst = '/home/LDAPdir/qnguyen19/'
user = 'qnguyen19'
pwd = 'quannguyen135'

def send(filepath):
    child = pexpect.spawn(f'scp {filepath} {user}@{host}:{dst}')
    child.expect(f"{user}@{host}s password:'")
    child.sendline(pwd)
    child.expect(pexpect.EOF, timeout=None)

    stdout = child.before
    cmd_output = stdout.split('\r\n')
    for data in cmd_output:
        print(data)
