import subprocess

host = 'alucard.csc.depauw.edu'
dst = '/home/LDAPdir/qnguyen19/'
user = 'qnguyen19'
pwd = 'quannguyen135\n'

def send(filepath):
    command = f'scp {filepath} {user}@{host}:{dst}'
    print(command)
    p = subprocess.Popen(command, shell=True,
        stdin=subprocess.PIPE, stderr=subprocess.PIPE)
    #p.stdin.write(pwd.encode())
    stdout, stderr = p.communicate(pwd.encode())

if __name__ == '__main__':
    send('output.txt')
