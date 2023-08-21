# PillPal
#### A Pharma Bot for Jean Coutu
<hr>
Welcome to the readme file for the INSY660 Group Project.<br>
This project is designed by: <br>
<li>Avi Malhotra</li> 
<li>Syed Ammad Sohail</li>
<li>Moiz Shaikh</li>

Here is a description of what each file does:
<hr>
<h3>main.py</h3>
This is the main file that runs the program. It is the file that you should run to start the program. <br><br>
This file contains evokes the functions for each of the 6 use cases demonstrated in the presentation/report. Please note that you may require Python version 3.10 or above to run this project. <br><br>
<hr>
<h3>availability.py</h3>
This file contains the function that checks the availability of a medicine in JC stores. <br><br>
<hr>
<h3>fetch_google_forms.py</h3>
This file uses the Google API client to extract information about a new user post-registration from Google sheets. Click <a href="https://docs.google.com/forms/d/e/1FAIpQLSfykpsjSNPkpye9TrR37B9qvP5ms5Hr9s4EOTs6I65qm9CU5w/viewform?fbzx=7672851772923116123">here</a> to access the registration form. <br><br>
<hr>
<h3>find_nearest_store.py</h3>
This file contains the function that finds the nearest JC store to the user's location. It uses the 'pgeocode' library to compute distances between postal codes. <br><br>
<hr>
<h3>google_client_id.json</h3>
This file contains the Google API client ID. It is required to run the program. Note that this file is not visible on GitHub for security reasons. However, it is included in the code submission.
<hr>
<h3>LogicalModel JC.pdf</h3>
This file contains the logical model envisioned for this project (for the extra credit).
<hr>
<h3>medicine_dataset.csv</h3>
The <a href="https://www.kaggle.com/datasets/shudhanshusingh/250k-medicines-usage-side-effects-and-substitutes"> kaggle dataset</a> used for this project <br><br>
The dataset contains the following information for each drug:

<li>Drug name</li>
<li>Adverse reactions and side effects</li>
<li>Drug interactions</li>
<li>Drug class</li>
<li>Substitute drugs</li>
<li>Active ingredients </li><br>
Dataset Related Info.:

<li>There are total of 5 substitutes columns in the dataset.</li>
<li>There are total of 41 Side Effects columns in the dataset. Drugs with less side effects have those columns as blank.</li>
<li>There are total of 5 usage columns in the dataset.</li>
<li>All other columns have their own individual identity.</li>
<hr>

<h3>order.py</h3>
This file is used to place an order for a medicine. It produces a text file containing the order details for each order.<br><br>
<hr>
<h3>order_details.txt</h3>
A sample text file containing the order details for a sample order. <br><br>
<hr>
<h3>prescription_refill.py</h3>
This file contains the function that refills a prescription for a user. It requires user authentication to refill an order. <br><br>

<hr>
<h3>README.md</h3>
This is the file you are reading right now! :D
<hr>
<h3>recommendations.py</h3>
This file contains the function that recommends medicines and/or its substitutes to the user based on their symptoms. It uses the rake-nltk library to extract keywords from user input using natural language heuristics. RAKE stands for 'Rapid Automatic Keyword Extraction' and by considering co-occurrence information, the rake algorithm provides a more context-aware approach to keyword extraction.<br><br>
This file also contains a function that searches the 'medicine_dataset.csv' for available medicine.
<hr>
<h3>store_locations.py</h3>
This file contains a dictionary of the JC store locations in Montreal. The information is stored in key (zip code) value (address) pairs. <br><br>
<hr>
<h3>token.json</h3>
This file stores the user credentials. Note that this file is not visible on GitHub for security reasons. However, it is included in the code submission.
<hr>
<h3>user_functions.py</h3>
This file contains two helper functions that are used to register a new user and to authenticate an existing user. <br><br>

<hr>
<h3>users.csv</h3>
This csv file is the database that stores all user information extracted from Google sheets.

