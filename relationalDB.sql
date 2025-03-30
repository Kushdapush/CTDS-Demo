TABLE genes (
  gene_id INT PRIMARY KEY,
  symbol VARCHAR(20),
  chromosome VARCHAR(5)
);

TABLE proteins (
  protein_id INT PRIMARY KEY,
  gene_id INT FOREIGN KEY,
  name VARCHAR(100)
);

TABLE drugs (
  drug_id INT PRIMARY KEY,
  name VARCHAR(100)
);

TABLE protein_drug_interactions (
  protein_id INT FOREIGN KEY,
  drug_id INT FOREIGN KEY,
  interaction_type VARCHAR(50),
  PRIMARY KEY (protein_id, drug_id)
);