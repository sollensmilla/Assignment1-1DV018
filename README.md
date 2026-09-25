# 1DV018 - Assignment 1

## Requirements

- Python 3.10+
- matplotlib (`pip install matplotlib`)
- flake8 (`pip install flake8`, optional, used for style checking)

## Running the experiments

Part 1 (3-sum algorithms):
```bash
python3 experiment1.py
```

Part 2 (sorting algorithms):
```bash
python3 experiment2.py
```

Each script prints correctness tests and timing results to the 
terminal, and opens matplotlib windows with the result plots. Each 
plot window must be closed manually before the program continues to 
the next one.

## Known issue

Occasionally, closing a plot window leaves a duplicate, frozen 
window on screen that cannot be interacted with. This does not 
affect the program's execution — it continues normally and all 
"real" plot windows still open and close as expected. The extra 
windows disappear once the script finishes running. This appears to 
be a quirk of matplotlib's window handling on macOS during long 
runs with many sequential plots, not a bug in the experiment logic.

## File structure

- `threesum.py`, `quadratic_time_algorithms.py`, 
  `n_log_n_algorithms.py`, `special_case_algorithms.py` — algorithm 
  implementations
- `experiment1.py`, `experiment2.py` — experiments, timing, and 
  plotting for Part 1 and Part 2 respectively
- `utils/experiment_utils.py` — shared experiment infrastructure 
  (timing, complexity estimation, plotting) used by both parts
- `report.md` — written report