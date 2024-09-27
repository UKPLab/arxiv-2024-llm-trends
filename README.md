# Transforming Scholarly Landscapes: Influence of Large Language Models on Academic Fields Beyond Computer Science

[![License](https://img.shields.io/github/license/UKPLab/ukp-project-template)](https://opensource.org/licenses/Apache-2.0)
[![Python Versions](https://img.shields.io/badge/Python-3.9-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)

This repository contains the code to procure and preprocess the dataset, introduced in the paper ["Transforming Scholarly Landscapes: Influence of Large Language Models on Academic Fields beyond Computer Science"](). The code is released under a **CC-BY-SA-4.0** license.

The code hosted in this repository extracts data and metadata from the Semantic Scholar Corpus (additionally requires the API key, see below), pre-processes it, and saves it locally in `.jsonl` format, which is compatible with common visualization tools (such as Tableau). While this data can be used for a broad analysis of scholarly documents, we use it to investigate the increasing application of Large Language Models (LLMs) across diverse fields outside of computer science.

Contact person: [Aniket Pramanick](mailto:aniket.pramanick@tu-darmstadt.de) 

Don't hesitate to send us an e-mail or report an issue if something is broken (and it shouldn't be) or if you have further questions. 

## Abstract

> Large Language Models (LLMs) have ushered in a transformative era in Natural Language Processing (NLP), reshaping research and extending NLP's influence to other fields of study. However, there is little to no work examining the degree to which LLMs influence other research fields. This work _empirically and systematically examines the influence and use of LLMs in fields beyond NLP._ We curate $106$ LLMs and analyze $\sim$ 148k papers citing LLMs to quantify their influence and reveal trends in their usage patterns. Our analysis reveals not only the increasing prevalence of LLMs in non-CS fields but also the disparities in their usage, with some fields utilizing them more frequently than others since 2018, notably Linguistics and Engineering together accounting for $\sim$ 45\% of LLM citations. Our findings further indicate that most of these fields predominantly employ task-agnostic LLMs, proficient in zero or few-shot learning without requiring further fine-tuning, to address their domain-specific problems. This study sheds light on the cross-disciplinary impact of NLP through LLMs, providing a better understanding of the opportunities and challenges.


## Getting Started

Follow the instructions below to create the Python experiment to fetch the data. 

```
$ conda create -n llmtrends pip python=3.9 
$ conda activate llmtrends
$ pip install -r requirements.txt
```

### Usage - Fetch Data

To use the dataset for analysis, you need to collect the dataset using the following code. You will need your semantic scholar [API Key](https://github.com/allenai/s2orc).

1. To fetch the __entire semantic scholar corpus__, use:

```
python -c "from code.get_s2roc import *; s2_api_key = "YOUR API KEY"; get_s2roc_files()" 

```
2. To fetch only the extracted __abstracts from scholarly documents__, use:
```
python -c "from code.get_s2roc import *; s2_api_key = "YOUR API KEY"; get_abstracts()"

```
4. To fetch the __research papers__, use:
```
python -c "from code.get_s2roc import *; s2_api_key = "YOUR API KEY"; get_papers()"

```
5. To fetch only the names of __the author data__ of the scholarly documents, use:
```
python -c "from code.get_s2roc import *; s2_api_key = "YOUR API KEY"; get_authors()"

```
6. To fetch __the citation graph__, use:
```
python -c "from code.get_s2roc import *; s2_api_key = "YOUR API KEY"; get_citations()" 

```
7. To fetch __the publication venues__ of the research papers, use:
```
python -c "from code.get_s2roc import *; s2_api_key = "YOUR API KEY"; get_publication_venues()" 

```

### Usage - Analyze Data

We have used [Tableau for Students](https://www.tableau.com/academic/students) to analyze the data and create all the plots. However, any other visualization software could be used as well to analyze the data. 

## Citation

If you use this code in your work, please cite our paper as follows:


## Disclaimer

> This repository contains experimental software and is published for the sole purpose of giving additional background details on the associated paper.
