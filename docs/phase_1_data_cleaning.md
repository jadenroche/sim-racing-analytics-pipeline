## Completed:
- Loaded raw JSON export from iRacing
- Identified nested structure (list → list → records)
- Converted JSON to pandas DataFrame
- Filtered to race-only events
- Extracted track_name from nested dictionary
- Selected relevant performance columns
- Standardized column names (lowercase + underscores)
- Exported clean dataset to CSV

## Key Challenges:
- JSON structure was nested (data[0] required)
- Track field was a dictionary, not flat
- Path issues when loading files
- Pandas not installed initially
- Column naming mismatch between CSV vs JSON fields
- Needed to ensure output file path included filename, not just folder

## Lessons Learned:
- How to convert JSON to DataFrame
- How to filter and select data using pandas
- How to flatten nested JSON fields using .apply()
- Importance of consistent column naming
- Debugging Python errors (NameError, FileNotFoundError, PermissionError)

## Current Ouput:
- File: processed_data/my_races_v1.csv
- Rows: 113
- Columns: 14
- Data scoped to race sessions only