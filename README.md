### Supporting Materials

##### Static IPython Notebooks

1. [Explore the data](http://nbviewer.ipython.org/github/mattwescott/birds-scipy2014/blob/master/ExploreData.ipynb)
2. [Build a model](http://nbviewer.ipython.org/github/mattwescott/birds-scipy2014/blob/master/CrowdsourcedCV.ipynb)
3. [Optimize a single call](http://nbviewer.ipython.org/github/mattwescott/birds-scipy2014/blob/master/SingleLabelModel.ipynb)
4. [Generate a Kaggle submission](http://nbviewer.ipython.org/github/mattwescott/birds-scipy2014/blob/master/SingleLabelKaggleSubmission.ipynb)
5. [Blend with other submissions](http://nbviewer.ipython.org/github/mattwescott/birds-scipy2014/blob/master/BlendSubmissions.ipynb)

##### Tutorial Video
[Be warned that this style doesn't adapt well to video](https://www.youtube.com/watch?v=-Rl9hviT5qw&feature=youtu.be)

##### Literature

1. My teammate Dima Kamalov's [reflections on the competition](http://www.kaggle.com/c/multilabel-bird-species-classification-nips2013/forums/t/6383/reflections/35139#post35139)
2. [Architectural inspiration](http://sis.univ-tln.fr/~odufour/fichiers/DufourICMLWshp_v6.pdf) from Dufour and friends
3. [Learning Decision Trees using AUROC](http://users.dsic.upv.es/grupos/elp/cferri/105.pdf)
4. [MFCC generation code](https://github.com/jameslyons/python_speech_features) which Dima adapted
5. [First place model](http://www.kaggle.com/c/multilabel-bird-species-classification-nips2013/forums/t/6383/reflections/35504#post35504)

### Setup Tutorial Environment

1. **Clone this repository**

  `git clone https://github.com/mattwescott/birds-scipy2014.git`

3. **Sign up for Kaggle**

  [Kaggle](http://www.kaggle.com/account/register)

4. **Get the data**

  [Contest Data](https://www.kaggle.com/c/multilabel-bird-species-classification-nips2013/data)

5. **Build environment**

  ###### Easy Method
  Install [Anaconda](https://store.continuum.io/cshop/anaconda/) for Python2.7 or Python3.4
  
  ###### Alternative Method
  Set up an environment with [these packages](requirements.txt)

6. Edit paths to data in [config.py](config.py)

7. Run [check_env.py](check_env.py) to make sure you are ready

  `python birds-scipy2014/check_env.py`

8. See you in Austin!
