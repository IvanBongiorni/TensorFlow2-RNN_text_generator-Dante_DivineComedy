# TensorFlow 2.0 Text generator on Dante Alighieri's Divine Comedy

This Notebook contains a text generator RNN that was trained on the **Divina Commedia** (the *Divine Comedy*) by **Dante Alighieri**. This is a poem written at the beginning of the XII century. It's hard to explain what it represents for Italian culture: it's without any doubt the main pillar of our national literature, one of the building blocks of modern Italian language, and arguably the gratest poem ever. All modern representations of Hell, Purgatory and Heaven derive from this opera.

Its structure is extremely interesting: each verse is composed of 11 syllables, and its rhymes follow an **A-B-A-B** structure. Lot of pattern to be learned!

-----

# TensorFlow 2.0 training with Autograph

This Neural Network is trained using **Autograph**, one of the best features in **TensorFlow 2.0** for custom training.

-----

## Repository structure

- **scraper_Divine_Comedy.py**:        script to download the Divine Comedy from Wikisource in a format I like
- **DivinaCommedia.txt**:              raw text
- **RNN_text_generator_00.ipynb**:     Notebook containing RNN training and examples of text generation
