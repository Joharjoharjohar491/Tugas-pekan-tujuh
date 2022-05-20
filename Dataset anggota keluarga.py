import pandas as pd

pizza = {
'Nama': ['Abdul', 'Yunus', 'Jomod', 'Johar', 'joang', 'jordi', 'Edi', 'Embuh', 'Jarene', 'Albert'],
'Tinggi Badan': [160, 145, 165, 175, 160, 165, 168, 172, 164, 166],
'Berat Badan' : [60, 50, 65, 90, 60, 70, 74, 80, 65, 68],
}

pizza_df = pd.DataFrame(pizza)
pizza_df
