import csv

with open('sales_data.csv', mode = 'r', newline='') as file:
    reader = csv.DictReader(file)
    data = [row for row in reader]

for row in data:
    print(row)

total_sales = 0
for entry in data:
    total_sales += int(entry["sales"])

region_sales = {}
for entry in data:
    region = entry["region"]
    sales = int(entry["sales"])
    if region in region_sales:
        region_sales[region] += sales
    else:
        region_sales[region] = sales

region_list = []
for region, sales in region_sales.items():
    region_list.append((region, sales))

for i in range(len(region_list)):
    for j in range(len(region_list) - 1):
        if region_list[j][1] < region_list[j + 1][1]:
            region_list[j], region_list[j + 1] = region_list[j + 1], region_list[j]

top_regions = region_list[:3]

bobbles_sales = 0
widgets_sales = 0
for entry in data:
    if entry["product"] == "bobbles":
        bobbles_sales += int(entry["sales"])
    elif entry["product"] == "widgets":
        widgets_sales += int(entry["sales"])

bobbles_price = 10.99
widgets_price = 15.99
bobbles_revenue = bobbles_sales * bobbles_price
widgets_revenue = widgets_sales * widgets_price

min_sales = float('inf')
min_region = ""
min_product = ""
for entry in data:
    sales = int(entry["sales"])
    if sales < min_sales:
        min_sales = sales
        min_region = entry["region"]
        min_product = entry["product"]

print(f"1. Total sales: {total_sales}")
print("2. Top three regions by sales:")
for region, sales in top_regions:
    print(f"   {region}: {sales}")
print(f"3. Bobbles sales: {bobbles_sales}, Widgets sales: {widgets_sales}")
print(f"   {'Bobbles' if bobbles_sales > widgets_sales else 'Widgets'} sold more")
print(f"4. Bobbles revenue: ${bobbles_revenue:.2f}")
print(f"   Widgets revenue: ${widgets_revenue:.2f}")
print(f"   {'Widgets' if widgets_revenue > bobbles_revenue else 'Bobbles'} made more revenue")
print(f"5. Least sold: {min_product} in {min_region} with {min_sales} sales")