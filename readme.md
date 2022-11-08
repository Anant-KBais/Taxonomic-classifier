# Taxonomic classification of organisms using ribosomal RNA sequences

## Background
Taxonomical Classification refers to grouping of organisms based on similar characteristics. This has helped in improving their understanding and their identification.

Ribosomal Ribonucleic acid (rRNA) is a universal molecule which is essential for translation of mRNA to proteins. This molecule consists of both highly conserved regions and variable regions, based on which taxonomic classification can be done.
Going beyond classification for the purpose of taxonomic studies, we can identify various pathogens from their sequenced genomic rRNA and use it for their diagnosis.
As per our goals and purpose, we seek to develop classification models for diagnosis using sequence data.

## Description
We are creating a machine learning model which will take the neucleotide data as input and  predict the taxonomic classification of the microorganism as the output.

## Database
[GRD - Genomic based 16s Ribosomal RNA Database](https://metasystems.riken.jp/grd/) has been used to train the models.
GRD is a manually-curated 16S rRNA database, in which both the 5' and 3' regions, including the anti-SD sites, have been carefully checked and contaminating sequences have been removed. 

**Salient Features of Data**
>Contains 2,275 complete and 5,664 draft genome sequences including the Human Microbiome Project (HMP) genome sequences data from NCBI (2013. Feb).
>These sequences were obtained after performing similarity analysis with the 16S rRNA gene sequence annotated in Escherichia coli str. K-12 substr.

___
***
***
# User Manual

*This user manual describes the structure and usage instructions of the Taxonomic classifier software. If you wish to look at the theoretical proof of concept and the principles behind them, kindly see the workflow overview presentation.*

***
## Software Structure

The package consists of 2 main folders, namely-

1. **Data** - It consists of data downloaded from the database, and their transformation into k-mers done by the Code files. Currently, the raw data has been downloaded from the [GRD - Genomic based 16s Ribosomal RNA Database](https://metasystems.riken.jp/grd/).

2. **Code** - It contains the program files which work on the data for various tasks such as data transformation, analysis, machine learning, and prediction pipeline.

***
### Data
1. **Sequence** - This contains the raw 16s rRNA sequences in fasta format downloaded from the database.
2. **Taxonomic_data** - It contains the taxonomic classification of each sequence contained in the sequence file.
3. **k(3)mer-k(7)mer data files** - These are the k-mer representation of the sequence data contained in the Sequence file. The number in parenthesis() indicates the k-mer length. for example, k(5)mer contain kmers of length 5 i.e pentamers.
4. **Metadata**- It consists of the A, T, G, C, and CG percentages present in the raw sequences.
5. **training_result** - It records the performance metrics of various models, deduced experimentally.

***
### Code
1. **Data analyses** - This file consists  data analyses done on the data files in the Data folder.
2. **Dashboard** - It contains the graphic user interface to access the software graphically (as streamlit application).
3. **Functions** - This file contains several important functions which are used in several code files.
4. **Classifier** - this contains the basic gaussian model. Used to test the efficiency of various conventional model structures in making prediction.
5. **Sequence_retriever_NCBI** - This is the application programming interface to retrieve various sequences from the NCBI server, for the purpose of training and testing of models.
6. **Neural_networks** - 
    1. **k(3-7)net.ipynb(jupyter notebooks)** - these contain the code to train various models.
    2. **k(3-7)net files** - These contain the saved models trained from their corresponding jupyter notebooks.
    3. **Composite_model** - Contain the code to evaluate the performance of the composite model(model contaning all the k-nets together).
    4. **Pipeline** - This is the programmatic interface to run the model and get the predictions.

***
## How to...? Guide
***
### Getting predictions-

1. **Using Webapp (streamlit)** - This is remote GUI access(requires internet connection). In your browser enter the url of the taxonomic classifier webapp, enter your personal access key(password), and copy-paste/upload the sequences in the indicated box, and click 'Analyze' to run the model and see the result.

2. **Using pipeline.ipynb jupyter notebook** - This is programmatic local access(doesn't requires internet connection for usage). After having downloaded the software package(the repository), go to Code>Neural_networks>pipeline.ipynb. 
In the jupyter notebook change the default file path to the file path of your "Code" folder. Run all the cells sequentially and input the sequences by either loading the fasta file(by inputting the file path) or by pasting the sequence(s) in the corresponding input code cell. You can get the predictions as the output of the following cells.

***
### Getting sequences

1. **Externally(your own)**- The classifier is flexible enough to handle sequences of any arbitrary length and composition. You can manually download the sequences from [NCBI](https://www.ncbi.nlm.nih.gov/) and use them or go to any other database of your choice and use those sequences or your own ones.

2. **Using 'Sequence_retriever_NCBI' file** - (Requires Internet connection) Go to Code> Sequence_retriever_NCBI.ipynb jupyter notebook and run the code cells. Enter the search query. The sequences will be automatically be loaded. You can download them/ use them directly for model prediction purposes.

***
### Getting Data analysed

To get standard data analyses(meant for modelling purpose) go to Code>Data_analyses.ipynb file. Replace the taxonomic, raw sequence, k-mer file paths with your own multifasta/csv files to get charts and descriptions giving standard insight into the data.
