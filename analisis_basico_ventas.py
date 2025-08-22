import pandas as pd

# Carga de datos
df = pd.read_csv("ventas_portafolio.csv", parse_dates=["Fecha"])

# Limpieza y enriquecimiento
df["AñoMes"] = df["Fecha"].dt.to_period("M").astype(str)
df["TicketPromedio"] = (df["Ventas"] / df["Cantidad"]).round(2)

# KPIs
kpis = {
    "ventas_totales": df["Ventas"].sum(),
    "margen_total": df["Margen"].sum(),
    "margen_pct_total": (df["Margen"].sum() / df["Ventas"].sum() if df["Ventas"].sum() > 0 else 0),
    "items_vendidos": int(df["Cantidad"].sum()),
    "ticket_promedio_global": (df["Ventas"].sum() / df["Cantidad"].sum()).round(2)
}

# Series temporales
ventas_mensuales = df.groupby("AñoMes")["Ventas"].sum().reset_index().sort_values("AñoMes")
margen_mensual = df.groupby("AñoMes")["Margen"].sum().reset_index().sort_values("AñoMes")

# Top productos y categorías
top_productos = df.groupby("Producto")["Ventas"].sum().nlargest(10).reset_index()
top_categorias = df.groupby("Categoría")["Ventas"].sum().sort_values(ascending=False).reset_index()
rentabilidad_region = df.groupby("Región")[["Ventas","Margen"]].sum().reset_index()
rentabilidad_region["MargenPct"] = rentabilidad_region["Margen"] / rentabilidad_region["Ventas"]

# Export básicos
ventas_mensuales.to_csv("ventas_mensuales.csv", index=False)
top_productos.to_csv("top_productos.csv", index=False)

# Impresiones de control
print("KPIs:", kpis)
print("Ventas mensuales:", ventas_mensuales.tail(), sep="\\n")
print("Top productos:", top_productos.head(), sep="\\n")
