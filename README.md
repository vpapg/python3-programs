# python3-programs
Various python 3 programs:

*multi-download.py* :
Downloads all files of a specified extension from an html webpage.
Code taken and modified from: https://null-byte.wonderhowto.com/how-to/download-all-pdfs-webpage-with-python-script-0163031/

*pdftitle.py* :
Renames every PDF file in a given directory, according to the title provided in the metadata of the file. If there is no title, the filename remains unchanged.

*copy_jpg_mp4.py* :
Copies all the jpg and mp4 files of a directory to the ./Copies subdirectory.

*EditDistance.py* :
An implementation of the Edit Distance algorithm. More info here: https://vpapg.github.io/posts/2018-11-07.html

*tfidf_austen.py* :
It calculates the tf, df, idf, cf, tf.idf of given words and texts (texts used: Jane Austen's books included in the Gutenberg corpus of the NLTK module).

*math_and_stat.py* :
Created while revising some basic stuff regarding statistical distributions and combinatorics.

*duolingo_vocab.py* :
It retrieves the vocabulary you have learnt from a specified language in Duolingo. You need to specify the txt file where the words will be stored. The format of the txt file is:
word \t word_using_simple_latin_characters \t category(skill).
The library used can be found here: https://github.com/KartikTalwar/duolingo . Ideally, this program would also translate each word, but the libraries I experimented with for this purpose did not always work properly.
