<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Atelier Étoile](#atelier-%C3%89toile)
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
  - [Code](#code)
      - [Files](#files)
      - [Environment variables (env.py)](#environment-variables-envpy)
      - [Database Configuration (settings.py & dj_database_url)](#database-configuration-settingspy--dj_database_url)
      - [Loose Coupling with urls.py](#loose-coupling-with-urlspy)
      - [References settings.py](#references-settingspy)
      - [AllAuth](#allauth)
      - [Email](#email)
      - [Templates and views](#templates-and-views)
        - [AllAuth](#allauth-1)
        - [Base template](#base-template)
        - [Home index.html](#home-indexhtml)
        - [base.css](#basecss)
      - [Code format](#code-format)
      - [Code understandability](#code-understandability)
      - [Code validation](#code-validation)
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
## Code

#### Files

-   Files are grouped in directories by file type
<pre><code>
ecommerce_site amitkapila$ ls *
db.sqlite3              manage.py               README.md
env.py                  Procfile                requirements.txt

__pycache__:
env.cpython-312.pyc     env.cpython-39.pyc

bag:
__init__.py     admin.py        contexts.py     models.py       templatetags    urls.py
__pycache__     apps.py         migrations      templates       tests.py        views.py

checkout:
__init__.py             forms.py                static                  views.py
__pycache__             migrations              templates               webhook_handler.py
admin.py                models.py               tests.py                webhooks.py
apps.py                 signals.py              urls.py

documentation:
all-devices-white.png   atelierWframe.png

ecommerce_site:
__init__.py     __pycache__     asgi.py         settings.py     urls.py         wsgi.py

home:
__init__.py     admin.py        migrations      templates       urls.py
__pycache__     apps.py         models.py       tests.py        views.py

media:
0900631B8140782DM.jpg                   DP0709201205510679M.jpg
...

products:
__init__.py     apps.py         migrations      tests.py        widgets.py
__pycache__     fixtures        models.py       urls.py
admin.py        forms.py        templates       views.py

profiles:
__init__.py     admin.py        forms.py        models.py       templates       urls.py
__pycache__     apps.py         migrations      static          tests.py        views.py

static:
css

templates:
account         allauth         base.html       includes        socialaccount   templates
</code></pre>

#### Environment variables (env.py)

- Keep sensitive data out of version control.
- Note: Never commit env.py to GitHub. By adding the env.py file to .gitignore, it will not be tracked by git or pushed to GitHub. This keeps our secret information safe by not having it publicly available. For example the os.environ.setdefault command sets an environment variable in the local operating system. We supply the variable name and value in the parentheses.


```
import os

os.environ.setdefault('STRIPE_PUBLIC_KEY', '')

os.environ.setdefault('STRIPE_SECRET_KEY', '')

os.environ.setdefault('STRIPE_WH_SECRET', '')

os.environ.setdefault('SECRET_KEY', '')

os.environ.setdefault('DEVELOPMENT', '1')

```

- In my products/views.py I added the @login_required decorator on several functions. This checks the user is logged in.

- I also use the decorator @require_POST, which is special cases of @require_http_methods. These enforce that you can only call a view with certain HTTP methods in the checkout/views.py.
<pre>
@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY

</pre>

- In my template html files I check if a user is authenticated:

<pre>
{% if user.is_authenticated %}
</pre>

#### Database Configuration (settings.py & dj_database_url)

```
import dj_database_url
from pathlib import Path
import os

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else: 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
```
- Heroku will provide the DATABASE_URL via Config Vars. I need to set the environment variable separately on Heroku because, as mentioned, our env.py file is not pushed to GitHub.
- The dj_database_url import is used to convert the database URL we copied from our PostgreSQL from Code Institute email into a format that Django can use to connect to an external database server.

#### Loose Coupling with urls.py
- Each app has its own urls.py. Having one urls.py file per app keeps our apps more modular and independent. This enables an app from one project to be dropped into another.
- Main project urls.py includes them:
```
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

#### References settings.py


```
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

1. **MEDIA_ROOT:**

Absolute filesystem path to the directory that will hold user-uploaded files.

2. **MEDIA_URL:**

URL that handles the media served from MEDIA_ROOT, used for managing stored files. It must end in a slash if set to a non-empty value. I configured these files to be served in both development and production environments.

I link up our static and media files. I add a STATICFILES_DIRS which is going to tell Django where all of our static files are located.
Since they're located in the project level static folder.
All we need to do is os.path.join(BASE_DIR, 'static').

To allow Django to see the MEDIA_URL in urls.py I added this code:

```
from django.conf import settings
from django.conf.urls.static import static
...
 + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
This will import our settings and the static function from django.conf.urls.static, then use the static function to add the MEDIA_URL to our list of URLs.

#### AllAuth

We can complete almost all the user stories in the Registration and User Accounts category at once.
By using a popular pre-built package called django-allauth as opposed to building our own authentication system gives us all the features we'll need for the site and it's completely customizable and will allow us to add even more functionality later on.
Additionally, it's open-source so it's backed by millions of developers who
keep it secure and up-to-date.
And it's unlikely we'd be able to create something better without a ton of extra development time.

In the settings.py, the request context processor here allows Allauth and Django itself for that matter to access the HTTP request object in our templates. So for example, if we wanted to access request.user or request.user.email in our Django templates, we'll be able to do it with this context processor.
It's required because the Allauth templates which we'll see and customize later on
use the request object frequently:

```
'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request', # required by allauth

...

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
]
```
The authentication backends we added give us a really nice feature.
Allowing users to log into our store via their email address which isn't supported by default in Django.
The other back-end handles superusers logging into the admin which Allauth doesn't handle.

```
 'allauth',
    'allauth.account',
    'allauth.socialaccount',
```

Finally the apps we added to our installed apps are Allauth itself and the account which is the Allauth app that allows all the basic user account stuff like logging in and out, user registration and password resets.
The social account specifically handles logging in via social media providers like Facebook and Google.
The contrib.sites app and the SITE_ID setting I added are used by the social account app to create the proper callback URLs when connecting via social media accounts.

#### Email

Since by default allauth will send confirmation emails to any new accounts I temporarily log those emails to the console so we can get the confirmation links.
To do that I can set the EMAIL_BACKEND setting to django.core.mail.backends.console.EmailBackend.

```
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

```
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
```
Tells allauth that we want to allow authentication using either usernames or emails.

```
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
```
These three email settings make it so that an email is required to register for the site.
Verifying your email is mandatory so we know users are using a real email.
They're gonna be required to enter their email twice on the registration page
to make sure that they haven't made any typos.

```
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = '/accounts/login/'  # page to redirect for login
LOGIN_REDIRECT_URL = '/'  # after successful login, where to go
```
Setting a minimum username length of four characters and specifying a login url and a url to redirect back to after logging in.

#### Templates and views

##### AllAuth
I created a directory for our templates.
Because I'll eventually want to customize the Allauth login templates, I make copies of them in our own templates/allauth directory to ensure that our templates take precedence over the built-in ones.
Anything I install with pip ends up in the site-packages directory where Allauth and all its built-in templates are.

```
$ pip3 show django-allauth | grep Location
Location: /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages
```
I copy everything I need with the command:

```
cp -r /Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/allauth/templates/* ./templates/allauth
```
This gives us a copy of every single Allauth template so I can customize them at will. I don't want to customize openid or the test templates so I delete those folders which will just revert those templates back to their Allauth defaults.

I get a copy of all the critical templates
including login and logout, password resets, sign up email verification, and so on.
Also there's a base Allauth template which is the base from which all these others extend.

```
$ ls templates/allauth/*
templates/allauth/base.html

templates/allauth/account:
account_inactive.html                   password_reset_from_key_done.html
base.html                               password_reset_from_key.html
email                                   password_reset.html
email_confirm.html                      password_set.html
email.html                              signup_closed.html
login.html                              signup.html
logout.html                             snippets
messages                                verification_sent.html
password_change.html                    verified_email_required.html
password_reset_done.html

templates/allauth/socialaccount:
authentication_error.html       login_cancelled.html            signup.html
base.html                       login.html                      snippets
connections.html                messages
```

##### Base template

This contains the main page header which contains our logo, the main search bar, and the accountant shopping bag links.
There is a link to the home page which uses several classes which we define in our CSS.
I link to the home url named in urls.py.
The next column contains our search form.
I got the boilerplate for this from the Bootstrap website, since I use Bootstrap for most of my CSS.

I add a meta tag to allow support
of older Internet Explorer versions and eliminate validation errors when validating our HTML.

```
<meta http-equiv="X-UA-Compatible" content="ie=edge">
```

I organize everything in my base templates into blocks so that when I extend this template I can replace chunks of it as needed.
I wrap all the meta stuff in a block meta, which gives me the ability to replace or extend it in templates that extend this base.
I do the same for the CSS and the JavaScript wrapping the CSS in a {% block corecss %} with a link to our main base.css file here.

```
{% block corecss %}
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Lato&display=swap">
  <link rel="stylesheet" href="{% static 'css/base.css' %}">
{% endblock %}
```

The JavaScript is in a {% block corejs %} in case I want to add any extra meta CSS or JavaScript in the head without interfering with the core requirements. I've put my kit code here in the corejs block.

```
{% block corejs %}
  <!-- Add your kit code -->
  <script src="https://kit.fontawesome.com/91373707a8.js" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js"
    integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"
    integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo"
    crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"
    integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6"
    crossorigin="anonymous"></script>
  <!-- Stripe -->
  <script src="https://js.stripe.com/v3/"></script>
  {% endblock %}
```
I also add three other blocks.
{% block extrameta %}
{% block extracss %}
and {% block extrajs %}
Finally I add a {% block extratitle %} inside the title tag which will allow me to add an extra chunk of text to the page title if we want.
For example, if I wanted it to say something like Atelier Etoile - products
or Atelier Etoile - home on different pages of the site. I could put that in this block.

I created a place to display any messages that we send back from Django.
I create a div with a class of message-container. and wrap it in an if messages template tag.

```
{% if messages %}
  <div class="message-container">
```

I created a block page header, which is going to act as an additional header on pages that extend this base template in case we want to put something at the top of those pages but underneath the main header.
I also need a place for our main page content itself to go, so I add a {% block content %}.
I also add a spot for me to put JavaScript that I want to load at the end of the body called that {% block postloadjs %}.

The header code:

```
<a class="text-black nav-link" href="#" id="user-options" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
  <div class="text-center">
    <div><i class="fas fa-user fa-lg"></i></div>
    <p class="my-0">My Account</p>
  </div>
</a>
```

The anchor element here is the parent menu containing the font awesome user icon and the text My Account in a paragraph.
It uses the data toggle attribute to link up to the Bootstrap JavaScript and open the drop-down menu when clicked.
The drop-down menu that opens uses several Django template tags to determine what to display in the menu.
If the user is authenticated we display a drop-down item for their profile and a link to logout.
Otherwise, we display the options to log in or register if they don't have an account.
The account_log out, account_signup, and account_login URLs are coming from the Allauth URLs included in the project level urls.py.
Finally, if the user is authenticated and a superuser I want to provide them with the link to manage the store by adding, updating, or deleting products.
The final list item here is the shopping bag link.
This is not much more than an anchor element with a font awesome icon in it.

```
 <a class="{% if grand_total %}text-info font-weight-bold{% else %}text-black{% endif %} nav-link" href="{% url 'view_bag' %}">
  <div class="text-center">
    <div><i class="fas fa-shopping-bag fa-lg"></i></div>
      <p class="my-0">
        {% if grand_total %}
          ${{ grand_total|floatformat:2 }}
        {% else %}
          $0.00
        {% endif %}
      </p>
    </div>
</a>
```

Here we're checking whether this grand total template variable exists, and if it does then we want to display the total formatted to two decimal places.
If not we'll just display 0.
We're using the same template variable to determine which classes to apply to the element
So if there's something in the bag the font will be bold and a different colour.

##### Home index.html

This extends the base template. The top portion of our main site header includes the logo in the upper left, the search bar in the middle and the My account and shopping bag links on the right.
The main site navigation will act as the foundation for giving our users the ability to sort, by price rating and category, identify different categories of products and easily find special offers and deals.

![Navigation](documentation/mainNav.png)

##### base.css

I add the background image to the body element which I can do with the size of cover and options of no-repeat center centre and fixed which will ensure that it stays put in the centre of the page.
```
body {
    background: url('/media/homepage_background_cropped.jpg') no-repeat center center fixed;
    background-size: cover;
    height: calc(100vh - 164px);
    color: #555;
    font-family: 'Lato';
}
```

I've taken this icon class from another CSS framework similar to Bootstrap called Bulma, which will ensure that whenever we use font awesome icons they will always stay perfectly centred and have a consistent size
unless we manually change it.

```
/* from Bulma */
.icon {
    align-items: center;
    display: inline-flex;
    justify-content: center;
    height: 1.5rem;
    width: 1.5rem;
}
```
The logo font class will be used throughout this site to maintain consistency with the uppercase font of the logo whenever we want to call attention to something.
The main logo link class, just makes it so that the logo only takes up as much space as the text requires and no more.

```
.logo-font {
    text-transform: uppercase;
}

.main-logo-link {
    width: fit-content;
}
```
This media query will widen the default
bootstrap container class on extra-large screens just to make better use of the
available screen real estate for people with extra-large monitors.
```
/* -------------------------------- Media Queries */

/* Slightly larger container on xl screens */
@media (min-width: 1200px) {
  .container {
    max-width: 80%;
  }
}
```
The next media query will add 164 pixels of padding to our header container class to push the body down to the bottom of the main page header.
This is the page header block that we added at the top of the index.html page in the home app.
The other class in this media query will be for the main site navbar. For both of these classes, I'm using a minimum screen width of 992 pixels. Since the main header will look different on mobile views we only want these to affect medium and larger screens.

```
/* fixed top navbar only on medium and up */
@media (min-width: 992px) {
    .fixed-top-desktop-only {
        position: fixed;
        top: 0;
        right: 0;
        left: 0;
        z-index: 1030;
    }

    .header-container {
        padding-top: 164px;
    }
}

/* pad the top a bit when navbar is collapsed on mobile */
@media (max-width: 991px) {
    .header-container {
        padding-top: 126px;
    }

    body {
        height: calc(100vh - 126px);
    }
}
```


#### Code format

-   VS code automatically indents HTML, Javascript and CSS to ease readability.

```

for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let holeId = e.target.getAttribute("hole_id");
    deleteConfirm.href = `delete_hole_guide/${holeId}`;
    deleteModal.show();
  });
}

```
#### Code understandability

-   Copious amounts of comments to explain what the code is doing and why.

```
@login_required
def course_detail(request, slug):
    """
    Display an individual :model:`courseguide.Course`.

    **Context**

    ``course``
        An instance of :model:`courseguide.Course`.

    **Template:**

    :template:`courseguide/course_detail.html`
    """

    queryset = Course.objects.filter(status=1)
    course = get_object_or_404(queryset, slug=slug)
    hole_guides = course.holes.filter(approved=True).order_by('hole_number')
    hole_count = course.holes.filter(approved=True).count()

```

#### Code validation

-   Python code was run through a Linter to analyze code and flag programming errors, bugs, stylistic errors and suspicious constructs.

![Python code linter](./documentation/codeLinter.png)

-   Javascript was run through JSHint without ES6 checks.

![Javascript code linter](./documentation/JSHint.png)

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
* Test allauth is working properly.
I run the server, then navigate to /accounts/login.
I login using the superuser I created earlier.
This directs us back to a page telling us we need to confirm our email.
So we know allauth is working because email confirmations are now required in order to log in.
The only problem here is that I created this user before installing allauth.
So I need to create and confirm an email manually.
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

- AllAuth I used the quickstart page to help me set it up [AllAuth quickstart](https://docs.allauth.org/en/latest/installation/quickstart.html)
- The Bootstrap Github Repository [Bootstrap repository](https://github.com/twbs/bootstrap)
- [Bootstrap Starter Template](https://getbootstrap.com/docs/4.6/getting-started/introduction/#starter-template)
- [Google Fonts Lato](https://fonts.google.com/specimen/Lato?query=lato&selection.family=Lato&sidebar.open=)


[GitHub Repository](https://github.com/AmitKapilaCodeIns/ecommerce_site)

