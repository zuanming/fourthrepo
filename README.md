# FSDev
<img src="https://res.cloudinary.com/dhktrng6p/image/upload/v1598206818/main-logo_fnpxiv.gif" alt="logo" width="300px">

### Full Stack Frameworks with Django Project (Code Institute)

This project is built as a webpage for aspiring developers to purchases digital courses online to learn and also to build a community of developers.

***

## Objective

As the world turns more towards digital products and services, processes are getting automated, and documents are being kept digitally. The demand for digital products and services is on the rise, and many jobs are being replaced by automation. As a result, we need to pick up new skills and keep up with the digital era.<br><br>
This website aims to achieve this objective by offering digital courses on software development by serving two purposes:
1. To allow users to purchase digital courses taught by established tutors
2. To build a community where users can help out each other and ask or answer questions in a forum.

### External user’s goal:
* To gain knowledge in software development through purchased digital content from the website
* To seek help in the forum if they face any difficulties in their learning or with any personal projects they may require assistance with
* To help other users by providing solutions to other users who are facing difficulties

### Site owner’s goal:
* To build a mobile responsive site to provide a means for users to learn and upgrade themselves with digital skills
* To build a supportive community for developers from all over
* To profit from the sales of digital content and expand the provision of products and services in the future

***

## Objective-based design

<img src="/static/images/readme/mockup.png" alt="Devices Mockup">

## UX
The UX is designed to deliver the website objective as directly and quickly as possible by providing minimal steps for users to access the desired information required, with a clean and uncluttered web interface.
The website is divided into 4 sections - **Courses**, **Tutors**, **Forum** and **Cart** - and is designed to allow access to different functions to the 3 different groups of people - **Administrators**, **Authenticated Users** and **Non-Authenticated Users**- based on the desired objective for each group.
* Each section is easily accessible via a permanent navigation bar at the top of the page that will collapse into a dropdown menu on mobile screens.
* Pages are kept as short as possible so that users do not have to scroll through an unnecessarily long page of content.
* Each page is made mobile responsive for devices with smaller screens.

#### Wireframe:
<img src="/static/images/readme/wireframe.png" width="600px" height="auto" alt="Devices Mockup">

### Home Page
<img src="/static/images/readme/home-page.png" width="600px" height="auto" alt="Home Page">

### Courses
This page displays the different courses grouped by the type of development, Frontend/Backend/Databases. 
Each course also has its own separate details page with a reviews section with reviews and comments on the reviews.<br>

**Non-Authenticated Users** can view the courses and course details pages. However, they are unable to add items to cart without an account - they will be directed to the signup page.
They are also unable to write reviews or comment on reviews.<br>

**Authenticated** users are able to add the courses to cart either from the courses page or the course details page, and will be able to write reviews or comment if they have a purchase record of the course.<br>

**Administrators** are able to access the edit and delete function for the courses on both courses and course details pages to edit the courses provided. They can also add courses from the courses page if they wish to provide more content for sale. They are however unable to add items to cart.

<p>
  <img src="/static/images/readme/cart.jpeg" width="auto" height="300px" alt="course - wireframe">
  <img src="/static/images/readme/course-user.png" width="auto" height="300px" alt="course - user view">
  <img src="/static/images/readme/course-admin.png" width="auto" height="300px" alt="course - admin view">
</p>

### Tutors
This page displays the different tutors and similarly to courses, users can access the details page for each tutor.<br>

**Non-Authenticated** & **Authenticated Users** are able to access only the content.<br>

**Administrators** have similar privileges as in the courses page; they can add tutors, edit or delete them.

### Cart
This page is for users to view what courses they are intending to purchase and check out their items for payment. The "add to cart" button will automatically update its text and be disabled according to event i.e. "In cart" and "purchased" respectively.<br>

<img src="/static/images/readme/navbar.jpeg"  width="auto" height="250px" alt="course - user view">

**Non-Authenticated Users** & **Administrators** will not be able to access this page.<br>
- Non-Authenticated User<br><img src="/static/images/readme/cart-nonauth.png"  width="auto" height="48px"alt="course - normal view"><br>
- Admin User<br><img src="/static/images/readme/cart-admin.png" width="auto" height="45px"alt="course - admin view"><br>

**Authenticated Users** will be able to access this page.
- Authenticated User<br><img src="/static/images/readme/cart-user.png" width="auto" height="50px" alt="course - user view"><br>

### Forum
This page is for users to ask and answer questions, and a search function is provided for users to search for the question title or for questions in each course category. 
Answers for each question are also available.

**Administrators** and **Authenticated Users** will be able to create, edit and delete only the questions or answers that they have posted. They are only able to view the questions and answers posted by other users. 
- Admin User & Authenticated User<br><img src="/static/images/readme/forum-auth.png" width="400px" height="auto" alt="course - admin view"><br>

**Non-Authenticated Users** will only be able to view and search for questions.
- Non-Authenticated User<br><img src="/static/images/readme/forum-nonauth.png" width="400px" height="auto" alt="course - nonauth view"><br>

In summary, **non-authenticated users** are limited to viewing content, whereas **authenticated users** are able to make purchases, write reviews and post questions or answers. 
**Administrators** have the privilege to add, edit and delete the courses and tutors information as the site owner/administrator.

***

## UI
The UI is designed with simplicity in mind. The site-wide color scheme used is a dark background with bright colored buttons as calls to action to mimic a code writing application such as Gitpod and Visual Studio Code.
The font selected for this site is 'Roboto Mono' google font as it represents the monospace font used in development platforms.
This was done to relate to software developing platform and give a feeling of familiarity to developers.

### Features
The website also has the following features:

