# Project Notes

## Challenges Encountered

- Normalized track and configuration names to prevent duplicate values.
- Added duplicate prevention using subsession_id as primary key.
- Expanded schema to include IDs for car classes, series, and event types.
- Filtered low-volume tracks and cars in Power BI to avoid misleading averages.

## Key Decisions

- Used SQLite for lightweight relational storage.
- Chose modular scripts for ingestion and processing.
- Kept dashboard filters synchronized between report pages.
- Used real iRacing data for iterative analysis and continuous project growth.

## Future Expansion

- API-based ingestion
- Telemetry metrics
- Expanded SQL analysis library
- Predictive performance analysis