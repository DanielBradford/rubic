# **<p align="center"> Testing </p>**

**HTML VALIDATION** - https://validator.w3.org/

- All HTML written in this project has been submitted for validation via the above software.
- The only errors were thrown due to the validator not recognising Jinja Templates. However Gitpod's prettier control allows the HTML to be validated inside the workspace.

**CSS VALIDATION** - https://jigsaw.w3.org/css-validator/

There were 3 minor errors that were corrected during testing:

        commit 2c8e061905795040d61851ad483cc667bb5d6804
        Author: Daniel Bradford <danielbradford@hotmail.co.uk>
        Date:   Thu Sep 17 14:53:17 2020 +0000

        Minor alterations resulted in passing jigssaw validation

- All CSS written in this project has been submitted for validation and passed via the above software.


**JAVASCRIPT VALIDATION** - https://jshint.com/

- ALL JS written in this project has been parsed through JSHint and no errors have been found.

        Metrics:
        There are 32 functions in this file. Function with the largest signature take 0 arguments, while the median is 0. Largest function has 33 statements in it, while the median is 2. The most complex function has a cyclomatic complexity value of 2 while the median is 1.

**PYTHON VALIDATION** - http://pep8online.com/

- ALL Python written in this project has been parsed  and linted using pep8 online and gitpod and no errors have been found. Upon scanning some lines of code needed to be shortened.

        commit 3c480c91bb56308f20ebc5e99f9db5a8fd71587a
        Author: Daniel Bradford <danielbradford@hotmail.co.uk>
        Date:   Wed Sep 16 18:55:00 2020 +0000
        Code layout cleaned to pass through pep8 validation


### **User Story Testing:**

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


### **LANDING PAGE**

This is the main landing page the user sees when the screen has loaded. An intro sound plays on loading (intro.mp3).

<img src="#" alt="screenshot of main page">

### **TITLE & ICON**

**Test**:
Verify the sizing of the box adjusts from desktop > tablet > mobile and that no over flow distorts the layout:

**Expectation**:


**RESULT**:

### **MENU / NAVIGATION Bar**

1.  **Test:** Verify that the sizing of the navigation bar adjusts with screen size changes:
    - **Result:** I made the navigation menu adapt to all screen sizes. For mobile, a hamburger button is used. This maximises screen real estate for smaller devices.
1.  **Test:** Verify that the menu drops down and that the menu text is clear and visible.
    - **Result:** I had difficulties during accessbility testing but found a color to make this work.
1.  **Test:** Hover over the navigation links and verify the CSS styling changes
    - **Result:** Some CSS styling choices were changed during testing due to accessbility/contrast issues
1.  **Test:** Click on each of the navigation links and verify that it opens the corresponding modals
    - **Result:** During testing i found all links to modals worked correctly.
1.  **Test:** Repeat verification of functionality and responsiveness on my mobile phone and tablet.

    **Result:** 

## Responsive Design Testing

For final testing [Responsinator](https://www.responsinator.com/) was used to test the application accross multiple devices.

### Screen Size Testing/Compability

Screen Size         | Size              | Comments
--------------------|-------------------|---------
X-Small             | <768px            | No space between buttons for landing template. Grid layout altered to rectify
Small               | >=768px           | Landing page stats given flow-text attr. to prevent distortion
Medium              | >=992px           | Passed, no changes neccessary.
Large               | >=1200px          | Passed, no changes neccessary.

Commit Examples:

        commit 7a286130e0414e9703575ff7e0777cd1aafab062
        Author: Daniel Bradford <danielbradford@hotmail.co.uk>
        Date:   Thu Sep 17 15:44:48 2020 +0000

        Media query alterations for responsive design improvements


        commit 4bde74435aaea76484abec91143be5529c7485d2
        Author: Daniel Bradford <danielbradford@hotmail.co.uk>
        Date:   Thu Sep 17 15:26:32 2020 +0000

        Post testing alterations made to enhance responsive design
### Browser Compability

Browser             | Version           | Comments
--------------------|-------------------|---------
Firefox             | 72.0.2 (64-bit)   | No errors observed
Edge                | 44.18362.449.0    | No errors observed
Chrome              | 80.0.3987.122     | No errors observed



## Development Issues / De-bugging:




### **RESPONSIVE DESIGN** (Materialise and Media Queries)

commit d11bb2716f24a9fdf42574bf275a7490d0e563d2 (HEAD -> master)
Author: Daniel Bradford <danielbradford@hotmail.co.uk>
Date:   Thu Sep 17 13:37:02 2020 +0000

    Menu buttons spaced. Post testing resolve


## **Future Issues to be fixed**

During development i encountered issues with the user session feature. When i a guest opens the application they are assigned a session['user] status as "Guest". This status allowed me to control their access throughout the application. This may have issues in the future if the application scope is to expand. 


## **Development Tools Testing**

From using the technologies of Wave and Lighthouse i was able to check the performance and accessiblity of the website. By utilizing this in DevTools i was able to generate reports for both desktop and mobile.
By analysing these rerports i was able to make alterations in both the HTML and CSS code to improve the accessiblity of the site.

**Performance**

- In initial reports the website had an average Performance rating of **74**.
- I changed changed the appropriate .jpg & .png files into webp format to minimise memory usage and speed up loading and rendering times.
- I streamlined the style.css file to lessen the data being loaded. (commit 
- By making these changes the current Performance rating is now (on average) **91**

**Accessibility**

- In initial reports the website had an average Accessibility rating of **84**
- I altered color schemes of text vs. background to maximise the contrast score allowing information to be more visible to a wider group of users with accessiblity issues.
- I resized icons and images to make them more visible
- By making these changes the current Performance rating is now (on average) **100**

**Best Practices**

- In initial reports the website had an average Best Practices Score of **88**
- I added meta tags, alt tags, and aria labels (commit c8e0752bba88a3db1f15b682f667785c412515bb)
- By making these changes the current Best Practices rating is now (on average)**100**

**Search Engine Optimisation**

- In initial reports the website had an average SEO rating of **98**
- I added in some META tags to give more information about th websites content and creator.
- By making these changes the current SEO rating is now **100**

**Lighthouse Desktop Report:**
<img src="#" alt="Landing Page - LIGHTHOUSE REPORT">

## Further Testing

I completed further testing by asking family and friends to play the game and give me feedback.
This stage of testing allowed me to understand a more realistic client/user impression of the game and guided me to altering some stylistic choices. e.g. bigger text in places and more breathing space between elements.