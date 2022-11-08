
##########################################################################################################################
# Load modules and environment variables
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

Sequence = os.getenv('SEQUENCE')
K7_PATH = os.getenv('K7_PATH')
K6_PATH = os.getenv('K6_PATH')
K5_PATH = os.getenv('K5_PATH')
K4_PATH = os.getenv('K4_PATH')
K3_PATH = os.getenv('K3_PATH')
RETMAX = os.getenv('RETMAX')
CODE_PATH = os.getenv('CODE_PATH')
TAXONOMIC_PATH = os.getenv('TAXONOMIC_PATH')
print(CODE_PATH)

from sklearn.model_selection import train_test_split
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
from Functions import k_mer_generator, k_mer_finder
from Bio import SeqIO
from sklearn.decomposition import PCA
from sklearn import preprocessing
from Bio import Entrez
from Bio import SeqIO
import sys
sys.path.append(r"C:\Users\anant\Documents\GitHub\Taxonomic_classifier\Code")

####################################################################################################################################
#fetch data
handle = Entrez.esearch(db="nucleotide", term="nuclear 16srRNA", retmax="5" )
record = Entrez.read(handle)
handle = Entrez.efetch(db='nucleotide', rettype= 'fasta',retmode='text',id = record['IdList'])
fasta_seq = []
for seq_record in SeqIO.parse(handle, 'fasta'):
    fasta_seq.append(seq_record.seq)


##############################################################################################################################
# Kmer-generation
conv_data = []
for x in [3,4,5,6,7]:

    k_mers = k_mer_generator(x, sequences=[])  #generate kmers
    data = k_mer_finder(fasta_seq, k_mers)
    conv_data.append([data])

x3 ,x4, x5, x6, x7 = conv_data

#########################################################################################################################################
# Model generation
for x , X  in zip(conv_data, [3,4,5,6,7]):
    x.to_csv(f"k{X}mer")
    y = pd.read_csv(TAXONOMIC_PATH, usecols=['Species'])
    pca = PCA(n_components=0.95)
    xx = pca.fit_transform(x)
    pca.inverse_transform(xx)
    pca.explained_variance_ratio_.sum()
    print(f"{x.shape[1]} columns originally present, \n{pca.n_components_} account for 95 percent variance ")
    print(f"corresponds to {100*pca.n_components_/x.shape[1]}% of total")

    train_x, test_x, train_y, test_y = train_test_split(xx, y, test_size=0.2, random_state=7)

    model = Sequential()
    model.add(Dense(20, input_shape =(None, train_x.shape[1]) , activation="relu"))
    model.add(Dense(len(y.Species.unique()),activation='softmax'))

    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])
    model.summary()

    
    lb = preprocessing.LabelBinarizer()
    lb.fit(y)
    test_y = lb.transform(test_y)
    train_y = lb.transform(train_y)

    model.fit(train_x, train_y, epochs = 25)

    model.save(f"k{X}-net")