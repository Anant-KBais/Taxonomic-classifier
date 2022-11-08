import streamlit as st
import  pandas as pd
from Bio import SeqIO, Seq

st.set_page_config(
   page_title="Dashboard",
   page_icon="📊",
   layout="wide",
   initial_sidebar_state="expanded",
)
st.title("Taxonomic Classification of Organisms")
st.title('NTCC Report')
st.text('Pragya Mishra     BTBM/19/126')
def check(data, text):
    check = st.checkbox(text)
    if check:
        st.write(data)

@st.cache(hash_funcs= {Seq.Seq: hash})
def load_fasta(file):
    sequences = []
    for seq_record in SeqIO.parse(file, 'fasta'):
        sequences.append(seq_record.seq)
    return sequences

data= pd.read_csv(r"C:\Users\anant\Documents\GitHub\Taxonomic_classifier\Data\Taxonomic_data.csv")
check(data, 'Show taxonomic data')


sequences = load_fasta(r'C:\Users\anant\Documents\GitHub\Taxonomic_classifier\Data\sequence.fasta')

size = [len(rec) for rec in sequences]

import matplotlib.pyplot as plt

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 3}

fig, ax = plt.subplots()
bin = st.slider("resolution", 1, 70, 40)
ax.hist(size, bins=bin)
fig.set_figwidth(4)
fig.set_figheight(1)
st.pyplot(fig)


from Bio.SeqUtils import GC
gc_val = sorted(GC(content) for content in sequences)

st.line_chart(gc_val)

check(data.describe().to_markdown(), "Show Taxonomy description")
check(sequences[0:5], 'Show sequences`')

