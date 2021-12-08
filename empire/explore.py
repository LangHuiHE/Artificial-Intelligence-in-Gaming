#!/usr/bin/env python3

import sys
import subprocess
import re
import copy
import time
import os

def get_map(empire_command):
    args = empire_command.split()
    client_process = subprocess.Popen(args, shell=False,
                                      encoding="utf-8",
                                      stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    client_process.stdin.write("map *\n")
    client_process.stdin.flush()

    client_process.stdin.write("quit\n")
    client_process.stdin.flush()
    
    client_process.wait()
    lines = []
    for line in client_process.stdout:
        line = line.rstrip()
        match = re.match('^.* Command : (.+)$', line)
        if match:
            line = match.group(1)
        if re.match('^$', line):
            continue
        if re.match('^[ \t]*-=O=-$', line):
            continue
        if re.match('telegram', line):
            print("SKIPPING:", line)
            continue
        if re.match('^Bye-bye$', line):
            continue
        if re.match('^Exit:', line):
            continue
        lines.append(line.rstrip())
    
    return lines

def run_commands(empire_command, cmds):
    args = empire_command.split()
    client_process = subprocess.Popen(args, shell=False,
                                      encoding="utf-8",
                                      stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    for cmd in cmds:
        client_process.stdin.write("{}\n".format(cmd))
        client_process.stdin.flush()

    time.sleep(1)
    client_process.stdin.write("quit\n")
    client_process.stdin.flush()
    
    client_process.wait()

    for line in client_process.stdout:
        line = line.rstrip()
        print(line)
    
    return

g_digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '-': 0, ' ': 99999999, }
def calculate_x_position(position, x_positions):
    value = 0
    for row in range(len(x_positions)):
        value *= 10
        c = x_positions[len(x_positions) - 1 - row][position]
        value += g_digit[c]

    i_zero = 0
    for i in range(len(x_positions[0])):
        ok = True
        for j in range(len(x_positions)):
            if x_positions[j][i] != '0':
                ok = False
        if ok:
            i_zero = i
            break
    if position < i_zero:
        value = -value
    return value

def parse_map(map_lines):
    header = 0
    while re.match('^( *)([0-9-]+)( *)$', map_lines[header]):
        header += 1
    header -= 1
    footer = len(map_lines) - 1
    while re.match('^( *)([0-9-]+)( *)$', map_lines[footer]):
        footer -= 1
    footer += 1

    x_positions = []
    for i in range(header, -1, -1):
        x_positions.append(map_lines[i])

    x_values = []
    for i in range(len(x_positions[0])):
        x = calculate_x_position(i, x_positions)
        x_values.append(x)

    y_values = []
    for i in range(len(map_lines)):
        if i <= header:
            y_values.append(99999999)
        elif i >= footer:
            y_values.append(99999999)
        else:
            match = re.match('^ *([0-9-]+) .*$', map_lines[i])
            if match:
                y = int(match.group(1))
            else:
                y = 99999999
            y_values.append(y)

    # print(x_values)
    # print(y_values)

    # print("\n".join(map_lines[header+1:footer]))

    sectors = {}
    for i in range(len(x_positions[0])):
        if abs(x_values[i]) > 1000000:
            continue
        for j in range(len(map_lines)):
            if abs(y_values[j]) > 1000000:
                continue
            key = x_values[i], y_values[j]
            if map_lines[j][i] != ' ':
                sectors[key] = map_lines[j][i]
    
    return sectors


g_deltas = { 
    'u': (1,-1),
    'y': (-1,-1),
    'j': (2,0),
    'g': (-2,0),
    'n': (1,1),
    'b': (-1,1),
    #'h': (0,0),
}

def explore(src, src_path, sectors):
    paths = {}
    children = []
    for delta in g_deltas:
        key = (src[0] + g_deltas[delta][0], src[1] + g_deltas[delta][1])
        key_path = src_path + delta
        if key in sectors and sectors[key] == '-':
            paths[key] = key_path + 'h'
        if key in sectors and sectors[key] != 'X' and sectors[key] != '.':
            children.append((key, key_path))
            sectors[key] = 'X'
    for child in children:
        paths.update(explore(child[0], child[1], sectors))

    return paths

def explore_wilderness(sectors):
    src = (0,0)
    cmds = []
    if src in sectors:
        paths = explore(src, "", copy.deepcopy(sectors))
        for key in paths:
            cmd = "expl civ {},{} {} {}".format(0, 0, 1, paths[key])
            cmds.append(cmd)
            cmd = "des {},{} {}".format(key[0], key[1], '+')
            cmds.append(cmd)
    return cmds

def main(argv):
    EMPIREHOST = os.getenv("EMPIREHOST")
    EMPIREPORT = os.getenv("EMPIREPORT")
    COUNTRY = os.getenv("COUNTRY")
    PLAYER = os.getenv("PLAYER")
    if len(EMPIREHOST) == 0:
        print("Expected EMPIREHOST environment variable to be set.")
        sys.exit(1)
    if len(EMPIREPORT) == 0:
        print("Expected EMPIREPORT environment variable to be set.")
        sys.exit(1)
    if len(COUNTRY) == 0:
        print("Expected COUNTRY environment variable to be set.")
        sys.exit(1)
    if len(PLAYER) == 0:
        print("Expected PLAYER environment variable to be set.")
        sys.exit(1)
    empire_command = "/usr/citlocal/cs4300/bin/empire"
    lines = get_map(empire_command)
    #print("\n".join(lines))
    sectors = parse_map(lines)
    # print(sectors)
    cmds = explore_wilderness(sectors)    
    for cmd in cmds:
        print(cmd)
    run_commands(empire_command, cmds)
    return

if __name__ == "__main__":
    main(sys.argv)
    
