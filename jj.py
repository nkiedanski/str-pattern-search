from exact_matches import exact_matches
from inexact_matches import inexact_matches

largo = "TTTTTTAACCTACTGTGTGTGTGGTTTTTTTTGGGTGTGCATGTGTACAGTGAGATTGTC\
AAAAAGGAAGGATGTCGTCTGTGAAGGCTCTCAATCCGTCCTTGCAGGCCCGCCGTGACC\
CGTACTACAAGCGCAACCACATGGGCCGCGTCACATGTACTCTCTGTGATGTCTGCTGCA\
CAGATGACAATAACTTTTTGAAGCATATTGCAGGGAAGACGCACTGCACACAACTGGAGC\
GCATGGAGCGTCACGCACGTCGTGAGGAGCGGCTGGCGGTTGAGGAGGAATTGAATAGGG\
AGGCATGTCGACGCGCGTCGCAGGAAAAGGCAGCACGTGAGCTTTTATTACAACAGCAGG\
ATCAGCAGGCAGGCAGTCGTGGTGGTGCGACAGGCACGGATATCGCATCCTTCGCACCTT\
TTGGCAGGCCGCAGTTCAATTACTGCACCGAAAATGATCCAGAGTTGTTTCAGACAAAAG\
TGTGGATTGAATTTTTCTTCCCGCAGGCAGCGGCGGGGGTTCGGCCACTGCACCGCTGGC\
GGTCTGCGAGAGAGCAGGACATGGAGAGGCCACCGGATGACAGTGTCGTGTATTTACTTG\
TGGCATGCGAGGGATATGTGACGATTGCCGTCAAGTTTCCATCGAAACTTCCGCGCACAT\
CTGCATCCTCCTCTGTTGCCATGACCGCAAAGACAATGGCATCCTACGGGAGTGAAGTTG"

corta = "GCATAM"

prueba_inexact_mateches = inexact_matches(corta, largo, 1)
prueba_exact_mateches = exact_matches(corta, largo)

print("inexact matches")
print (prueba_inexact_mateches)

print("exact matches")
print (prueba_exact_mateches)
