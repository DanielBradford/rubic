<div align="center"><img src="documents/screenshots/logo.png"></div>
<a name="top">
# Table of contents

1. <a href="#whatis">What is Rubric?</a>
1. <a href="#whatdo">What does it do?</a>
1. <a href="#how">How does it work?</a>
1. <a href="#creation">Creation & Design</a>
1. <a href="#strategy">Strategy</a>
1. <a href="#scope">Scope</a>
1. <a href="#structure">Structure</a>
1. <a href="#skeleton">Skeleton (Wireframes)</a>
1. <a href="#surface">Surface</a>
1. <a href="#features">Features</a>
1. <a href="#future">Future Features</a>
1. <a href="#defensive">Defensive Programming</a>
1. <a href="#responsive">Responsive Design</a>
1. <a href="#hardware">Hardware & Technology Used</a>
1. <a href="#testing">Testing</a>
1. <a href="#deployment">Deployment</a>
1. <a href="#credits">Credits</a>



<a name="details"></a><div align="center"><p>Project Live Demo:<a href="https://rubric-recipe-manager.herokuapp.com/"> **RUBRIC - RECIPE MANAGER**</a>

<a name="whatis"></a>
## <p align="center" style="color:teal">WHAT IS RUBRIC?</p>
Rubric is an efficient personal recipe management web application.  It provides a full recipe management service, free of charge which allows users to have access to a selection of recipes, including their own, all in one place. The project is a combination of HTML, CSS, JavaScript, and Python and utilizes a NoSQL Database (MongoDB) with Flask.
<a name="whatdo"></a>
## <p align="center"  style="color:teal">WHAT DOES IT DO?</p>
It allows users to Create, Read, Update and Delete Recipe Documents. It also has features that allow registered users to save recipes they like and rate other peoples recipes. 

<div align="center"><img style="width: 70%" src="documents/screenshots/desktop.png" alt="screenshot of landing page"></div>
<a name="how"></a>

## **HOW DOES IT WORK?**
There are 3 stages of access

1. **Unregistered Access:** This allows users to view all recipes without being able to add, save or edit. It also limits their access to a products, tools and discounts page.
1. **Registered Access:** Once the user has logged in or registered, they can Create, Read, Update, Delete, Save and Rate recipes on the application. 
(*The user can only edit and delete their own recipes and can only rate the recipes of others*)
1. **Admin Access** Only admin can access the management page which has full CRUD functionality over all contents of the application including Users, Recipes, Recipe Types, Products and Tools.
<a name="creation"></a>
## **Creation and Design**

### **Behaviour Driven Development vs Test Driven Development or Acceptance Test Driven Development**

Due to the complexity of the application, test driven development was paramount when developing the system. The behaviour needed to match the users needs while the functionality needed to pass essential tests. In addition to providing full CRUD (Create, Read, Update, Delete) functionality.
<a name="strategy"></a>
### **UX - STRATEGY:**

The application is designed to provide an essential service to users looking for an online recipe management system.

**_BUSINESS GOALS OF APPLICATION_**
- To provide an efficient recipe management web application
- To CREATE, READ, UPDATE and DELETE User Information
- To CREATE, READ, UPDATE and DELETE Recipe Information
- To CREATE, READ and DELETE Recipe Type Data
- To CREATE, READ and DELETE Product Information
- To CREATE, READ and DELETE Tool Information
- To PROMOTE recipe related Amazon products such as appliances and tools, to MONETIZE the application
- To direct online traffic and encourage shopping of said products through the incentive of discounts 
- To generate a large user base to monetise the site through advertising by providing a free, useful and easy to use application

**_USER GOALS OF APPLICATION_**
- To CREATE and store a Recipe
- To READ / VIEW all recipes
- To UPDATE any recipe i created
- To DELETE any recipe i created
- To RATE other peoples recipes
- To SAVE other peoples recipes
- To READ / VIEW all recipes i have created
- To view recommended and recipe related tools and products
- To get discounts for products


**_WHO IS THE USER?_**

- The ideal user for Rubric:
  - Over the age of 10
  - Interested in Cooking and or Baking
  - Wants to cook more
  - Needs an online place to view and store recipes
  - Has disposable income for e-commerce
