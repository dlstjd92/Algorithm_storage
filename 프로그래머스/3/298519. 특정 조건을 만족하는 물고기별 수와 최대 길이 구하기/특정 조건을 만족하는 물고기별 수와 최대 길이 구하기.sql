SELECT 
    COUNT(*) AS FISH_COUNT,
    MAX(COALESCE(length, 10)) AS MAX_LENGTH,
    fish_type AS FISH_TYPE
FROM fish_info
GROUP BY fish_type
HAVING AVG(COALESCE(length, 10)) >= 33
ORDER BY fish_type;