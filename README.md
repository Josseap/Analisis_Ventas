# Sales and Profitability Dashboard

This project demonstrates the full process of **data cleaning with Python** and the creation of an **interactive Power BI dashboard** to analyze sales performance, margins, and profitability for a fictitious company.

---

## Objective
Build a clean and reliable dataset to analyze:
- Total Sales.  
- Total Margin and % Margin.  
- Units Sold.  
- Average Ticket Size.  
- Performance by **Region, Channel, and Product Category**.  

---

## Tools & Technologies
- **Python (Dataspell IDE)**  
  - `pandas` → data cleaning and transformation.  
  - `matplotlib`, `seaborn` → preliminary visualizations.  

- **Power BI**  
  - DAX measures for KPIs:  
    ```DAX
    Total Sales = SUM('ventas_limpias'[Ventas])
    Total Margin = SUM('ventas_limpias'[Margen])
    Units Sold = SUM('ventas_limpias'[Cantidad])
    Avg Ticket = DIVIDE([Total Sales], [Units Sold])
    % Margin = DIVIDE([Total Margin], [Total Sales])
    ```
  - Interactive dashboard with dynamic slicers by Date, Region, Channel, and Category.  

---

## Key Results
The final dashboard includes:
- **Executive KPIs**: Total Sales, Total Margin, % Margin, Units Sold, and Average Ticket.  
- **Visualizations**:
  - Monthly sales trend (line chart).  
  - Sales by Product Category (bar chart).  
  - Sales by Channel (bar chart).  
  - Margin % by Region (bar chart).  
- **Dynamic slicers** for exploratory analysis.  

---

## Dashboard Preview
![Dashboard Preview](path/to/your/image/dashboard.png)

---

## Portfolio Value
This project showcases skills in:
- Data processing and cleaning with Python.  
- Building business KPIs and DAX measures in Power BI.  
- Designing professional dashboards for executive reporting.  

---

## Repository Contents
- `analisis_basico_ventas.py` → Python script for data cleaning.  
- `ventas_portafolio.ipynb` → Jupyter notebook with exploratory analysis.  
- `ventas_limpias.csv` → Processed dataset.  
- `Proyecto_Ventas_Portafolio.pbix` → Power BI dashboard.  
- `README.md` → Project documentation.  

---

✉️ Author: **Jose Alfredo Jimenez**  
📍 Portfolio project for **Data Analyst / Business Intelligence** positions.  
