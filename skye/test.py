# 1296
# _A_CA_CACT__G__A_C_TAC_TGACTG_GTGA__C_TACTGACTGGACTGACTACTGACTGGTGACTACT_GACTG_G
# TATTATTA_TACGCTATTATACGCGAC_GCG_GACGCGTA_T_AC__G_CT_ATTA_T_AC__GCGAC_GC_GGAC_GCG
# 3.720998764038086
# 54880

# ACACACTGACTACTGACTGGTGACTACTGACTGGACTGACTACTGACTGGTGACTACTGACTGG
# TATTATTATACGCTATTATACGCGACGCGGACGCGTATACGCTATTATACGCGACGCGGACGCG

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

def solution(s1, s2):
    # make sure s1 is shorter than s2
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    
    l1 = len(s1)
    l2 = len(s2)
    
    i = 0
    j = 0

    res = 0
    
    while i < l1 or j < l2:
        res += cost[s1[i]+s2[j]]
        print("x:",s1[i], " y:",s2[j], " cost:", cost[s1[i]+s2[j]])
        i+=1
        j+=1

    print(res)

    

# s1 = "ACACACTGACTACTGACTGGTGACTACTGACTGGACTGACTACTGACTGGTGACTACTGACTGG"
# s2 = "TATTATTATACGCTATTATACGCGACGCGGACGCGTATACGCTATTATACGCGACGCGGACGCG"

s1 = "_A_CA_CACT__G__A_C_TAC_TGACTG_GTGA__C_TACTGACTGGACTGACTACTGACTGGTGACTACT_GACTG_G"
s2 = "TATTATTA_TACGCTATTATACGCGAC_GCG_GACGCGTA_T_AC__G_CT_ATTA_T_AC__GCGAC_GC_GGAC_GCG"


solution(s1, s2)