### Courses and Tutors
* The courses page is displayed with multi-carousels showing the course title, a logo image and its price for users to scroll through, separated into the types of development platforms.
    * The multi-item carousel reduces in items shown on smaller screens.
* This is done to prevent the cluttering of information, by showing only critical details on the main pages and additional details in their detail pages.
* Users can access the details page by either clicking on the "Profile" or "View Details" buttons for Tutors and Courses respectively or by clicking on the profile image or logo image.
* Within each details page, the related tutors or courses are displayed in small cards and are hyperlinked to their respective details page for users to quickly navigate between pages for information.<br>
* Buttons are designed with bootstrap colors and are consistent site0wide for users to identify easily:
    * Turquoise is for submission of create/update forms
    * Blue is for the main call to action and adding of courses/tutors/questions/reviews
    * Red is for deletion 
    * Grey is for the cancellations and review comments
* Flash messages feature is implemented to alert users that their actions have been registered and completed by the application.

### Future Features
Due to the limitations of time, features were added based on priority versus estimated time required to implement, remaining features will be added in the future.

- All forms for CRUD to be changed to Modal, form update to be processed via AJAX for data retrieval
- Forum to add checkbox for user to select which posted answer was the most relevant and useful. Upon indicating the best answer, the question will be marked and indicated as 'Answered'.
- Posted reviews, questions and answers to indicate "edited on -datetime-" after an edit has been made
    - To also indicate a "Deleted by -user/administrator-" for deleted items instead of removing from database completely

***

## Technologies Used
The following programming languages and tools were used to build the website:

- HTML 5
- CSS
- JavaScript
- Bootstrap v4.4
- jQuery library for DOM manipulation
- Python
- Django framework
- Heroku for Deployment
- PostgreSQL database
- Gitpod and Visual Studio Codefor the writing of codes and testing of website
- W3C Markup Validation Service for HTML and CSS validation
- GitHub for repository hosting

### Database
The deployed web application uses SQL database to store its data.
- The entities are all inter-related, hence a relational database was required
- SQL was selected instead of MongoDb which stores data in JSON format

Entity Relationship Diagram:<br>
<img src="/static/images/readme/erd.png" width="800px" height="auto" alt="ERD">
    
***

## Testing

The website has been tested for viewing and responsiveness on various screen sizes, including but not limited to the following web browsers and devices:

- Apple Safari Web Browser
  1. macOS
  2. Windows 10
  3. iOS
  4. iPadOS
- Mozilla Firefox Web Browser
  1. macOS
  2. Windows 10
  3. Android 10
- Microsoft Edge (Chromium) Web Browser
  1. macOS
  2. Windows 10
  3. Android 10
- Google Chrome Web Browser
  1. macOS
  2. Windows 10
  3. Android 10

* HTML, CSS validated by W3C Markup Validation

1. Testing was first done by applying CRUD to Courses and Tutors entities using the Django Admin and SQLite database during the construction of the project. This was to ensure the django models were created properly according to the ERD.
2. Upon successful deployment onto Heroku, the database was replaced with PostgreSQL.
3. CRUD for the courses entity was once again tested on the deployed web interface and new database using the administrator account and checked if they Wireframe displayed correctly. Tutors entities were subsequently added and related to courses. 
4. The deployed webpage is then provided to random testers to test out the user authentication interfaces and functions (sign up and login).
5. Following this, the testers are directed to try making purchases to test the checkout process.
6. This process is tried on different web browsers and devices to ensure the process is consistent.
7. UI/UX feedback was taken into consideration and changes were made as required, such as color palettes and browsing interfaces 
    - e.g. horizontal scroll flex display of courses was changed to multi-item carousel after test user feedback
8. As the website is near completion, the webpages are passed through W3C validators to ensure the code is clean.
9. The edited final web application is then updated onto the host server

***

## Deployment

The website is deployed on Heroku, using GitHub to host the project repository. The website can be found at this [link](http://programming-course-project.herokuapp.com).<br>
The deployment process is as such:
1. Code was written on gitpod using Code Institute's template. Heroku was installed in gitpod and setup using an existing account.
2. An application was created on heroku using an unique name and environment variables such as passwords and session keys were added to the application settings.
3. Database was switched over to PostgreSQL as Heroku did not support SQLite.
4. Content was populated again using interface as part of application testing.
5. Deployed website was provided to testers for testing purposes, afterwhich adjustments were made.
6. Code was pushed onto Heroku again after changes were done, and final testing was conducted to check the UI/UX elements and processes.
7. Final adjustments were made and pushed onto Heroku for submission.

For submission purposes to Code Institute:
1. Administrator account
    - Username = staffuser1
    - Password = commonpassword123
2. Authenticated User account
    - Username = testuser1
    - Password = commonpassword123


***

## Credits
This website was built using tools and data from various sources, including but not limited to the following:

- [Heroku](https://www.heroku.com) for the hosting of the web application.

- [Unsplash](https://unsplash.com/) for the images on the cover page.
- [Canva](https://material.io/design/color/dark-theme.html#ui-application) for the logo design
- [jQuery script.net](https://www.jqueryscript.net/slider/responsive-bootstrap-carousel-multiple-items.html) for the multi-item responsive carousel sample
- [favicon.io](https://favicon.io/favicon-converter) for the favicon generator 
- [Wikimedia](https://commons.wikimedia.org/wiki/Main_Page) for the development platform logos
- **Last but not least, to [Trent Global](https://www.trentglobal.edu.sg/diplomainsoftwaredevelopment/?gclid=EAIaIQobChMI8M3ezf6t6QIV2BwrCh2R6A44EAAYASAAEgL6__D_BwE) and [Code Institute](https://codeinstitute.net) for the teachings and support to have made this project possible.**
