import pandas as pd
import numpy as np
import requests
import os
import urllib
import json
import pathlib
from pprint import pprint
from tqdm import tqdm

s2_api_key = "6ocjziAkTp3rhulhevE1t7O4Xr2pdPhWaMV3WAyU"

def get_s2roc_readme():
    latest_release = requests.get("http://api.semanticscholar.org/datasets/v1/release/latest").json()

    release_readme_path = "assets/s2roc_release_readme.json"
    release_readme_path = pathlib.Path(release_readme_path)

    with open(release_readme_path, 'w', encoding="utf-8") as f_out:
        json.dump(latest_release, f_out, indent=6)

    return     

def get_abstracts():
    abstracts_metadata = requests.get("http://api.semanticscholar.org/datasets/v1/release/latest/dataset/abstracts", headers={'X-API-KEY': s2_api_key}).json()
    abstracts_files_list = abstracts_metadata["files"]

    output_dir = "data/s2roc/abstracts"
    output_dir = pathlib.Path(output_dir)

    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)

    meta_data_path = f"data/s2roc/metadata/abstracts_metadata.json"
    meta_data_path = pathlib.Path(meta_data_path)

    if not meta_data_path.parent.exists():
        meta_data_path.parent.mkdir(parents=True, exist_ok=True)

    with open(meta_data_path, 'w', encoding="utf-8") as f_out:
        json.dump(abstracts_metadata, f_out, indent=6)
    
    for i in tqdm(range(len(abstracts_files_list))):
        file_url = abstracts_files_list[i]
        output_file_path = pathlib.Path(f"{output_dir}/abstracts_part_{i}.jsonl.gz")

        urllib.request.urlretrieve(file_url, output_file_path)


def get_authors():
    authors_metadata = requests.get("http://api.semanticscholar.org/datasets/v1/release/latest/dataset/authors", headers={'X-API-KEY': s2_api_key}).json()
    authors_files_list = authors_metadata["files"]

    output_dir = "data/s2roc/authors"
    output_dir = pathlib.Path(output_dir)

    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)

    meta_data_path = f"data/s2roc/metadata/authors_metadata.json"
    meta_data_path = pathlib.Path(meta_data_path)

    if not meta_data_path.parent.exists():
        meta_data_path.parent.mkdir(parents=True, exist_ok=True)

    with open(meta_data_path, 'w', encoding="utf-8") as f_out:
        json.dump(authors_metadata, f_out, indent=6)
    
    for i in tqdm(range(len(authors_files_list))):
        file_url = authors_files_list[i]
        output_file_path = pathlib.Path(f"{output_dir}/authors_part_{i}.jsonl.gz")

        urllib.request.urlretrieve(file_url, output_file_path)

def get_citations():
    citations_metadata = requests.get("http://api.semanticscholar.org/datasets/v1/release/latest/dataset/citations", headers={'X-API-KEY': s2_api_key}).json()
    citations_files_list = citations_metadata["files"]

    output_dir = "data/s2roc/citations"
    output_dir = pathlib.Path(output_dir)

    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)

    meta_data_path = f"data/s2roc/metadata/citations_metadata.json"
    meta_data_path = pathlib.Path(meta_data_path)

    if not meta_data_path.parent.exists():
        meta_data_path.parent.mkdir(parents=True, exist_ok=True)

    with open(meta_data_path, 'w', encoding="utf-8") as f_out:
        json.dump(citations_metadata, f_out, indent=6)

    for i in tqdm(range(len(citations_files_list))):
        file_url = citations_files_list[i]
        output_file_path = pathlib.Path(f"{output_dir}/citations_part_{i}.jsonl.gz")

        if not output_file_path.exists():
            urllib.request.urlretrieve(file_url, output_file_path)
        # urllib.request.urlretrieve(file_url, output_file_path)

def get_paper_ids():
    paper_ids_metadata = requests.get("http://api.semanticscholar.org/datasets/v1/release/latest/dataset/paper-ids", headers={'X-API-KEY': s2_api_key}).json()
    paper_ids_files_list = paper_ids_metadata["files"]

    output_dir = "data/s2roc/paper_ids"
    output_dir = pathlib.Path(output_dir)

    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)

    meta_data_path = f"data/s2roc/metadata/paper_ids_metadata.json"
    meta_data_path = pathlib.Path(meta_data_path)

    if not meta_data_path.parent.exists():
        meta_data_path.parent.mkdir(parents=True, exist_ok=True)

    with open(meta_data_path, 'w', encoding="utf-8") as f_out:
        json.dump(paper_ids_metadata, f_out, indent=6)

    for i in tqdm(range(len(paper_ids_files_list))):
        file_url = paper_ids_files_list[i]
        output_file_path = pathlib.Path(f"{output_dir}/paper_ids_part_{i}.jsonl.gz")

        urllib.request.urlretrieve(file_url, output_file_path)


