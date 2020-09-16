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

### **Contact Us / Feedback Form**

1.  **Test:** Click "Send" with empty input fields to verify the form will NOT submit and reminds the user the inputs need to be made

    **Result:** Success. The user can only send the form when all input fields have been filled.

    (During testing this failed and the logic.js file was adapted to make this pass the test.

         Git commit 61f5a54e993c2b9a2a5851648223819981f3923e

1.  **Test:** Purposely enter an INVALID email address in email input to verify the form validation reminds user to enter VALID email address.

    **Result:** Currently a work in progress. (current onclick conflicts with bootstrap settings)

1.  **Test:** Click Send with VALID inputs to verify the form is sent via EmailJS API and closes at completion.

     <img src="https://github.com/DanielBradford/Touchdown/blob/faa77ad3a53784464ff60ea63a9f8e61b4686374/assets/images/ScreenshotTestForm.png" alt="screenshot of test form">

    **Result:** The form is sent via EmailJS and received with the correct form data.
    Here is a screenshot of an examplary email received:

    <img src="https://github.com/DanielBradford/Touchdown/blob/12bb437a1a9056353f53a23729e9ae428a7c84ea/assets/images/screenshots/ScreenshotEmailRecieved.png" alt="screenshot of email recieved through EmailJS API">

1.  **Test:** Click Close button to verify the modal closes correctly.

    **Result:** The modal closes correctly.

1.  **Test:** Verify the form is visible and functional in tablet and mobile.

    **Result:** The form is fully visible on all devices.

### **"Restart" Button**

1. **Test:** Hover on button to verify CSS styling causes color change to allow user to see selection before clicking.

   **Result:** CSS stylings are functional and correct

1. **Test:** Click button to verify the restart check is initiated.

   - A confirmation box should be displayed to confirm the user wants to restart and reminds them all progress will be reset.

   **Result:** A confirmation box is presented to confirm that the user wants to restart and reminds them all progress will be reset.

    <img src="https://github.com/DanielBradford/Touchdown/blob/d71fa5712e62d9da2bad03a39e57a57d1c4c1d63/assets/images/screenshots/ScreenshotRestart.png" alt="screenshot of restart check">

1. **Test:** Click the ok button to verify the game is restarted:

   **Expectation:**

   - status displays should reset and update (Please see <a href="https://github.com/DanielBradford/Touchdown/blob/f222fe7b80efa1141f5353df48280d5f0fde8ce6/jasmine-testing/test.js" target="_blank">Jasmine Automated Tests</a>)
   - Restart sound should play
   - Arrays/Sequences should reset
   - Ball Icon should continue rotating

   **Result:**

   - All status displays are reset and updated. (Please see <a href="https://github.com/DanielBradford/Touchdown/blob/f222fe7b80efa1141f5353df48280d5f0fde8ce6/assets/images/screenshots/ScreenshotJasmine.png" target="_blank">Jasmine Automated Test Results</a>)
   - Restart sound is played (restart.mp3)
   - All game sequences/arrays are reset
   - Ball Icon in title continues rotating

### **"Start Game" Button**

1. **Test:** Hover on button to verify CSS styling causes color change to allow user to see selection before clicking

   **Result:** All styles are correct and corresponding with the CSS styles set.

1. **Test:** Click button to verify the game starts.

   **Result:** The game starts on the click of this button and all pointer actions are stopped and started in the correct places.

   - The cards individually flash for the user to remember.

     <img src="https://github.com/DanielBradford/Touchdown/blob/d71fa5712e62d9da2bad03a39e57a57d1c4c1d63/assets/images/screenshots/ScreenshotFlash.png" alt="screenshot of card flashing">

### **"Replay" Button**

1. **Test** Hover on button to verify CSS styling causes color change to allow user to see selection before clicking

   **Result:** All styles are correct and corresponding with the CSS styles set.

1. **Test** Click Replay button to verify the replay confirmation box is presented to the user.

   **Result:** A confirmation box is presented to the user confirming they want to replay the current round at a cost of -5 points.

   <img src="https://github.com/DanielBradford/Touchdown/blob/d71fa5712e62d9da2bad03a39e57a57d1c4c1d63/assets/images/screenshots/ScreenshotReplay.png" alt="screenshot of replay confirmation">

1. **Test:** Click confirm button to verify the current game sequence is replayed.

   **Result:** On every test, the current round is replayed succesfully.

### **GAME PLAY CARDS**

1. **Test:** Verfiy the cards operate consistantly on all devices and screen sizes.

   **Result:** During testing the cards remained hightlighted on touchscreen devices which added confusion to the game play.
   This was corrected by only applying the hover class on larger screens using a mouse interaction (over 1200px).

   Git commit: 817426cdb02f006feff89ced5ab0110c13ac8d82

1. **Test:** Verfiy the cards can be clicked and the function operates correctly

   **Result:** Cards can be clicked and the onclick function operates correctly.

1. **Test:** (On Desktop) Verify the cards 'highlight' when hovered over

   **Result:** All cards take on the highlight class when hovered over. (Only on larger screens)

## **Status Bar**

### **Round Counter**

1. **Test:** Check the round number displayed is correct before, during and after the game. (Including restarts and replays)

   **Result:** The round number is correct at all times.

### **Lives Counter**

1. **Test:** Verfiy the correct lives amount is displayed during the game. (Including restarts and replays)

   **Result:** The life count is displayed correctly at all times and adjusts accordingly.

### **Points Counter**

1. **Test:** Verify the correct points amount is displayed during the game. (Including restarts and replays)

   **Result:** The points counter is correct at all times.

### **Footer**

1. **Test:** Hover over the icons to verify the hover color change is applied

   **Result:** All styles are correct and corresponding with the CSS styles set.

1. **Test:** Click each of the Social Media Icons and verify the user is taken to the corresponding websites.

   (During testing one link lead to a 404 error. This was then rectified. Git commit: b17465a7c52e8e537a710a4ea7977bc7bbc029c6)

   **Result:** All icons take the user to corresponding website.

1. **Test:** Verfiy the icons are visible

   **Result:** All icons are visible. (During testing i altered the color of the icons to give a higher contrast rating to make them more visible)

1. **Test:** Click "Rate this game" link to verify the contact us modal is opened.

   **Result:** Successful.

1. **Test:** Reduce and expand width of window to verify that the footer is responsive and looks good on all device widths.

   **Result:** Successful.

## **Audio / Sound Effect Testing**

**Test:** Verify all audio effects are clear and played at the correct time.

**Result:**

1. intro: new Audio("assets/audio/intro.mp3") **PLAYS ON PAGE LOAD**
1. woo: new Audio("assets/audio/woo.mp3") **PLAYS WHEN CORRECT ANSWER GIVEN**
1. boo: new Audio("assets/audio/boo.mp3") **PLAYS WHEN INCORRECT ANSWER GIVEN**
1. whistle: new Audio("assets/audio/whistle.mp3") **PLAYS WHEN GAME IS STARTED**
1. ping: new Audio("assets/audio/ping.mp3") **PLAYS WHEN CARD FLASHES / CLICKED BY USER**
1. restartSound: new Audio("assets/audio/restart.mp3") **PLAYS WHEN GAME IS RESTARTED**
1. gameOver: new Audio("assets/audio/gameOver.mp3") **PLAYS WHEN USER HAS LOST THE GAME**
1. touchdown: new Audio("assets/audio/touchdown.mp3") **PLAYS WHEN USER COMPLETES THE GAME**

## Jasmine Testing (AUTOMATED) of Javascript Functions:

Jasmine is designed for Behaviour Driven Development. I utilised this testing tool to automate tests.
These tests include:

- Verfiy the in-game settings are on default value at the start of game e.g. Life Counter = 3, Round Counter = 1, Points Counter = 0.
- Verify the in-game settings are reset when game is restarted via restart button.
- Verify the default difficulty is preset to "Rookie" (Game speed).

Testing documents: <a href="https://github.com/DanielBradford/Touchdown/blob/c08a79c89c54b331c5b30f4d2b2509139f268fe9/jasmine-testing/test.js" target="_blank">Please find the Jasmine automated tests (test.js) here</a>

Test Result:

<img src="https://github.com/DanielBradford/Touchdown/blob/master/assets/images/screenshots/ScreenshotJasmine.png" alt="Jasmine Testing Screenshot">

Although i am familiar with the Jasmine testing suite there were some limits in automating testing for this particular project due the user interaction involved.

## Development Issues / De-bugging:

### **POINTER EVENT CONTROL** (during gameplay)

During the development of the game it was evident the user could still select cards, and click on buttons during the game.
This created bugs in the gameplay. This was resolved by controlling the pointer events during gameplay in the logic.js file. Git commit record below:

    commit 255cbc605fe96a4320d8d8084ce720001d1d239b
    Author: Daniel Bradford <danielbradford@hotmail.co.uk>
    Date:   Sun Jul 26 15:00:51 2020 +0000

    User pointer events blocked while main function is called. prevents cheating or confusion.

### **LOGIC ISSUES** (JAVASCRIPT)

During the development of the logic.js file, there were bugs/issues with the logic of the game.
The initial plan was to start with 3 lives. If the user answered incorrectly they would remain on the same round but lose one life.
This concept of remaining on the same round had issues within the game logic (assets/js/logic.js).
After re-analysing the game design and user stories i simplified the logic and introduced a point system.
If the player was incorrect, they would lose a life, start at round one and lose 5 points.
This concept eliminated the issue and resolved the bug. Git commit record below:

    commit 2a0035f71ad0828a2789474837eea568c3756962
    Author: Daniel Bradford <danielbradford@hotmail.co.uk>
    Date:   Tue Jul 28 15:42:37 2020 +0000

    Selection/answer comparisson bug fixed. Full restart to the begining prevents issues with selection matching answer.

### **404 ERROR** (SHOWN IN CONSOLE)

    GET https://8000-d9f452af-0079-4875-b36c-1deee4de621c.ws-eu01.gitpod.io/favicon.ico 404

This was **solved** by adding a link to the head of the index.html file. The favicon is now a Touchdown graphic (winning.webp). This solution was found on <a href="https://stackoverflow.com/questions/31075893/im-getting-favicon-ico-error" target="_blank">HERE</a> on Stack Overflow.

    commit a41d8a8bf199e7eb1fa87f401d44b4be7e73e02d (HEAD -> master, origin/master, origin/HEAD)
    Author: Daniel Bradford <danielbradford@hotmail.co.uk>
    Date:   Wed Aug 5 18:19:16 2020 +0000

    link added to index.html to stop 404 FAVICON error

### **RESPONSIVE DESIGN** (Materialise and Media Queries)

<span><img height="200px" src="#" alt="Screenshot of Mobile"></span><span><img height="300px" src="#" alt="screenshot of tablet"></span>

As in any project, responsive design is an extremely important factor.
I used a combination of Bootstrap features (index.html) and Media Queries (assets/css/style.css) to ensure the game is responsive on all screen-sizes.
Git commits below:

    commit 9775527ef4274153e769c5fcde5d74a84c721c7e
    Author: Daniel Bradford <danielbradford@hotmail.co.uk>
    Date:   Wed Aug 5 15:17:36 2020 +0000

    Further responsive design changes to style.css. Media queries added

    commit 715d250faa712b8b097e42bdb1cecf2542b2a080
    Author: Daniel Bradford <danielbradford@hotmail.co.uk>
    Date:   Wed Jul 29 18:42:43 2020 +0000

    Stylistic changes to layout, font and image sizes matching responsive design needs



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