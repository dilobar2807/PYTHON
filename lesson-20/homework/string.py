import pandas as pd
import sqlite3
conn=sqlite3.connect("chinook.db")
customers=pd.read_sql("SELECT * FROM customers", conn)
invoices=pd.read_sql("SELECT * FROM invoices", conn)
invoice_items=pd.read_sql("SELECT * FROM invoice_items", conn)

###  1. Customer Purchases Analysis     ####

#Find the total amount spent by each customer on purchases (considering invoices)

customer_total=invoices.groupby('CustomerId')['Total'].sum().reset_index()
customer_total=customer_total.merge(customers[['CustomerId', 'FirstName', "LastName"]], how='left', on="CustomerId")
customer_total

#Identify the top 5 customers with the highest total purchase amounts.
top5_customers=customer_total.sort_values("Total", ascending=False).head()
top5_customers

#Display the customer ID, name, and the total amount spent for the top 5 customers.
result=top5_customers[['CustomerId', "FirstName", "Total"]]
result


invoices = pd.read_sql("SELECT * FROM invoices", conn)
invoice_items = pd.read_sql("SELECT * FROM invoice_items", conn)
tracks = pd.read_sql("SELECT * FROM tracks", conn)
albums = pd.read_sql("SELECT * FROM albums", conn)

# 3️⃣ Invoice va tracklarni birlashtirish
df = invoice_items.merge(tracks[['TrackId', 'AlbumId']], on='TrackId', how='left')

# 4️⃣ Har bir invoice uchun har bir albomdagi track sonini hisoblash
invoice_album = df.groupby(['InvoiceId', 'AlbumId']).agg(
    tracks_bought=('TrackId', 'count')
).reset_index()

# 5️⃣ Albomdagi tracklar sonini olish
album_track_counts = tracks.groupby('AlbumId').agg(
    total_tracks=('TrackId', 'count')
).reset_index()

# 6️⃣ Invoice’dagi xarid qilingan track soni bilan albomdagi track sonini solishtirish
invoice_album = invoice_album.merge(album_track_counts, on='AlbumId', how='left')

# 7️⃣ Full album sotilgan yoki individual track
invoice_album['full_album'] = invoice_album['tracks_bought'] == invoice_album['total_tracks']

# 8️⃣ Har bir invoice’ni “full album” yoki “individual track” sifatida belgilash
# Agar invoice bir nechta albomni o'z ichiga olsa, faqat barcha tracklar xarid qilingan albomlar full_album bo'ladi
invoice_full_album = invoice_album.groupby('InvoiceId')['full_album'].all().reset_index()

# 9️⃣ Individual track xarid qilgan invoice’larni aniqlash
invoice_full_album['individual_track'] = ~invoice_full_album['full_album']

# 10️⃣ Foizni hisoblash
total_customers = invoices['CustomerId'].nunique()
# Har bir invoice bir mijozga tegishli bo‘lsa, unikal mijozlar sonini aniqlaymiz
customers_individual = invoices[invoices['InvoiceId'].isin(
    invoice_full_album[invoice_full_album['individual_track']]['InvoiceId']
)]['CustomerId'].nunique()

percentage_individual = (customers_individual / total_customers) * 100

print(f"Percentage of customers who prefer to buy individual tracks: {percentage_individual:.2f}%")