def get_publication_venues():
    publication_venues_metadata = requests.get("http://api.semanticscholar.org/datasets/v1/release/latest/dataset/publication-venues", headers={'X-API-KEY': s2_api_key}).json()
    publication_venues_files_list = publication_venues_metadata["files"]

    output_dir = "data/s2roc/publication_venues"
    output_dir = pathlib.Path(output_dir)

    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)
    
    meta_data_path = f"data/s2roc/metadata/publication_venues_metadata.json"
    meta_data_path = pathlib.Path(meta_data_path)

    if not meta_data_path.parent.exists():
        meta_data_path.parent.mkdir(parents=True, exist_ok=True)

    with open(meta_data_path, 'w', encoding="utf-8") as f_out:
        json.dump(publication_venues_metadata, f_out, indent=6)
    
    for i in tqdm(range(len(publication_venues_files_list))):
        file_url = publication_venues_files_list[i]
        output_file_path = pathlib.Path(f"{output_dir}/publication_venues_part_{i}.jsonl.gz")

        urllib.request.urlretrieve(file_url, output_file_path)

def get_tldrs():
    tldrs_metadata = requests.get("http://api.semanticscholar.org/datasets/v1/release/latest/dataset/tldrs", headers={'X-API-KEY': s2_api_key}).json()
    tldrs_files_list = tldrs_metadata["files"]

    output_dir = "data/s2roc/tldrs"
    output_dir = pathlib.Path(output_dir)

    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)
    
    meta_data_path = f"data/s2roc/metadata/tldrs_metadata.json"
    meta_data_path = pathlib.Path(meta_data_path)

    if not meta_data_path.parent.exists():
        meta_data_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(meta_data_path, 'w', encoding="utf-8") as f_out:
        json.dump(tldrs_metadata, f_out, indent=6)
    
    for i in tqdm(range(len(tldrs_files_list))):
        file_url = tldrs_files_list[i]
        output_file_path = pathlib.Path(f"{output_dir}/tldrs_part_{i}.jsonl.gz")

        urllib.request.urlretrieve(file_url, output_file_path)

def get_s2roc_files():
    s2roc_meta_data = requests.get("http://api.semanticscholar.org/datasets/v1/release/latest/dataset/s2orc", headers={'X-API-KEY': s2_api_key}).json()
    s2roc_files_list = s2roc_meta_data["files"]

    output_dir = "data/s2roc/s2roc"
    output_dir = pathlib.Path(output_dir)

    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)

    meta_data_path = f"data/s2roc/metadata/s2roc_metadata.json"
    meta_data_path = pathlib.Path(meta_data_path)

    if not meta_data_path.parent.exists():
        meta_data_path.parent.mkdir(parents=True, exist_ok=True)

    with open(meta_data_path, 'w', encoding="utf-8") as f_out:
        json.dump(s2roc_meta_data, f_out, indent=6)
    
    for i in tqdm(range(len(s2roc_files_list))):
        file_url = s2roc_files_list[i]
        output_file_path = pathlib.Path(f"{output_dir}/s2roc_part_{i}.jsonl.gz")

        if not output_file_path.exists():
            urllib.request.urlretrieve(file_url, output_file_path)
        # urllib.request.urlretrieve(file_url, output_file_path)

def get_papers():
    paper_meta_data =  requests.get("http://api.semanticscholar.org/datasets/v1/release/latest/dataset/papers", headers={'X-API-KEY':s2_api_key}).json()
    paper_files_list = paper_meta_data["files"]


    output_dir = "data/s2roc/papers"
    output_dir = pathlib.Path(output_dir)

    if not output_dir.exists():
        output_dir.mkdir(parents=True, exist_ok=True)

    meta_data_path = f"data/s2roc/metadata/papers_metadata.json"
    meta_data_path = pathlib.Path(meta_data_path)

    if not meta_data_path.parent.exists():
        meta_data_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(meta_data_path, 'w', encoding="utf-8") as f_out:
        json.dump(paper_meta_data, f_out, indent=6)
    
    exit(0)
    
    for i in tqdm(range(len(paper_files_list))):
        file_url = paper_files_list[i]
        output_file_path = pathlib.Path(f"{output_dir}/papers_part_{i}.jsonl.gz")

        urllib.request.urlretrieve(file_url, output_file_path)
    



if __name__ == '__main__':
    # get_s2roc_readme()
    get_papers()
    # print("Hello World")
