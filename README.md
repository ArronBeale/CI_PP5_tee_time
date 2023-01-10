# eCommerce: Teetime

![Am I Responsive](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/responsive.PNG)

**Developer: Arron Beale**

💻 [Visit live website](https://ci-pp5-teetime.herokuapp.com/)  
(Ctrl + click to open in new tab)



## Table of Contents
  - [Executive Summary](#executive-summary)
     - [Market Analysis](#market-analysis)
     - [Marketing and Sales Strategy](#marketing-and-sales-strategy)
     - [Operations and Management](#operations-and-management)
     - [Financial Plan](#financial-plan)
     - [Conclusion](#conclusion)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Design](#design)
    - [Colors](#colors)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [AWS](#aws)
      - [Database](#database)
      - [Models](#models)
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

<hr>

## Business Plan  
### Executive Summary:

Teetime is a web-based platform that connects golfers with golf clubs and societies. It offers a convenient and easy-to-use platform for booking tee times, as well as an ecommerce shop for purchasing golf-related products. In addition, Teetime features a blog with the latest news and tips on golf, as well as a contact page for inquiries and support.

Our target market is golfers of all skill levels and demographics, as well as golf clubs and societies looking for a streamlined solution for managing bookings and tee times. We aim to differentiate ourselves from competitors by offering a more user-friendly and intuitive platform, as well as a wider range of products in our ecommerce shop.

In terms of revenue, Teetime will generate income through two main streams: the sale of products in our ecommerce shop and the sale of our software to golf clubs and societies. We will also explore potential partnerships and sponsorships with golf-related brands to further monetize the platform.

Overall, Teetime aims to become the go-to destination for golfers looking to book tee times and purchase golf-related products, as well as a trusted and reliable solution for golf clubs and societies looking to manage their bookings and tee times.

### Market Analysis:

The golf industry is a multi-billion dollar industry, with a large and dedicated consumer base. While traditional methods of booking tee times (such as calling the club or booking in-person) are still popular, there is a growing trend towards online booking platforms. This shift towards online booking presents a significant opportunity for Teetime to establish itself as a leading player in the market.

In terms of competition, Teetime will face other online booking platforms as well as traditional methods of booking. However, we believe that our user-friendly platform and wide range of products in our ecommerce shop will differentiate us from competitors and make us a preferred choice for golfers.

In terms of target market, our primary focus will be on golfers of all skill levels and demographics. We will also target golf clubs and societies as potential customers for our software, as these organizations are constantly seeking ways to streamline their operations and manage bookings.

### Marketing and Sales Strategy:

Teetime will utilize a combination of online and offline marketing tactics to reach our target market. These tactics will include:

Online advertising through Google AdWords and social media platforms such as Facebook and Instagram
Content marketing through our blog and email newsletter
Partnerships and sponsorships with golf-related brands
Public relations efforts to generate press coverage and raise awareness of Teetime
In terms of sales, our primary focus will be on converting website visitors into customers through the use of persuasive copy and calls-to-action. We will also explore partnerships with golf clubs and societies to offer our software as a solution for managing bookings and tee times.

### Operations and Management:

Teetime will be operated and managed by a small team of experienced professionals. The team will consist of a CEO, CTO, and marketing and sales staff.

In terms of operations, we will utilize a cloud-based platform to host the website and software, as well as a payment gateway for processing transactions. We will also utilize third-party fulfillment centers to handle the storage, packing, and shipping of products purchased through our ecommerce shop.

#### Financial Plan:

Teetime will generate revenue through the sale of products in our ecommerce shop and the sale of our software to golf clubs and societies. In terms of expenses, the main cost will be marketing and advertising efforts to drive traffic to the website and attract customers. We will also incur expenses related to the development.

In terms of financing, Teetime will initially be funded through a combination of personal investment and a small seed round of funding. As the business grows, we will explore additional funding options such as venture capital or a larger round of financing.

In terms of projections, we anticipate strong growth in both revenue streams over the first few years of operation. In the first year, we expect to generate €500,000 in revenue, with €300,000 coming from product sales and €200,000 coming from the sale of our software. In the second year, we expect to see revenue increase to €750,000, with €450,000 coming from product sales and €300,000 coming from software sales. By the third year, we anticipate revenue to reach €1 million, with €600,000 coming from product sales and €400,000 coming from software sales.

In terms of profitability, we expect to break even within the first year of operation and achieve profitability in the second year.

### Conclusion:

Teetime is a unique and innovative platform that aims to connect golfers with golf clubs and societies, while also offering a convenient and user-friendly platform for booking tee times and purchasing golf-related products. With strong growth potential and a clear revenue model, we believe that Teetime has the potential to become a leading player in the golf industry.
##### Back to [top](#table-of-contents)<hr>

## User Goals

- To easily and conveniently book tee times at golf clubs and societies
- To browse and purchase a wide range of golf-related products through the eCommerce shop
- To access the latest news and tips on golf through the blog
- To contact the Teetime team with any inquiries or support needs through the contact page

## Site Owner Goals

- Generate revenue through the sale of products in the ecommerce shop and the sale of software to golf clubs and societies
- Build a strong and loyal customer base by providing an easy-to-use platform and high-quality products
- Establish Teetime as a trusted and respected brand in the golf industry
- Achieve profitability and sustain long-term growth
<hr>


## User Experience

### Target Audience
- Golf enthusiasts who are interested in booking tee times at golf clubs and purchasing golf-related products.
- Golf clubs and golf societies who may be interested in using the software to manage tee time bookings and potentially purchasing products through the ecommerce shop.
- Individuals who are looking for information and resources related to golf, as indicated by the presence of a blog on the app.
- Individuals who are interested in scheduling and organizing golf games or events, as the app allows users to book tee times at golf clubs.
- Any individual who is interested in purchasing golf-related products through the app's ecommerce shop.

### User Requirements and Expectations

- A user-friendly interface: Users will expect the app to be easy to navigate and use, with clear and concise instructions for booking tee times and purchasing products.
- Reliability: Users will expect the app to be reliable and function smoothly, without any errors or technical issues.
- Security: Users will expect their personal and financial information to be secure when using the app, and will expect the app to have appropriate measures in place to protect their data.
- A wide selection of golf clubs and tee times: Users will expect the app to have a wide selection of golf clubs and tee times available for booking.
- Accurate and up-to-date information: Users will expect the app to provide accurate and up-to-date information about golf clubs, tee times, and products.
- Competitive prices: Users will expect the prices for tee times and products to be competitive with other options available on the market.
- Good customer service: Users will expect the app to have good customer service, including responsive and helpful support in the event of any issues or questions.
- Accessibility

##### Back to [top](#table-of-contents)<hr>


## User Stories


| User Story ID                  | As A/AN             | I CAN...                                                | SO THAT I CAN...                                          |
|--------------------------------|---------------------|---------------------------------------------------------|-----------------------------------------------------------|
| Registration and User Accounts |                     |                                                         |                                                           |
| 1                              | Shopper / Site User | register for an account                                 | have an account and view my profile                       |
| 2                              | Shopper / Site User | login and logout                                        | have an account with my information stored for fast usage |
| 3                              | Shopper / Site User | recover my password                                     | set a new password if I forgot it                         |
| 4                              | Shopper / Site User | receive an email confirmation after registration        | be notified registration was successful                   |
| 5                              | Shopper / Site User | have a profile                                          | store my information for faster checkouts in the future   |
| Viewing and navigation         |                     |                                                         |                                                           |
| 6                              | Shopper / Site User | navigate across the site                                | can access all parts of the site                          |
| 7                              | Shopper / Site User | use a navbar, footer, and social icons                  | navigate the site, access menus, and access socials       |
| 8                              | Shopper / Site User | be notified of my actions                               | be aware the action was completed successfully or not     |
| 9                              | Shopper / Site User | see my login status                                     | know if I am logged in or not                             |
| 10                             | Shopper / Site User | visit the shop                                          | view all products available                               |
| 11                             | Shopper / Site User | view my basket and total cost at any time               | so I am aware of what I am buying and it's cost           |
| 12                             | Shopper / Site User | view a list of products                                 | select a product to purchase                              |
| 13                             | Shopper / Site User | view an individual product details                      | view a more detailed view of the product                  |
| 14                             | Shopper / Site User | view a list of golf courses                             | select a golf course I want to play on                    |
| 15                             | Shopper / Site User | view individual golf course details                     | see more detailed information about it                    |
| 16                             | Shopper / Site User | view a list of tee times available for each golf course | select a date and time to play                            |
| Sorting and Searching          |                     |                                                         |                                                           |
| 17                             | Shopper / Site User | search for a product by name or description             | find a certain product                                    |
| 18                             | Shopper / Site User | see my search results                                   | only see what I am searching for                          |
| 19                             | Shopper / Site User | sort by category                                        | select products of a certain category                     |
| 20                             | Shopper / Site User | sort by price low to high and high to low               | view products according to my budget                      |
| 21                             | Shopper / Site User | select only available dates/times                       | I can only purchase available tee slots                   |
| Purchasing and Checkout        |                     |                                                         |                                                           |
| 22                             | Shopper / Site User | use a card as the payment method                        | complete my purchase                                      |
| 23                             | Shopper / Site User | select the size and quantity of a product               | select a size and quantity to my needs                    |
| 24                             | Shopper / Site User | view items in my basket                                 | be aware of what I am buying and it's cost                |
| 25                             | Shopper / Site User | adjust item quantity in my basket                       | increase or reduce item count according to my needs       |
| 26                             | Shopper / Site User | receive order confirmation                              | be notified of a successful order                         |
| 27                             | Shopper / Site User | receive email confirmation                              | have a record of my purchase                              |
| Admin and Store Management     |                     |                                                         |                                                           |
| 28                             | Store Owner / Admin | add a product                                           | add new products to the shop                              |
| 29                             | Store Owner / Admin | edit a product                                          | edit existing products in the shop                        |
| 30                             | Store Owner / Admin | delete a product                                        | delete existing products from the shop                    |
| 31                             | Store Owner / Admin | add a golf club                                         | add a golf club to the site                               |
| 32                             | Store Owner / Admin | edit a golf club                                        |edit an existing golf club on the site|
| 33 | Store Owner / Admin | delete a golf club | delete existing golf club from the site  |
| 34 | Store Owner / Admin | add a tee time     | add a tee time to a golf club            |
| 35 | Store Owner / Admin | edit a tee time    | edit an existing tea time on a golf club |
| 36 | Store Owner / Admin | delete a tee time  | delete a tee time from a golf club       |


### Kanban, Epics & User Stories
- GitHub Kanban was used to track all open user stories
- Epics were created using the milestones feature
- Backlog, In Progress, Done headings were used in the kanban

<details><summary>Epic Overview</summary>

![Epics](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/agile/epics1.PNG)
</details>

<details><summary>Epic 1</summary>

![Epic 1](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/agile/epics2.PNG)
</details>

<details><summary>Epic 2</summary>

![Epic 2](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/agile/epics3.PNG)
</details>

<details><summary>Epic 3</summary>

![Epic 3](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/agile/epics4.PNG)
</details>

<details><summary>Epic 4</summary>

![Epic 4](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/agile/epics5.PNG)
</details>



<details><summary>User Stories</summary>

![User stories](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/agile/user-stories1.PNG)
![User stories](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/agile/user-stories2.PNG)
![User stories](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/agile/user-stories3.PNG)

</details>

<details><summary>Kanban</summary>

![Kanban Start](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/agile/kanban-start.PNG)
![Kanban Middle](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/agile/kanban-mid.PNG)
![Kanban End](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/agile/kanban-end.PNG)

</details>


##### Back to [top](#table-of-contents)<hr>


## Design

### Colors


The color I chose was dark green with a light background.  
<details><summary>See Color Palette</summary>

![Color Palette](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/coolors-teetime.png)
</details>

### Fonts

 The font selected was from Google Fonts, Roboto.

 <details><summary>See Font Image</summary>

![Font Image](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/font-roboto.PNG)
</details>
<hr>

# Structure

The site was designed for the user to be familiar with the layout such as a navigation bar along the top of the pages and a hamburger menu button for smaller screen.

The footer contains all relevant social media links that the business has so the user can visit any social media site and follow the business there to expand the businesses followers, likes and shares.
It contains an email sign up form and useful links as well as contact information.

## Website pages

- The site consists of the following pages:
  - Home
  - Golf Clubs
  - Golf Club Expanded
  - Booking List
  - Edit Booking
  - Cancel Booking
  - Product List
  - Product Expanded
  - Basket
  - Checkout
  - Checkout Success
  - Blog
  - Blog expanded
  - Contact
  - Register
  - Profile
  - Login
  - Logout
  - Reset Password
  - Register
  - 404

  ##### Back to [top](#table-of-contents)
  <hr>

## AWS 

I am using AWS S3 buckets to store my data. S3 is a highly scalable and durable cloud storage service provided by Amazon Web Services. It allows me to easily store and retrieve large amounts of data, and its built-in security features provide added protection for my files. I chose S3 for its scalability, durability, and security features.

<details><summary>See AWS Images</summary>

![aws bucket](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-s3-bucket.PNG)
![aws media](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-s3-bucket-media.PNG)
![aws static](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-s3-bucket-static.PNG)
</details>
<hr>


## Database

I built my database using PostgreSQL. It's a powerful and open-source object-relational database system that is known for its reliability, robustness, and performance. I chose it because it provides a flexible tool for efficiently managing and organizing my data.

<a href="https://docs.google.com/spreadsheets/d/13d5eeCcBG7GWVxWo78qZi8OyIZ10Tu6Ze7brLsul9qo/edit?usp=sharing" target="_blank">Link Database Schema</a>  
(Ctrl + click to open in new tab)
<hr>

## Models  

### User Model

| Key        | Name         | Type        |
| ---------- | ------------ | ----------- |
| PrimaryKey | user_id      | AutoField   |
|            | password     | VARCHAR(45) |
|            | last_login   | VARCHAR(45) |
|            | is_superuser | BOOLEAN     |
|            | username     | VARCHAR(45) |
|            | first_name   | VARCHAR(45) |
|            | last_name    | VARCHAR(45) |
|            | email        | VARCHAR(45) |
|            | is_staff     | BOOLEAN     |
|            |              |             |
|            | is_active    | BOOLEAN     |
|            | date_joined  | VARCHAR(45) |

### User Profile Model

| Key        | Name                 | Type          |
| ---------- | -------------------- | ------------- |
| PrimaryKey | user_profile_id      | AutoField     |
| ForeignKey | user                 | User model    |
|            | default_phone_number | CharField[20] |
|            | default_address1     | CharField[80] |
|            | default_address2     | CharField[80] |
|            | default_town_city    | CharField[40] |
|            | default_county       | CharField[80] |
|            | default_postcode     | CharField[20] |
|            | default_country      | CharField[40] |

### Club Model

| Key        | Name           | Type          |
| ---------- | -------------- | ------------- |
| PrimaryKey | club_id        | AutoField     |
|            | golf_club_name | CharField[50] |
|            | slug           | SlugField     |
|            | description    | TextField     |
|            | available      | BooleanField  |
|            | image          | ImageField    |
|            | excerpt        | TextField     |

### Booking Model

| Key        | Name           | Type            |
| ---------- | -------------- | --------------- |
| PrimaryKey | booking_id     | AutoField       |
|            | created_date   | DateTime        |
|            | requested_date | DateTime        |
|            | requested_time | CharField[10]   |
| ForeignKey | golf_club_name | Golf club model |
| ForeignKey | user           | User model      |
|            | name           | CharField[50]   |
|            | email          | EmailField      |
|            | phone          | PhoneNumField   |
|            | status         | CharField[50]   |
|            | players        | Tuple           |
|            | player_count   | intField        |

### Product Model

| Key        | Name        | Type           |
| ---------- | ----------- | -------------- |
| PrimaryKey | product_id  | AutoField      |
|            | code        | CharField[50]  |
|            | brand       | CharField[50]  |
|            | name        | CharField[50]  |
|            | description | TextField      |
|            | has_sizes   | BooleanField   |
|            | price       | DecimalField   |
| ForeignKey | category    | Category model |
|            | rating      | DecimalField   |
|            | image       | ImageField     |

### Category Model  

| Key        | Name          | Type      |
| ---------- | ------------- | --------- |
| PrimaryKey | category_id   | AutoField |
|            | name          | Char[254] |
|            | friendly_name | Char[254] |

### Order Model  

| Key        | Name            | Type               |
| ---------- | --------------- | ------------------ |
| PrimaryKey | order_id        | AutoField          |
|            | order_number    | CharField[40]      |
| ForeignKey | user_profile    | User profile Model |
|            | full_name       | CharField[50]      |
|            | email           | EmailField[254]    |
|            | phone_number    | CharField[20]      |
|            | address1        | CharField[80]      |
|            | address2        | CharField[80]      |
|            | town_city       | CharField[40]      |
|            | postcode        | CharField[20]      |
|            | county          | CharField[80]      |
|            | country         | CharField[40]      |
|            | date            | DateTimeField      |
|            | delivery_cost   | DecimalField[6]    |
|            | order_total     | DecimalField[10]   |
|            | grand_total     | DecimalField[10]   |
|            | original_basket | TextField          |
|            | stripe_pid      | CharField          |

### OrderLineItem Model  

| Key        | Name             | Type            |
| ---------- | ---------------- | --------------- |
| PrimaryKey | OrderLineItem_id | AutoField       |
| ForeignKey | order            | Order Model     |
| ForeignKey | product          | Product Model   |
|            | product_size     | CharField[2]    |
|            | quantity         | IntegerField    |
|            | line_item_total  | DecimalField[6] |

### Post Model

| Key        | Name           | Type                |
| ---------- | -------------- | ------------------- |
|            | title (unique) | Char[200]           |
|            | slug (unique)  |                     |
| PrimaryKey | post_id        | AutoField           |
| ForeignKey | author         | User model          |
|            | created_date   | DateTime            |
|            | updated_date   | DateTime            |
|            | content        | TextField           |
|            | featured_image | Cloudinary<br>image |
|            | excerpt        | TextField           |
|            | status         | Integer             |

### Comment Model

| Key        | Name         | Type                                   |
| ---------- | ------------ | -------------------------------------- |
| ForeignKey | post         | Post model<br>Cascade on<br>delete     |
|            | name         | CharField[80]                          |
|            | email        | EmailField                             |
|            | body         | TextField                              |
|            | created_date | DateTimeField<br>auto_now_<br>add_true |
|            | approved     | BooleanField<br>default False          |
|            |              |                                        |
|            |              |                                        |
|            | Meta         | created_on                             |

### ContactUs Model

| Key        | Name         | Type             |
| ---------- | ------------ | ---------------- |
| PrimaryKey | message_id   | AutoField        |
|            | created_date | DateTimeField    |
| ForeignKey | user         | User model       |
|            | name         | CharField        |
|            | email        | EmailField       |
|            | phone        | PhoneNumberField |
|            | body         | TextField        |  

##### Back to [top](#table-of-contents)
<hr>


### Wireframes
I used Balsamiq to create wireframes for my project. It's a user-friendly wireframing tool that enables me to quickly and easily create mockups for my website or application. It offers a wide range of pre-built UI elements, and allows for easy collaboration with my team. I linked a pdf of my wireframes, which you can access it and check it out the design, layout and the flow of the project before implementing it in the real product.  

<a href="https://github.com/ArronBeale/CI_PP5_tee_time/blob/main/docs/wireframes/wireframes-teetime.pdf" target="_blank">Download Wireframes PDF</a>  
(Ctrl + click to open in new tab)  

<details><summary>Wireframe Home</summary>
![Epics](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/wireframes/wireframe-home.PNG)
</details>

<details><summary>Wireframe Profile</summary>
![Epic 1](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/wireframes/wireframe-profile.PNG)
</details>

<details><summary>Wireframe Clubs</summary>
![Epic 2](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/wireframes/wireframe-clubs.PNG)
</details>

<details><summary>Wireframe Club Detail</summary>
![Epic 3](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/wireframes/wireframe-club-detail-01.PNG)
![Epic 3](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/wireframes/wireframe-club-detail-02.PNG)
</details>

<details><summary>Wireframe Shop</summary>
![Epic 4](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/wireframes/wireframe-shop.PNG)
</details>  

<details><summary>Wireframe Product Detail</summary>
![Epic 4](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/wireframes/wireframe-product-detail.PNG)
</details> 

<details><summary>Wireframe Checkout</summary>
![Epic 4](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/wireframes/wireframe-checkout.PNG)
</details>

<details><summary>Wireframe Checkout</summary>
![Epic 4](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/wireframes/wireframe-checkout.PNG)
</details>

<hr>


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