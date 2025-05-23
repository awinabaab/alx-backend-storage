-- Lists all bands with "Glam rock" as their main style, ranked by their longetivity

SELECT band_name, IFNULL(split, 2022) - formed AS lifespan
FROM metal_bands
WHERE style REGEXP "Glam rock"
ORDER BY lifespan DESC;
