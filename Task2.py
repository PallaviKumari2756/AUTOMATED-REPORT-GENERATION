import pandas as pd
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

data = {
    'Date': pd.date_range(start='2025-06-01', periods=7),
    'Sales': [1500, 1600, 1800, 1700, 1750, 1600, 1900]
}
df = pd.DataFrame(data)

df.to_excel("weekly_sales.xlsx", index=False)
plt.figure(figsize=(8, 4))
plt.plot(df['Date'], df['Sales'], marker='o')
plt.title('Weekly Sales Trend')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.grid(True)
plt.tight_layout()
plt.savefig('sales_plot.png')
def create_pdf_report(dataframe, image_path, output_path):
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, height - 50, "Weekly Sales Report")

    c.setFont("Helvetica", 12)
    y = height - 100
    for i, row in dataframe.iterrows():
        c.drawString(100, y, f"{row['Date'].date()} : ₹{row['Sales']}")
        y -= 20

    c.drawImage(image_path, 100, y - 250, width=400, height=200)
    c.save()

create_pdf_report(df, 'sales_plot.png', 'sales_report.pdf')
