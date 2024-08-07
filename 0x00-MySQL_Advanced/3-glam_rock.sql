-- Write a SQL script that lists all bands with Glam roc
SELECT band_name, (IFNULL(split, '2023') - formed) AS lifespan
    FROM metal_bands
    WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
    ORDER BY lifespan DESC;
