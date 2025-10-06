# Atelier Étoile

A fully featured **Django-based e-commerce web application** that demonstrates secure payment processing, robust authentication, and modern deployment practices.

[Live Site](https://milestone4ecommerce-6c0c8f5c0454.herokuapp.com)

---

## Table of Contents

* [Overview](#overview)
* [Features](#features)
* [Technology Stack](#technology-stack)
* [System Architecture](#system-architecture)
* [Database Design](#database-design)
* [Deployment](#deployment)
* [Setup Instructions](#setup-instructions)
* [Testing](#testing)
* [Future Enhancements](#future-enhancements)
* [Credits](#credits)

---

## Overview

This project was built as part of my ongoing exploration of **Django web application development**. It implements a complete e-commerce solution with product management, order handling, Stripe-based payments, and secure user authentication.

The goal is to demonstrate the ability to build and deploy a production-grade Django application with a cloud-hosted database and static/media asset management via Heroku.

---

## Features

* **Product Management**

  * Browse, search, and filter products by category
  * Detailed product pages with pricing and image support

* **Shopping Cart and Checkout**

  * Add/remove/update items in cart
  * Checkout workflow with Stripe integration
  * Secure payments with real-time success/failure feedback

* **User Accounts**

  * Registration, login, logout, and password management
  * Profile management with order history tracking
  * Email confirmation for new users

* **Admin Interface**

  * Product and order management via Django Admin
  * Secure access for superusers

* **Responsive UI**

  * Clean, accessible, and mobile-friendly design
  * Built using Bootstrap and Django templates

---

## Technology Stack

| Layer                  | Technology                                      |
| ---------------------- | ----------------------------------------------- |
| **Backend Framework**  | Django (Python 3.9)                             |
| **Database**           | PostgreSQL (via ElephantSQL)                    |
| **Payment Processing** | Stripe                                          |
| **Frontend**           | HTML5, Bootstrap 5, CSS, JavaScript             |
| **Cloud Hosting**      | Heroku                                          |
| **Media Storage**      | Cloudinary                                      |
| **Version Control**    | Git / GitHub                                    |
| **Email Backend**      | Django Allauth and SMTP for verification emails |

---

## System Architecture

```
User → Django Views → Models → PostgreSQL
       ↓
     Templates + Static Files (Bootstrap)
       ↓
  Stripe API for Payments
       ↓
  Cloudinary (Image Hosting)
```

---

## Database Design

* **Category**

  * name
  * friendly_name

* **Product**

  * name
  * description
  * price
  * category (ForeignKey)
  * image

* **Order**

  * user (ForeignKey)
  * full_name
  * email
  * address
  * total_cost

* **OrderLineItem**

  * order (ForeignKey)
  * product (ForeignKey)
  * quantity

---

## Deployment

This project is deployed on **Heroku** with the following configuration:

* `Procfile` defines the app’s web process
* `requirements.txt` specifies Python dependencies
* `runtime.txt` sets the Python version
* Environment variables for sensitive data such as:

  * `SECRET_KEY`
  * `DATABASE_URL`
  * `STRIPE_PUBLIC_KEY`
  * `STRIPE_SECRET_KEY`
  * `CLOUDINARY_URL`

Static and media files are served via **Cloudinary**.

---

## Setup Instructions

### Prerequisites

* Python 3.9+
* pip and virtualenv

### Installation

```bash
git clone https://github.com/AmitKapilaCodeIns/ecommerce_site.git
cd ecommerce_site
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file with the following:

```
SECRET_KEY=your_django_secret_key
DATABASE_URL=your_postgres_url
STRIPE_PUBLIC_KEY=your_stripe_public_key
STRIPE_SECRET_KEY=your_stripe_secret_key
CLOUDINARY_URL=your_cloudinary_url
DEBUG=True
```

### Run Locally

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Access the site at `http://127.0.0.1:8000/`

---

## Testing

* Unit tests implemented for key views and models
* Manual testing for checkout, payments, and authentication
* Stripe test cards used to validate payment integration

---

## Future Enhancements

* Add product reviews and ratings
* Implement discount codes and coupons
* Introduce order tracking functionality
* Integrate CI/CD pipeline (GitHub Actions)

---

## Credits

Developed by **Amit Kapila**
Hosted on Heroku
For educational and demonstration purposes

[GitHub Repository](https://github.com/AmitKapilaCodeIns/ecommerce_site)

