SELECT  AVG(finish_position) AS average_finish_position,
        MIN(finish_position) AS best_finish,
        MAX(finish_position) AS worst_finish,
        COUNT(*) AS total_races
FROM races;