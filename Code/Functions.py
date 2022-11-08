from Bio import  SeqUtils
import pandas as pd
import numpy as np
from copy import deepcopy


# This function returns the unique nucleotides in a sequence and their count
def bases(sequences):
    unique = {}
    for seq in sequences:
        for nucleotide in seq:
            if nucleotide not in unique:
                unique[nucleotide] = 1
            else:
                unique[nucleotide] += 1
    return unique



# the k_mer_generator take size of the k_mer as input and returns all the possible kmers
def k_mer_generator(k,sequences, seq= ''  ):
    
    nucleotides = ['A','T', 'C', 'G']
  
    for base in nucleotides:
        if len(seq) < k:   
            seq += base    
            sequences, seq = k_mer_generator(k,sequences, seq)
        else:
            sequences.append(seq)
            
            break
        seq = seq[0:-1]
 
        if len(sequences)==4**k and seq == '':
            k_mers = deepcopy(sequences)
            del(sequences)
            return k_mers   

    return sequences, seq



# the following code calculates the frequency of each k mer in each of the sequences-
#  and returns their occurance as a dataframe
def k_mer_finder(fasta_seq, k_mers):
    t_freq = np.empty(0)
    freqns = np.empty(0)
    for f_seq in fasta_seq:
        for seq in k_mers:
            freq = len(SeqUtils.nt_search(str(f_seq), seq))-1
            freqns = np.append(freqns, freq)
        t_freq = np.append(t_freq, freqns )
        freqns = np.empty(0)

    conv_data = pd.DataFrame(data=t_freq.reshape(len(fasta_seq),len(k_mers)), columns=k_mers)
    return conv_data


# the following code calculates the a,t,g,c, cg percentages for each sequence
def atgc_cg(fasta_seq):
    A=[]
    T =[]
    C = []
    G = []
    CG = []
    for seq in fasta_seq:
        length = len(seq)
        A.append(seq.count('A')/length)
        T.append(seq.count('T')/length)
        C.append(seq.count('C')/length)
        G.append(seq.count('G')/length)
        CG.append(seq.count("CG")/length)
    all = {"A":A,"T": T, "C":C, "G":G, "CG":CG}
    data = pd.DataFrame(all)
    return data

