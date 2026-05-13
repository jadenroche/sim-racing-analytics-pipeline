SELECT  track_name,
        COUNT(*) AS total_races,
        SUM(incidents) AS total_incidents,
        ROUND(AVG(incidents), 2) AS avg_incidents,
        MAX(incidents) AS max_incidents
FROM races
GROUP BY track_name
ORDER BY avg_incidents DESC;