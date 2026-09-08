import matplotlib.pyplot as plt

# -------------------------------
# 1. Line Chart - Trend over time
# -------------------------------

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 130, 180, 220]

plt.plot(months, sales, marker='o')
plt.title("Sales Trend Over Time")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()


# -------------------------------
# 2. Bar Chart - Product sales
# -------------------------------

products = ["Laptop", "Phone", "Tablet", "Headphones"]
product_sales = [50, 80, 40, 70]

plt.bar(products, product_sales)
plt.title("Sales of Different Products")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()


# -------------------------------
# 3. Histogram - Age distribution
# -------------------------------

ages = [18, 20, 21, 19, 22, 25, 30, 21, 23, 19,
        20, 22, 24, 26, 28, 21, 20, 19, 23, 25]

plt.hist(ages, bins=5)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# -------------------------------
# 4. Pie Chart - Category distribution
# -------------------------------

categories = ["Science", "Arts", "Commerce", "Computer"]
students = [30, 20, 25, 25]

plt.pie(students, labels=categories, autopct="%1.1f%%")
plt.title("Student Category Distribution")
plt.show()
