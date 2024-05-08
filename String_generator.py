def generate_string(base_string, index_list):
    current_string = base_string
    for index in index_list:
        # Insert the current string into itself at the specified index
        current_string = (current_string[:index + 1] + current_string + current_string[index + 1:])
        print(current_string)
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

# Usage
filename = 'Project/Project/SampleTestCases/input1.txt'
s0,s_index,t0,t_index = read_and_print_file(filename)
print(s0,s_index,t0,t_index)
Final_s = generate_string(s0,s_index)
Final_t = generate_string(t0,t_index)


check = '_A_CA_CACT__G__A_C_TAC_TGACTG_GTGA__C_TACTGACTGGACTGACTACTGACTGGTGACTACT_GACTG_G'
clean_string = check.replace("_", "")
print(Final_s==clean_string)
check = 'TATTATTA_TACGCTATTATACGCGAC_GCG_GACGCGTA_T_AC__G_CT_ATTA_T_AC__GCGAC_GC_GGAC_GCG'
clean_string = check.replace("_", "")
print(Final_t==clean_string)

# filename = 'Project/Project/SampleTestCases/input2.txt'
# s0,s_index,t0,t_index = read_and_print_file(filename)
# print(s0,s_index,t0,t_index)
# filename = 'Project/Project/SampleTestCases/input3.txt'
# s0,s_index,t0,t_index = read_and_print_file(filename)
# print(s0,s_index,t0,t_index)
# filename = 'Project/Project/SampleTestCases/input4.txt'
# s0,s_index,t0,t_index = read_and_print_file(filename)
# print(s0,s_index,t0,t_index)
# filename = 'Project/Project/SampleTestCases/input5.txt'
# s0,s_index,t0,t_index = read_and_print_file(filename)
# print(s0,s_index,t0,t_index)

