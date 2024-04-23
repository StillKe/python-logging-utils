def aggregate_data(*data_sources):
    """
    Aggregate data from multiple sources.

    Parameters:
        *data_sources: tuple
            Variable number of data sources containing values to be aggregated.

    Returns:
        list: A list containing the aggregated values from all data sources.
    """
    aggregated_data = []

    # Iterate over each data source
    for source in data_sources:
        # Aggregate values from the current data source
        aggregated_data.extend(source)

    return aggregated_data

def get_data_from_user():
    data_sources = []
    while True:
        user_input = input("Enter data (separate values by spaces, leave empty to finish): ")
        if not user_input:
            break
        # Split the input by spaces and convert each value to integer if possible
        try:
            data = [int(x) for x in user_input.split()]
            data_sources.append(data)
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")

    return data_sources

# Get data from the user
data_sources = get_data_from_user()

# Aggregate the data
aggregated_data = aggregate_data(*data_sources)
print("Aggregated Data:", aggregated_data)
