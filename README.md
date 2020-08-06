# Simple Python Flask app that utilizes Onshape API calls 

## Functionality
- Currently deployed to [heroku](pythoncontourapp.herokuapp.com)
- Allows users to input an Onshape Feature Studio URL, an image, and the title for the feature studio
- Users get led to another page that lets them change the scale of the image and threshold of the image mask before sending the data to the feature studio

## Todos: 
- Allow multiple contour functionality
- Fix multiple user logic
- Convert API call from Feature Studio Update to Update Feature Tree Contents
- Add more modifiers (just scale and threshold now)

### June 23rd 
Built a simple form (minimal error detection, must fix) that allows the user to copy their did, wid, and eid. The server then makes an API call to Onshape that returns configuration details.

Todo: have this API request serve as a method to error-check if the user inputs correct ids. Once a user inputs valid ids, add a list of valid API calls to use. 
Save to file? 
Send data back? 
STL viewer with plotly and Dash? 
