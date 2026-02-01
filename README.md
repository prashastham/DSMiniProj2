# ERP Analysis Mini Project

## Project Overview

This project analyzes Event-Related Potentials (ERPs) from ECoG (Electrocorticography) brain data associated with finger movements. The analysis processes brain signals recorded during finger movements (fingers 1-5) and computes the mean ERP for each finger across multiple trials.

ERP analysis is a key technique in neuroscience for studying brain responses to specific events. This project focuses on time-locked brain activity around finger movement events, extracting signal segments from 200ms before to 1000ms after movement onset.

## Project Structure

```
DSMiniProj2/
├── main.py                      # Main execution script
├── fingers_erp.py               # Core ERP calculation functions
├── README.md                    # Project documentation
├── data/                        # Data directory
│   ├── brain_data_channel_one.csv   # ECoG time series data
│   └── events_file_ordered.csv      # Movement event timestamps
└── notebooks/                   # Jupyter notebooks
    └── ERPSync.ipynb           # Interactive analysis notebook
```

### File Descriptions

- **main.py**: Entry point for the project. Loads data, calls the ERP calculation function, and visualizes results with 5 subplots (one per finger).
- **fingers_erp.py**: Contains `calc_mean_erp()` function that processes trial events and brain data to compute mean ERPs for each finger.
- **data/brain_data_channel_one.csv**: Single-column CSV containing continuous ECoG signal recordings.
- **data/events_file_ordered.csv**: Three-column CSV with trial information (starting_point, peak_point, finger).
- **notebooks/ERPSync.ipynb**: Jupyter notebook for interactive exploration and analysis.

## Requirements

- Python 3.x
- numpy
- pandas
- matplotlib
- logging (standard library)

## How to Execute

### Run the main script

```bash
python main.py
```

This will:
1. Load the trial events and ECoG data from the `data/` directory
2. Calculate mean ERPs for all 5 fingers
3. Display the shape of the resulting matrix (should be 5x1201)
4. Generate a figure with 5 subplots showing the mean ERP for each finger

## Output

The program outputs:
- **Console**: Shape of the computed ERP matrix (5x1201)
- **Visualization**: A matplotlib figure with 5 subplots showing:
  - Time axis: -200ms to 1000ms (relative to movement onset)
  - Amplitude: ECoG signal amplitude
  - One subplot per finger (Finger 1 through Finger 5)

## Algorithm Details

The `calc_mean_erp()` function:
1. Loads trial events (starting points, peak points, finger labels)
2. Loads continuous ECoG brain signal data
3. For each of the 5 fingers:
   - Extracts all trials associated with that finger
   - Segments the signal: [start_point - 200ms] to [start_point + 1000ms]
   - Averages all segments to compute the mean ERP
4. Returns a 5×1201 matrix where each row is the mean ERP for one finger

## Data Format

### events_file_ordered.csv
- **starting_point** (int): Index marking movement onset
- **peak_point** (int): Index marking movement peak
- **finger** (int): Finger identifier (1-5)

### brain_data_channel_one.csv
- Single column containing continuous ECoG signal amplitudes
- Row indices correspond to time samples

## Notes

- The program skips trials where the extracted time window exceeds data boundaries
- Logging warnings are displayed for out-of-bounds trials or fingers with no valid data
- Time resolution: Each sample represents 1ms (1201 samples = -200 to +1000ms)
