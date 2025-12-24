# EnergyHub - Full Stack Web Application

![Django](https://img.shields.io/badge/Django-6.0-green)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Overview

**EnergyHub** is a full-stack web application for a service-based energy company (Stark Industries). The platform includes user authentication, dynamic service pages, and a responsive mobile-first design.

Built from scratch to understand real-world web development concepts: authentication, session management, security, and full-stack architecture.

<img width="1920" height="1080" alt="Signup" src="https://github.com/user-attachments/assets/bfa3a9b0-0987-4bf5-bfe3-5994dd1bf75a" />
<img width="1920" height="1080" alt="Signin" src="https://github.com/user-attachments/assets/023eca8d-dfae-424e-9525-e8ddbdc4965b" />
<img width="1920" height="1080" alt="home" src="https://github.com/user-attachments/assets/ecef7945-bd54-4a93-bc53-f7f06cc3e499" />
<img width="1920" height="1080" alt="content" src="https://github.com/user-attachments/assets/b32d9944-bb39-4bcf-b979-57689478fb4b" />
<img width="1920" height="1080" alt="footer" src="https://github.com/user-attachments/assets/4a18857d-85fe-41c5-b8ea-33a5721828f8" />
<img width="1920" height="1080" alt="next_page" src="https://github.com/user-attachments/assets/1a977cd6-3c89-47c6-a7bc-0f54f40a1519" />

---

## 🎯 Features

✅ **User Authentication**
- Signup with email and password
- Secure signin with password verification
- Logout functionality
- Session management (users stay logged in)

✅ **Security**
- Password hashing (PBKDF2 with SHA256)
- CSRF protection on all forms
- Unique email constraint (no duplicate accounts)
- Secure session storage

✅ **Responsive Design**
- Mobile-first approach
- Desktop: Left-right card animation
- Mobile: Up-down card animation
- Works on all devices (tested on 425px to 1920px)

✅ **Service Pages**
- Energy Solutions
- Gas Solutions
- Power Generation
- Sustainability
- Resources Management
- Contact Form
- Support & FAQ

✅ **User Dashboard**
- Welcome message with user name
- Navigation to all service pages
- Logout button
- Personalized experience

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Django 6.0 (Python 3.12) |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Database** | SQLite3 |
| **Hosting Ready** | Heroku, Render, PythonAnywhere |
| **Design** | Mobile-responsive CSS |

---

## 📁 Project Structure

EnergyHub/
│
├── app/                          # Main application
│   ├── migrations/               # Database migrations
│   ├── static/
│   │   └── core/
│   │       ├── css/              # CSS files
│   │       ├── js/               # JavaScript files
│   │       ├── font/             # FontAwesome icons
│   │       └── image/            # Images (bg, clouds, man, etc)
│   ├── templates/
│   │   ├── base.html            # Reusable template
│   │   ├── index.html           # Signup/Signin page
│   │   ├── main.html            # Home dashboard
│   │   ├── energy.html          # Energy services page
│   │   ├── gas.html             # Gas services page
│   │   ├── power.html           # Power generation page
│   │   ├── sustainability.html  # Sustainability page
│   │   ├── resources.html       # Resources page
│   │   ├── contact.html         # Contact form page
│   │   └── support.html         # Support/FAQ page
│   ├── forms.py                 # Django Forms (Signup, Signin)
│   ├── models.py                # User model
│   ├── views.py                 # All view functions
│   ├── urls.py                  # URL routing
│   ├── admin.py
│   ├── apps.py
│   └── init.py
│
├── project/                     # Django project settings
│   ├── settings.py              # Configuration
│   ├── urls.py                  # Main URL router
│   ├── wsgi.py
│   └── init.py
│
├── manage.py                    # Django management
├── .gitignore                   # Files to ignore in git
├── README.md                    # This file
└── LICENSE                      # MIT License

---

## 🚀 How to Run Locally

### Prerequisites
- Python 3.8+
- Git
- Any code editor (VS Code, PyCharm, etc)

### Installation Steps

#### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/EnergyHub.git
cd EnergyHub
```

#### 2️⃣ Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

#### 3️⃣ Install Django
```bash
pip install django
```

#### 4️⃣ Apply Database Migrations
```bash
python manage.py migrate
```

#### 5️⃣ Run Development Server
```bash
python manage.py runserver
```

#### 6️⃣ Open in Browser

http://127.0.0.1:8000/

#### 7️⃣ Test Login
- Signup: Create new account
- Click "Sign Up" button → Fill form → Submit
- Get redirected to dashboard
- See your name in welcome message
- Click logout to test

---

## 📚 Learning Journey & Challenges

### Challenge 1: Signup vs Signin - Separate Models?
**Problem:** Initially created two separate User models for signup and signin

**Solution:** Realized both operations use the same user data:
- Signup: Create new user (INSERT)
- Signin: Check existing user (SELECT + verify)
- Used single User model for both

**Code:**
```python
# Signup - Create user
user = User(name=name, email=email, password=make_password(password))
user.save()

# Signin - Verify user
if check_password(entered_password, user_obj.password):
    request.session['user_id'] = user_obj.id
```

---

### Challenge 2: Static Files Not Loading
**Problem:** CSS, JS, images weren't showing on website (404 errors)

**Root Cause:** Wrong file paths and missing `{% static %}` tags

**Solution:** 
- Moved files to `static/core/` folder
- Used Django `{% static %}` template tag
- Updated all image paths

**Before (Wrong):**
```html
<img src="image/bg.jpg" />
<link rel="stylesheet" href="./css/style.css" />
```

**After (Correct):**
```html
{% load static %}
<img src="{% static 'core/image/bg.jpg' %}" />
<link rel="stylesheet" href="{% static 'core/css/style.css' %}" />
```

---

### Challenge 3: Mobile Card Animation
**Problem:** Desktop left-right animation didn't work on narrow mobile screens

**Why:** Screen too small for side-by-side cards

**Solution:** Used CSS media queries for different animations
```css
/* Desktop */
transform: translateX(100%);  /* Left-right */

/* Mobile (max-width: 480px) */
transform: translateY(100%);  /* Up-down */
```

---

### Challenge 4: JavaScript Not Working
**Problem:** Card slider buttons didn't toggle between signin/signup

**Causes Found:**
1. JavaScript file in wrong folder (not in `static/`)
2. Trying to access elements before DOM loaded
3. Missing `return` statements in views

**Solution:**
```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Now DOM is ready, can safely access elements
    const signUpButton = document.getElementById('signUp');
    signUpButton.addEventListener('click', () => {
        container.classList.add("right-panel-active");
    });
});
```

---

### Challenge 5: Django Rejected External URL
**Problem:** ngrok forwarding URL returned DisallowedHost error

**Error:** DisallowedHost: Invalid HTTP_HOST header: '76398cdddc1b.ngrok-free.app'  (Example)
**Solution:**
```python
# settings.py
ALLOWED_HOSTS = ['*']  # Development only
```

---

## 🔐 Security Features Implemented

| Feature | Implementation |
|---------|-----------------|
| **Password Hashing** | PBKDF2 with SHA256 (Django default) |
| **CSRF Protection** | `{% csrf_token %}` on all forms |
| **Unique Email** | `unique=True` on User model |
| **Session Storage** | Server-side with encrypted cookies |
| **Password Verification** | `check_password()` function |

---

## 📊 User Model
```python
class User(models.Model):
    id              # Auto-generated primary key
    name            # CharField, max 100 characters
    email           # EmailField, unique=True (no duplicates)
    password        # CharField, 254 chars (stores hash, not plain text)
