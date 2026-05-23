# DAY5 — Matplotlib / Pandas / Seaborn exercises

Quick instructions to reproduce the analyses and run the tasks from `note.txt`.

Prerequisites
- python3 (3.10+ recommended)
- A virtual environment (recommended)

Setup (Linux / macOS)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r DAY5/requirements.txt
```

Setup (Windows - PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r DAY5/requirements.txt
```

Run the scripted solution
- The repository includes `DAY5/student_analysis.py` which implements the numbered tasks from `note.txt`.
```bash
python3 DAY5/student_analysis.py --input "DAY5/Students (1).csv"
```

Notebooks
- Open the notebooks in `DAY5/` with VS Code or Jupyter. Select the kernel named `Python (dataspace_venv)` (or the venv Python) so imports resolve.
- To execute a notebook headlessly and produce an executed copy:
```bash
# while venv is active
python3 -m nbconvert --to notebook --execute DAY5/matplotlib.ipynb --output /tmp/matplotlib-executed.ipynb
```

<!-- README footer intentionally left minimal -->
