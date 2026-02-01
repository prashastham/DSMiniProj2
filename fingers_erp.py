import numpy as np
import pandas as pd
import logging

def calc_mean_erp(trial_points: str, ecog_data: str) -> np.ndarray:
    '''
    Calculate the mean ERP (Event-Related Potential) from the given data.
    Args:
        1. trial_points -> a CSV file with three columns with the starting point of every movement, 
        the peak of every movement and the number finger (we worked on this together in the review session.) 
        Your function needs to make sure the data imported is of type “int” for ONLY this csv file. 
        (name of file: events_file_ordered.csv)

        2. ecog_data -> A CSV file of one column with the time series of the signal recorded using an ECOG electrode. 
        The indices in this file (number of rows) match up to the indices that appear in the starting points and peak 
        points in the trial_points data. 
        (name of file: brain_data_channel_one.csv)

    Returns:
        A matrix with five rows and 1201 columns 5x1201 into a variable named 
        “fingers_erp_mean” in the order of fingers 1, 2, 3, 4, 5.
    '''

    # Load the trial points
    try:
        trials_df = pd.read_csv(trial_points, dtype={'starting_point': int, 'peak_point': int, 'finger': int})
        logging.info("Trial points CSV loaded successfully.")
    except Exception as e:
        raise ValueError(f"Error reading trial points CSV: {e}")

    # Load the ECOG data
    try:
        ecog_df = pd.read_csv(ecog_data)
        logging.info("ECOG data CSV loaded successfully.")
    except Exception as e:
        raise ValueError(f"Error reading ECOG data CSV: {e}")
    
    # Get unique fingers
    fingers = sorted(trials_df['finger'].unique())
    fingers_erp_mean = np.zeros((len(fingers), 1201))

    # Calculate mean ERP for each finger
    for i, finger in enumerate(fingers):
        finger_trials = trials_df[trials_df['finger'] == finger]
        erp_segments = []

        for _, row in finger_trials.iterrows():
            start = row['starting_point'] - 200
            end = row['starting_point'] + 1000

            if start >= 0 and end < len(ecog_df):
                segment = ecog_df.iloc[start:end + 1, 0].values
                erp_segments.append(segment)
            else:
                logging.warning(f"Skipping trial for finger {finger} due to out-of-bounds indices: start={start}, end={end}")
        
        if erp_segments:
            fingers_erp_mean[i, :] = np.mean(erp_segments, axis=0)
        else:
            logging.warning(f"No valid trials found for finger {finger}.")

    return fingers_erp_mean