# 🍽️ Restaurant Manager Advanced

A full-featured **Django-based restaurant management system** with an interactive **dashboard**, **Bootstrap UI**, **authentication (login/register)**, and complete **CRUD operations** for tables, menu items, and orders.

---

## 🌟 Features

- 🔐 **User Authentication**
  - Register, Login, and Logout system using Django Auth.
  - Secure access to admin and management pages.

- 📊 **Dashboard Overview**
  - Displays all key restaurant data (tables, menu items, and orders).
  - View, edit, and delete records from one place.

- 🍴 **Table Management**
  - Add, update, or remove tables.
  - Track seat availability and current status.

- 🧾 **Menu Management**
  - Manage menu items with categories, availability, and prices.
  - Search and filter menu items.

- 🧍 **Order Management**
  - Assign orders to tables and add multiple menu items.
  - View total price and order status (pending, served, etc.).

- 🎨 **Bootstrap-Powered UI**
  - Clean and responsive interface for all pages.
  - Modern dashboard layout and simple navigation.

---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Django 5.x |
| Frontend | HTML, CSS, Bootstrap |
| Database | SQLite |
| Auth System | Django Authentication |
| Template Engine | Django Templates |

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/banumariwan/restaurant_manager_advanced.git
cd restaurant_manager_advanced
2️⃣ Install Dependencies
bash
Copy code
pip install django
3️⃣ Run Database Migrations
bash
Copy code
python manage.py migrate
4️⃣ Create Superuser
bash
Copy code
python manage.py createsuperuser
5️⃣ Run the Development Server
bash
Copy code
python manage.py runserver
Then open http://127.0.0.1:8000 in your browser.

🧭 Project Structure
bash
Copy code
restaurant_manager_advanced/
│
├── restaurant/                 # Main app for tables, menu, and orders
│   ├── templates/restaurant/   # HTML templates
│   ├── models.py               # Database models
│   ├── views.py                # Business logic
│   └── urls.py                 # Route definitions
│
├── restaurant_manager/         # Project settings and URLs
├── db.sqlite3                  # SQLite database
├── manage.py                   # Django management file
└── README.md                   # Project documentation
🧑‍💻 Admin Panel
Access the Django admin at
👉 http://127.0.0.1:8000/admin

Use the superuser credentials you created earlier.

🧠 Learning Highlights
This project demonstrates:

CRUD operations in Django

Django ORM queries for filtering/sorting

User authentication with login/logout

Bootstrap template integration

Admin panel configuration

💡 Future Improvements
Add real-time order tracking using Django Channels.

Integrate a payment gateway.

Include chart analytics in the dashboard.

📜 License
This project is open-source and available under the MIT License.

Author: @banumariwan
🚀 Built with Django & Bootstrap

yaml
Copy code
