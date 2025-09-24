Welcome file
Welcome file


# aircheck_model

`aircheck_model` is a Python package for **training** and **screening** machine learning models on chemical compound datasets.  
It provides a **Python API** (simple `train` and `screen` functions) and a **Command-Line Interface (CLI)** for easy integration in pipelines or local workflows.

The package is designed to work with molecular fingerprints (e.g., ECFP) and chemical structure data in formats such as CSV or Parquet.

---

## ✨ Features

- Train ML models with training and optional test datasets  
- Save trained models to a specified directory  
- Evaluate models on test datasets  
- Screen new compounds using trained models  
- Simple CLI powered by [Typer](https://typer.tiangolo.com/)  

---

## 📦 Installation

Install from PyPI (once published):

```bash
pip install aircheck-test-model
```
Or install locally for development:

`git clone <your-repo-url> cd aircheck_model
pip install -e '.[dev]'`

## 🐍 Python API Usage

After installation, you can import the top-level functions `train` and `screen`:



## --- Train models ---

```
from aircheck_model import train, screen

train_result, test_result = train(
    train_file="location of parquet file",
    train_column="ECFP6",
    label="LABEL",
    model_dir="aircheck_model/new_model",
    # test_file is optional (default=None)
)
```
Accepts training and test datasets in **Parquet format**. Please provide the file path. Datasets can be downloaded from our website [AIRCHECK](https://www.aircheck.ai/datasets)


print(result_df.head())

The `train` function returns two outputs: `train_result` and `test_result`.

- **`train_result`**: a DataFrame object containing model metrics and fold information.  
- **`test_result`**: a DataFrame object if a `test_file` is provided; otherwise, an empty dataframe .  




## --- Screen compounds ---
```
result_df = screen(
    screen_file="data/ScreenData1.csv",
    smile_column="SMILES",
    fingerprint_type="ECFP6",
    model_directory="aircheck_model/new_model"
)
```



## 💻 CLI Usage

The package also provides a command-line tool:

`aircheck_model --help` 

### 🔹 Check Version

`aircheck_model version` 

----------

### 🔹 Train Models

`aircheck_model train \
    --train-data data/WDR91.parquet \
    --column ECFP6 \
    --label LABEL \
    --model-dir aircheck_model/new_model \
    --test-data data/sampled_data_test_1.parquet` 

**Arguments:**

-   `--train-data, -t` (**required**): Path to training data (CSV/Parquet)
    
-   `--test-data, -e`: Optional path to test data
    
-   `--column, -c` (**required**): Feature column (e.g., fingerprint type such as ECFP4, ECFP6)
    
-   `--label, -l` (**required**): Label column name
    
-   `--model-dir, -m`: Directory to save trained models (default: `~/model`)
    

----------

### 🔹 Screen Compounds

`aircheck_model screen \
    --screen-data data/ScreenData1.csv \
    --column SMILES \
    --fingerprints-column ECFP6 \
    --model-dir aircheck_model/new_model` 

**Arguments:**

-   `--screen-data, -s` (**required**): Path to compound data file
    
-   `--column, -c` (**required**): Column containing SMILES strings
    
-   `--fingerprints-column, -l` (**required**): Fingerprint column name
    
-   `--model-dir, -m`: Directory where trained models are stored
    

----------

## 🛠 Development

Run tests and linting locally:

`pytest
ruff check .`
aircheck_model
aircheck_model is a Python package for training and screening machine learning models on chemical compound datasets.
It provides a Python API (simple train and screen functions) and a Command-Line Interface (CLI) for easy integration in pipelines or local workflows.

The package is designed to work with molecular fingerprints (e.g., ECFP) and chemical structure data in formats such as CSV or Parquet.

✨ Features
Train ML models with training and optional test datasets
Save trained models to a specified directory
Evaluate models on test datasets
Screen new compounds using trained models
Simple CLI powered by Typer
📦 Installation
Install from PyPI (once published):

pip install aircheck-model
Or install locally for development:

git clone <your-repo-url> cd aircheck_model pip install -e '.[dev]'

🐍 Python API Usage
After installation, you can import the top-level functions train and screen:

from pathlib import Path
from aircheck_model import train, screen

— Train models —
    train_file="location of parquet file",
    train_column="ECFP6",
    label="LABEL",
    model_dir="aircheck_model/new_model",
    # test_file is optional (default=None)
)
Accepts training and test datasets in Parquet format. Please provide the file path. Datasets can be downloaded from our website AIRCHECK

— Screen compounds —
result_df = screen(
screen_file=“data/ScreenData1.csv”,
smile_column=“SMILES”,
fingerprint_type=“ECFP6”,
model_directory=“aircheck_model/new_model”
)

print(result_df.head())

💻 CLI Usage
The package also provides a command-line tool:

aircheck_model --help

🔹 Check Version
aircheck_model version

🔹 Train Models
aircheck_model train \ --train-data data/WDR91.parquet \ --column ECFP6 \ --label LABEL \ --model-dir aircheck_model/new_model \ --test-data data/sampled_data_test_1.parquet

Arguments:

--train-data, -t (required): Path to training data (CSV/Parquet)

--test-data, -e: Optional path to test data

--column, -c (required): Feature column (e.g., fingerprint type such as ECFP4, ECFP6)

--label, -l (required): Label column name

--model-dir, -m: Directory to save trained models (default: ~/model)

🔹 Screen Compounds
aircheck_model screen \ --screen-data data/ScreenData1.csv \ --column SMILES \ --fingerprints-column ECFP6 \ --model-dir aircheck_model/new_model

Arguments:

--screen-data, -s (required): Path to compound data file

--column, -c (required): Column containing SMILES strings

--fingerprints-column, -l (required): Fingerprint column name

--model-dir, -m: Directory where trained models are stored

🛠 Development
Run tests and linting locally:

pytest ruff check .

Markdown 3105 bytes 370 words 122 lines Ln 47, Col 3HTML 2259 characters 333 words 58 paragraphs
