## 📄 README.md

### Project: dsjson

A lightweight Python package to convert clinical tabular datasets (e.g., SDTM/ADaM) and metadata into **CDISC Dataset-JSON v1.1** format. It supports multiple metadata input formats including CSV, Excel, JSON, and XML (planned).


[![PyPI](https://img.shields.io/pypi/v/dsjson.svg)](https://pypi.org/project/dsjson/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dsjson.svg)](https://pypi.org/project/dsjson/)


### 🔧 Features

* Converts `DataFrame` + column metadata to Dataset-JSON v1.1
* Supports CSV, Excel, JSON for metadata
* Auto-generates `datasetJSONCreationDateTime`
* Enforces required top-level metadata
* Extract Variable Label from Specification
* Converts extracted Variable Labels into column metadata

### 📦 Installation
```
pip install dsjson
```

### 🚀 Quick Start

```python
from dsjson import load_metadata, to_dataset_json, extract_labels, make_column_metedata
import pandas as pd

my_excel_path = r"specification path"

# Load data
rows = pd.read_csv("examples/vs.csv")

# Extract variables from specification and convereted that to column metadata
variable_labels = extract_labels(spec_path=my_excel_path, sheet_name="DM", variable_name_col="Variable Name", variable_label_col="Variable Label")
columns = make_column_metadata(df=data_df, variable_labels=variable_labels, domain="DM")

# this can be used where we already have column metadata already defined in a file - if you make column metadata as per above code, then this is not required
columns = load_metadata("examples/columns_vs.csv", file_type="csv")

# Create Dataset-JSON
ds = to_dataset_json(
    data_df=rows,
    columns_df=columns,
    name="VS",
    label="Vital Signs",
    itemGroupOID="IG.VS",
    originator="My CRO",
    sourceSystem_name="Python",
    sourceSystem_version="3.10",
    fileOID="F.VS.001",
    studyOID="S.1234"
)
```



