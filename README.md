# Transforming Scholarly Landscapes: Influence of Large Language Models on Academic Fields beyond Computer Science

[![License](https://img.shields.io/badge/license-CC--4.0--BY--SA-green)](https://creativecommons.org/licenses/by-sa/4.0/deed.en)
[![Python Versions](https://img.shields.io/badge/Python-3.9-blue.svg?style=flat&logo=python&logoColor=white)](https://www.python.org/)

This repository contains the code to procure and preprocess the dataset, introduced in the paper ["Transforming Scholarly Landscapes: Influence of Large Language Models on Academic Fields beyond Computer Science"](). The code is released under a **CC-BY-SA-4.0** license.

Contact person: [Aniket Pramanick](mailto:aniket.pramanick@tu-darmstadt.de) 

Don't hesitate to send us an e-mail or report an issue if something is broken (and it shouldn't be) or if you have further questions. 

## Abstract

> Large Language Models (LLMs) have ushered in a transformative era in Natural Language Processing (NLP), reshaping research and extending NLP's influence to other fields of study. However, there is little to no work examining the degree to which LLMs influence other research fields. This work _empirically and systematically examines the influence and use of LLMs in fields beyond NLP._ We curate $106$ LLMs and analyze $\sim$ 148k papers citing LLMs to quantify their influence and reveal trends in their usage patterns. Our analysis reveals not only the increasing prevalence of LLMs in non-CS fields but also the disparities in their usage, with some fields utilizing them more frequently than others since 2018, notably Linguistics and Engineering together accounting for $\sim$ 45\% of LLM citations. Our findings further indicate that most of these fields predominantly employ task-agnostic LLMs, proficient in zero or few-shot learning without requiring further fine-tuning, to address their domain-specific problems. This study sheds light on the cross-disciplinary impact of NLP through LLMs, providing a better understanding of the opportunities and challenges.


## Getting Started

Follow the instructions below to create the python experiment to fetch the data. 

```
$ conda create -n llmtrends pip python=3.9 
$ conda activate llmtrends
$ pip install -r requirements.txt
```
