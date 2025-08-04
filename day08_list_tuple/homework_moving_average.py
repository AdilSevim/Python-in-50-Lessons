"""
Day 8, Homework: Moving Average Calculator

Purpose: Calculate the moving average of a list of numbers over a sliding window.
We use lists to store values and calculate averages over subsets of data.

Expected output when run:
Data points: [10, 15, 12, 18, 20, 16, 22, 25]
Moving averages (window size 3): [12.33, 15.0, 16.67, 18.0, 19.33, 21.0]
"""

def moving_average(data, window_size):
    """Calculate moving averages over a sliding window.
    
    Args:
        data: A list of numbers
        window_size: The number of elements to include in each average
    
    Returns:
        A list of moving averages
    """
    # Create an empty list for the averages
    averages = []
    
    # Calculate moving averages
    for i in range(len(data) - window_size + 1):
        # Get the window of data
        window = data[i : i + window_size]
        
        # Calculate the average of the window
        total = 0
        for value in window:
            # Iterating through the window to calculate total
            total = total + value
        average = total / window_size
        
        # Add the average to our list
        averages.append(round(average, 2))
    
    return averages


def main():
    """Calculate moving averages for a list of data points."""
    # List of data points
    data_points = [10, 15, 12, 18, 20, 16, 22, 25]
    
    # Set window size
    window = 3
    
    # Calculate moving averages
    moving_averages = moving_average(data_points, window)
    
    # Display the results
    print("Data points:", data_points)
    print(f"Moving averages (window size {window}):", moving_averages)


if __name__ == "__main__":
    main()
