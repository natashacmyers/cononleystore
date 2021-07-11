# Cononley Village Store
Cononley Village Store is a website for a real village store in Cononley, a small village in North Yorkshire. The website sells all the products found in Cononley store, ranging from essentials to eco cleaning products. There is also a blog where the store owners provide updates of new products, closing times over the christmas period and other important pieces of information for the locals to view. Additionally, there is a link to their sister store where e-bikes are sold. This link is not part of the project, and is simply available to show the two sites would be related in real time. 

The goal of the site is for users to be able to view products, add to bag, and checkout/pay for their shopping all online. This will be especially useful to elderly/less abled customers who may find visiting the store a challenge. The shopping experience is aimed to relfect that of the actual store. Rustic, unique, cosy and inviting. The store real store has a very villagey-feel to it and this has been mirrored throughout the site. 

The users (customers) are able to purchase products add comments to blogs, whilst the owners (superusers) are able to modify and add products as well as post new blogs.

![alt text][Cononley Village Store]

[logo]: https://github.com/natashacmyers/cononley-store/blob/master/media/responsive-view-cvs.png?raw=true

## Table of Contents
- [UX](#ux)
  * [Strategy Plane](#strategy-plane)
  * [Scope Plane](#scope-plane)
  * [Structure Plane](#structure-plane)
  * [Skeleton Plane](#skeleton-plane)
  * [Surface Plane](#surface-plane)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Disclaimer](#disclaimer)

## UX
To understand what the result of the website needs to be, we need to define the development process of each stage. This can be done by analyzing and breaking down the problem into five planes:

### Strategy Plane
The strategy plane defines the developer’s objective and the user needs (goals).

#### User Stories
As a **User** I want to:
1.  Buy store products
2.	Be informed of any new products / store updates
3.	Contact the website owner
4.	Pay safely
5.	Check my purchase history
6.	Register my profile
7.	Login to my profile

As a **Developer** I want to:
1.  Gain more knowledge on Django
2.	Create a full-stack framework
3.	Learn more on databases, such as MySQL

As an **Admin** I want to:

1.	Add products/services
2.	Manage products/services
3.	Remove users
4.	Check user’s purchase history


### Scope Plane
The scope plane defines the features that are and are not possible to include on the website.
This will be further explained in the next chapter. A summary of the included and not included features are:

| Features (included) | Future features (not included)|
| :------------- | :---------- |
|1. Navigation menu | 1. Order confirmation by mail |
|2. Banner | 2. Contact form rather than contact information |
|3. Side panel for quick links on homepage | 
|4. Landing page| 
|5. Product view & detail pages |
|6. Product edit pages (superuser only) | 
|7. Add products page (superuser only) | 
|8. Blog view, add & edit pages (superuser only) | 
|9. Cart & Checkout pages |
|10. Login & registration pages |
|11. Profile page |

### Structure Plane

The structure plane defines the information architecture and interaction design with the user. 

#### Interaction Design
The following definitions has been used for this website:
- First impression of the website needs to be comforting and similiar to that of the store
- No more than three clicks are required for the user to reach the page
- The type of information architecture that will be used is the ‘Hierarchical Tree’, see below:


#### Information architecture

SQLite3 was used during development which is included in the default Django installation. Heroku Postgres is used in the production site.
![Database Schema](media/database-schema.png)

Databases have been setup in models.py of the following apps:

- Products
- Categories
- Blogs
- Comments
- Profiles
- Checkout

An example of the Products's database can be found below:

| **Name** | **Field Type** | **Validation** |
--- | --- | --- 
 category | ForeignKey |  null=True, blank=True, on_delete=models.SET_NULL
 sku | CharField | max_length=254, null=True, blank=True
 name | CharField | max_length=254
 description | TextField | 
 price | DecimalField | max_digits=6, decimal_places=2
 image | URLField | max_length=1024, null=True, blank=True

More about the Django database models can be found [here](https://docs.djangoproject.com/en/3.1/topics/db/models/#field-options).

### Skeleton Plane
The skeleton plane defines a basic visual design of the website through, for example, a wireframe.  
The wireframes for this project are made with Balsamiq can be downloaded from the following link:

- [Wireframe - Desktop version]()
- [Wireframe - Tablet version]()
- [Wireframe - Mobile version]()

### Surface Plane
The surface plane defines the appearance of the website. This website needs to attract and encourage users to focus on the website's content.
The following design style has been used:

| Design Style | Design Choice|
| :------------- | :---------- |
Font: Amatic SC | A font that reflects the rustic villagey-feel of the store |
Text colour: #476b6b | A soft colour that matches the colour scheme of the store |
Background colour: #FFFF| To enhance text and images |

#### Color Scheme

I have chosen to match the colours of the store, which are rustic, villagey and in-touch with nature. The main background image is the front of the store which is a light teal colour. To match this I have used:
#009973 for success, #476b6b for baseline writing, rgb(202, 202, 202) as a soft background colour overlay, and white elsewhere to keep the site light and welcoming.

## Features
A summary of the features was described in the scope plane. This chapter will explain what the purpose is of each feature and what will be left to implement for the future.

### Existing Features
| Features (included) | Explanation|
| :------------- | :---------- |
|1. Navigation menu | 1. Allows user to quick access different pages of the website|
|2. Banner image links back to homepage | 2. Allows users easy navigation back to home |
|3. Landing page | 3. Allows users to identify which products are available and which blogs can be read |
|4. Products pages | 4. Allows users to view all the products |
|5. Blogs pages | 5. Allows users to, besides reading all the blogs, add comments, and edit and delete their own comments|
|6. Cart & Checkout pages | 6. Allows users to add products to the cart and checkout from the cart by completing the payment|
|7. Login & Registration pages | 7. Allows users to create a new profile
|8. User's profile page | 8. Allows users to view all their purchase history

### Features Left to Implement
| Features (not included) | Explanation|
| :------------- | :---------- |
|1. Order confirmation by email | This feature allows users to receive a confirmation by email when the order is completed|
|2. Contact form rather than contact information | This feature allows the user to contct the store owners easier, currently the contact information is available in the main nav, but needs to be executed by the user. A contact form would mean less input by the user for a better user experience.

## Technologies Used
The following technologies have been used to achieve this project:

Resources
- [HTML](https://www.w3.org/TR/html52/) is used as the main writing language of this project
- [CSS](https://www.w3.org/Style/CSS/Overview.en.html) is used for styling the HTML text
- [JavaScript](https://www.javascript.com/) is used for Stripe payments, scroll-to-top button, owl carousel and hiding and showing contact form
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) is used as templating language for Python and its depending framework Django
- [Jquery](https://jquery.com/) is used for simplifying JavaScript commands

Styling
- [FontAwesome](https://fontawesome.com/) is used to improve the visual design of the website
- [Contrast-ratio.com](https://contrast-ratio.com/) is used to test the visibility of the text with the background color
- [Google fonts](https://fonts.google.com/) is used for the style the font

Framework, Libraries & API
- [Django](https://www.djangoproject.com/ is used as main web framework for the website
- [Django Crispyforms](https://django-crispy-forms.readthedocs.io/en/latest/#) is used for simplifying forms through Python
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) is used for user login and user registration
- [Bootstrap](https://getbootstrap.com/) is used for its grid system and navigation bar
- [Stripe](https://stripe.com/) is used for the payment system in the checkout app
- [Gunicorn](https://gunicorn.org/) is used for the deployment to Heroku
- [Psycopg2](https://pypi.org/project/psycopg2/) is used as an adapter for PostgreSQL with Django 

Database & Platform
- [sqlite3](https://www.sqlite.org/download.html) is used for storing data from the store. Specifically, for this website: storing of user order information, blogs and products
- [PostgreSQL](https://www.postgresql.org/) is used for the same purpose as sqlite3, but is used for production
- [Heroku](https://heroku.com/) is used for deploying the app through its cloud platform
- [AWS S3](https://aws.amazon.com/) is used to store static and media files in production

Wireframe
- [Balsamic](https://balsamiq.com/) is used to draw wireframes for the skeleton plane and making the visual design of the structure plane

Testing
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) is used to test the responsiveness of the website and to debug any problems
- [Validator.w3.org](https://validator.w3.org/) is used to validate the HTML code
- [Jigsaw.w3.org/css-validator](https://jigsaw.w3.org/css-validator/validator.html.en) is used to validate the CSS code
- [JSHint](https://jshint.com/) is used to validate the JavaScript code
- [Pep8](http://pep8online.com/) is used to validate the Python code

## Testing
The test procedures and the key issues of the tests are written in the file[TEST.md]().


## Deployment
The following chapter explains how to:
    - Clone a Repository from Github
    - Work with a Local Copy
    - Deployment on Heroku and file storage on AWS

### Requirements
- Python (version 3.0)
- Heroku account
- Github account
- Stripe account
- Gmail account
- AWS account

### Cloning the Repository
To work with a local copy of this project the following steps needs to be taken:

1. Go to the main page of the GitHub repository and click on the dropdown menu **Code**

2. Copy the URL and go to your local IDE

3. In the terminal of your IDE type in **git clone** and the paste the URL copied from step 2
4. Press Enter and the clone will be created


### Working with a Local Copy
To work with the local copy that is created the following steps needs to be taken:

#### Step 1: Installing the Requirements
1. To install all the required libraries of the project go to the workspace of your local copy
2. In the terminal window of your IDE type in: **pip3 install -r requirements.txt**

#### Step 2: Setting Up Environment Variables
Depending on the IDE, the user has to make sure that the Environment Variables are properly setup. The following Environment Variables have been set up in **GitPod** to ensure that the project keys and project files are respectively taken from and migrated to the correct source. 


| Name | Value|
| :------------- | :---------- |
|1. DEVELOPMENT | True|
|2. SECRET_KEY | *'Your Secret Key'*|
|2. STRIPE_PUBLIC_KEY | *'Your Stripe Public key'* |
|3. STRIPE_SECRET_KEY | *'Your Stripe Secret key'* |
|4. STRIPE_WH_SECRET | *'Your Stripe WH Secret key'* |

For more information about Stripe API keys, please read the [Stripe API keys documentation](https://stripe.com/docs/keys).


#### Step 3: Migrating the Database
1. In the terminal window of your IDE type in: **python3 manage.py makemigrations**
2. In the terminal window of your IDE type in: **python3 manage.py migrate**

#### Step 4: Create SuperUser
1. In the terminal window of your IDE type in: **python3 manage.py createsuperuser**
2. Enter the credentials of the Superuser to access the Django Admin panel

#### Step 5: Loading Fixtures
1. In the terminal window of your IDE type in: **./manage.py loaddata 'Fixture_Filename'.json**
2. Make sure to that load the fixtures in the following order:
    - Categories
    - Products
    - Blogs
3. Please note that a SuperUser has to be created **first**, in order to load the *blogs.json* fixture

You can also load media manually into the database through the admin portal 

#### Step 6: Run the App
1. Open your terminal window in your IDE
2. Type in **python3 app.py** to run the app
3. To access the Djanog Admin panel, add **/admin** at the end of the URL link and login with your credentials


### Heroku Deployment
To host this project on Heroku the following steps needs to be taken:

#### Step 1: Setting Up Heroku
1. Create a Heroku account
2. Create a new app and select your region

#### Step 2: Preparing Local Workspace for Heroku
In the terminal window of your local IDE type in the following:
file. This file is needed so that Heroku knows which files needs to be installed
1. **python app.py > Procfile** to create a Procfile. This file is needed so that Heroku knows which file is needed as its entry point to get the app up and running
2. Inside the Procfile enter: *web: gunicorn cononley_store.wsgi:application* and then save the file
3. **pip3 install psycopg2-binary** to use PostgreSQL as the database
4. **pip3 install gunicorn** to install Gunicorn, which will act as the webserver and replace our development server once the app is deployed to Heroku
5. **pip3 freeze --local > requirements.txt** to store the packages into a file that tells Heroku what to install

#### Step 3: Setting the Configuration Variables in Heroku
1. Go back to your Heroku account and go to **settings**
2. Click on **Reveal Config Vars** to reveal the keys and the values
3. Set the keys and values as follow:
    (**KEY: VALUE**)
    - AWS_ACCESS_KEY_ID: *'Your Key'*
    - AWS_SECRET_ACCESS_KEY: *'Your Key'*
    - DATABASE_URL: *'Your Key'*
    - EMAIL_HOST_PASS: *'Your Key'*
    - EMAIL_HOST_USER: *'Your Email'*
    - SECRET_KEY: *'Your Key'*
    - STRIPE_PUBLIC_KEY: *'Your Key'*
    - STRIPE_SECRET_KEY: *'Your Key'*
    - STRIPE_WH_SECRET: *'Your Key'*
    - USE_AWS: *True*

#### Step 4: Preparing migration to PostgreSQL Database
1. Go back to your Heroku account and go to **Resources**
2. Search for Heroku PostgreSQL and add to Heroku
3. Go back to the IDE and comment out the Default configuration:
```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
```
4. Then add:
```
 DATABASES = {     
        'default': dj_database_url.parse("Your Postgres database URL")     
    }
```
Important note: Do **NOT** save and commit this change, this is a temporary procedure to push the files to PostgreSQL database. Commiting this file will expose the PostgreSQL Database URL.

#### Step 5: Migrating to PostgreSQL Database
1. In the terminal window of your IDE type in: **python3 manage.py makemigrations**
2. In the terminal window of your IDE type in: **python3 manage.py migrate**

#### Step 6: Create SuperUser
1. In the terminal window of your IDE type in: **python3 manage.py createsuperuser**
2. Enter the credentials of the Superuser to access the Django Admin panel

#### Step 7: Loading Fixtures
1. In the terminal window of your IDE type in: **./manage.py loaddata 'Fixture_Filename'.json**
2. Make sure to that load the fixtures in the following order:
    - Categories
    - Products
    - Blogs
3. Please note that a SuperUser has to be created **first**, in order to load the *blogs.json* fixture

You can also load media manually into the database through the admin portal 

#### Step 8: Pushing files to Heroku 
1. In the terminal window of your local IDE type in **heroku login** or **heroku login -i** and fill in your heroku credentials and password
2. Commit all your files and type in the same terminal window **git push heroku master**. Now all your files are committed to Heroku

#### Step 9: Open App in Heroku
1. Click on **Open app** in the right corner of your Heroku account, the application will open in a new window
2. The live link is available from the address bar

#### Storing Static and Media files with AWS
For setting up the AWS S3 bucket please refer to the 
[AWS S3 Bucket documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-bucket.html) and the [S3BotoStorage documentation](https://django-storages.readthedocs.io/en/latest/backends/amazon-S3.html). The media files have to be taken from the repository and manually placed into the AWS S3 bucket.

#### Gmail
To obtain the **EMAIL_HOST_PASS**, please refer to 
[Google SMTP documentation](https://support.google.com/a/answer/176600?hl=en#zippy=%2Cuse-the-gmail-smtp-server).


## Credits
### Content
- All the products's descriptions are taken from Cononley Store (paperwork format)
- Blog content was written in collaboration with the owners' of Cononley Store


### Media
- All photos for this project are used from:
    - [Suma Wholesale](https://www.suma.coop/)
    - [Waitrose](https://www.waitrose.com/)  

### Source of Codes
The following codes were inspired or taken from:
- [Code Institute](https://codeinstitute.net/): The project is mainly based on the Boutique Ado example project from the module Full-stack Framework with Django. 

### Acknowledgement
The completion of this project could not have been possible without support and the extensive knowledge of other people. My appreciation goes to:
- Gerard (Gerry) McBride, my mentor, for being so supportive and a pleasure to work with throughout MS4 and all of my time with Code Institute. Thank you for helping with testing and overall feedback throughout.
- Code Institute tutors for continuous support throughout MS4, special thanks for Sheryl for her continued support whilst connecting my edit comment page to the database.
- Stack Overflow, for the wealth of knowledge available and easily accessible at anytime.
- Slack community for having asked specific project-based questions that I have been able to refer to for help along the way.

