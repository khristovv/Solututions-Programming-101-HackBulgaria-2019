--Gets those manufacturers who have made 
--more than 3 distinct pc models

SELECT product.maker, COUNT(DISTINCT pc.model) as distinct_models
    FROM pc
    INNER JOIN product
        ON pc.model = product.model
GROUP BY product.maker
    HAVING distinct_models > 3;
