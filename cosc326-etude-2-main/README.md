# COSC326 Etude 2 - Syllables

Machine learning program trained to detect the number of syllables in a word.

## Dependencies
The project uses the scikit-learn machine learning package along with pandas for the data. These can be installed using the requirements.txt file or manually as follows:

From the file:
```bash
pip install -r requirements.txt
```
Manually:
```bash
pip install scikit-learn pandas
```

## Start Up

First the model must be generated and trained by using the model.py script. This can be simply run from the following command:

##### Note: There is already a pre-trained model available in the pickle file so this step can be skipped.

```bash
python model.py
```
This will generate and train a machine learning model and dump the binary model to the pickle/model.pkl folder

The model can then be interacted with and tested through the script.py file. This can be simply run from the following command:

```bash
python script.py
```

This will then read from stdin and output the amount of syllables the model estimates to be in the word.

#### Autojudge file
The autojudge file contains a base64 encoded version of the model that is hard encoded into the file and can be run instead of the script file.

```bash
python autojudge.py
```

### How the Model Works

For Etude 2 we created a machine learning model using a sklearn decision tree classifier to predict the number of syllables in a word.

A decision tree classifier works by recursively splitting the data into smaller subsets based on decision rules. This creates a tree where each branch is a different if-else statement. These if-else statements are repeated until all of the target values fall into the same class or there are no more features left to split.

The model works by first reading in a text file of words and their number of syllables. This data is called the training data. The model then splits words based on their key features, it repeats this process until all words with the same features are in the same grouping where hopefully all of the words will have the same syllable count. If not, whatever the most common syllable count is will be that set of features syllable count.

The features that we decided to extract are: wordLength, the number of A's , E's, O's, U's, I's, Y's, total number of vowels, if the word starts with a vowel, if the word ends with a vowel, what the final letter is, the number of diphthongs, the number of triphthongs, if the word contains "ia", the number of prefixes, the number of suffixes, and the word count vectorized.

An example of how this would work is, if there was a word in the training data that has the key values of a length of 7, 4 vowels, 1 diphthong, end in a vowel and contain 3 syllables. If a different word with the same key features was inputted it would make the prediction that the word contains 3 syllables awell as it would be making the same feature splits.

## Testing

Testing the model was done over a large set of data rather than testing individual words. This is due to it being difficult to fix individual words based on the nature of the model and any fixes to individual words would not have a large impact on the overall accuracy of the model. Therefore, our testing philosophy was simple, we iteratively improved the model aiming for a 90% accuracy score on our collected data set of 6000 words and their syllables. 

### Data collection

Our first, smallest, data set was collected from a github repository [here](https://github.com/mholtzscher/syllapy/blob/master/syllapy/data.csv). This data set was the main data set used for testing the accuracy of the model, the size of this data set (6000) was simply too small to be able to accurately train a model with.

The largest data set came from the [IPA Pronouncing Dictionary](https://github.com/open-dict-data/ipa-dict) which someone had already transformed. This contained around 130000 words and was found [here](https://www.kaggle.com/datasets/schwartstack/english-phonetic-and-syllable-count-dictionary). This data set, while large, was too inconsistent to successfully train the model on.

The third data set, which the model was trained on, was made by crossing a list of [100000 most common](https://gist.github.com/h3xx/1976236) english words with the IPA list of syllables to form a data set of 30000 common english words. This was the data set used to train the model as it contained the best quality of data while still maintaining a large quantity.

### Accuracy score

When a model was trained the accuracy of it was tested to give a percentage of values it got correct. The goal was to reach 90% accuracy and we started from ~80%. We used an iterative process of adding features and changing models to incrementally improve the overall accuracy to a point where we felt it was performing well. These improvements included changing models and data sets to updating features such as whether the word contained a dipthong to the amount of dipthongs and adding features such as prefixes/suffixes to help the model better classify words.

## Benchmarking

Given the nature of our program, performance was not something we were able to work on and improve. The time it takes to both perform the machine learning prediction is, however, quite fast and therefore we were not worried about the performance of the program, the complexity of the algorithm or the time it takes to train the model given that this is a compile time constant that can be saved to disk. The only way we could improve the speed of the program is by removing features or reducing test data both of which would have an important impact on the accuracy of the model. We made sure that we did not add excessive features that did not improve the program to keep the model fast but did not worry about checking performance as it was somewhat out of our control.
