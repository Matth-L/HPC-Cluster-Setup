# inspired by: /usr/lib64/nagios/plugins/ in the slurm vm 

import os
import sys
import optparse
import subprocess
try:
    import paramiko
except ImportError:
    print("ERROR : this plugin needs the python-paramiko module. Please install it")
    sys.exit(2)

# Load plugin utils
my_dir = os.path.dirname(__file__)
sys.path.insert(0, my_dir)

try:
    import schecks
except ImportError:
    print("ERROR : this plugin needs the local schecks.py lib. Please install it")
    sys.exit(2)

VERSION = "0.1" 

def execute_slurm_check(client, command):
    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode().strip()
    client.close()

    return output

# [matthias.lapu@hpc01 ~]$ sinfo
# PARTITION AVAIL  TIMELIMIT  NODES  STATE NODELIST
# inter        up   infinite      2   idle hpc[02-03]
# calcul*      up   infinite     10   idle hpc[04-13]

def parse_slurm_output(output, partition):
    lines = output.split('\n')
    for line in lines:
        if partition in line:
            data = line.split()
            if data[1] == "up":
                return "OK: Partition %s is up" % partition
            else:
                return "Partition %s is down" % partition


parser = optparse.OptionParser(
    "%prog [options]", version="%prog " + VERSION)
parser.add_option('-H', '--hostname',
                  dest="hostname", help='Hostname to connect to')
########Added ########
parser.add_option('--partition',
                  dest="partition", help='Partition name to check the availability')
######################
parser.add_option('-p', '--port',
    dest="port", type="int", default=22,
    help='SSH port to connect to. Default : 22')
parser.add_option('-i', '--ssh-key',
                  dest="ssh_key_file", help='SSH key file to use. By default will take ~/.ssh/id_rsa.')
parser.add_option('-u', '--user',
                  dest="user", help='remote use to use. By default shinken.')
parser.add_option('-P', '--passphrase',
                  dest="passphrase", help='SSH key passphrase. By default will use void')
parser.add_option('-r', '--check_path',
                  dest="check_path", help='Path of the remote perfdata check to execute')


if __name__ == '__main__':
    opts, args = parser.parse_args()
if args:
    parser.error("Does not accept any argument.")

if not opts.hostname:
    print("Error : hostname parameter (-H) is mandatory")
    sys.exit(2)

# we must check the command is used properly
# we need the partition, warning and critical thresholds
partition = opts.partition
if not partition:
    print("Error : partition parameter (--partition) is mandatory")
    sys.exit(2)
warning = opts.warning
if not warning:
    print("Error : warning parameter (-w) is mandatory")
    sys.exit(2)
critical = opts.critical
if not critical:
    print("Error : critical parameter (-c) is mandatory")
    sys.exit(2)

client= schecks.connect_ssh(opts.hostname, opts.port, opts.user, opts.ssh_key_file, opts.passphrase)
output = execute_slurm_check(client, partition)
result = parse_slurm_output(output, opts.threshold)
print(result)
sys.exit(0)