(:Gene {
  symbol: "BRCA1",
  chromosome: "17"
})-[:ENCODES]->(:Protein {
  name: "BRCA1 protein"
})-[:INTERACTS_WITH {
  type: "inhibitor"
}]->(:Drug {
  name: "Olaparib"
})