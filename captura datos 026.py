import streamlit as st
import pandas as pd
import os

# Título de la aplicación
st.title("Consolidación de Datos")

# Selección de la carpeta de origen (aunque no se puede seleccionar una carpeta completa directamente en Streamlit, puedes cargar los archivos .xlsx manualmente)
carpeta_origen = st.text_input("Carpeta de origen", 'H:/Mi unidad/01. ZNI EXPERT/1. EMPRESAS/5. DISPOWER/5. Calculos 026/2024/12. Diciembre/Excel')

# Selección del mes y año
mes = st.selectbox("Selecciona el mes", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
año = st.number_input("Ingresa el año", min_value=2000, max_value=2100, value=2024)

# Asignar ipp_base como constante
ipp_base = 147.65

# Archivo de salida
archivo_salida = f'{carpeta_origen}/calculos_026_{mes}_{año}.xlsx'

# Lista para almacenar datos extraídos
datos_consolidados = []

# Selección de archivos Excel en la carpeta
archivos = [f for f in os.listdir(carpeta_origen) if f.endswith('.xlsx')]
archivos_seleccionados = st.multiselect("Selecciona los archivos Excel", archivos)

if archivos_seleccionados:
    # Procesar los archivos seleccionados
    for archivo in archivos_seleccionados:
        ruta_archivo = os.path.join(carpeta_origen, archivo)
        
        # Lee el archivo Excel (puedes especificar hojas con sheet_name)
        df = pd.read_excel(ruta_archivo, sheet_name=0)  # Cambia '0' si necesitas otra hoja
        
        # Extrae valores de celdas específicas
        valor_a1 = df.iloc[5, 1]  # Departamento
        valor_a2 = df.iloc[5, 2]  # Municipio
        valor_a3 = df.iloc[5, 3]  # Divipola
        valor_a4 = df.iloc[5, 4]  # Radiacion
        valor_a5 = df.iloc[8, 2]  # tipo sistema
        valor_a6 = df.iloc[9, 2]  # Almacenamiento
        valor_a7 = df.iloc[10, 2]  # Whd
        valor_a8 = df.iloc[12, 2]  # IPPm-1
        valor_a9 = df.iloc[78, 2]  # Total Cartera Vencida entre 90 -360
        valor_a10 = df.iloc[79, 2]  # Total Cartera Subsidios m-1
        valor_a11 = df.iloc[81, 2]  # Tasa costo financiero capital de trabajo m-2
        valor_a12 = df.iloc[110, 2]  # AMGCnu_0
        valor_a13 = df.iloc[111, 2]  # AMGCvi_0
        valor_a14 = df.iloc[112, 2]  # AMGCau_0
        valor_a15 = df.iloc[113, 2]  # AMGCnf_0
        valor_a16 = df.iloc[114, 2]  # AMGCro_0
        valor_a17 = df.iloc[110, 3]  # AMGCnu_m
        valor_a18 = df.iloc[111, 3]  # AMGCvi_m
        valor_a19 = df.iloc[112, 3]  # AMGCau_m
        valor_a20 = df.iloc[113, 3]  # AMGCnf_m
        valor_a21 = df.iloc[114, 3]  # AMGCro_m
        valor_a22 = df.iloc[122, 2]  # Inversion
        valor_a23 = df.iloc[123, 2]  # AMGCm
        valor_a24 = df.iloc[124, 2]  # Disponibilidad
        valor_a25 = df.iloc[125, 2]  # Facturacion (Subtotal)
        valor_a26 = df.iloc[127, 2]  # Subsidio
        valor_a27 = df.iloc[129, 2]  # Tarifa
        valor_a28 = df.iloc[122, 4]  # Empresa SIN
        valor_a29 = df.iloc[122, 5]  # Tarifa SIN
        valor_a30 = df.iloc[125, 5]  # Subsidio dia
        valor_a31 = df.iloc[126, 5]  # Porcentaje Subsidio

        # Agrega los datos a la lista
        datos_consolidados.append({
            'Archivo': archivo,
            'Departamento': valor_a1,
            'Municipio': valor_a2,
            'Divipola': valor_a3,
            'Radiacion': valor_a4,
            'Tipo de Sistema': valor_a5,
            'Almacenamiento': valor_a6,
            'Whd': valor_a7,
            'IPP_base' : ipp_base,
            'IPPm_1': valor_a8,
            'Cartera vencida 90_360': valor_a9,
            'Cartera_Subs': valor_a10,
            'Tasa_Costo_Fin': valor_a11,
            'AMGCnu_0': valor_a12,
            'AMGCvi_0': valor_a13,
            'AMGCau_0': valor_a14,
            'AMGCnf_0': valor_a15,
            'AMGCro_0': valor_a16,
            'AMGCnu_m': valor_a17,
            'AMGCvi_m': valor_a18,
            'AMGCau_m': valor_a19,
            'AMGCnf_m': valor_a20,
            'AMGCro_m': valor_a21,
            'Inversion': valor_a22,
            'AMGCm': valor_a23,
            'Disponibilidad': valor_a24,
            'Facturacion_mes': valor_a25,
            'Subsidio_mes': valor_a26,
            'Tarifa_mes': valor_a27,
            'Empresa SIN': valor_a28,
            'Tarifa SIN': valor_a29,
            'Subsidio_dia': valor_a30,
            'Porcentaje_subsidio': valor_a31,
            'Año' : año,
            'Mes' : mes
        }) # Consolidar y guardar en Excel

    if datos_consolidados:
        df_consolidado = pd.DataFrame(datos_consolidados)
        df_consolidado.to_excel(archivo_salida, index=False)
        st.success(f'Datos consolidados guardados en: {archivo_salida}')
    else:
        st.warning("No se encontraron datos válidos para consolidar.")
else:
    st.info("Por favor, selecciona los archivos que deseas procesar.")
