# 📚 Library Management System (Django)

A Library Management web app built with **Django** in just 2 days as part of an interview assignment at **Zillion Infotech**.  
It allows **librarians** to manage books and **users** to borrow/request them, with role-based access control.  

---

## 🚀 Features

### 🔑 Authentication
- User registration with roles (**Librarian / Normal User**)  
- Login & Logout with session management  

### 👩‍💼 Librarian
- Add new books with title, author, and stock  
- Check **stock status** of books  
- Approve user book requests (auto reduce stock & set renewal date)  
- View assigned books  

### 👨‍🎓 Normal User
- Browse available books  
- Request a book (duplicate requests prevented)  
- View assigned/approved books  

---

## 🛠 Tech Stack
- **Backend:** Django  
- **Database:** SQLite (default, can be replaced)  
- **Frontend:** Django Templates (HTML, CSS, Bootstrap)  
- **Authentication:** Django’s built-in `User` model + custom profile  

---

## 📂 Project Structure (main apps)
- `register_page`, `login_page`, `logout_view` → Authentication  
- `librarian_page`, `stock_status`, `approved_request`, `assign_books` → Librarian module  
- `normal_user`, `available_books`, `assigned_books` → User module



-gement
