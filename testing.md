# **<p align="center"> Testing </p>**

**HTML VALIDATION** - https://validator.w3.org/

- All HTML written in this project has been submitted for validation via the above software.
- ALL pages returned the vaildation that "Document checking completed. No errors or warnings to show."

**CSS VALIDATION** - https://jigsaw.w3.org/css-validator/

- All CSS written in this project has been submitted for validation via the above software.
  <img src="#" alt="CSS Validation">

**JAVASCRIPT VALIDATION** - https://jshint.com/

- ALL JS written in this project has been parsed through JSHint and no errors have been found.

 **Metrics:**
  There are 32 functions in this file. Function with the largest signature take 0 arguments, while the median is 0. Largest function has 33 statements in it, while the median is 2. The most complex function has a cyclomatic complexity value of 2 while the median is 1.

**PYTHON VALIDATION** - http://pep8online.com/

- ALL Python written in this project has been parsed through pep8 online and gitpod and no errors have been found. Upon scanning some lines of code needed to be shortened.

        commit 3c480c91bb56308f20ebc5e99f9db5a8fd71587a
        Author: Daniel Bradford <danielbradford@hotmail.co.uk>
        Date:   Wed Sep 16 18:55:00 2020 +0000
        Code layout cleaned to pass through pep8 validation




  



### **Client Story Testing:**

## Logical Testing (MANUAL) of all functions and elements:

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

## Development Issues / De-bugging:


### **RESPONSIVE DESIGN** (Materialise and Media Queries)

commit d11bb2716f24a9fdf42574bf275a7490d0e563d2 (HEAD -> master)
Author: Daniel Bradford <danielbradford@hotmail.co.uk>
Date:   Thu Sep 17 13:37:02 2020 +0000

    Menu buttons spaced. Post testing resolve


## **Future Issues to be fixed**

Following testing there are issues that still could be improved:


## **Development Tools Testing**

From using the technologies of Wave and Lighthouse i was able to check the performance and accessiblity of the website. By utilizing this in DevTools i was able to generate reports for both desktop and mobile.
By analysing these rerports i was able to make alterations in both the HTML and CSS code to improve the accessiblity of the site.

**Performance**

- In initial reports the website had an average Performance rating of **74**.
- I changed changed the appropriate .jpg & .png files into webp format to minimise memory usage and speed up loading and rendering times.
- I streamlined the style.css file to lessen the data being loaded. (commit 988437bcb814fe1235dfb5ecc33d9eae2832bae2)
- By making these changes the current Performance rating is now (on average) **91**

**Accessibility**

- In initial reports the website had an average Accessibility rating of **84**
- I altered color schemes of text vs. background to maximise the contrast score allowing information to be more visible to a wider group of users with accessiblity issues.
- I resized icons and images to make them more visible
- I re-assessed background image choices for their contrast score (commit aaec109f844de9865edeea2d8415630d683557d9)
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