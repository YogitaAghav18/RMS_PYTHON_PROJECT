RMS_PYTHON_PROJECT(RESTAURANT MANAGEMENT SYSTEM) -:
###################################################

## INTRODUCTION-

This project is a simple restaurant management system that allows users to place an order, see the menu, display their bill, make payments, and receive a thank-you message. The project is implemented using the Python programming language in an object-oriented manner. It has a menu list that is displayed to users so they can select their desired food items. Once an order is placed, the system shows the price and the user is expected to make a payment. The program also has a GUI interface built on the Tkinter library. Finally, the project is capable of receiving user input from a file and creating a menu for the restaurant.


## DESCRIPTION-

This code defines a class called RMS which simulates a virtual coffee shop. The class contains methods to welcome users, display the menu, take orders, prepare orders, serve orders, display the bill, verify payment, thank the user, and manage the overall order process.
The class takes the restaurant name and menu items as input during initialization. It then interacts with the user through various methods to take orders, prepare and serve them, display the bill, and handle payment. The user can continue to place orders until they indicate they are done.
The last part of the code utilizes the tkinter library to create a graphical user interface (GUI) window for the virtual coffee shop. The window includes a welcome message, a 'START' button to begin the order process by calling the order_process method of the RMS class, and runs the GUI main loop.


## FLOW OF THE CODE-

1.  The RMS class is defined with various methods to manage the restaurant operations.
2.  The order_process method is the main method that controls the flow of the program:
    a. It starts by displaying a welcome message and the menu to the user.
    b. It then takes the user's order and checks if it is a valid item from the menu.
    c. If the order is valid, it prepares and serves the order, and then asks if the user wants to order anything else. If the user wants to order more, it loops back and takes the order again.
    d. Once the user is done with ordering, it displays the bill and asks for payment. If the payment is less than the bill amount, it prompts for the remaining payment. If there is more payment than the bill, it        returns the change.
    e. Finally, it thanks the user for visiting the coffee shop.
3.  The control of the program is handled in the if __name__=="__main__": block:
    a. It reads input from a file (user input.txt) to get the restaurant name and the menu items with their prices.
    b. It creates an instance of the RMS class with the restaurant name and the menu.
    c. It then creates a GUI interface using tkinter with a welcome message and a "START" button, which triggers the order_process method.

When the user clicks the "START" button on the GUI, it initiates the order process, and the user can interact with the virtual coffee shop by placing orders and making payments through the GUI interface.
Overall, this code simulates the functionality of a real coffee shop, providing a user-friendly experience for placing orders and making payments.


## HOW TO RUN-

1.  To run this Python code, you need to have Python installed on your system. You also need to install the tkinter library.
2.  Download the RMS.py file from the repository and save it to a directory. Also, save the user input.txt file to the same directory. The user  input.txt file contains information about the restaurant name (rn)      and menu (rm).
    Make sure the user input.txt file is correctly formatted with the restaurant name on the first line, followed by a list of food names separated by commas on the second line, and corresponding prices separated     by commas on the third line.
3.  Open the terminal or command prompt and navigate to the directory where the RMS.py file is saved. After running the code, the system first reads the restaurant name and menu items from the user input.txt file     and initializes the RMS class instance with these values.
4.  The GUI interface is opened when running the code.The user can then click on the "START" button to begin the order process,which includes: taking orders, preparing orders, serving orders, displaying the bill,     verifying payments, and thanking the user. The user can order multiple items, and the total cost will be displayed at the end. If the payment is successful, the system thanks the user for visiting the     
    restaurant, and the GUI interface closes.


