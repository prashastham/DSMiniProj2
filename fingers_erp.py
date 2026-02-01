def calc_mean_erp(trial_points, ecog_data):
    '''
    Calculate the mean ERP (Event-Related Potential) from the given data.
    Args:
        1. trial_points -> a CSV file with three columns with the starting point of every movement, 
        the peak of every movement and the number finger (we worked on this together in the review session.) 
        Your function needs to make sure the data imported is of type “int” for ONLY this csv file. 
        (name of file: events_file_ordered.csv)

        2. ecog_data -> A CSV file of one column with the time series of the signal recorded using an ECOG electrode. 
        The indices in this file (number of rows) match up to the indices that appear in the starting points and peak 
        points in the trial_points data. (name of file: brain_data_channel_one.csv)

    Returns:
        Your function will output a matrix with five rows and 1201 columns 5x1201 into a variable named 
        “fingers_erp_mean” in the order of fingers 1, 2, 3, 4, 5.
    '''
    pass
