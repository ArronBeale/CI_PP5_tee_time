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

- To provide a solution to allow users to book a tee time
- To provide a solution to allow users to buy from the shop
- To attract more business with a well crafted site
- Provide a modern application with an easy navigation
- Fully responsive and accessible
<hr>


## User Experience

### Target Audience
- 
- 
- 
- 
- 

### User Requirements and Expectations

- Fully responsive
- Accessible
- A welcoming design
- 
- 
- Social media
- Contact information
- Accessibility

##### Back to [top](#table-of-contents)<hr>


## User Stories

### Users

1.	
2.	
3.	
4. 
5. 
6. 
7. 
8. 
9. 
10. 




### Admin / Authorised User
11. 
12. 
13. 
14. 




### Site Owner  
15. 
16. 
17. 
18. 
19. 



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
<img src="docs/coolors.png">
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
- Contact info such as, phone, email, and address is displayed
- A Google Map is embedded with the address for users to use
  
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

<details><summary>Food Menu</summary>
<img src="">
<img src="">
</details>

<details><summary>Drinks Menu</summary>
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
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/unittest-bar-and-grill-test-models.PNG">
</details>

<details><summary> App, test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/unittest-bar-and-grill-test-views.PNG">
</details>

<details><summary> App, test_urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/unittest-bar-and-grill-test-urls.PNG">
</details>

<details><summary> App, Coverage</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/testing/coverage-bar-and-grill.PNG">
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