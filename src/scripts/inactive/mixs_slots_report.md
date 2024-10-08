Not called by any Makefile target, GitHub action, or other Python code. No `tool.poetry.scripts` alias in
the `pyproject.toml` file.

Can be run as `poetry run python mixs_slots_report.py` from the `src/scripts/` directory.

This Python script processes a YAML schema file to extract and report on specific properties of schema slots. It
performs data extraction, transformation, and outputs the cleaned data into CSV and YAML formats. Here’s a breakdown of
the script's operations, structure, and functionality:

1. **Imports and Setup**:
    - The script imports several standard Python modules such as `csv`, `os`, and `pprint`, as well as `defaultdict`
      from `collections` for maintaining counts, and `yaml` for handling YAML files.
    - Paths to the schema file and output files (CSV and YAML) are defined using relative paths.

2. **Function: load_yaml_file**:
    - **Purpose**: To load and parse a YAML file.
    - **Operation**: Opens and reads a YAML file, returning the parsed content or `None` if an error occurs during
      parsing.
    - **Error Handling**: Prints an error message if the YAML parsing fails.

3. **Schema File Checking and Loading**:
    - Checks if the schema file exists at the specified path.
    - If the file exists, it uses `load_yaml_file` to load the schema. If the file is not loaded successfully, the
      script prints a failure message and exits.
    - If the file does not exist, prints an error message and exits.

4. **Data Processing**:
    - Extracts the 'slots' dictionary from the loaded schema.
    - Collects all unique keys used across all slots for potential analysis (commented out `pprint.pprint` line
      indicates this step was used for debugging or exploratory analysis).
    - Counts annotations within the slots using a `defaultdict` to track occurrences of each annotation type.

5. **Annotation Count Output**:
    - Prints the counts of different annotations found within the slots, providing insights into the usage of specific
      annotations across the schema.

6. **Data Cleaning and Preparation**:
    - Filters out slots based on specific criteria (e.g., ignores slots with 'domain' set to 'MixsCompliantData').
    - Constructs a cleaned list of dictionaries with selected information (name, description, title, expected values
      from annotations) for each slot, applying custom formatting to handle nested dictionaries and lists.

7. **CSV Output**:
    - Writes the cleaned slot data to a CSV file, specifying the fields to include.
    - Uses `csv.DictWriter` for writing the data, ensuring that each row corresponds to a slot with its associated
      cleaned data.

8. **YAML Output**:
    - Writes the entire 'slots' dictionary to a YAML file, maintaining the original structure but potentially filtering
      or modifying some data.

### Detailed Observations:

- **Effective Data Handling**: The script demonstrates robust handling of YAML files, including error management during
  file reading and parsing.
- **Complex Data Transformation**: Applies complex transformations to clean and prepare the data for reporting,
  showcasing advanced Python data manipulation capabilities.
- **Dual Output Formats**: Outputs data in both CSV and YAML formats, catering to different needs for data consumption (
  CSV for tabular data, YAML for structured data retention).
- **Selective Data Processing**: Carefully selects and formats data to include in the output, based on specific
  attributes and properties of the slots.

### Overall Analysis:

- The script is well-structured and effectively processes schema data to extract meaningful information and generate
  reports. It uses Python’s built-in and external libraries efficiently to handle file operations, data cleaning, and
  output generation.

