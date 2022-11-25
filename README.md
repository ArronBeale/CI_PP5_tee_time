# eCommerce: Teetime (Building in Progress)

![Am I Responsive]()

**Developer: Arron Beale**

💻 [Visit live website](https://ci-pp5-teetime.herokuapp.com/)



## Table of Contents
  - [About](#about)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colours](#colours)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [Database](#database)
    - [Wireframes](#wireframes)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
    - [Tests on various devices](#tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Heroku Deployment](#heroku-deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

### About

Teetime is an eCommerce web app built for Golf Clubs and Golf Societies to use to list their golf courses and golf outings for members and guests.
It allows Golf Courses to be listed on the app so Golfers can find and book a time to golf on their course whether they are a guest or a member.
It is also an online shop that sells golf merchandise to customers.
<hr>

### User Goals

- To book a tee time
- To buy products from the shop
- To find golf courses listed

### Site Owner Goals

- To provide a solution to allow users to purchase a tee time
- To provide a solution to allow users to buy from the shop
- To attract more business with a well crafted site
- Provide a modern application with an easy navigation
- Fully responsive and accessible
<hr>


## User Experience

### Target Audience
- Golfers looking to book a round of Golf
- Golfers looking for Golf courses
- Golf Clubs interested in being listed on the site
- Golf Societies who would like to purchase and use the web app for their society (Many Golf societies use Whatsapp)
- Customers looking to purchase Golf clothing and accesories from the Shop

### User Requirements and Expectations

- Fully responsive
- Accessible
- A welcoming design
- Relevant Content
- Ease of use
- Social media
- Contact information
- Accessibility

##### Back to [top](#table-of-contents)<hr>


## User Stories

### Site User

1. As a Site User I can register for an account so that I have an account and view my profile
2. As a Site User I can login and logout so that I can have an account with my information stored for fast usage
3. As a Site User I can recover my password so that I can set a new password if I forgot it
4. As a Site User I can receive an email confirmation after registration so that I can be notified registration was successful
5. As a Site User I can have a profile so that I can store my information for faster checkouts in the future


### Shopper

6. As a Shopper I can navigate across the site so that I can can access all parts of the site
7. As a Shopper I can use a navbar, footer, and social icons so that I can navigate the site, access menus, and access socials
8. As a Shopper I can be notified of my actions so that I can be aware the action was completed successfully or not
9. As a Shopper I can see my login status so that I can know if I am logged in or not
10. As a Shopper I can visit the shop so that I can view all products available
11. As a Shopper I can view my basket and total cost at any time so that I can be aware of what I am buying and it's cost
12. As a Shopper I can view a list of products so that I can select a product to purchase
13. As a Shopper I can view an individual product details so that I can view a more detailed view of the product
14. As a Shopper I can view a list of golf courses so that I can select a golf course I want to play on
15. As a Shopper I can view individual golf course details so that I can see more detailed information about it
16. As a Shopper I can view a list of tee times available for each golf course so that I can select a date and time to play
17. As a Shopper I can search for a product by name or description so that I can find a certain product
18. As a Shopper I can see my search results so that I can only see what I am searching for
19. As a Shopper I can sort by category so that I can select products of a certain category
20. As a Shopper I can sort by price low to high and high to low so that I can view products according to my budget
21. As a Shopper I can select only available dates/times so that I can I can only purchase available tee slots
22. As a Shopper I can purchase a golf course tee time so that I can buy a slot for a date and time that is available
23. As a Shopper I can use a card as the payment method so that I can complete my purchase
24. As a Shopper I can select the size and quantity of a product so that I can select a size and quantity to my needs
25. As a Shopper I can view items in my basket so that I can be aware of what I am buying and it's cost
26. As a Shopper I can adjust item quantity in my basket so that I can increase or reduce item count according to my needs
27. As a Shopper I can receive order confirmation so that I can be notified of a successful order
28. As a Shopper I can receive email confirmation so that I can have a record of my purchase

### Store Owner

29. As a Store Owner I can add a product so that I can add new products to the shop
30. As a Store Owner I can edit a product so that I can edit existing products in the shop
31. As a Store Owner I can delete a product so that I can delete existing products from the shop
32. As a Store Owner I can add a golf club so that I can add a golf club to the site
33. As a Store Owner I can edit a golf club so that I can edit an existing golf club on the site
34. As a Store Owner I can delete a golf club so that I can delete existing golf club from the site
35. As a Store Owner I can add a tee time so that I can add a tee time to a golf club
36. As a Store Owner I can edit a tee time so that I can edit an existing tea time on a golf club
37. As a Store Owner I can delete a tee time so that I can delete a tee time from a golf club



### Kanban, Epics & User Stories
- GitHub Kanban was used to track all open user stories
- Epics were created using the milestones feature
- Backlog, In Progress, Done headings were used in the kanban

<details><summary>Epics</summary>

![Epics]()
![Epic 1]()
![Epic 2]()
![Epic 3]()
![Epic 4]()
</details>

<details><summary>User Stories</summary>

![User stories]()

</details>

<details><summary>Kanban</summary>

![Kanban mid]()
![Kanban finish]()

</details>


##### Back to [top](#table-of-contents)<hr>


## Design

### Colours

I chose the following...

The colors I wanted to stay close to  [Coolors.co](https://coolors.co/)
<details><summary>See colour pallet</summary>
<img src="">
</details>

### Fonts

 The fonts selected were from Google Fonts, .......

### Structure

#### Website pages

The site was designed for the user to be familiar with the layout such as a navigation bar along the top of the pages and a hamburger menu button for smaller screen.

The footer contains all relevant social media links that the business has so the user can visit any social media site and follow the business there to expand the businesses followers, likes and shares.

- The site consists of the following pages:
  - Homepage
  - 
  - 
  - Blog page has a paginated list of blogs posted by an admin or authorised user, 4 per page
  - Blog expanded
  - Book
  - My bookings
  - Edit booking
  - Cancel booking
  - Contact us
  - Login / Logout allows users to login
  - Register
  - 404 error page to display if a 404 error is raised

#### Database

- Built with Python and the Django framework with a Postgres database for the deployed Heroku version(production)
- 

<details><summary>Show diagram</summary>
<img src="">
</details>


##### User Model
The User Model contains the following:
- user_id
- password
- last_login
- is_superuser
- username
- first_name
- last_name
- email
- is_staff
- is_active
- date_joined

##### Model
The Model contains the following:
- 
- 
- 
- 
- 

##### Booking Model
The Booking Model contains the following:
- 
- 
- 
- 
- 
- 
- 
- 

##### Post Model
The Post Model contains the following:
- title
- post_id (PrimaryKey)
- author (ForeignKey)
- created_date
- updated_date
- content
- featured_image
- excerpt
- slug
- status

##### Comment Model
The Comment Model contains the following:
- post (ForeignKey)
- name
- email
- body
- created_date
- approved
- Meta: created_on

##### ContactUs Model
The ContactUs Model contains the following:
- contact_id (PrimaryKey)
- name (ForeignKey)
- email (ForeignKey)
- phone (ForeignKey)
- body


### Wireframes
The wireframes were created using Balsamiq
<details><summary></summary>
<img src="">
</details>


## Technologies Used

### Languages & Frameworks

- HTML
- CSS
- Javascript
- Python
- Django


### Libraries & Tools

- [Am I Responsive](http://ami.responsivedesign.is/)
- [Balsamiq](https://balsamiq.com/)
- [Bootstrap v5.2](https://getbootstrap.com/)
- [Cloudinary](https://cloudinary.com/)
- [Favicon.io](https://favicon.io)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools/)
- [Font Awesome](https://fontawesome.com/)
- [Git](https://git-scm.com/)
- [GitHub](https://github.com/)
- [Google Fonts](https://fonts.google.com/)
- [Heroku Platform](https://id.heroku.com/login)
- [jQuery](https://jquery.com)
- [Postgres](https://www.postgresql.org/)
- [Summernote](https://summernote.org/)
- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [JShint](https://jshint.com/)
  - [Pycodestyle(PEP8)](https://pypi.org/project/pycodestyle/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
  - [Wave Validator](https://wave.webaim.org/)

##### Back to [top](#table-of-contents)


## Features

### Home page
- Home page includes nav bar, main body and a footer


<details><summary>See feature images</summary>

![Home page]()
</details>


### Logo & Navigation
- Custom logo for the business
- Fully Responsive
- On small screens switches to hamburger menu
- Indicates login/logout in status
- displayed on all pages

<details><summary>See feature images</summary>

![Footer]()
![Footer]()
![Footer]()
</details>


### Footer
- Contains social media links and copyright
- displayed across all pages
- 

<details><summary>See feature images</summary>

![Footer]()
</details>


### Sign up / Register
- Allow users to register an acoount
- Username and password is required, email is optional

<details><summary>See feature images</summary>

![Register]()
</details>


### Login
- User can login

<details><summary>See feature images</summary>

![Login]()
![Login]()
</details>


### Logout
- Allows the user to securely log out
- Ask user if they are sure they want to log out

<details><summary>See feature images</summary>

![Logout]()
</details>


### Book
- Allows the user to book
- Messages are displayed if the data is not valid such as phone number lenght is too short and the email address is not a valid format

<details><summary>See feature images</summary>

![Book]()
![Book]()
![Book]()
</details>


### My Bookings
- Allows the user to see their booking
- 
- 

<details><summary>See feature images</summary>

![My Bookings]()
</details>


### Edit Booking
- Allows the user to edit their booking
<details><summary>See feature images</summary>

![Edit Booking](docs/features/feature-edit-booking.PNG)
![ImaEdit Bookingge]()
</details>


### Cancel Booking 
- Allows the user to cancel their booking, asks user are they sure
  
<details><summary>See feature images</summary>

![Cancel Booking]()
</details>


### Blog
- The blog displays each post made by a staff member
- Paginations is used to display 4 posts per page
  
<details><summary>See feature images</summary>

![Blog]()
</details>


### Blog Expanded
- Expands into the selected blog the user wishes to read
- Displays a featured image uploaded by the poster
- If no image is uploaded a default image is then used
- Registerd user can comment on the blog
  
<details><summary>See feature images</summary>

![Blog Expanded]()
</details>


### Comments
- Comments made are set to pending approval status to ensure nothing bad is displayed
- Only registered users can comment on a blog post
- Staff can approve comments via the admin panel on the backend
  
<details><summary>See feature images</summary>

![Comments]()
</details>


### Contact Us
- 
- 
- 
  
<details><summary>See feature images</summary>

![Contact Us]()
![Contact Us]()
</details>


### Social Media Links
- A logo and link is used for each social media displayed
- All links open in a new tab to ensure user is not directed away from the business
- Displayed on all pages
  
<details><summary>See feature images</summary>

![Social Media Links]()
</details>


### Pagination
- Pagination is used on the
- Ensures the page is kept tidy
  
<details><summary>See feature images</summary>

![Pagination]()
</details>


##### Back to [top](#table-of-contents)<hr>


## Validation

The W3C Markup Validation Service
<details><summary>Home</summary>
<img src="">
</details>

<details><summary>Register</summary>
<img src="">
</details>

<details><summary>Login</summary>
<img src="">
</details>

<details><summary>Logout</summary>
<img src="">
</details>

<details><summary>Bookings</summary>
<img src="">
</details>

<details><summary>Edit Booking</summary>
<img src="">
</details>

<details><summary>Cancel Booking</summary>
<img src="">
</details>

<details><summary>Blog</summary>
<img src="">
</details>

<details><summary>Blog Expanded</summary>
<img src="">
</details>

<details><summary>Contact Us</summary>
<img src="">
</details>

<details><summary>Confirmed</summary>
<img src="">
</details>

<details><summary>404</summary>
<img src="">
</details><hr>


### CSS Validation
The W3C Jigsaw CSS Validation Service

<details><summary>Style.css</summary>
<img src="">
</details><hr>

### JavaScript Validation
JSHint JS Validation Service

<details><summary>Script.js</summary>
<img src="">
</details><hr>

### PEP8 Validation
PEP8 Validation Service was used to check the code for PEP8 requirements via Pycodestyle as PEP8online was down

<details><summary>Tool used: Pycodestyle</summary>
<img src="">
</details>

<hr><summary>App</summary><hr>


<details><summary>Admin.py</summary>
<img src="">
</details>

<details><summary>models.py</summary>
<img src="">
</details>

<details><summary>urls.py</summary>
<img src="">
</details>

<details><summary>views.py</summary>
<img src="">
</details>

<details><summary>test_models.py</summary>
<img src="">
</details>

<details><summary>test_views.py</summary>
<img src="">
</details>

<details><summary>test_urls.py</summary>
<img src="">
</details>

<hr><summary>App</summary><hr>


<details><summary>Admin.py</summary>
<img src="">
</details>

<details><summary>models.py</summary>
<img src="">
</details>

<details><summary>urls.py</summary>
<img src="">
</details>

<details><summary>views.py</summary>
<img src="">
</details>

<details><summary>test_models.py</summary>
<img src="">
</details>

<details><summary>test_views.py</summary>
<img src="">
</details>

<details><summary>test_urls.py</summary>
<img src="">
</details>

<hr><summary>App</summary><hr>


<details><summary>Admin.py</summary>
<img src="">
</details>

<details><summary>models.py</summary>
<img src="">
</details>

<details><summary>urls.py</summary>
<img src="">
</details>

<details><summary>views.py</summary>
<img src="">
</details>

<details><summary>test_models.py</summary>
<img src="">
</details>

<details><summary>test_views.py</summary>
<img src="">
</details>

<details><summary>test_urls.py</summary>
<img src="">
</details>

<hr><summary>App</summary><hr>


<details><summary>Admin.py</summary>
<img src="">
</details>

<details><summary>models.py</summary>
<img src="">
</details>

<details><summary>urls.py</summary>
<img src="">
</details>

<details><summary>views.py</summary>
<img src="">
</details>

<details><summary>test_models.py</summary>
<img src="">
</details>

<details><summary>test_views.py</summary>
<img src="">
</details>

<details><summary>test_urls.py</summary>
<img src="">
</details>

### Lighthouse

Performance, best practices and SEO was tested using Lighthouse.

#### Desktop
<details><summary>Index</summary>
<img src="">
</details>

<details><summary>Register</summary>
<img src="">
</details>

<details><summary>Login</summary>
<img src="">
</details>

<details><summary>Logout</summary>
<img src="">
</details>

<details><summary>Blog</summary>
<img src="">
</details>

<details><summary>Blog Expanded</summary>
<img src="">
</details>

<details><summary>Book</summary>
<img src="">
</details>

<details><summary>Booking List</summary>
<img src="">
</details>

<details><summary>Edit Booking</summary>
<img src="">
</details>

<details><summary>Cancel Booking</summary>
<img src="">
</details>

<details><summary>Contact Us</summary>
<img src="">
</details>

#### Mobile
<details><summary>Index</summary>
<img src="">
</details>

<details><summary>Register</summary>
<img src="">
</details>

<details><summary>Login</summary>
<img src="">
</details>

<details><summary>Logout</summary>
<img src="">
</details>

<details><summary>Blog</summary>
<img src="">
</details>

<details><summary>Blog Expanded</summary>
<img src="">
</details>

<details><summary>Book</summary>
<img src="">
</details>

<details><summary>Booking List</summary>
<img src="">
</details>

<details><summary>Edit Booking</summary>
<img src="">
</details>

<details><summary>Cancel Booking</summary>
<img src="">
</details>

<details><summary>Contact Us</summary>
<img src="">
</details><hr>

### Wave
WAVE was used to test the websites accessibility.

<details><summary>Index</summary>
<img src="">
<img src="">
</details>

<details><summary>Register</summary>
<img src="">
<img src="">
</details>

<details><summary>Login</summary>
<img src="">
<img src="">
</details>

<details><summary>Logout</summary>
<img src="">
<img src="">
</details>

<details><summary>Book</summary>
<img src="">
<img src="">
</details>

<details><summary>My Bookings</summary>
<img src="">
<img src="">
</details>

<details><summary>Edit Booking</summary>
<img src="">
<img src="">
</details>

<details><summary>Cancel Booking</summary>
<img src="">
<img src="">
</details>

<details><summary>Blog</summary>
<img src="">
<img src="">
</details>

<details><summary>Blog Expanded</summary>
<img src="">
<img src="">
</details>

<details><summary>Contact Us</summary>
<img src="">
<img src="">
</details>

<details><summary>404</summary>
<img src="">
<img src="">
</details>


##### Back to [top](#table-of-contents)<hr>


## Testing

1. Manual testing
2. Automated testing

### Manual testing

1. As a User I

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Click on the 'Home' link in the navigation bar | Homepage will load| Works as expected |


<details><summary></summary>
<img src="">
<img src="">
<img src="">
<img src="">
<img src="">
<img src="">
<img src="">
<img src="">
<img src="">
<img src="">
<img src="">

</details>



9. As an Admin / Authorised User I can log in so that I can access the back end of the site

**Step** | **Expected Result** | **Actual Result**
------------ | ------------ | ------------ |
| Visit the admin page  | Enter admin login credentials, gain access to back end |  |


<details><summary></summary>
<img src="">
<img src="">


</details>


### Automated testing

- Testing was done using the built in Django module, unittest.
- Coverage was also usesd to generate a report


<details><summary> App, test_models.py</summary>
<img src="">
</details>

<details><summary> App, test_views.py</summary>
<img src="">
</details>

<details><summary> App, test_urls.py</summary>
<img src="">
</details>

<details><summary> App, Coverage</summary>
<img src="">
</details>


### Device Testing & Browser compatibility

The site uses to test on various real world devices was [BrowserStack]()  

This allowed me to test on real devices and not just device emulators.

The following devices were used to test my site:

<details><summary>Samsung Galaxy S22 Ultra</summary>
<img src="">
</details>

<details><summary>Apple iPhone 13</summary>
<img src="">
</details>

<details><summary>Google Pixel 5</summary>
<img src="">
</details>

<details><summary>Mozilla Firefox (v105 latest)</summary>
<img src="">
</details>

<details><summary>Google Chrome (v106 latest)</summary>
<img src="">
</details>

<details><summary>Safari (Monteray v15.3 latest)</summary>
<img src="">
</details>


##### Back to [top](#table-of-contents)<hr>


## Bugs

| **Bug** | **Fix** |
| ------- | ------- |
| | |


##### Back to [top](#table-of-contents)<hr>


### Heroku Deployment

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-01.PNG">
</details>

2. Create an app, give it a name for such as ci-pp4-the-diplomat, and select a region
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-02.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-03.PNG">
</details>

3. Under resources search for postgres, and add a Postgres database to the app
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-04.PNG">
</details>

Heroku Postgres

1. Note the DATABASE_URL, this can be set as an environment variable in Heroku and your local deployment(env.py)
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-18.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-17.PNG">
</details>

2. Install the plugins dj-database-url and psycopg2-binary.

3. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-05.PNG">
</details>

4. Create a Procfile with the text: web: gunicorn the_diplomat.wsgi
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-06.PNG">
</details>

5. In the settings.py ensure the connection is to the Heroku postgres database, no indentation if you are not using a seperate test database.
I store mine in env.py
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-07.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-08.PNG">
</details>

6. Ensure debug is set to false in the settings.py file
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-09.PNG">
</details>

7. Add localhost, and ci-pp4-the-diplomat.herokuapp.com to the ALLOWED_HOSTS variable in settings.py

8. Run "python3 manage.py showmigrations" to check the status of the migrations

9. Run "python3 manage.py migrate" to migrate the database

10. Run "python3 manage.py createsuperuser" to create a super/admin user

11. Run "python3 manage.py loaddata categories.json" on the categories file in products/fixtures to create the categories

12. Run "python3 manage.py loaddata products.json" on the products file in products/fixtures to create the products

13. Install gunicorn and add it to the requirements.txt file using the command pip3 freeze > requirements.txt

14. Disable collectstatic in Heroku before any code is pushed using the command heroku config:set DISABLE_COLLECTSTATIC=1 -a ci-pp4-the-diplomat
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-19.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-10.PNG">
</details>


15. Ensure the following environment variables are set in Heroku
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-11.PNG">
</details>

16. Connect the app to GitHub, and enable automatic deploys from main if you wish
<details>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-13.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-14.PNG">
</details>

17. Click deploy to deploy your application to Heroku for the first time

18. Click on the link provided to access the application

19. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue
<hr>

### Fork Repository
To fork the repository by following these steps:
1. Go to the GitHub repository
2. Click on Fork button in upper right hand corner
<hr>

### Clone Repository
You can clone the repository by following these steps:
1. Go to the GitHub repository 
2. Locate the Code button above the list of files and click it 
3. Select if you prefere to clone using HTTPS, SSH, or Github CLI and click the copy button to copy the URL to your clipboard
4. Open Git Bash
5. Change the current working directory to the one where you want the cloned directory
6. Type git clone and paste the URL from the clipboard ($ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY)
7.Press Enter to create your local clone.

##### Back to [top](#table-of-contents)<hr>


## Credits

### Images



### Code



##### Back to [top](#table-of-contents)<hr>

## Acknowledgements

### Special thanks to the following:
- Code Institute
- My Mentor Mo Shami