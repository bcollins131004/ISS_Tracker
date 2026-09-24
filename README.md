# ISS_Tracker
This GitHub provides files and des
cription of an International Space Station (ISS), web server site that tracks the live location of the ISS.


<img width="1855" height="892" alt="image" src="https://github.com/user-attachments/assets/42e6f65c-5188-4aac-953e-0bd86851a52c" />


It tracks the live location of the ISS and displays it on a map of the world. It also shows the path of the ISS for the duration of the length of your session.

## Instructions:

### File Structure:

<img width="186" height="228" alt="image" src="https://github.com/user-attachments/assets/51268709-123a-462a-a1db-3a05e46d7108" />

                                                                                                                                                                                     
### File Outlines:
#### app.py:

This is the code file that is ran when the host URL is visited. It points the page to the index file which displays the interface. Using this [API](https://api.wheretheiss.at/v1/satellites/25544), the live location, speed and altitude of the ISS can be retrieved.

