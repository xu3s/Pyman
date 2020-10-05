# import subprocess
# import os

# #tsh = subprocess.Popen(['/home/exel/mhserver/AdhocServer'], stdout= subprocess.PIPE)
# os.popen('screen -S mhserver sh /home/exel/mhserver/AdhocServer')




# import subprocess
# import tempfile

# with tempfile.TemporaryFile() as tempf:
#     proc = subprocess.Popen(['echo', 'a', 'b'], stdout=tempf)
#     proc.wait()
#     tempf.seek(0)
#     print tempf.read()



from subprocess import Popen, PIPE

def run(command):
    process = Popen(command, stdout=PIPE, shell=True)
    while True:
        line = process.stdout.readline().rstrip()
        if not line:
            break
        yield line


if __name__ == "__main__":
    for path in run("/home/exel/mhserver/AdhocServer"):
        print (path)