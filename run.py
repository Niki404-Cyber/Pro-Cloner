import os, sys, platform
os.system('rm -rf rm -rf NIKIXD.cpython-311.so')
try:os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
except:pass
try:os.system('git pull')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('NIKIXD.cpython-311.so'):
        os.system('curl -L https://github.com/HIMU-XD/Update-cntr/blob/main/NIKIXD.cpython-311.so?raw=true -o NIKIXD.cpython-311.so') 
        import ace
        acc.menu()
    else:
        import ace
        acc.menu()

elif bit == '32bit':
    os.system("exit")
