import paramiko

def sshclient_execmd(hostname='ddns.rockchen26sh.top',
                    port=22,
                    username='liunx',
                    password='28488747',
                    execmd='free'):
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    s.connect(hostname=hostname,port=port,username=username,password=password)
    stdin, stdout, stderr = s.exec_command(execmd)
    stdin.write("Y")
    print (stdout.read())
    s.close()
