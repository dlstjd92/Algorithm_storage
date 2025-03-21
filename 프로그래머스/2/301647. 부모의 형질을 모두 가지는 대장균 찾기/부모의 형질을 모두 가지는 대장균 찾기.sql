SELECT 
    e.id, 
    e.genotype,
    p.genotype AS parent_genotype
FROM ecoli_data e
JOIN ecoli_data p ON e.parent_id = p.id
WHERE (e.genotype & p.genotype) = p.genotype
ORDER BY e.id;