# FSDev

### Data Centric Development Project (Code Institute)

This project is built as a webpage for aspiring developers to purchases digital courses online to learn and also to build a community of developers.
***
## Objective

As the world turns more towards digital products and services, processes are getting automated and documents are being kept digitally. 
The demand for digital products and services is on the rise and many jobs are being replaced by automation. 
As a result, we need to pick up new skills and keep up with the digital era.<br><br>This website aimes to achienve this objective by offering digital courses on software development by serving two purposes:
1. To allow users to purchase digital courses taught by established tutors
2. To build a community where users can help out each other and ask or answer questions in a forum. 

#### External user’s goal:
* To gain knowledge in software development through purchased digital content from the website
* To seek help in the forum if they face any diffuclties in their learning or with any personal projects they may require assistance with
* To help other users by providing solutions other users who are f acing difficulties

#### Site owner’s goal:
* To build a mobile responsive site to provide a means for users to learn and upgrade themselves with digital skills
* To build a supportive community for developers from all over
* To profit frome the sales of digital content and expand the provision of products and services in the future
***
## Objective-based design

![Mockup image](/static/images/mockup.png "Devices Mockup")

## UX
The UX is designed to deliver the website objective as directly and quickly as possible by providing minimal steps for users to access the desired information required, with a clean and unclutered web interface.
The website 
The website is divided into 4 sections - **Courses**, **Tutors**, **Forum** and **Cart** - and is designed to allow access to different functions to the 3 different groups of people - **Administrators**, **Authenticated Users** and **Non-Authenticated Users**- based on the desired objective for each group.
* Each section is easily accessible via a permanent navigation bar at the top of the page that will collapse into a dropdown menu on mobile screens.
* Pages are kept as short as possible so that users do not have to scroll through an unnecessarily long page of content.
* Each page is made mobile responsive for devices with smaller screens.
### Courses
This page displays the different courses grouped by the type of development, Frontend/Backend/Databases. 
Each course also has its own separate details page with a reviews section with reviews and comments on the reviews.<br>
**Non-Authenticated Users** can view the courses and course details pages, however they are unable to add items to cart without an account - they will be directed to the signup page.
They are also unable to write reviews or comment on reviews.<br>
**Authenticated** users are able to add the courses to cart either from the courses page or the course details page, and will be able to write reviews or comment if they have a purchase record of the course.<br>
**Administrators** are able to access the edit and delete function for the courses on both courses and course details pages to edit the courses provided. They can also add courses from the courses page if they wish to provide more content for sale. They are however unable to add items to cart.

### Tutors
This page displays the different tutors and similarly to courses, users can access the details page for each tutor.<br>
**Non-Authenticated** & **Authenticated Users** are able to access only the content.<br>
**Administrators** have similar privileges as in the courses page; they can add tutors, edit or delete them.

### Cart
This page is for users to view what courses they are intending to purchase and checkout their items for payment. If the item has been added to cart or purchased, the "add to cart" button will indicate that the item is already in cart.<br>
**Non-Authenticated Users** & **Administrators** will not be able to access this page.<br>
**Authenticated Users** will be able to acces this page.

### Forum
This page is for users to ask and answer questions, and a search function is provided for users to search for the question title or for questions in each course category. 
Answers for each question are also available.
**Administrators** and **Authenticated Users** will be able to create, edit and delete only the questions or answers that they have posted. They are only able to view the questions and answers posted by other users. 
**Non-Authenticated Users** will only be able to view and search for questions.

In summary, **non-authenticated users** are limited to viewing content, whereas **authenticated users** are able to make purchases, write reviews and post questions or answers. 
**Administrators** have the privilege to add, edit and delete the courses and tutors information as the site owner/administrator.

`wireframes`
  

## UI
The UI is designed with simplicity in mind. The site-wide color scheme used is a dark background with bright colored buttons as calls to action to mimic a code writing application such as Gitpod and Visual Studio Code.
This was done to relate to software developing platform and give a feeling of familiarity to developers

`stopped`
### Features
The website also has the following features:

### Courses and Tutors
* The courses page is displayed with multi-carousels showing the course title, a logo image and its price for users to scroll through, divided into the type of development platforms.
    * The multi-item carousel becomes a single-item carousel on mobile screens.
* This is done to prevent the cluttering of information, by showing only critical details on the main pages and additional details in their detail pages.
* Users can access the details page by either clicking on the "Profile" or "View Details" buttons for Tutors and Courses respectively, or by clicking on the Profile image or Logo image.
* Within each details page, the related tutors or courses are displayed in small cards and are hyperlinked to their respective details page for users to quickly navigate between pages for information.<br>
* Buttons are designed with bootstrap colors and are consistent site0wide for users to identify easily:
    * Turquoise is for submission of create/update forms
    * Blue is for the main call to action and adding of courses/tutors/questions/reviews
    * Red is for deletion 
    * Grey is for the cancellations and review comments
* A messages feature is implemented to alert users that their actions have been registered and completed by the application.
*** 
### Future Features

- AJAX update - Store data in card div per review, on click extract data and put into empty form as values

Forum checkbox for ‘answered question’ and ’this answered my question’

Reviews.comments CRUD

Delete shows “-deleted\_
Edit shows “edited”

## Technologies Used

The following programming languages and tools were used to build the website:

- HTML 5
- CSS
- JavaScript
- Bootstrap v4.4 toolkit to organize the elements in the page
- jQuery library for DOM manipulation
- Python
- Flask
- Gitpod for the writing of codes and testing of website
- Mongodb Atlas for the hosting of database
- W3C Markup Validation Service for HTML and CSS validation
- GitHub
- Cloudinary image hosting

## Database

- DB selected because of:
- The database is hosted and stored postgres
- `Database design`

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
- Microsoft Edge Web Browser
  1. macOS
  2. Windows 10
  3. Android 10
- Google Chrome Web Browser
  1. macOS
  2. Windows 10
  3. Android 10

* HTML, CSS validated by W3C Markup Validation
* JavaScript Syntax validated by Esprima

1. Testing was first done by applying CRUD to `items` the built web interface. Upon successful CRUD operations and image uploading, the hosted webpage is then provided to random testers to test out the CRUD operations and UX and their feedback is taken into consideration.
2. After the testing is done, additional features are added based on priority versus estimated time required to implement, remaining features will be added in the future.
3. The web application is then tested on various web browsers and device screens for compatibility purposes.
4. The edited final web application is then updated onto the host server

## Deployment

The website is deployed on Heroku, using GitHub to host the project repository. The website can be found at this [link](http://foodiereview.herokuapp.com).

- Database passwords and session keys are stored in the .env file which is included in the .gitignore.
  `steps taken to deploy`

## Credits

This website was built using tools and data from various sources, including but not limited to the following:

- [Heroku](https://www.heroku.com) for the hosting of the web application.

Photo by Wes Hicks on Unsplash
Photo by John Schnobrich on Unsplash
Canva logo
https://material.io/design/color/dark-theme.html#ui-application

Carousel
https://www.jqueryscript.net/slider/responsive-bootstrap-carousel-multiple-items.html

https://favicon.io/favicon-converter/

Last but not least, to [Trent Global](https://www.trentglobal.edu.sg/diplomainsoftwaredevelopment/?gclid=EAIaIQobChMI8M3ezf6t6QIV2BwrCh2R6A44EAAYASAAEgL6__D_BwE) and [Code Institute](https://codeinstitute.net) for the teachings and support to have made this project possible.