<a name="scope"></a>
### **UX - SCOPE:**
**Business Intentions**

The Register/Log In feature is utilised in this application as it encourages data capture in exchange for added features free of charge. The added features that registering allow access to include:
- Saving Recipes to a private folder
- Rating recipes to give users feedback on their contributions
- Recommended Products and Tools page with prices, images and descriptions.
- Discounts for affiliate sites and products

Although registering is also free the user must give their full name and email address which has the scope in the future to be utilised for news, updates and marketing purposes.

**What do the NEW users want?**
- Users that are new to the application will want to navigate throughout the site easily and intuatively. They want to find and view recipes free of charge with the option of registering for the added features.

**What do the RETURNING users want?**
- Returning users want to log in easily to their profile on the application to use the application as a registered user with access to all features available.

**USER STORIES**`

1. As a new or returning user i want to navigate the application easily
1. As a new user i want the option to register to the site
1. As a returning user i want the option to login to the application
1. As a new or returning user i want to view all recipes on the application
1. As a new or returning user i want to easily search through all the recipes on the application
1. As a new or returning user i cant decide what recipe to view and want to be shown a random recipe to make my recipe choice experience fun and enjoyable
1. As a new or returning user i want to view all recipe types
1. As a new or returning user i want to view a recipe that is displayed clearly and makes my cooking experience easier
1. As a new or returning user i want to view all Vegan recipes 
1. As a registered user i want to add a recipe to the application
1. As a registered user i want to view all the recipes i have added/contributed
1. As a registered user i want to easily search through all recipes i have added/contributed
1. As a registered user i want to save recipes of other registered users
1. As a registered user i want to view all the recipes i have saved
1. As a registered i want to easily search through all the recipes i have saved
1. As a registered user i want to view cooking related products and tools recommended by Rubric
1. As a registered user i want to receive discount codes for cooking related products.

<a name="structure"></a>
### **UX - STRUCTURE:**

The next plane to approach was Structure. What the application will do and and the external factors that might affect it.
This allowed an insight into the user experience and how a visitor uses the application.

**Here is the link to the structural sitemap:**
<a  href="https://github.com/DanielBradford/rubric/blob/793f1b03bbb0c314173efad35b1952d0630e94d5/documents/wireframes/Rubric%20Sitemap.pdf" target="_blank">SITEMAP</a>

Structure:

The application uses Mongo DB, a noSQL database system. 

Within the Rubric Recipe Manager Database their are 5 collections

1. USERS 

    - The majority of the fields use String input.
    - The saved recipes uses an array which stores the ObjectIds of the recipes that have been saved by this user.
    - The contributed field uses the Int32 value to allow a number to  increment/decrement easily
    <img style="width:80%"  src="documents/screenshots/user_data_model.png">

1.  RECIPES 

    - The majority of the fields in this collection also use String values.
    - The rating field uses an Array to collect all the ratings. The output is the sum of the array divided by the length.
    <img style="width:80%"  src="documents/screenshots/recipe_data_model.png">

1. RECIPE TYPE 
    - 2 Fields have string values
    - The count field is Int32 to allow for incrementation / decrementation
    <img style="width:80%"  src="documents/screenshots/recipe_type_data_model.png">

1. TOOLS

    - All string values
    <img style="width:80%"  src="documents/screenshots/tool_data_model.png">

1. PRODUCTS 

    - All string values
    <img style="width:80%"  src="documents/screenshots/product_data_model.png">

    *In future development i would make the price field a decimal*

<a name="skeleton"></a>
### **UX - SKELETON:**

The skeleton of this project was designed and established using Balsamiq (Cloud): https://balsamiq.cloud/

### **Wireframe Designs**

All wireframe designs can be found here:

Mobile: <a href="https://github.com/DanielBradford/rubric/blob/239022217d7984c6c0c9a6378e43f6daf76b7dc3/documents/wireframes/RUBRIC%20MOBILE%20WIREFRAMES.pdf">Mobile Wireframe Designs</a>

Desktop: <a href="https://github.com/DanielBradford/rubric/blob/c4a2399f3f18880deb4bf009fe06c59fb35feba8/documents/wireframes/RUBRIC%20DESKTOP%20WIREFRAMES.pdf">Desktop Wireframe Designs</a>


<a name="surface"></a>
### **UX - SURFACE:**

The final element to consider was the surface plane of UX design. This is the look and feel of the application.
Below are some screen shots of the application in use:

## **Style / Theme**

- It was important to me that the application remained gender neutral in order to maximise potential user scope. Upon researching current applications it appears many have a feminine tone which might discourage male users. From the start i intended the site to be bright, fun and intuitive.
The main COLOR scheme used includes:
- **Coral** (rgb(255, 95, 37))
- **Teal** (rgb(1, 128, 128))
- **White** (#ffffff)
As the application is centered around recipes and cooking i used a Chef Hat Symbol as the main logo.
The FONTS used were from Google Fonts:
- **Fredoka One**
- **Gayathri**
To maintain the idea of being approachable, bright and friendly i used supporting colors for icons and buttons:
- **Pink** (#e91f63)
- **Purple** (#9c27b0)
- **Yellow** (#fdd835)
This was maintained through out the application using a mix of customised CSS and Materialize framework.
<a name="features"></a>
## **Features**

### **Repeating Features**

### The following features are repeated across the application allowing a consistent design format for the user to feel comfortable and familiar;

### Navigation

- **Mobile** The navigation menu is represented by the hamburger icon. The mobile menu uses Materialize JS and is displayed in a user-friendly and stylish format. A breadcrumb navbar allows a tracking of inner application movement.
- **Desktop** The navigation menu is clear and accessible. When hovered over the links are highlighted. A breadcrumb navbar allows a tracking of inner application movement.
- **Registered Users** 
    Once logged in users can enjoy the extra feature of the floating action menu. This is located in the lower right corner of the screen and allows quick access to the following:
   <ul style="width:50%"> <img align="right" style="width:25px; height:100px" src="documents/screenshots/floating_menu.png">
        <li>Add Recipe (Green Plus Icon)</li>
        <li>Products and Tools (Purple Blender Icon)</li>
         <li>My Recipes (Coral archive icon)</li>
        <li>Random Recipe (Pink random icon)</li>
        <li>Saved Recipes (Yellow Thumbtack icon)</li>
   


    The placement of the floating menu is positioned using the Gestalt theory and principle of proximity. Lower right corner is intuitive for users.

### Footer

- **Social Media Icons:** These icons when clicked take the user (on a new page) to the corresponding website for that social media e.g. LinkedIn of Creator, Facebook & Instagram of Rubric.

## USER FEATURES

### **Login Feature**
This allows registered members to login into application in order to access the extra features. This contains back-end verifcation that checks if the username exists in the database.

If the unhashed password in the database matches the user's password, they are then able to login.

<img style="width:100%" src="documents/screenshots/login.png">

### **Register Feature**

This allows new users to register for free so they can access the extra features. The data entry form has front-end and back-end validation to ensure full protection and help prevent user error. For example:

- The First Name cannot be over 20 characters
- The email must contain the '@' and '.' symbol in a recognised format
- The password and confirm password field must match 
- The password is also hashed for security purposes
<br/>

<img style="width:100%" src="documents/screenshots/register1.png">
<img style="width:100%" src="documents/screenshots/register2.png">

### **Recipes Page**
The recipes page is the main dashboard for all the recipes. 

<img style="width:100%"  
src="documents/screenshots/recipes1.png">

There is a control panel that presents 4 options:

- All Recipes: Displays all recipes in alphabetical order:

<div align="center"><img style="width:50%"  src="documents/screenshots/recipes2.png"></div>

- Random: The random feature button allows any indecisive user to click the button and they will be presented with a random recipe from the database: 

<div align="center"><img style="width:50%"  src="documents/screenshots/random.png"></div>

- Types: Allows the user to see the categories of recipes i.e. Snack, Main etc. **Each category has a corresponding related image. This is repeated in the recipe cards as circular avatars**:

<div align="center"><img style="width:50%"  src="documents/screenshots/recipe_types.png"></div>  

- Vegan: Allows the user to filter the results to only show Vegan recipes:

<div align="center"><img style="width:50%"  src="documents/screenshots/vegan_result.png"></div>

### **Search Feature**
This feature occurs in a number of pages in the application.
The search feature allows the user to input text and search the database for the relevant inputted data.
- **Search recipes page** allows the user to search within the index of recipe name and recipe ingredients

    <div align="center"><img style="width:80%" src="documents/screenshots/search_result.png"></div>
- **Search saved recipes page** allows the user to search within the index of recipe name and recipe ingredients within their saved recipes contents
- **Search my recipes page** allows the user to search within the index of recipe name and recipe ingredients within their 'my recipes' contents

### **View/Read Recipes**
This allows all users to view the recipe of their choice from the selection in the database. The view recipe page has the following features:

- The ingredients are split by "," and displayed in an unordered list

    view_recipe.html (line 135)

        {% for ing in item.ingredients.split(",") %}

- Check boxes are displayed to be ticked if the user has the ingredient on the list
-The method instructions are split by "." and displayed in an ordered list

    view_recipe.html (line 111)

        {% for ing in item.method.split(".") %}

- Check boxes are displayed to be ticked if the user has completed the stage of the method/instructions

- When the appliance name is clicked it takes the user to the recommended appliance on the affiliate website. (THIS ALLOWS FOR THE APPLICATION TO BE MONETIZED THROUGH ADVERTSING AND AFFILILIATE MARKETING)

 For example:

<img style="width:50%" src="documents/screenshots/view_recipe.png"><img style="width:50%" src="documents/screenshots/view_recipe2.png">
<div align="center"><img style="width:50%" src="documents/screenshots/amazon_product.png"></div>


## **REGISTERED USER FEATURES**
Apart from Login and Register, all of the above features are accessible in addition to the following:

## **Profile Page**
After login and registration the user is directed to the profile page. On first arrival they are greeted with a flash message 'Welcome {username}'.

The search feature in this page is identical in funcitonality and display to the search feature of the recipes page.

The profile feature presents a dashboard display of the applications features. From the profile they can view:

- All Recipes
- Saved Recipes
- My Recipes
- Top Tools & Products

<img style="width:100%"  src="documents/screenshots/profile.png">

When the cards are selected they reveal information and a link to the corresponding profile section.

<img style="width:100%"  src="documents/screenshots/profile_cards.png">

## **My Recipes**
This page displays all recipes contributed by the user. The number in brackets counts the total amount. 

This page presents the add recipe button which redirects the user to the add recipe page. This allows the user to add a recipe. 

On the recipe cards displayed there are buttons to edit (blue) or delete (red) their recipe. Or by clicking the card they can view the recipe.

<img style="width:100%"  src="documents/screenshots/my_recipes.png">

## **Saved Recipes**

This page displays all recipes saved by the user. The number in brackets counts the total amount.

The user has the option to search all recipes within their saved list.

They also have the option to remove the recipe using the trash icon. When this is clicked there is an option to remove the item. They have to confirm to complete this function.


<img style="width:100%"  src="documents/screenshots/saved_recipes.png">

## **Create/Add recipes**
The ADD RECIPE button in 'My Recipes' and the Floating Menu ADD RECIPE Button (Green) direct the user here.

The create recipe feature allows the user to add their own recipe using the data entry form provided. 

The user is encouraged to seperate all ingredients with "," and seperate all method instructions with "." 

This is important for the processing and displaying of information in the view_recipe.html template. *This method can be improved as it relies entirely on user compliance*

The data entry form has front-end and back-end validation to reduce user error and help prevent malicious activity. For example:

- Character min and max limits on text inputs

 <img style="width:100%" src="documents/screenshots/add_recipe.png">
<img style="width:100%" src="documents/screenshots/add_recipe2.png">

## **Delete recipes**
The delete option is presented to the registered user in 'My Recipes' and 'View Recipe' Pages. If the user selects delete they have to confirm this via a Javascript Pop Up confirm box.

<div align="center"><img style="width:50%" src="documents/screenshots/edit_delete_option.png"></div>

## **Edit/Update recipes**
The Edit Recipe Feature allows users to modify any recipe they have created. They are presented with the data enrty form used when adding but with populated fields using the data of the recipe they have chosen to edit. They also have the option cancel the editing proccess.

<img style="width:50%" src="documents/screenshots/edit_recipe.png"><img style="width:50%" src="documents/screenshots/edit_recipe2.png">

## **Save recipes**
The save recipes feature allows a registered user to click 'save' on any recipe they havent created and save it to their "saved recipes" page which can be accessed via their profile. (This is supported with the feature that can also remove the saved recipe).
This was created using an Array in the User Collection document. Below shows the SAVED status and an example of the Saved Recipes Page.

 <img style="width:100%"  src="documents/screenshots/add_to_saved.png"><img style="width:50%" src="documents/screenshots/saved.png"><img style="width:50%" src="documents/screenshots/saved_recipes.png">

## **Rate recipes**
The rate recipe feature allows all registered users to rate a recipe out of 10 if they have not created it. This generates user feedback and allows users to see which recipes are rated well for reccomendation. The rating and the count of how many times it has been rated is clearly displayed. Below is a screenshot of the feature on the View Recipe page.

<div align="center"><img style="width:50%" src="documents/screenshots/rating.png"></div>

## **Product & Tools**
This feature presents recomended tools and products.
The product image, description and price are displayed with clickable links to the corresponding site. A registered user has access to discount codes which are displayed via modal when clicked.
The modal also allows the user to click the copy icon to copy to the device's clipboard for future use.

<img style="width:100%" src="documents/screenshots/tools_products.png"><img style="width:100%" src="documents/screenshots/products2.png"><img style="width:50%" src="documents/screenshots/discount_code.png"><img style="width:50%" src="documents/screenshots/amazon_tool.png">

## **ADMIN / MANAGEMENT FEATURES**

<img src="documents/screenshots/manage_top.png">

When Admin logs in they are directed to the management versus the usual profile page for non admin users.

## **Users Table**

The user table displays all user information. The table displays:
- **User Name** (There are 2 symbols. When clicked a toast is shown explaining. Leaf = Vegan, Star = Over 5 recipes contributed)
- **Last Name** (Records sorted by this field alphabetically)
- **First Name**
- **Email address** (When clicked this opens an email to be sent to the member from RUBRIC ACCOUNT MANAGEMENT) This allows for easier communication if needed between admin and members.

    commit cf0cf744e09639f4de4b7c0dc829994d702a13a7



- **Contributed** (Number of recipes added by user)
- **Saved** (Number of recipes user has saved)

### ADD USER
The green button with the plus icon allows redirects the user to the registration page where they can add/create/register a new user.

### EDIT USER
This is the blue button with pencil icon. The edit user button directs the admin to the edit user page. This page is identical to the add user form but is populated with the corresponding user details and is without password fields. This is to protect the users privacy and security. Only Name, Username and Email can be updated.

<img style="width:100%" src="documents/screenshots/edit_user.png">


### DELETE USER
This is the red button with the trash icon. This button deletes the user but the admin has to confirm this . They are presented with a Javascript Confirm Pop Up window to ensure they intend to delete the user. 
<img style="width:100%" src="documents/screenshots/users_recipes.png">

### **Search Users**
In the management page the admin can search within the index of username and last name and the results are displayed in the table.

<img style="width:100%" src="documents/screenshots/search_users.png">

 ### ***All user data is viewable apart from their password. This is to protect the privacy of the users. A future feature will be a password recovery feature if the password is lost or forgotten or needs to be changed.***

## Recipes Table

The recipes table displays all recipe information in the database collection. The amount of data displayed varies depending on screen size. This information includes:

- **Recipe Name** (If the name has a leaf symbol it means the recipe is vegan)
- **Recipe Type** (Displays the category of recipe)
- **Rating** (Average rating / 10)
- **Created by** (Shows the creator's username)

### ADD RECIPE
This green button with the plus icon allows the admin user to add a recipe. The admin user will be redirected to the add recipe page.

### DELETE RECIPE
This red button with the trash icon will delete the corresponding recipe. The user will have to verify the deletion via a Javascript Confirm window. 

<img style="width:100%" src="documents/screenshots/users_recipes.png">


## Recipe Type Table
This table displays all recipe types within the database. The data includes:

- **Type Name** (This is the name of the recipe type)
- **Description** (This is a short description of the category)
- **Recipe Count** (This counts how many recipes are in this category)

When a recipe is added or deleted this count is incremented/decremented accordingly.

<img style="width:100%"  src="documents/screenshots/manage_recipe_type.png">

### ADD RECIPE TYPE

The green tab with the plus icon toggles a data entry form where the admin can add a recipe type. **If a new recipe type is added it is assigned a default image for corresponding recipe card avatars**.

<img style="width:100%"  src="documents/screenshots/add_recipe_type.png">

### DELETE RECIPE TYPE

The red button with the trash icon deletes the recipe type. The user is presented with a confirm window to double check they wish to do this. This helps prevent accidental deletion. *This function is validated in the back-end to check if there is a recipe under this recipe type category. If there is the recipe type cannot be deleted!*

### ***AN EDIT FEATURE WAS ADDED BUT REMAINS DISABLED DUE TO ONGOING FUNCTIONALITY DEVELOPMENT. THIS WOULD BE A FUTURE FEATURE ON THE SYSTEM***

## Products Table / Tools Table
This table displays all information about the products and tools stored in the Mongo database.

Products and Tools Info:

*For the purpose of this project all information was taken from AMAZON as an exemplary sponsored associate*

- **Name**
- **Description**
- **Price**

<img src="documents/screenshots/products_tools.png">

### ADD PRODUCT / TOOL
The add button with the plus icon toggles a data entry form within the window which allows admin to add a product or tool to the database.

<img src="documents/screenshots/add_product_tool.png">

### DELETE PRODUCT/TOOL
This allows the user to delete a product/tool from the system. This action is met with same verifcation as other deletion proccess.

 
### ***AN EDIT FEATURE FOR TOOLS AND PRODUCT WOULD BE A FUTURE FEATURE ON THE SYSTEM***
<a name="future"></a>
## **FUTURE FEATURES**

- Comment Section on view recipe page
- Products and Tools page populated through API / AWS (Amazon Web Services)
- Messaging system and Inbox for  registered users
- Leaderboard and points system for recipes and ratings
- Coin earning/payment system for contributions. You earn coins for watching recipe videos/ adverts. You can redeem them for online discounts
<a name="defensive"></a>
## **Defensive Programming**
A primary objective when developing this application from a defensive design standpoint was to limit the users access and prevent the system breaking due to user input or malicious activity.

For this project, i have deployed full CRUD functionality and allowed any user to view the recipes but only registered users can Create, Edit and Delete them.

Back-end routing checks prevent any cross site activity that may result in unwanted behaviour from a malicious user.

This application uses both front-end  and back-end data validation via the formfield attributes (max and min # of characters, only accepting valid url, etc.) along with back-end defensive programming in app.py

This ensures the amount of data for each recipe is limited/controlled however the content of the data is not.

A user could upload any text (for example offensive text) into the database at this point.

A future feature i have considered is an approval functionality from an admin user that requires approval before the uploaded recipe/information is made publicly available.

*For details on defensive design testing, please see <a href="https://github.com/DanielBradford/rubric/blob/f255ded4eaef409b9e71a8dc2d2aded3fe14e3d5/testing.md" target="_blank">testing section</a>.
<a name="responsive"></a>
## **Responsive Design**
<div><img style="width: 20%" src="static/images/qrcode.png" alt="qrcode"><img style="width: 50%" class="align-center" src="documents/screenshots/ipad.png" alt="screenshot of ipad view"><span>   </span><img style="width: 20%" class="align-center" src="documents/screenshots/mobile.png" alt="screenshot of mobile view"></div>

The application has been built using a mobile-first approach. The Materialize grid system was utilized to maintain the responsiveness of this application accross all screen sizes. Throughout the development process, chrome developer tools, multiple desktops and mobile devices
where used to ensure responsivness across all screen resolutions. *(The application was also tested by family and friends using various devices and browsers.)*

Please see the <a href="https://github.com/DanielBradford/rubric/blob/239022217d7984c6c0c9a6378e43f6daf76b7dc3/testing.md" target="_blank">TESTING.md</a> file for more information
<a name="hardware"></a>
## **Hardware Used**

- ### **MacBook Pro (Retina, 13-inch, Mid 2014)**

## **Technologies Used**
IDE:
- ### **Gitpod** - https://gitpod.io/
Version Control:
- ### **Git** https://git-scm.com/
- ### **GitHub** https://github.com/
Deployment: 
- ### **Heroku** https://www.heroku.com

Languages:
- ### **HTML / HTML5**
  - Used to create the structure of the pages
- ### **CSS / CSS3**
  - Used to style the elements and customise layout. e.g. Color Schemes, design elements
- ### **JQuery**
  - Used to enhance the interactivity
- ### **Python (3)** 
  - For all application functionality and databse interaction

Frameworks/Libraries:

- ### **Materialize** 1.0.0 (CSS & Javascript/JQuery) https://materializecss.com/
  - Used mainly for responsive design and layout. Other elements used were Tables and Modals
- ### **Font Awesome** - v5.10.0 https://fontawesome.com/
  - All icons used in this project were from Font Awesome
- ### **Mongo DB** 
  - For all database functionality
- ### **Dnspython** 2.0.0
- ### **Flask** 1.1.2
- ### **Flask-PyMongo** 2.3.0
- ### **PyMongo** 3.11.0

- ### **Lighthouse Analytics** (DevTools)
  - This was used to analayse the performance, accessiblity, best practices and SEO scores of the site.
(Accessibility Testing)

<br>


<a name="testing"></a>
## **TESTING**

### Please refer to <a href="https://github.com/DanielBradford/rubric/blob/master/testing.md" target="_blank">TESTING.md</a> for a full testing breakdown

<a name="deployment"></a>
## **Deployment**

This project was **developed** using a <a href="https://gitpod.io/" target="_blank">GITPOD IDE</a>, committed to git and pushed to <a href="https://github.com/" target="_blank">GitHub</a> using the built in terminal feature.

- To add:
  - git add "filename"
- To commit:
  - git commit "filename" -m "unique message for commit"
- To push:
  - git push

This project was **deployed** using **HEROKU**.

**How to deploy to Heroku using GitPod:**

1. Created a new application using the Heroku dashboard.
2. Go to settings tab, click on 'reveal config vars' and add config vars such as IP (0.0.0.0), PORT (5000), MongoDB Name, MongoDB URI (URL with DB name and password).
3. Install Heroku via the console using 'pip3 install -g Heroku'.
4. Log into Heroku via the console using 'heroku login' and follow the on screen instructions to log in.
5. Create a requirements.txt via the console using 'pip3 freeze > requirements.txt'.
6. Create a Procfile via the console using 'echo web: python app.py > Procfile'.
7. Connect GitHub to Heroku via the console using 'heroku git:remote a rubric-recipe-manager'
8. Commit all files in your project via the console using 'git add .' and 'git commit -m "Message"'.
9. Deploy your project to Heroku via the console using 'git push heroku master'.


### **To run locally:**

To clone this project from GitHub:

1. Follow this link to the <a href="#" target="_blank">Project GitHub repository</a>.
1. Under the repository name, click **"Clone or download"**.
1. In the Clone with HTTPs section, copy the clone URL for the repository.
1. In your local IDE open Terminal/Git Bash.
1. Change the current working directory to the location where you want the cloned directory to be made.
1. Type git clone, and then paste the URL you copied in Step 3.
   - **e.g. "git clone https://github.com/DanielBradford/Rubric"**
1. Press _**Enter**_. Your local clone will be created.
1. To cut ties with this GitHub repository, type git remote rm origin into the terminal.

**Further reading and troubleshooting on <a href="https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository" target="_blank">cloning a repository from GitHub here.</a>**
<a name="credits"></a>
## **Credits**
Content :
- Materialize was heavily utilised in this project 
- Unsplash for Images
- QR CODE GENERATOR : https://www.the-qrcode-generator.com/

For continual guidance:
- Brain Macharia (CI Mentor)
- Stack Overflow (https://stackoverflow.com/)
- W3 Schools (https://www.w3schools.com/)

<div align="center"><a href="#top">BACK TO TOP</a></div>