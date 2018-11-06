import pexpect
from pexpect.popen_spawn import PopenSpawn

host = 'alucard.csc.depauw.edu'
dst = '/home/LDAPdir/qnguyen19/'
user = 'qnguyen19'
pwd = 'quannguyen135'

def send(filepath):
    command = f'scp {filepath} {user}@{host}:{dst}'
    print(command)
    child = PopenSpawn(command)
    i = child.expect([f"{user}@{host}'s password:", f"{user}@{host}'s password: ", '[#\$]'])
    print(i)
    #child.expect("qnguyen19@alucard.csc.depauw.edu's password:")
    child.sendline(pwd)
    child.expect(pexpect.EOF, timeout=None)

    stdout = child.before.decode()
    cmd_output = stdout.split('\r\n')
    for data in cmd_output:
        print('Output:', data)

if __name__ == '__main__':
    send('output.txt')
