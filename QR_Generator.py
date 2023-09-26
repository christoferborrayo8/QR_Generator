import pandas as pd
import segno

df = pd.read_csv('./Enlaces.csv') 
columnas_deseadas = ['Nombre', 'Link']
df_filtrado = df[columnas_deseadas]

data_dark = (229, 90, 25)  # Naranja suave (R, G, B)
light = (255, 255, 255)  # Blanco (R, G, B)
dark = (79, 79, 79) # Gris (R, G, B)

for indice, fila in df_filtrado.iterrows():
    qrcode = segno.make_qr(fila["Link"])
    qrcode.to_artistic(
            background="./Logo.jpeg",
            target=f'./out/{fila["Nombre"]}.png',
            scale=10,
            dark=dark,
            data_dark=data_dark,
        )