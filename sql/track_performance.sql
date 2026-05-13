SELECT  track_name,
        COUNT(*) AS total_races,
        ROUND(AVG(finish_position), 2) AS avg_finish,
        ROUND(AVG(incidents), 2) AS avg_incidents
FROM races
GROUP BY track_name
ORDER BY avg_finish;