```

**Why 254 chars for password?**
- PBKDF2 hash ≈ 80-100 chars
- Plus algorithm, salt, iterations: ≈ 150-200 chars total
- 254 is safe margin

---

## 🧪 Testing Performed

### Manual Tests (What I Did)

✅ **Signup Flow**
- Create new account
- Email uniqueness works
- Password hashing works
- Redirects to dashboard

✅ **Signin Flow**
- Login with correct password → Success
- Login with wrong password → Error
- Session stores user data
- User name displays on dashboard

✅ **Navigation**
- All nav links work
- Active page highlighted
- Can't access pages without login (redirects to index)

✅ **Mobile Responsiveness**
- Card animation works up-down on mobile
- Card animation works left-right on desktop
- Forms responsive on all screen sizes
- Images load properly

✅ **Security**
- CSRF token works
- Logout clears session
- Can't access /main/ without login

---

## 🔄 How It Works (User Flow)
User visits website
↓
See signin/signup page
↓
Click "Sign Up" → Form slides to signup
↓
Fill form (name, email, password)
↓
Backend hashes password
↓
User saved to database
↓
Redirects to /main/
↓
Session stores user_id
↓
Dashboard displays user name
↓
User can access service pages
↓
Click logout → Session cleared
↓
Redirected to login page

---

## 🚀 Deployment Guide

### Before Deploying:
```python
# settings.py
DEBUG = False  # CRITICAL! Not True
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECRET_KEY = os.environ.get('SECRET_KEY')  # Use environment variable
```

### Recommended Platforms:
- **Heroku** (Easy, free tier available)
- **Render** (Free, modern)
- **PythonAnywhere** (Simple, good for beginners)

### Database for Production:
- Replace SQLite3 with PostgreSQL
- Use proper backups
- Monitor performance

---

## 📈 Future Improvements

### Phase 2 Features (Could add):
- [ ] Email verification on signup
- [ ] Password reset (forgot password)
- [ ] User profile page
- [ ] Edit profile
- [ ] Service request history
- [ ] Email notifications
- [ ] Admin dashboard

### Phase 3 Features (Advanced):
- [ ] Payment integration (Stripe)
- [ ] Subscription plans
- [ ] API endpoints
- [ ] Mobile app
- [ ] Two-factor authentication
- [ ] OAuth (Google/Facebook login)

---

## 🤝 Contributing

This is a learning project, but if you'd like to contribute:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**In plain English:** You can use this code for personal or commercial projects, modify it, distribute it, but you must include the original license.

---

## 👨‍💻 Author

**Om Bhosle**
- GitHub: ombhosle5 (https://github.com/ombhosle5)
- Email: ombhosale24@gmail.com
- Location: Ahmedabad, Gujarat, India

---

## 🙏 Acknowledgments

- Django Documentation: https://docs.djangoproject.com/
- FontAwesome Icons: https://fontawesome.com/
- Inspired by real-world energy companies' websites

---

## 📞 Support

Found a bug or have a question?

1. Check existing issues on GitHub
2. Create a new issue with:
   - Clear title
   - Description of problem
   - Steps to reproduce
   - Expected vs actual behavior

---

## 📝 Changelog

### Version 1.0.0 (Initial Release)
- User authentication (signup/signin/logout)
- Session management
- Password hashing
- Service pages (Energy, Gas, Power, etc)
- Responsive mobile design
- Contact form
- Support FAQ

---

## ⭐ If You Found This Helpful

Please consider:
- Starring the repository
- Following on GitHub
- Sharing with others learning Django
- Providing feedback/suggestions

---

**Last Updated:** December 2025
**Status:** Active Development ✅
**Python Version:** 3.12+
**Django Version:** 6.0+



