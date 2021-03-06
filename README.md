# Clickbait-Detection

## Requirements
| Name        | Version | Install                   | Description                      |
|-------------|---------|---------------------------|----------------------------------|
| pytesseract | 0.3.2   | `pip install pytesseract` | 'Reads' text embedded in images. This also requires tesseract to be installed on your system and in your PATH. This library is only used to annotate the images in `annotate_images.py`, results are already saved (see: `media_annotations.jsonl`).|
| pyenchant | 2.0.0  | `pip install pyenchant`| Used to identify the formality of words. |
| numpy | 1.18.1 | `pip install numpy` | Used for scientific computing.|
| nltk | 3.4.5 | `pip install nltk` | NLP tools used to find features. |

## Data

| Filename | Location | # posts |  % clickbait | Download link |
|----------|----------|---------------|----|----|
|  clickbait17-train-170331.zip        |  [/datasets/big_training](/datasets/big_training)        |      19538         | 24.4% | [link](http://www.uni-weimar.de/medien/webis/corpora/corpus-webis-clickbait-17/clickbait17-train-170331.zip)|
|   clickbait17-train-170630.zip       |   [/datasets/small_training](/datasets/small_training)       |       2495        | 30.1% | [link](http://www.uni-weimar.de/medien/webis/corpora/corpus-webis-clickbait-17/clickbait17-train-170630.zip)|


**Note:** the `/media` folders have been removed from the repo due to the size. Download them yourself and copy to the right location.

Data can be loaded as follows:
```python
# Provide the directory path containing instances.
# Needs to include: instances.jsonl, truth.jsonl and /media folder.
small_dataset = Dataset("datasets/small_training")
```
To get an overview of the dataset: `small_dataset.print_summary()`, which outputs:
```bash
--- Dataset Summary --
Directory: datasets/small_training
Amount of elements: 2459
Percentage clickbait: 30.98820658804392
Percentage non-clickbait: 69.01179341195608
----------------------
```

### Features
| &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; #  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;    | Name          | Description                            |
|:-------:|:---------------:|:---------------------------------:|
| 1 | Image availability | Checks if post has an image available. |
| 2 | Image text availability | Checks if a post image has text.   |
| 3-9 | Length of article content | Counts amount of characters in the `post_title`, `media_text`, `target_title`, `target_description`, `target_keywords`, `target_captions` and `target_paragraphs` fields.| 
| 10-30 | Number of chars difference | Features 3-9 are compared to find the absolute difference. |
| 31-51 | Number of chars ratio | The (absolute) ratio of combined features 3-9 are computed. |
| 52-58 | Word counts | Counts the words in the `post_title`, `media_text`, `target_title`, `target_description`, `target_keywords`, `target_captions` and `target_paragraphs` fields. |
| 59-79 | Word count difference | Features 52-58 are compared to find the absolute difference 
| 80-100 | Word count ratio | The (absolute) ratio of combined features 52-58 are computed. |
| 101-106 | Common keywords | Computes the amount of (unique) overlap of the `target_keywords` with all other fields. |
| 107-113 | Formal words | For each field, computes the amount of formal words (i.e. does the word exist in the English dictionary) |
| 114-120| Informal words | For each field, computes the amount of informal words (i.e. does the word NOT exist in the English dictionary) |
| 121-127| Formal words ratio | For each field, computes the formal words ratio (w.r.t all the words in the field). |
| 128-127| Informal words ratio | For each field, computes the informal words ratio (w.r.t all the words in the field). |
| 135 | Amount of `@` symbols. | Computes the amount of `@` symbols in the complete post. |
| 136 | Amount of `#` symbols. | Computes the amount of `#` symbols in the complete post. | 
| 137 | Amount of retweet symbols. | Computes the amount of `RT` and `retweet` symbols in the complete post. | 
| 138 | Amount of additional symbols. | Computes the amount of additional symbols: `?`, `,`, `:` and `...` in the complete post. |
| 139-141 | Amount of keywords/paragraphs/captions | Computes the amount of keywords, paragraphs and captions in the post. |
| 142-144| Polarity scores.| Computes the polarity scores (== sentiment) for `post_text`, `target_title` and `target_paragraphs` fields. |
| 145-146| Starts with number.| Checks if the `target_title` and `post_text` start with a number `10 Best Ways To Blablaa`. |
| 147-148| Formality scores. | Checks how formal the `post_text` and the `target_paragraphs` are. |

To get the features, use `[small|big]_dataset.get_features()`:
```bash
 [  1.   1.  98. ... 129.   3.  36.]
 [  0.   0.  89. ...   0.  16.   3.]
 ...
 [  1.   0.  65. ...   0.  34.   0.]
 [  0.   0.  88. ... 131.  15.   5.]
 [  1.   0.  57. ...   0.  11.   0.]]
```
It returns an `instances * features` matrix. Its loaded from a file by default, to regenerate this matrix use the `overwrite=True` flag.
To retrieve the corresponding (target) labels, use `[small|big]_dataset.get_target_labels()`:
```bash
[0 0 1 ... 0 0 0]
```
