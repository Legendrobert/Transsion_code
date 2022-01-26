# import numpy as np
from sklearn.metrics import classification_report

import torch

from datasets import load_dataset, Dataset, concatenate_datasets

from transformers import AutoTokenizer
from transformers.data.data_collator import DataCollatorWithPadding

import esntorch.core.reservoir as res
import esntorch.core.learning_algo as la
import esntorch.core.merging_strategy as ms
import esntorch.core.esn as esn


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def tokenize(sample):
    """Tokenize sample: variable 'tokenizer' contains the """
    sample = tokenizer(sample['text'], truncation=True, padding=False)
    return sample
    
def add_lengths(sample):
    """Add 'lengths' field to sort batch by length"""
    sample["lengths"] = sum(sample["input_ids"] != 0)
    return sample
    
def load_and_prepare_dataset(dataset_name, split, cache_dir):
    """
    Load dataset from the datasets library of HuggingFace.
    Tokenize and add length.
    """
    
    # Load dataset
    dataset = load_dataset(dataset_name, split=split, cache_dir=CACHE_DIR)
    
    # Rename label column (use 'label-fine' for fine-grained labels)
    # Used for tokenization purposes.
    dataset = dataset.rename_column('label-coarse', 'labels')
    
    # Tokenize data
    dataset = dataset.map(tokenize, batched=True)
    dataset.set_format(type='torch', columns=['input_ids', 'attention_mask', 'labels'])
    
    # Add 'lengths' feature
    dataset = dataset.map(add_lengths, batched=False)
    
    return dataset


tokenizer = AutoTokenizer.from_pretrained('uncased_L-12_H-768_A-12')

# Load and prepare data
CACHE_DIR = 'cache_dir/' # put your path here

full_dataset = load_and_prepare_dataset('trec', split=None, cache_dir=CACHE_DIR)
train_dataset = full_dataset['train'].sort("lengths")
test_dataset = full_dataset['test'].sort("lengths")

# Create dict of all datasets
dataset_d = {
    'train': train_dataset,
    'test': test_dataset
    }