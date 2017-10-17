#Query Classifier for Clarity Medical 

This program supports the training of and prediction with “main” and “clerical” logistic regression classifiers, where the “main” model classifies according to clinical, clerical, and other, and the “clerical” classifier classifies according to (currently) 7 different stock clerical question classes. This program additionally supports the editing/maintenance of a file called data_store_df.csv, which serves as an inventory of all data sources currently available to the program (more info below). Most of these APIs can be run by first importing their corresponding classes in the Python interpreter. Additionally, the Predict.py module can be run from the command line.

##The directory structure, and (current) files are as follow:

###~/

1. LogRegr.py : module contain the logistic regression classifier
2. Predict.py : module for running prediction using the trained models
3. Preprocessing.py : module for preprocessing of data
4. Tests.py : module containing API tests
5. Train.py : module for training the models
6. data_store_df.csv : spreadsheet serving as inventory for available data sets
7. README.md
8. Main_model.pkl : the trained main model
9. cler_model.pkl : the trained clerical model
10. GoogleNews-vectors-negative300.bin : the pretrained Google word vectors
11. requirements.txt : lists program requirements; generated automatically using pigar. Please ensure all listed packages are installed by running `pip install -r requirements.txt —no-cache-dir`

PLEASE NOTE THAT YOU MUST PLACE THE FILE GoogleNews-vectors-negative300.bin.gz IN THIS DIRECTORY & UNZIP IT. IT IS NOT INCLUDED IN THIS REPO BECAUSE IT IS TOO LARGE. YOU CAN DOWNLOAD IT FROM http://mccormickml.com/2016/04/12/googles-pretrained-word2vec-model-in-python/. OR, I CAN SHARE IT WITH YOU FROM MY DROPBOX FOLDER.



###~/data/

---VARIOUS DATA FILES; LOOK AT data_store_df.csv FOR DETAILS\


##API info


###Preprocessing.DataStoreManager class

Used for loading, editing, and saving the file "data_store_df.csv," which records the different sources of available data and relevant details about these sources. The API defined by this class will be important as you add additional data and remove old data, or as you adjust how much data from each source you want to include. For description of methods, see the docstrings included in each method’s definition.


###Train.Trainer class

This class is used to train the main and clerical models. You will need to use this module if you want to retrain models as you add additional / remove data. For a description of methods, see the docstrings in each method’s definition


###Predict module

This module contains functions for running prediction using trained models. It can also be run as a stand-along program from the command line, assuming that trained main and clerical models have been previously saved to disk. For information on the API for this module in interactive mode, see the docstrings in the module file. To run this program from the command line, cd to the appropriate directory and type python Predict.py



##Info on data_store_df.csv

This file serves as an inventory of the available data sets. Each row corresponds to a different file. The column descriptions are as follows:

1. NAME : the name of the data set
2. MAIN_TYPE : whether the data set belongs to the clinical, clerical, or other class
3. NUM_SENTENCES : the size of the data set in sentences. This value is calculated automatically by the Preprocessing module.
4. PATH : the subdirectory location of the data file. All should begin with /data/
5. RANDOM: when sampling from all sentences in order to get a training and test set, should the sample be randomly selected?
6. SAMPLE_SIZE: the total number of sentences to sample for the combined training and test sets. If this is set to 0, that data set will not be used.
7. SUBTYPE : the subtype of the data set. Might be identical to the NAME. 
8. UNIQUE_SENTENCES : number of unique sentences in the data set. Automatically calculated.
9. USE_UNIQUE : whether to only use unique sentences in the sample.



##Info on creating new data file

Note that the data files are all in Python lists of strings that have been saved in JSON format. In these lists, each element is a string which corresponds to a single sentence or other short sequence of text. When new data is generated, care should be taken to use this same format.
