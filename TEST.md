# Testing 

## User Story Testing
### Anonymous user
#### View the site on all screen sizes
* Site tested on all screen sizes as described in the responsive testing section.
#### Understanding what the site is about from landing page
- **Testing:** Used the [deployed site url](https://cononley-store.herokuapp.com/) and clicked enter, the page opened showing the landing page. The background image displayed Cononley Store, instantly explaining to the user what the site is about.
#### Navigating around the site
- The site contains mutlitple ways to navigate, for example the navbar is fixed so no matter how far down a page the menu dropdown is available. On the mobile device the navbar is available in a mobile friendly format so the user can easily navigate. The home page has a quick links section that allows users to navigate quickly to commonly used pages. And the logo is a quick link back to the homepage, regardless of where the user is in the site.
- **Testing:** From the landing page I used the dropdown menu and tested all links, all links were correct. From the home page I clicked all the quick links (All Products, Blogs, E-bike Hire) and they all work correctly. I systematically tested all buttons on each page as I moved through the site as a user and found no errors along the way.
#### Searching for products
- **Testing:** On the products page I used the search bar to search treatments by name and description to check correct results was returned. Using the search bar I put in a product that did not exist, the the page returned 0 products found as expected.
#### Filtering search results
- **Testing:** Searched for a product then using the 'sort by..' dropdown tested options. When sorting by each category the results were returned in the correct way. For example, when I sorted by price, the items were sorted in ascending price order.
#### Reading details about products
- **Testing:** On the products page I clicked a product to test the product details page opened, displaying the correct title, image, description and price.
#### Adding products to the cart
- **Testing:** On the product details page I selected a quantity and clicked 'add to cart' button, checked the total was displayed at the top right of the navbar, checked toast showed when adding the treatment. Clicked 'Go to Secure Checkout' button to make sure the product was now in the bag - which it was. I tested a few items to ensure multiple items could be added to the bag.
#### Understanding why I should sign up
- The aim of the site is for all users to be able to make purchases but there are two reasons for a user to sign up. 1) To save billing information for next time checkout. 2) To add comments to blogs
- **Testing:** On the checkout page I checked non-logged in users could not save there information and that logged in users could. On the blogs page I checked that logged in user could add comments and non-logged in users could not.
#### Registering for a user profile account by choosing a username and password
- **Testing:** Using the sign up page I filled information wrong by including spaces to check validation worked correctly, I then put information of another user in to check the validation worked there, worked successfully. I then put new user details in the check a user was successfully created.
#### Able to view blog/comments for the company
- **Testing:** On the blog page I checked all users had access then clicked a blog to make sure the blog details page opened correctly. I also checked to make sure anonymous users were unable to add comments, only able to view blogs and comments.

### Registered User
#### Logging in and out of an account
- **Testing:** First I put wrong information in checking form validation worked. Then using previous sign up details I went to the login page and put details in checked I was logged in correctly.
#### Updating billing information
- **Testing:** First I went to the checkout page and filled in billing information making sure the save information checkbox was selected then made the purchase. From there I went to my profile and checked my details were showing successfully, then I made changes to the information in the profile clicked 'Update Information', I went back to the checkout to check information was changed successfully.
#### Adding to order history and checking previous order recipts
- **Testing:** Made a purchase then went to my profile, checked the order number matched the purchase and that the recipt showed when clicked.
#### Adding comments to the site
- **Testing:** I clicked on the blogs link and clicked 'add comment' under a blog, which opened the add comment form. I filled in the form with the correct details and added it, I then checked it was added to the site with the correct user and blog name.
#### Editing blogs
- **Testing:** Going to an existing comment I clicked the edit button and made sure the edit comment form opened. I made changes to the details and clicked update, from there I checked the changes were applied correctly.
#### Deleting blogs
- **Testing:** Click on a comment and checked the delete button is displayed, I then clicked the delete button. Once I clicked delete, then checked the blog was gone.

### Site admin/superuser
#### Adding new products to the site
- **Testing:** I clicked product management link to check it opened the add product form. I filled in the form with the correct details and added it, I then checked it was added to the site.
#### Editing a product
- **Testing:** Going to an existing product I clicked the edit button and made sure the edit product form opened. I made changes to the details and clicked update, from there I checked the changes were applied correctly.
#### Deleting products
- **Testing:** Clicked on an existing product and check the delete button is displayed, I then clicked the delete button. Once I clicked delete, I checked the treatment was gone.
#### Adding blogs to the site
- **Testing:** I clicked on the blogs link and clicked 'add blog', which opened the add blog form. I filled in the form with the correct details and added it, I then checked it was added to the site.
#### Editing blogs
- **Testing:** Going to an added blog I clicked the edit button and made sure the edit blog form opened. I made changes to the details and clicked update, from there I checked the changes were applied correctly.
#### Deleting blogs
- **Testing:** Click on a blog and checked the delete button is displayed, I then clicked the delete button. Once I clicked delete, then checked the blog was gone.

## Stripe Tests
* Using stripe dashboard in the webhooks section I checked my site returned webhooks correctly. **Worked**

## Responsive Tests
- DevTools - Devices tested across a range of widths:
  - Mobiles: iphone5(320px) | Samsung S5 (360px) | iPhone 6/7/8/X (375px) | iPhone 6/7/8 Plus (414px)
  - Tablets: iPad (768px) | iPad Pro (1024px)
  - Desktops: Laptop (1200px) | Large Desktop screen (1920px)

- Viewed on physical devices:
  - Mobiles: small phone (320px) | large phone (414px)
  - Tablets: large tablet (768px)
  - Desktops: Medium laptop (1366px) | Large Desktop screen (1920px) | Very Large Desktop screen (1440px)

- Viewed site on above range (including Responsive mode) on various browsers: >   
  - Google Chrome
  - Firefox
  - Opera
  - Safari

## Known Bugs & Issues
* UX is not perfect - ran out of time. Ideally I would want the background to scale seamlessly and I would make some buttons on mobile device placed in a more UX friendly way.
* 

## Deployment
* Ensured deployed page on Heroku loads up correctly.
* Ensured Debug variable in app.py file is set to False.
* Confirmed that there is no difference between the deployed version and the development version.
