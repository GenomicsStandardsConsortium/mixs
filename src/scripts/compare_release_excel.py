import pprint

import pandas as pd

# Cache to store headers from sheets that have already been read
headers_cache = {}


def get_excel_headers(file_path, sheet_name):
    """ Retrieves column headers, using cached data if available. """
    # Create a unique key for each file and sheet combination
    cache_key = (file_path, sheet_name)

    # Check if the headers are already cached
    if cache_key in headers_cache:
        return headers_cache[cache_key]

    # Load the specified sheet from the Excel file into a DataFrame
    df = pd.read_excel(file_path, sheet_name=sheet_name)
    headers = list(df.columns)

    # Cache the headers
    headers_cache[cache_key] = headers

    return headers


def compare_sheets(comparisons):
    """ Compares columns of specified sheets in given file paths. """
    results = {}

    for comparison in comparisons:
        # Unpack each comparison specification
        first_file, first_sheet, second_file, second_sheet = comparison

        # Read headers from both sheets using the caching function
        first_headers = get_excel_headers(first_file, first_sheet)
        second_headers = get_excel_headers(second_file, second_sheet)

        # Find headers unique to each sheet and common headers
        unique_to_first = set(first_headers) - set(second_headers)
        unique_to_second = set(second_headers) - set(first_headers)
        intersection = set(first_headers) & set(second_headers)

        # Organize the results
        results[f"{first_file}:{first_sheet} vs {second_file}:{second_sheet}"] = {
            "unique_to_first": unique_to_first,
            "unique_to_second": unique_to_second,
            "intersection": intersection
        }

    return results


# Specify comparisons in tuples: (first_file, first_sheet, second_file, second_sheet)
comparisons = [
    ("../../MIxSv6_release.xlsx", "MIxSv6-Core", "../../mixs_v6.xlsx", "MIxS"),
    ("../../MIxSv6_release.xlsx", "MIxSv6_packages", "../../mixs_v6.xlsx", "environmental_packages")
]

# Perform comparisons
comparison_results = compare_sheets(comparisons)

# Print the results
for comp, result in comparison_results.items():
    print(f"Comparison: {comp}")
    pprint.pprint(result)
