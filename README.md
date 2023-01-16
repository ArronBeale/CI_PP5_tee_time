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
  - [Marketing](#marketing)
     - [Social Media](#social-media)
     - [Mailing List](#mailing-list)
  - [User Goals](#user-goals)
  - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
  - [User Stories](#user-stories)
  - [Wireframes](#wireframes)
  - [Design](#design)
    - [Colors](#colors)
    - [Fonts](#fonts)
    - [Structure](#structure)
      - [Website pages](#website-pages)
      - [AWS](#aws)
      - [Database](#database)
      - [Models](#models)
  - [Technologies Used](#technologies-used)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [Automated testing](#automated-testing)
    - [Tests on various devices](#tests-on-various-devices)
    - [Browser compatibility](#browser-compatibility)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
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

## Marketing  

### Social Media  
The web app "teetime" has a presence on both Facebook and Instagram. The Facebook page serves as a platform to promote upcoming events, post updates on the latest features, and share user-generated content. The Instagram page primarily focuses on showcasing beautiful golf courses, highlighting new products in the shop, and providing a behind-the-scenes look at the company. These social media accounts allow users to stay informed and connected with the "teetime" community.

[Facebook](https://www.facebook.com/profile.php?id=100088722476900)  
[Instagram](https://www.instagram.com/teetimegolfapp/)

### Mailing List  

Teetime uses Mailchimp to manage its mailing list. By joining the mailing list, users will receive updates on new features, upcoming events, and exclusive promotions. The process to join the mailing list is simple, users just need to provide their email address on the website, and they will start receiving email updates. Mailchimp allows the "teetime" team to segment the mailing list, personalize emails and track the success of email campaigns. By joining the mailing list, users will stay informed and be the first to know about new developments in the "teetime" web app.  

<details><summary>See Image</summary>

![Mailchimp](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-mailing-list-sign-up.PNG)  
![Email](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/web-marketing/marketing-mailchimp-01.PNG)
![Email content](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/web-marketing/marketing-mailchimp-02.PNG)
</details> 

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
| Registration and User Accounts ||||
| 1 | Shopper / Site User | register for an account | have an account and view my profile |
| 2 | Shopper / Site User | login and logout | have an account with my information stored for fast usage |
| 3 | Shopper / Site User | recover my password | set a new password if I forgot it                         |
| 4 | Shopper / Site User | receive an email confirmation after registration| be notified registration was successful                   |
| 5 | Shopper / Site User | have a profile | store my information for faster checkouts in the future |
| Viewing and navigation ||||
| 6 | Shopper / Site User | navigate across the site | can access all parts of the site                          |
| 7 | Shopper / Site User | use a navbar, footer, and social icons | navigate the site, access menus, and access socials       |
| 8 | Shopper / Site User | be notified of my actions | be aware the action was completed successfully or not     |
| 9 | Shopper / Site User | see my login status | know if I am logged in or not |
| 10 | Shopper / Site User | visit the shop| view all products available |
| 11 | Shopper / Site User | view my basket and total cost at any time | so I am aware of what I am buying and it's cost |
| 12 | Shopper / Site User | view a list of products | select a product to purchase                              |
| 13 | Shopper / Site User | view an individual product details | view a more detailed view of the product |
| 14 | Shopper / Site User | view a list of golf courses | select a golf course I want to play on |
| 15 | Shopper / Site User | view individual golf course details | see more detailed information about it |
| 16 | Shopper / Site User | view a list of tee times available for each golf course | select a date and time to play |
| Sorting and Searching ||||
| 17 | Shopper / Site User | search for a product by name or description | find a certain product                                    |
| 18 | Shopper / Site User | see my search results | only see what I am searching for |
| 19 | Shopper / Site User | sort by category | select products of a certain category |
| 20 | Shopper / Site User | sort by price low to high and high to low | view products according to my budget |
| 21 | Shopper / Site User | select only available dates/times | I can only purchase available tee slots |
| Purchasing and Checkout ||||
| 22 | Shopper / Site User | use a card as the payment method | complete my purchase                                      |
| 23 | Shopper / Site User | select the size and quantity of a product | select a size and quantity to my needs |
| 24 | Shopper / Site User | view items in my basket | be aware of what I am buying and it's cost |
| 25 | Shopper / Site User | adjust item quantity in my basket | increase or reduce item count according to my needs |
| 26 | Shopper / Site User | receive order confirmation | be notified of a successful order |
| 27 | Shopper / Site User | receive email confirmation | have a record of my purchase |
| Admin and Store Management | | | |
| 28 | Store Owner / Admin | add a product | add new products to the shop |
| 29 | Store Owner / Admin | edit a product | edit existing products in the shop |
| 30 | Store Owner / Admin | delete a product | delete existing products from the shop |
| 31 | Store Owner / Admin | add a golf club | add a golf club to the site |
| 32 | Store Owner / Admin | edit a golf club |edit an existing golf club on the site|
| 33 | Store Owner / Admin | delete a golf club | delete existing golf club from the site |
| 34 | Store Owner / Admin | add a tee time | add a tee time to a golf club |
| 35 | Store Owner / Admin | edit a tee time | edit an existing tea time on a golf club |
| 36 | Store Owner / Admin | delete a tee time | delete a tee time from a golf club |
| 37 | Shopper / Site User | book a tee time | book a tee time for a golf club |
| 38 | Shopper / Site User | edit a tee time booking | edit a tee time booking as I alter my schedule to play golf |
| 39 | Shopper / Site User | delete a tee time booking | delete a tee time booking if I need to cancel |
| 40 | Shopper / Site User | view my tee time bookings | view my tee time bookings |


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

## Wireframes
I used Balsamiq to create wireframes for my project. It's a user-friendly wireframing tool that enables me to quickly and easily create mockups for my website or application. It offers a wide range of pre-built UI elements, and allows for easy collaboration with my team. I linked a pdf of my wireframes, which you can access it and check it out the design, layout and the flow of the project before implementing it in the real product.  

<a href="https://github.com/ArronBeale/CI_PP5_tee_time/raw/main/docs/wireframes/wireframes-teetime.pdf" target="_blank">Download Wireframes PDF</a>  
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

<hr>

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

<a href="https://github.com/ArronBeale/CI_PP5_tee_time/raw/main/docs/database/db-schema.pdf" target="_blank">Download Schema PDF</a>  
<a href="https://docs.google.com/spreadsheets/d/13d5eeCcBG7GWVxWo78qZi8OyIZ10Tu6Ze7brLsul9qo/edit?usp=sharing" target="_blank">Database Schema</a>  
(Ctrl + click to open in new tab)  
<details><summary>See Database Image</summary>
![schema](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/database/image-db-schema.PNG)
</details>
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
- [AWS](https://aws.amazon.com/)
- [jQuery](https://jquery.com)
- [Postgres](https://www.postgresql.org/)
- [Summernote](https://summernote.org/)
- Validation:
  - [WC3 Validator](https://validator.w3.org/)
  - [Jigsaw W3 Validator](https://jigsaw.w3.org/css-validator/)
  - [JShint](https://jshint.com/)
  - [CI Python Liner(PEP8)](https://pep8ci.herokuapp.com/)
  - [Lighthouse](https://developers.google.com/web/tools/lighthouse/)
  - [Wave Validator](https://wave.webaim.org/)

##### Back to [top](#table-of-contents)


## Features  


### Search Engine Optimisation (SEO)
I have used meta tags in the HTML of my web app's pages to optimize them for search engines. The description tag provides a brief summary of the content on the page, while the keywords tag lists relevant keywords to help search engines understand the content of the webpage and its relevance to related search queries.


<details><summary>See feature image</summary>

![SEO](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-seo.PNG)
</details>  

### Home page
- Home page includes nav bar, main body and a footer.


<details><summary>See feature images</summary>

![Home page](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-home.PNG)
</details>  


### Logo
- A custom logo for the business.
- User stories covered: 6, 7

<details><summary>See feature images</summary>

![Logo](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-logo.PNG)
</details>  


### Navigation
- Fully Responsive.
- On small screens switches to hamburger menu.
- Indicates login/logout in status.
- displayed on all pages.  
- User stories covered: 6, 7

<details><summary>See feature images</summary>

![Navigation](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-nav.PNG)
</details>


### Footer
- Contains social media links, privacy policy, and copyright.
- displayed across all pages.  
- User stories covered: 6, 7

<details><summary>See feature images</summary>

![Footer](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-footer.PNG)
</details>  

### Mailing List Sign Up
- Mailchimp signup for email mailing list.  

<details><summary>See feature images</summary>

![Mailing](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-mailing-list-sign-up.PNG)
</details>


### Sign up / Register
- Allow users to register an acoount.
- User stories covered: 1  

<details><summary>See feature image</summary>

![Signup](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-sign-up.PNG)
</details>


### Sign In
- User can sign in.  
- User stories covered: 2

<details><summary>See feature images</summary>

![Signin](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-sign-in.PNG)
</details>


### Sign Out
- Allows the user to securely sign out.
- Ask user if they are sure they want to sign out.  
- User stories covered: 2

<details><summary>See feature image</summary>

![Sign out](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-sign-out.PNG)
</details>  


### Golf Clubs
- Allows the user to view all listed golf clubs.  
- User stories covered: 14

<details><summary>See feature image</summary>

![Golf Clubs](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-golf-clubs.PNG)
</details>  


### Golf Club Detail
- Allows the user to view details of a specific golf club.  
- User stories covered: 15

<details><summary>See feature image</summary>

![Golf Club Detail](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-club-detail.PNG)
</details>


### Book a Tee Time
- Allows the user to book a tee time.
- Messages are displayed if the data is not valid such as phone number lenght is too short and the email address is not a valid format.  
- User stories covered: 37

<details><summary>See feature images</summary>

![Book](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-booking-form.PNG)
</details>


### My Teetimes
- Allows the user to see their bookings.  
- User stories covered: 40

<details><summary>See feature image</summary>

![Teetimes](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-booking-list.PNG)
</details>  


### Edit Booking
- Allows the user to edit their bookings.  
- User stories covered: 38

<details><summary>See feature image</summary>

![Edit Booking](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-booking-edit.PNG)
</details>  


### Cancel Booking
- Allows the user to cancel their bookings.  
- User stories covered: 39

<details><summary>See feature image</summary>

![Cancel Booking](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-booking-cancel.PNG)
</details>  


### Alert Box
- Allows the user to see relevant alerts.  
- User stories covered: 8

<details><summary>See feature image</summary>

![Edit Booking](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-alert-box.PNG)
</details>  


### Shop
- Allows the user to view the listed products in the shop.  
- User stories covered: 10

<details><summary>See feature image</summary>

![Shop](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-shop.PNG)
</details>  


### Sort
- Allows the user to sort the listed products.  
- User stories covered: 19, 20

<details><summary>See feature images</summary>

![Sort1](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-shop-sort-01.PNG)
![Sort2](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-shop-sort-02.PNG)
</details>  


### product Detail
- Allows the user to view the products details.  
- User stories covered: 13

<details><summary>See feature image</summary>

![product Detail](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-product-detail.PNG)
</details>  


### Search
- Allows the user to search for products.  
- User stories covered: 17, 18

<details><summary>See feature image</summary>

![Search](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-search.PNG)
</details>  


### Basket
- Allows the user to view the basket with their items.
- Pops up as items are added and removed.  
- User stories covered: 24, 11

<details><summary>See feature image</summary>

![Basket1](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-basket.PNG)
![Basket2](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-alert-box.PNG)
</details>  


### Checkout
- Allows the user to purchase items in their basket.  
- User stories covered: 22, 23, 24, 25

<details><summary>See feature image</summary>

![Checkout](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-checkout.PNG)
</details>  


### Stripe
- Allows the user to use stripe for card payments.  
- User stories covered: 22

<details><summary>See feature image</summary>

![Stripe](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-stripe.PNG)
</details>  


### Email Confirmation
- Allows the user to receive an email confirmation for their order.  
- User stories covered: 27

<details><summary>See feature image</summary>

![Email Confirmation](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-email-confirmation.PNG)
</details>  


### Profile
- Allows the user to update their information and see their order history.  
- User stories covered: 5

<details><summary>See feature image</summary>

![Profile](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-profile.PNG)
</details>  


### Add Product
- Allows the Admin to add new products.  
- User stories covered: 28

<details><summary>See feature image</summary>

![Add Product](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-add-product.PNG)
</details>  


### Edit Product
- Allows the user to edit the products.  
- User stories covered: 29

<details><summary>See feature image</summary>

![Edit Product](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-edit-product.PNG)
</details>  


### Delete Product
- Allows the user to delete products, includes confirmation prompt before deletion.  
- User stories covered: 30

<details><summary>See feature image</summary>

![Delete Product](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-delete-product.PNG)
</details>  


### Blog
- The blog displays each post made by a staff member
- Paginations is used to display 4 posts per page  
- User stories covered: extra feature
  
<details><summary>See feature images</summary>

![Blog](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-blog.PNG)
</details>


### Blog Expanded
- Expands into the selected blog the user wishes to read
- Displays a featured image uploaded by the poster
- If no image is uploaded a default image is then used
- Registerd user can comment on the blog  
- User stories covered: extra feature
  
<details><summary>See feature images</summary>

![Blog Expanded](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-blog-detail.PNG)
</details>


### Comments
- Comments made are set to pending approval status to ensure nothing bad is displayed
- Only registered users can comment on a blog post
- Staff can approve comments via the admin panel on the backend  
- User stories covered: extra feature
  
<details><summary>See feature images</summary>

![Comments](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-blog-comments.PNG)
</details>


### Contact Us / Send Message
- A contact page with all contact details listed
- Users can send a message via the message form  
  
<details><summary>See feature images</summary>

![Contact Us](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-contact.PNG)
![Message](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-contact-message.PNG)
</details>


### Social Media Links
- A logo and link is used for the Facebook business page and Instagram page.
- All links open in a new tab to ensure the user is not directed away from the business.
- noopener, noreferrer, nofollow used to communicate with web crawlers and for security and privacy concerns.  
- User stories covered: 7
  
<details><summary>See feature image</summary>

![Social Media Links](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-footer.PNG)
</details>


### Pagination
- Pagination is used on the
- Ensures the page is kept tidy  
  
<details><summary>See feature images</summary>

![Pagination](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/features/feature-pagination.PNG)
</details>


##### Back to [top](#table-of-contents)<hr>

# Validation  

## HTML Validation

The W3C Markup Validation Service was used to validate the HTML of the website.  

### Home  

index.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-pp5-teetime.herokuapp.com/) 
- No Errors Found


| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A |  


### Golf Clubs  

golf_clubs.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-pp5-teetime.herokuapp.com/bookings/golf_clubs) 
- No Errors Found


| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A |  


### Golf Club Details  

club_expanded.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-pp5-teetime.herokuapp.com/bookings/druids-vale/) 
- No Errors Found


| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A |  


### My Teetimes  

<details><summary>Booking List</summary>

![booking list](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/html/validation-html-booking-list.PNG)
</details>

- No Errors Found

| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A |  


### Edit Booking

<details><summary>edit_booking.html</summary>

![booking list](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/html/validation-html-edit-booking.PNG)
</details>

- No Errors Found

| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A |  


### Cancel Booking

<details><summary>cancel_booking.html</summary>

![booking list](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/html/validation-html-cancel-booking.PNG)
</details>

- No Errors Found

| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A |  


### Shop  

product_list.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-pp5-teetime.herokuapp.com/products/) 
- No Errors Found


| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A |  


### Product Detail  

product_detail.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-pp5-teetime.herokuapp.com/products/15/) 
- No Errors Found


| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A |  


### Add Product

<details><summary>add_product.html</summary>

![add product](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/html/validation-html-add-product.PNG)
</details>

- No Errors Found

| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A | 


### Edit Product

<details><summary>edit_product.html</summary>

![edit product](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/html/validation-html-edit-product.PNG)
</details>

- No Errors Found
1 Info detected

| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A | 
| Info | Edit Product | Trailing slash on void elements has no effect and interacts badly with unquoted attribute values. | Noted| 


### Basket  

basket.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-pp5-teetime.herokuapp.com/basket/) 
- No Errors Found


| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A |  


### Checkout  

checkout.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-pp5-teetime.herokuapp.com/checkout/) 
- No Errors Found


| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A |  


### Checkout Success  

<details><summary>checkout_success.html</summary>

![checkout success](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/html/validation-html-checkout-success.PNG)
</details>

- No Errors Found

| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A | 


### Profile  

<details><summary>profile.html</summary>

![profile](https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/html/validation-html-profile.PNG)
</details>

- No Errors Found

| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A | 


### Blog  

blog.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-pp5-teetime.herokuapp.com/blog/) 
- No Errors Found


| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A |  


### Blog Expand 

blog_expand.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-pp5-teetime.herokuapp.com/golf-etiquette/) - 405 Errors Found (Summernote Editor)


| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | Blog Expand | CSS / Parse Error | These errors are caused by the Summernote editor and not by code written by the developer of this project. Time constraints did not allow me to resolve these issues at the present time |
| Warning | N/A | N/A | N/A |  


### Contact 

contact.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-pp5-teetime.herokuapp.com/contact/) 
- No Errors Found


| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A |  


### Sign In 

login.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-pp5-teetime.herokuapp.com/accounts/login/) 
- No Errors Found


| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A |  


### Sign Out  

logout.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-pp5-teetime.herokuapp.com/accounts/logout/) 
- No Errors Found  


| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A | 


### Register  

signup.html [results](https://validator.w3.org/nu/?doc=https%3A%2F%2Fci-pp5-teetime.herokuapp.com/accounts/signup/) 
- No Errors Found


| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A |  


### 404  

404.html [results](https://validator.w3.org/nu/?checkerrorpages=yes&useragent=Validator.nu%2FLV+http%3A%2F%2Fvalidator.w3.org%2Fservices&acceptlanguage=&doc=https%3A%2F%2Fci-pp5-teetime.herokuapp.com%2Faccounts%2F404%2F) 
- No Errors Found


| **Level** | **Feature** | **Issue Description** | **Comment** |
|-------------|-------------|----------------------|-------------|
| Error | N/A | N/A | N/A |
| Warning | N/A | N/A | N/A |  

##### Back to [top](#table-of-contents)<hr>  


### CSS Validation
The W3C Jigsaw CSS Validation Service was used to validate the CSS of the website.

<details><summary>base.css</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/css/validation-base-css.PNG">
</details> 

<details><summary>profile.css</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/css/validation-base-css.PNG">
</details>  

<details><summary>checkout.css</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/css/validation-checkout-css.PNG">
</details><hr>

### JavaScript Validation
JSHint javaScript Validation Service was used to validate all javaScript files.

<details><summary>stripe_elements.js</summary>  
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/js/validation-js-stripe-elements.PNG">
</details>  

- one undefined variable Stripe which originates from a external script

<details><summary>checkout.js</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/js/validation-js-checkout.PNG">
</details>  

- one undefined variable Stripe which originates from a external script

<details><summary>country_field.js</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/js/validation-js-country-field.PNG">
</details>

- No issues raised  

##### Back to [top](#table-of-contents)<hr>  

## PEP8 Validation
[CI Python Linter](https://pep8ci.herokuapp.com/) was used to check the code for PEP8 requirements.


<summary>Basket</summary>

<details><summary>contexts.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-basket-contexts.PNG">
</details>

<details><summary>basket_tools.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-basket-tools.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-basket-views.PNG">
</details>

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-basket-test-views.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-basket-urls.PNG">
</details>

<hr><summary>Blog</summary>

<details><summary>Admin.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-blog-admin.PNG">
</details>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-blog-forms.PNG">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-blog-models.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-blog-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-blog-views.PNG">
</details>

<hr><summary>Bookings</summary>

<details><summary>Admin.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-bookings-admin.PNG">
</details>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-bookings-forms.PNG">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-bookings-models.PNG">
</details>

<details><summary>test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-bookings-test-models.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-bookings-urls.PNG">
</details>

<details><summary>test_urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-bookings-test-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-bookings-views.PNG">
</details>

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-bookings-test-views.PNG">
</details>

<hr><summary>checkout</summary>

<details><summary>Admin.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-admin.PNG">
</details>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-forms.PNG">
</details>  

<details><summary>test-forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-test-forms.PNG">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-models.PNG">
</details>

<details><summary>test-models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-test-models.PNG">
</details>

<details><summary>signals.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-signals.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-views.PNG">
</details>  

<details><summary>test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-test-views.PNG">
</details>  

<details><summary>webhook_handler.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-webhook-handler.PNG">
</details>  

<details><summary>webhook.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-checkout-webhooks.PNG">
</details>  

<hr><summary>contact</summary>

<details><summary>Admin.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-contact-admin.PNG">
</details>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-contact-forms.PNG">
</details>

<details><summary>test-forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-contact-test-forms.PNG">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-contact-models.PNG">
</details>

<details><summary>test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-contact-test-models.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-contact-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-contact-views.PNG">
</details>

<hr><summary>home</summary>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-home-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-home-views.PNG">
</details>

<hr><summary>products</summary>

<details><summary>Admin.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-products-admin.PNG">
</details>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-products-admin.PNG">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-products-models.PNG">
</details>

<details><summary>test-models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-products-test-models.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-products-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-products-views.PNG">
</details>  

<details><summary>test-views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-products-test-views.PNG">
</details>  

<details><summary>widgets.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-products-widgets.PNG">
</details>

<hr><summary>profiles</summary>

<details><summary>forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-profiles-forms.PNG">
</details>

<details><summary>models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-profiles-models.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-profiles-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-profiles-views.PNG">
</details>  

<hr><summary>teetime</summary>

<details><summary>asgi.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-teetime-asgi.PNG">
</details>

<details><summary>settings.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-teetime-settings.PNG">
</details>

<details><summary>urls.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-teetime-urls.PNG">
</details>

<details><summary>views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-teetime-views.PNG">
</details>  

<details><summary>wsgi.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-teetime-wsgi.PNG">
</details>

<hr><summary>root</summary>

<details><summary>custom_storages.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/py/validation-root-custom-storages.PNG">
</details>  

##### Back to [top](#table-of-contents)<hr>  

## Accessibility  
The [WAVE WebAIM web accessibility evaluation tool](https://wave.webaim.org/ was used to ensure the website met high accessibility standards.  
- All pages returned 0 errors.  
- All alerts presented were for redundant links whichweres taken into account duringdevelopmentt.

<details><summary>Home</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-home.PNG">
</details>  

<details><summary>Golf Clubs</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-golf-clubs.PNG">
</details>  

<details><summary>Club Expand</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-club-expand.PNG">
</details>  

<details><summary>Booking List</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-booking-list.PNG">
</details>  

<details><summary>Edit Booking</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-edit-booking.PNG">
</details>  

<details><summary>Cancel Booking</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-cancel-booking.PNG">
</details>  

<details><summary>Product List</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-product-list.PNG">
</details>  

<details><summary>Product Expand</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-product-expand.PNG">
</details>  

<details><summary>Add Product</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-add-product.PNG">
</details>  

<details><summary>Edit Product</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-edit-product.PNG">
</details>  

<details><summary>Basket</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-basket.PNG">
</details>  

<details><summary>Checkout</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-checkout.PNG">
</details>  

<details><summary>Checkout Success</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-checkout-success.PNG">
</details>  

<details><summary>Blog</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-blog.PNG">
</details>  

<details><summary>Blog Expand</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-blog-expand.PNG">
</details>  

<details><summary>Contact</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-contact.PNG">
</details>  

<details><summary>Profile</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-profile.PNG">
</details>  

<details><summary>Sign Up</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-sign-up.PNG">
</details>  

<details><summary>Sign In</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-sign-in.PNG">
</details>  

<details><summary>Sign Out</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-log-out.PNG">
</details>  

<details><summary>404</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/accessibility/accessibility-wave-404.PNG">
</details>  

##### Back to [top](#table-of-contents)<hr>  

## Lighthouse

Performance, best practices and SEO was tested using Lighthouse.

#### Desktop
<details><summary>Home</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-home.PNG">
</details>

<details><summary>Sign Up</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-sign-up.PNG">
</details>

<details><summary>Sign In</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-login.PNG">
</details>

<details><summary>Sign Out</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-logout.PNG">
</details>

<details><summary>Golf Clubs</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-golf-clubs.PNG">
</details>

<details><summary>Club Expand</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-club-expand.PNG">
</details>

<details><summary>Booking List</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-booking-list.PNG">
</details>

<details><summary>Edit Booking</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-edit-booking.PNG">
</details>

<details><summary>Cancel Booking</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-cancel-booking.PNG">
</details>

<details><summary>Product List</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-product-list.PNG">
</details>

<details><summary>Product Expand</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-product-expand.PNG">
</details>  

<details><summary>Add Product</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-add-product.PNG">
</details>  

<details><summary>Edit Product</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-edit-product.PNG">
</details>  

<details><summary>Basket</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-basket.PNG">
</details>  

<details><summary>Checkout</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-checkout.PNG">
</details>  

<details><summary>Checkout Success</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-checkout-success.PNG">
</details>  

<details><summary>Blog</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-blog.PNG">
</details>  

<details><summary>Blog Expand</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-blog-expand.PNG">
</details>  

<details><summary>Contact</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-contact.PNG">
</details>  

<details><summary>Profile</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/validation/lighthouse/lighthouse-desktop-profile.PNG">
</details>  

##### Back to [top](#table-of-contents)<hr>


## Testing

1. Manual testing User Stories
2. Automated testing

### Manual testing

1.	As A/AN Shopper / Site User	I CAN register for an account	SO THAT I CAN have an account and view my profile  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Sign Up | Click pofile button and select register, user is brought to the sign up page| User is brought to the sign up page | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-01a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-01b.PNG">
</details>  

2.	As A/AN Shopper / Site User	I CAN login and logout SO THAT I CAN have an account with my information stored for fast usage  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Sign In | Click pofile button and select login, user is brought to the sign in page | User is brought to the sign in page | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-01a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-02-b.PNG">
</details>  

3.	As A/AN Shopper / Site User	I CAN recover my password	SO THAT I CAN set a new password if I forgot it  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Reset Password | Click pofile button and select login, user is brought to the sign in page, click forgot password to go to password reset page | User is brought to password reset page | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-01a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-02-b.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-03b.PNG">
</details>  

4.	As A/AN Shopper / Site User	I CAN receive an email confirmation after registration	SO THAT I CAN be notified registration was successful  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Registration | Upon registration an email is sent to verify the email address submitted | Registration email arrives into inbox of the email address used to sign up | Works as expected  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-04b.PNG">
</details>  

5.	As A/AN Shopper / Site User	I CAN have a profile SO THAT I CAN store my information for faster checkouts in the future  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Profile | From the Nav click the profile icon, select profile from dropdown and be broought to the profile page where user information is stored | Be brought to profile page | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-05.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-05b.PNG">
</details>  

6.	As A/AN Shopper / Site User	I CAN navigate across the site 	SO THAT I CAN can access all parts of the site  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Navbar | Click on any link in the navbar to be brought to a relevant page, shop for example | Be brought to shop to view all products after clicking all products in the navbar | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-06.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-02-b.PNG">
</details>  

7.	As A/AN Shopper / Site User	I CAN use a navbar, footer, and social icons  SO THAT I CAN navigate the site, access menus, and access socials  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Navbar/Footer | Scoll to footer, click on the Instagram logo | A new tab will open and bring user to the Teetime Instagram page | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-07.PNG">
</details>  

8.	As A/AN Shopper / Site User	I CAN be notified of my actions	SO THAT I CAN be aware the action was completed successfully or not  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Alert Box | Add an item from the shop to the basket | A message will appear in the alert box on screen to notify the user of this action | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-08a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-08b.PNG">
</details>  

9.	As A/AN Shopper / Site User	I CAN see my login status	SO THAT I CAN know if I am logged in or not  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Navigation | While logged out the profile icon in the navbar will be gray, log in it will change to a green color | Once logged in the profile icon will be green | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-06.PNG">
</details>  

10.	As A/AN Shopper / Site User	I CAN visit the shop SO THAT I CAN view all products available  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Shop | Click shop in the navbar, select all products | User is then brought to the all products page of the shop | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-06.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-10.PNG">
</details>  

11.	As A/AN Shopper / Site User	I CAN view my basket and total cost at any time	so I am aware of what I am buying and it's cost  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Basket | Click the basket icon in the navbar | User is brought to the basket page where all products in basket are displayed along with their price and total cost | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-11a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-11b.PNG">
</details>  

12.	As A/AN Shopper / Site User	I CAN view a list of products	SO THAT I CAN select a product to purchase  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Categories | Select a category on the side panel, select Gents Polos     |     User is brought to the selected category of product and all products are listed | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-12.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-12b.PNG">
</details>  

13.	As A/AN Shopper / Site User	I CAN view an individual product details SO THAT I CAN view a more detailed view of the product  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Product Detail | Click on any item image in the shop, or the view button     |  User is borught to the product detail page where product details are displayed | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-13.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-13b.PNG">
</details>  

14.	As A/AN Shopper / Site User	I CAN view a list of golf courses	SO THAT I CAN select a golf course I want to play on  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Golf Clubs |  From the navbar click Clubs | User is brought to the Golf Clubs List page | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-06.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-14b.PNG">
</details>  

15.	As A/AN Shopper / Site User	I CAN view individual golf course details	SO THAT I CAN see more detailed information about it  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Golf Club Details | From the Golf Clubs List page select a club and click the view golf club button | User is brought to the details page for the selected golf club | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-15.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-15b.PNG">
</details>  

16.	As A/AN Shopper / Site User	I CAN view a list of tee times available for each golf course	SO THAT I CAN select a date and time to play  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Book a Tee Time | From golf club details page find the book a teetime form on the page, select a club, date and time | User is then brought to a confirmation page | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-16.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-16b.PNG">
</details>  

17.	As A/AN Shopper / Site User	I CAN search for a product by name or description	SO THAT I CAN find a certain product 
 
| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Search | Search box in the navigation bar, input keyword to search such as "blue", click search | All items with the relevant keyword will be displayed | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-17a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-17b.PNG">
</details>  

18.	As A/AN Shopper / Site User	I CAN see my search results	SO THAT I CAN only see what I am searching for  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Search | Input a keyword into the search box in the navbar and click search | All items matching the search critearia are only displayed | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-18a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-18b.PNG">
</details>  

19.	As A/AN Shopper / Site User	I CAN sort by category SO THAT I CAN select products of a certain category  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Sort | From the shop page, click a category on the side panel such as headwear | User is brought to the headwear page where only products classed as headwear are displayed | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-19a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-19b.PNG">
</details>  

20.	As A/AN Shopper / Site User	I CAN sort by price low to high and high to low	SO THAT I CAN view products according to my budget 
 
| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Sort | From the shop page, click the sort box and select price from high to low | All items will be sorted from the highest price to the lowest price | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-20.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-20b.PNG">
</details>  

21.	As A/AN Shopper / Site User	I CAN select only available dates/times	SO THAT I CAN I can only purchase available tee slots  

- The format used was unique together which checks that the selected date, time and club booking is unique, if the user selects a date, time and club already booked they will get a message asking them to select another time/date. Ideally I plan to remove the unavailable times from the dropdown to avoid the user clicking and going through the process to be told to select another time/date. Time constraints was the main isssue.

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Book a tee time | From golf club detail page, select a date and time for selected club | If time is available a confirmation page will appear, if the time is already booked an error message will appear asking the user to select another time. | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-21.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-21b.PNG">
</details>  

22.	As A/AN Shopper / Site User	I CAN use a card as the payment method SO THAT I CAN complete my purchase  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Checkout | From the basket select secure checkout | Input user information, input card number 4242 4242 4242 4242 04/24 424 24242, payment is successful | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-22.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-22b.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-22c.PNG">
</details>  

23.	As A/AN Shopper / Site User	I CAN select the size and quantity of a product	SO THAT I CAN select a size and quantity to my needs  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Product Details | From Product details page select a size for the product in the size box, increase or decrease quantity from the quantity box | Sizes will be selected and quantity adjusted | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-23.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-23b.PNG">
</details>  

24.	As A/AN Shopper / Site User	I CAN view items in my basket	SO THAT I CAN be aware of what I am buying and it's cost  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Basket | Click the basket icon in the navbar | The basket page will appear and display all items in the basket and their cost alongside total price for all items | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-24a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-24b.PNG">
</details>  

25.	As A/AN Shopper / Site User	I CAN adjust item quantity in my basket	SO THAT I CAN increase or reduce item count according to my needs  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Basket | From the basket press the increase/ decrease button to desired number, click update | The basket will update with the desired quantity | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-24b.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-25b.PNG">
</details>  

26.	As A/AN Shopper / Site User	I CAN receive order confirmation SO THAT I CAN be notified of a successful order  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Alert Box | Upon a successful checkout an alert box will be visible to the user | Alert box pops up with the order details | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-25b.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-26.PNG">
</details>  

27.	As A/AN Shopper / Site User	I CAN receive email confirmation SO THAT I CAN have a record of my purchased28	Store Owner / Admin	add a product	add new products to the shop  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Email Confirmation | Upon a successful checkout a confirmation email will be sent to the provided email address which contains the details of the order |     Email confirmation arrives into inbox | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-27.PNG">
</details>  

28.	As A/AN Store Owner / Admin	I CAN add a product SO THAT I CAN add new products to the shop  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Add Product | From the navbar select the profile button as an admin logged in, click add product from the dropdown | The add product page will appear allowing the addition of a new product via the add product form | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-28a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-28b.PNG">
</details>  

29.	As A/AN Store Owner / Admin	I CAN edit a product SO THAT I CAN edit existing products in the shop  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Edit Product | From product detail as an admin account, find a edit button on the page, click edit | Admin is brought to the edit product page where they can adjust any part of the product | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-29a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-29b.PNG">
</details>  

30.	As A/AN Store Owner / Admin	I CAN delete a product SO THAT I CAN delete existing products from the shop  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Delete Product  | From product detail as an admin account, find a delete button on the page, click delete | A modal pops up and asks the admin to confirm they wish to delete the product | Works as expected |  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-29a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-30b.PNG">
</details>  

31.	As A/AN Store Owner / Admin	I CAN add a golf club	SO THAT I CAN add a golf club to the site  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Golf Clubs | In the url address go to https://ci-pp5-teetime.herokuapp.com/admin/, log in as admin and select clubs in the side panel to the left, the clubs screen will appear and then click add club button on the top right of the screen. Add club page will appear | Add club page will appear and the user can then add information for a new golf club | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-admin-login.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-31.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-31b.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-31c.PNG">
</details>  

32.	As A/AN Store Owner / Admin	I CAN edit a golf club SO THAT I CAN edit an existing golf club on the site  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Golf Clubs | In the url address go to https://ci-pp5-teetime.herokuapp.com/admin/, log in as admin and select clubs in the side panel to the left, the clubs screen will appear and then click a club that you desire to edit. The club page will appear allowing the user to edit information | The club page will appear and the user can then edit information for the golf club             | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-admin-login.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-31.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-31b.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-32b.PNG">
</details>  

33.	As A/AN Store Owner / Admin	I CAN delete a golf club SO THAT I CAN delete existing golf club from the site  

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Golf Clubs | In the url address go to https://ci-pp5-teetime.herokuapp.com/admin/, log in as admin and select clubs in the side panel to the left, the clubs screen will appear, select the club using the checkbox and cick the action dropdown above, choose delete selected clubs and press go | The club will be deleted | Works as expected  

<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-admin-login.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-31.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/manual-testing/user-story-33b.PNG">
</details>  

34.	As A/AN Store Owner / Admin	I CAN add a tee time SO THAT I CAN add a tee time to a golf club  
- Time constraints did not allow this to happen, the path chosen was to preload the standard tee times for golf clubs to cover all times during the year.

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Future Feature | N/A | N/A |

35.	As A/AN Store Owner / Admin	I CAN edit a tee time	SO THAT I CAN edit an existing tea time on a golf club 
- Time constraints did not allow this to happen, the path chosen was to preload the standard tee times for golf clubs to cover all times during the year. 

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Future Feature | N/A | N/A |

36.	As A/AN Store Owner / Admin	I CAN delete a tee time	SO THAT I CAN delete a tee time from a golf club  
- Time constraints did not allow this to happen, the path chosen was to preload the standard tee times for golf clubs to cover all times during the year.

| Feature | Action | Expected Result | Actual Result |
| ------- | ------ | --------------- | ------------- |
| Future Feature | N/A | N/A |


### Automated testing

- Testing was done using the built in Django module, unittest.
- Coverage was also usesd to generate a report


<details><summary> Basket, test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-basket-test-views.PNG">
</details>

<details><summary> Bookings, test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-bookings-test-views.PNG">
</details>

<details><summary> Bookings, test-models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-bookings-test-models.PNG">
</details>

<details><summary> Bookings, Test-urls</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-bookings-test-urls.PNG">
</details>  
<details><summary> Checkout, test-forms.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-checkout-test-forms.PNG">
</details>

<details><summary> Checkout, test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-checkout-test-models.PNG">
</details>

<details><summary> Checkout, test_views.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-checkout-test-views.PNG">
</details>

<details><summary> contact, forms</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-contact-test-forms.PNG">
</details>  
<details><summary> Contact, test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-contact-test-models.PNG">
</details>

<details><summary> Contact, test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-contact-test-models.PNG">
</details>

<details><summary> Products, test_models.py</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-products-test-models.PNG">
</details>

<details><summary> Products, test-views</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-products-test-views.PNG">
</details>  

### Coverage  
A Python test plugin called coverage was used to generate the following results and display how much of the code was covered by the unittest module.

<details><summary> Coverage</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-coverage-01.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/auto-tests/auto-test-coverage-02.PNG">
</details>


### Device Testing & Browser compatibility

The site uses to test on various real world devices was [BrowserStack](https://www.browserstack.com/)  

This allowed me to test on real devices and not just device emulators.

The following devices were used to test my site:

<details><summary>Apple iPhone 12</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/browsertack/browserstack-iphone-12.PNG">
</details>

<details><summary>Samsung Galaxy S21</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/browsertack/browserstack-galaxy-s21.PNG">
</details>

<details><summary>Mozilla Firefox (v105 latest)</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/browsertack/browserstack-firefox.PNG">
</details>

<details><summary>Google Chrome (v106 latest)</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/browsertack/browserstack-chrome.PNG">
</details>

<details><summary>Safari (Monteray v15.3 latest)</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/browsertack/browserstack-safari.PNG">
</details>

<details><summary>Microsoft Edge</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/browsertack/browserstack-edge.PNG">
</details>


##### Back to [top](#table-of-contents)<hr>


## Bugs

| **Bug** | **Fix** |
| ------- | ------- |
| Bookings made for same club, date and time | UniqueTogether was used to ensure no double bookings could be made |
| Increment and decrement product queantity in basket not working | Increment and decrement buttons being linked to jQuery script solved this |
| Webhooks not working | Endpoint was not fully configured, adding the correct settings resolved this |
| Payment intent not being created | Both local and deployed endpoints had incorrect initial settings which was corrected and allowed the payment intent to succeed |



##### Back to [top](#table-of-contents)<hr>

## Deployment  
### AWS S3 Bucket Setup  

To set up an AWS S3 bucket:

1. Sign in to the AWS Management Console and open the Amazon S3 console.  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-01a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-01b.PNG">
</details>

2. Click on the "Create Bucket" button.  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-02.PNG">
</details>

3. Enter a unique name for your bucket, and select the region where you want the bucket to be located.
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-03a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-03b.PNG">
</details>

4. Configure any additional options, such as versioning, object-level logging, and object tagging, as needed.  

5. Click on the "Create" button to create the bucket.

6. Set up the appropriate permissions for the bucket, such as access control lists (ACLs) and bucket policies, to control who can access the data in the bucket.  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-06a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-06b.PNG">
</details>

7. Upload files to the bucket using the AWS S3 console, the AWS S3 CLI, or the AWS S3 SDK.  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-07a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-07b.PNG">
</details>

8. Access your files through the AWS S3 Console, AWS S3 CLI, or the AWS S3 SDK.  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/aws/aws-setup-08.PNG">
</details>  

### Stripe Endpoint

1. Register for a Stripe account at stripe.com
2. Log into your Stripe account and navigate to the Developers section  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-02a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-02b.PNG">
</details>  

3. In the Developers section, locate the API keys section and take note of the publishable and secret keys  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-03a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-03b.PNG">
</details> 

4. Create environment variables in your local environment and on Heroku, such as STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY, with the values of the publishable and secret keys  

5. Return to the Developers section of your Stripe account and click on the Webhooks tab  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-05a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-05b.PNG">
</details> 

6. Create a webhook with the URL of your website, such as https://example.com/checkout/wh/  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-06a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-06b.PNG">
</details> 

7. Choose the events you want to receive, such as payment_intent.payment_failed and payment_intent.succeeded  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-07a.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-07b.PNG">
</details> 

8. Take note of the key generated for this webhook  

9. Create an environment variable, such as STRIPE_WH_SECRET, with the value of the webhook secret key on your local environment and Heroku  

10. Test the webhook to ensure it is working properly and troubleshoot any issues that may arise.  
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP5_tee_time/main/docs/stripe/stripe-setup-10.PNG">
</details> 

### Heroku  

[Official Page](https://devcenter.heroku.com/articles/git) (Ctrl + click)

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at heroku.com
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-01.PNG">
</details>

2. Create an app, give it a name for such as ci-pp4-the-diplomat, and select a region
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-02.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-03.PNG">
</details>

3. Under resources search for postgres, and add a Postgres database to the app
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-04.PNG">
</details>

Heroku Postgres

1. Note the DATABASE_URL, this can be set as an environment variable in Heroku and your local deployment(env.py)
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-18.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-17.PNG">
</details>

2. Install the plugins dj-database-url and psycopg2-binary.

3. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-05.PNG">
</details>

4. Create a Procfile with the text: web: gunicorn the_diplomat.wsgi
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-06.PNG">
</details>

5. In the settings.py ensure the connection is to the Heroku postgres database, no indentation if you are not using a seperate test database.
I store mine in env.py
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-07.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-08.PNG">
</details>

6. Ensure debug is set to false in the settings.py file
<details><summary>See Images</summary>
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
<details><summary>See Images</summary>
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-19.PNG">
<img src="https://raw.githubusercontent.com/ArronBeale/CI_PP4_the_diplomat/main/docs/heroku/heroku-deployment-10.PNG">
</details>


15. Ensure the following environment variables are set in Heroku
<details><summary>See Images</summary>
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

### Code  
- Code Institute for the bag and checkout app as a basis for my checkout and basket apps
- Code Institute Slack community for guidance on many of my bug fixes.

### Media
[Pexels](https://www.pexels.com/)

##### Back to [top](#table-of-contents)<hr>

## Acknowledgements

### Special thanks to the following:
- My Mentor Mo Shami for his excellent guidance and valuable advice  
- Code Institute Slack Community
- Code Institute Tutor Support