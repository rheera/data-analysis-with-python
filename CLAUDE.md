# CLAUDE.md

Final project for Course 7 of IBM's Data Analyst Professional Certificate (Coursera). Two Jupyter notebooks, each a small regression analysis with pandas and scikit-learn:

- `InsuranceCostAnalysis.ipynb`: part 1, medical insurance charges (`medical_insurance_dataset.csv`, no header row; the notebook sets the column names).
- `House_Sales_in_King_Count_USA.ipynb`: final assignment, King County house prices (`kc_house_data.csv`).

## Environment

- Cloud sessions run on the `data-analysis-with-python` environment. Its setup script installs pandas, numpy, matplotlib, seaborn, scikit-learn, nbconvert and ipykernel into the system `python3`, so no virtualenv is needed.
- The container runs Python 3.13; the README lists 3.12.2. Both notebooks run cleanly on 3.13.
- Network access is limited to package registries plus `cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud`. Ask before adding hosts.

## Data

- The notebooks load their data from the IBM course URLs, not the local files. The CSVs in the repo are byte-identical copies (same SHA-256), so use them for offline work. `kc_house_data.csv` is the same file as the remote `kc_house_data_NaN.csv`.
- Don't change the notebooks' load paths unless asked.

## Running notebooks

- Execute a notebook without touching the original:
  `jupyter nbconvert --to notebook --execute <notebook>.ipynb --output-dir <scratch dir>`
- The committed notebooks keep their cell outputs. Only re-run and save outputs into the repo copy when asked.
- `.ipynb_checkpoints/` is gitignored; never commit it.

## Conventions

- When changing a model or its features, report R² before and after the change.
