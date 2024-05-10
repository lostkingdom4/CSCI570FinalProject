import sys
from resource import * 
import time
import psutil

def process_memory():
    process = psutil.Process() 
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss/1024)
    return memory_consumed


def generate_string(base_string, index_list):
    current_string = base_string
    for index in index_list:
        current_string = (current_string[:index + 1] + current_string + current_string[index + 1:])
    return current_string

def read_and_print_file(filename):
    s0 = ''
    s_index = []
    t0 = ''
    t_index = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if s0 == '':
                s0 = line
                continue
            if line.isdigit():
                line = int(line) 
                if t0 == '':
                    s_index.append(line)
                else:
                    t_index.append(line)
                continue
                    
            if t0 == '':
                t0 = line
    return s0,s_index,t0,t_index

def calculate_alignment_cost(X, Y, delta, score):
    m = len(X)
    n = len(Y)
    
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    track = [[-2 for _ in range(n + 1)] for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        dp[i][0] = i * delta
        track[i][0] = 0
    for j in range(1, n + 1):
        dp[0][j] = j * delta
        track[0][j] = 1
    # print(dp)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1]+Y[j-1] in score.keys():
                cost = score[X[i-1]+Y[j-1]]
            else:
                cost = delta
            dp[i][j] = min(dp[i-1][j-1]+cost,dp[i-1][j]+delta,dp[i][j-1]+delta)
            if dp[i][j] == dp[i-1][j-1]+cost:
                track[i][j] = -1
            elif dp[i][j] == dp[i-1][j]+delta:
                track[i][j] = 0
            else:
                track[i][j] = 1
                
    resultx = ''
    resulty = ''
    a = m
    b = n
    while a != 0 or b !=0:
        indicator = track[a][b]
        if indicator == 0:
            resultx += X[a-1]
            resulty += '_'
            a = a-1
            
        if indicator == 1:
            resulty += Y[b-1]
            resultx += '_'
            b = b-1
            
        if indicator == -1:
            resultx += X[a-1]
            resulty += Y[b-1]
            a = a-1
            b = b-1
            
    memory_consumed = process_memory()
    return dp[m][n],resultx[::-1],resulty[::-1],memory_consumed

def time_wrapper(X, Y, delta, score):
    start_time = time.time()
    cost, x_a, y_a, memory_consumed = calculate_alignment_cost(X, Y, delta, score)
    end_time = time.time()
    time_taken = (end_time - start_time)*1000 
    return cost, x_a, y_a, time_taken, memory_consumed

def writeIntoFIle(results, fileName):
    with open(fileName, 'w') as f:
        f.writelines("%s\n" % string for string in results)

def main(inputFileName,outputFileName):
    # Usage
    filename = inputFileName
    s0,s_index,t0,t_index = read_and_print_file(filename)
    Final_s = generate_string(s0,s_index)
    Final_t = generate_string(t0,t_index)

    delta = 30
    mismatch_cost = {
            "__":30,
            "_A":30, "_C":30, "_G":30, "_T":30,
            "A_":30, "C_":30, "G_":30, "T_":30, 
            "AA":0, "CC":0, "GG":0, "TT":0,
            "AC":110, "AG":48, "AT":94,
            "CA":110, "CG":118, "CT":48,
            "GA":48, "GC":118, "GT":110,
            "TA":94, "TC":48, "TG":110
            }

    results = time_wrapper(Final_s, Final_t, delta, mismatch_cost)
    writeIntoFIle(results, outputFileName)

if __name__ == '__main__':
    arguments = sys.argv

    inputFileName = arguments[1]
    outputFileName = arguments[2]
    main(inputFileName,outputFileName)
