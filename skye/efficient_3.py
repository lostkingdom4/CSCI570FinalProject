import sys
from resource import * 
import time 
import psutil

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
            # print("line: ",line)
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


def writeIntoFIle(results, fileName):
    # Open a file in write mode ('w')
    with open(fileName, 'w') as f:
        # Write each string in the list to a separate line
        f.writelines("%s\n" % string for string in results)


def efficient_solution(seq1, seq2, cost_matrix):
    # Lengths of input sequences
    m = len(seq1)
    n = len(seq2)
    
    # Initialize the previous row of the DP matrix
    prev_row = [i * cost_matrix["_" + seq2[0]] for i in range(n + 1)]
    
    # Initialize variables to store the current row and the previous diagonal value
    current_row = [0] * (n + 1)
    prev_diagonal = 0
    
    # Initialize traceback matrix
    traceback = [[None] * (n + 1) for _ in range(m + 1)]
    
    # Fill the dynamic programming matrix
    for i in range(1, m + 1):
        # Store the current value of the first column
        current_row[0] = i * cost_matrix[seq1[i - 1] + "_"]
        
        for j in range(1, n + 1):
            # Calculate the three values for the current step
            diag = prev_row[j - 1] + cost_matrix[seq1[i - 1] + seq2[j - 1]]
            up = prev_row[j] + cost_matrix[seq1[i - 1] + "_"]
            left = current_row[j - 1] + cost_matrix["_" + seq2[j - 1]]
            
            # Choose the minimum value and update the current step
            current_row[j] = min(diag, up, left)
            
            # Update the traceback matrix
            if current_row[j] == diag:
                traceback[i][j] = 'diag'
            elif current_row[j] == up:
                traceback[i][j] = 'up'
            else:
                traceback[i][j] = 'left'
        
        # Update the previous diagonal value and the previous row
        prev_diagonal = prev_row[0]
        prev_row = current_row[:]
    
    # Traceback to find the alignment
    align1 = []
    align2 = []
    i, j = m, n
    while i > 0 or j > 0:
        if traceback[i][j] == 'diag':
            align1.append(seq1[i - 1])
            align2.append(seq2[j - 1])
            i -= 1
            j -= 1
        elif traceback[i][j] == 'up':
            align1.append(seq1[i - 1])
            align2.append('_')
            i -= 1
        else:
            align1.append('_')
            align2.append(seq2[j - 1])
            j -= 1
    
    # Reverse the alignment sequences
    alignment1 = ''.join(align1[::-1])
    alignment2 = ''.join(align2[::-1])
    
    # Calculate the minimum cost
    min_cost = current_row[n]
    
    return alignment1, alignment2, min_cost


def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss/1024)
    return memory_consumed


# Cost matrix
cost = {
    "__":30,
    "_A":30, "_C":30, "_G":30, "_T":30,
    "A_":30, "C_":30, "G_":30, "T_":30, 
    "AA":0, "CC":0, "GG":0, "TT":0,
    "AC":110, "AG":48, "AT":94,
    "CA":110, "CG":118, "CT":48,
    "GA":48, "GC":118, "GT":110,
    "TA":94, "TC":48, "TG":110
}


if __name__ == "__main__":

    arguments = sys.argv

    inputFileName = arguments[1]
    outputFileName = arguments[2]

    s0,s_index,t0,t_index = read_and_print_file(inputFileName)

    seq1 = generate_string(s0,s_index)
    seq2 = generate_string(t0,t_index)

    # print(seq1, seq2)
    
    # Measure running time
    start_time = time.time()
    
    aligned_seq1, aligned_seq2, alignment_cost = efficient_solution(seq1, seq2, cost)
    
    end_time = time.time()
    time_taken = (end_time - start_time) * 1000 

    # Measure memory consumption 
    mem_consumed =  process_memory()

    print("Datapoint:", inputFileName)
    print("Alignment Cost:", alignment_cost)
    print("Aligned Sequence 1:", aligned_seq1)
    print("Aligned Sequence 2:", aligned_seq2)
    print("Running time:", time_taken, "ms")
    print("Memory consumed:", mem_consumed, "KB")

    writeIntoFIle([alignment_cost, aligned_seq1, aligned_seq2, time_taken, mem_consumed], outputFileName)