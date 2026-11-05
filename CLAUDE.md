# CLAUDE.md

Final project for Course 7 of IBM's Data Analyst Professional Certificate (Coursera). Two Jupyter notebooks, each a small regression analysis with pandas and scikit-learn:

- `InsuranceCostAnalysis.ipynb`: part 1, medical insurance charges (`medical_insurance_dataset.csv`, no header row; the notebook sets the column names).
- `House_Sales_in_King_Count_USA.ipynb`: final assignment, King County house prices (`kc_house_data.csv`).

## Environment

- Cloud sessions run on the `data-analysis-with-python` environment. Its setup script installs pandas, numpy, matplotlib, seaborn, scikit-learn, nbconvert and ipykernel into the system `python3`, so no virtualenv is needed.
- The container runs Python 3.13; the README lists 3.12.2. Both notebooks run cleanly on 3.13.
- Network access is limited to package registries, `cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud`, and `api.minimax.io` (opened by its saved key, see below). Ask before adding hosts.

## MiniMax API

- A MiniMax API key for `api.minimax.io` is saved as a network secret on the cloud environment. The network proxy adds `Authorization: Bearer <key>` to every request to that host.
- No environment variable holds the key. Never ask for it in chat or write it to a file. In code, read it with a placeholder fallback so the same code works locally and in the cloud (the proxy overwrites the header):
  `os.environ.get("MINIMAX_API_KEY", "proxy-injected")`
- Use the international host: `https://api.minimax.io/v1` (OpenAI-compatible, e.g. `/v1/chat/completions`, `/v1/models`), not `api.minimaxi.com`.
- An HTTP 402 `insufficient_balance_error` means the MiniMax account needs credit, not that the key is wrong.

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
