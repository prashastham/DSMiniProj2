from fingers_erp import calc_mean_erp
import matplotlib.pyplot as plt

def main():
    # Read the input CSV files
    trial_points_file = 'data/events_file_ordered.csv'
    ecog_data_file = 'data/brain_data_channel_one.csv'

    # Calculate the mean ERP
    fingers_erp_mean = calc_mean_erp(trial_points_file, ecog_data_file)

    # Print the shape of the resulting matrix
    print("Shape of fingers_erp_mean:", fingers_erp_mean.shape)

    # Plot the mean ERP for each finger
    subplot_titles = ['Finger 1', 'Finger 2', 'Finger 3', 'Finger 4', 'Finger 5']
    fig, axs = plt.subplots(5, 1, figsize=(10, 10))
    time_axis = range(-200, 1001)  # Time from -200ms to 1000ms
    for i in range(5):
        axs[i].plot(time_axis, fingers_erp_mean[i, :])
        axs[i].set_title(subplot_titles[i])
        axs[i].set_xlabel('Time (ms)')
        axs[i].set_ylabel('Amplitude')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()