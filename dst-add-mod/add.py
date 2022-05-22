import re
import platform



mod_loc = 'C:\Program Files (x86)\Steam\steamapps\common\Don\'t Starve Together Dedicated Server\mods'
loc = mod_loc + 'dedicated_server_mods_setup.lua'

local = open("./modoverrides.lua", 'r')
server = open("./dedicated_server_mods_setup.lua", 'r')

if platform.system == 'Windows':
    server = open(loc, 'r')

server_mods = []
line = server.readline()
while line:
    if re.search(r'ServerModSetup', line):
        server_mod_num = re.sub(r'\D', "", line)
        server_mods.append(server_mod_num)
    line = server.readline()
server.close()

line = local.readline()
while line:
    if re.search(r'workshop-', line):
        local_mod_num = re.sub(r'\D', "", line)
        if local_mod_num not in server_mods:
            f = open("./server2.lua", 'a')
            f.write('\n' + '\t' +
                    f'ServerModSetup("{local_mod_num}")'.format(local_mod_num))
    line = local.readline()
