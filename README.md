<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Atelier Étoile](#atelier-%C3%89toile)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Requirements](#requirements)
  - [User Stories](#user-stories)
    - [View products](#view-products)
      - [As a **Shopper,** I can **view a list of products** so that **I can select some to purchase**](#as-a-shopper-i-can-view-a-list-of-products-so-that-i-can-select-some-to-purchase)
    - [Product details](#product-details)
      - [As a **Shopper,** I can **view individual product details** so that **I can identify the price, description, product rating, product image and available sizes**](#as-a-shopper-i-can-view-individual-product-details-so-that-i-can-identify-the-price-description-product-rating-product-image-and-available-sizes)
    - [Special offers](#special-offers)
      - [As a **Shopper,** I can **quickly identify deals, clearance items and special offers** so that **take advantage of special savings on products I'd like to purchase**](#as-a-shopper-i-can-quickly-identify-deals-clearance-items-and-special-offers-so-that-take-advantage-of-special-savings-on-products-id-like-to-purchase)
    - [View total](#view-total)
      - [As a **Shopper,** I can **easily view the total of my purchases at any time** so that **avoid overspending**](#as-a-shopper-i-can-easily-view-the-total-of-my-purchases-at-any-time-so-that-avoid-overspending)
    - [Registration](#registration)
      - [As a **Site User** I want to **easily register for an account** so that **I have a personal account and can view my profile**](#as-a-site-user-i-want-to-easily-register-for-an-account-so-that-i-have-a-personal-account-and-can-view-my-profile)
    - [Login Logout](#login-logout)
      - [As a **Site User** I want to **easily login or logout** so that **I can access my personal account information**](#as-a-site-user-i-want-to-easily-login-or-logout-so-that-i-can-access-my-personal-account-information)
    - [Password recovery](#password-recovery)
      - [As a **Site User** I want to **easily recover my password in case I forget it** so that **I can recover access to my account**](#as-a-site-user-i-want-to-easily-recover-my-password-in-case-i-forget-it-so-that-i-can-recover-access-to-my-account)
    - [Email confirmation](#email-confirmation)
      - [As a **Site User** I want to **receive an email confirmation after registering** so that **I can verify my account registration was successful**](#as-a-site-user-i-want-to-receive-an-email-confirmation-after-registering-so-that-i-can-verify-my-account-registration-was-successful)
    - [Personal user information](#personal-user-information)
      - [As a **Site User** I want to **have a personalised user profile** so that **I can view my personal order history and order confirmations, and save my payment information**](#as-a-site-user-i-want-to-have-a-personalised-user-profile-so-that-i-can-view-my-personal-order-history-and-order-confirmations-and-save-my-payment-information)
    - [Sort the products](#sort-the-products)
      - [As a **Site User** I want to **sort the list of available products** so that **I can easily identify the best rated, the best priced and categorically sorted products**](#as-a-site-user-i-want-to-sort-the-list-of-available-products-so-that-i-can-easily-identify-the-best-rated-the-best-priced-and-categorically-sorted-products)
  - [Wireframes](#wireframes)
    - [Home page](#home-page)
  - [Features](#features)
  - [Technology Stack](#technology-stack)
  - [System Architecture](#system-architecture)
  - [Database Design](#database-design)
  - [Deployment](#deployment)
  - [Setup Instructions](#setup-instructions)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Environment Variables](#environment-variables)
    - [Run Locally](#run-locally)
  - [Testing](#testing)
  - [Future Enhancements](#future-enhancements)
  - [Credits](#credits)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Atelier Étoile


A fully featured **Django-based e-commerce web application** that demonstrates secure payment processing, robust authentication, and modern deployment practices.

![Mockup](./documentation/all-devices-white.png)


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

This project demonstrates the use of Django Template Language (DTL) to build a reusable base layout with Bootstrap for styling. The base template provides a consistent navigation bar, footer, and message display system across all pages.

## Requirements

The site owner wants readers to enjoy using the site. With that in mind the pages should be visually appealing at the same time simple to use.

The site should be responsive, adapting to all screen sizes.

## User Stories

### View products
#### As a **Shopper,** I can **view a list of products** so that **I can select some to purchase**

- When a category of products is clicked on a listing is seen.

### Product details
#### As a **Shopper,** I can **view individual product details** so that **I can identify the price, description, product rating, product image and available sizes**

- When a product is clicked on it's details are visible.

### Special offers
#### As a **Shopper,** I can **quickly identify deals, clearance items and special offers** so that **take advantage of special savings on products I'd like to purchase**

- A navigation link that allows me to view different saving types

### View total
#### As a **Shopper,** I can **easily view the total of my purchases at any time** so that **avoid overspending**

- A navigation link that adjusts as the shopping bag is modified.

### Registration
#### As a **Site User** I want to **easily register for an account** so that **I have a personal account and can view my profile**

### Login Logout
#### As a **Site User** I want to **easily login or logout** so that **I can access my personal account information**

### Password recovery
#### As a **Site User** I want to **easily recover my password in case I forget it** so that **I can recover access to my account**

### Email confirmation
#### As a **Site User** I want to **receive an email confirmation after registering** so that **I can verify my account registration was successful**

### Personal user information
#### As a **Site User** I want to **have a personalised user profile** so that **I can view my personal order history and order confirmations, and save my payment information**

### Sort the products
#### As a **Site User** I want to **sort the list of available products** so that **I can easily identify the best rated, the best priced and categorically sorted products**

## Wireframes

-   These wireframes were created using simple ASCII-style text during the Scope Plane part of the design and planning process for this project. The site was developed with the Desktop layout method first. The wireframes were therefore drawn with that thought in mind and adapted alongside project changes.
### Home page
-   ![Screenshot Home Page wireframe ](./documentation/atelierWframe.png)
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

