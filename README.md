# **Hackers Poulette™ Contact Form**  
A simple Flask-based application that displays and processes a contact form for the Hackers Poulette™ website.

## **Project Overview**  
Hackers Poulette™ specializes in DIY Raspberry Pi kits and accessories. This application provides users with a contact form to reach the technical support team. It ensures proper data sanitization, validation, and anti-spam protection.  

### **Features**
- Backend implemented using Flask.
- Form fields include:
  - First Name & Last Name.
  - Email Address.
  - Country (Dropdown).
  - Gender (Radio buttons).
  - Message (Textarea).
  - Topics (Checkboxes: Repair, Order, Others).
- Server-side sanitization and validation of form inputs.
- Honeypot technique for anti-spam protection.
- Error messages displayed near corresponding fields.
- Feedback page summarizing submitted information.

---

## **Getting Started**

### **Prerequisites**
Ensure the following software is installed on your machine:
- Python (3.8 or later)
- Pip (Python package manager)

### **Installation**
1. Clone the repository:
   ```bash
   git clone https://github.com/serena1308/Python-Flask-Project.git
   cd Python-Flask-Project
   ```
2. Install the required Python packages:
   ```bash
   pip install flask
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser and visit:
   ```
   http://127.0.0.1:5000/
   ```

---

## **Project Structure**
```
Python-Flask-Project/
├── app.py                # Main application file
├── templates/            # Folder containing HTML templates
│   ├── base.html         # Base template for consistent layout
│   ├── form.html         # Contact form page
│   └── thanks.html       # Feedback page
```
---

## **Features in Detail**

### **1. Form Sanitization**
- Prevents XSS attacks by neutralizing potentially malicious user input.
- All inputs are escaped using Flask's `escape()` function.

### **2. Form Validation**
- Checks if all required fields are filled.
- Validates email format using a regex.

### **3. Honeypot Anti-Spam**
- Includes a hidden field (`honeypot`) in the form.
- Any value in this field triggers a spam detection error.

### **4. Error Handling**
- If errors are detected during validation, the form is redisplayed with:
  - Error messages next to invalid fields.
  - Previously entered values preserved.

### **5. Feedback Page**
- Upon successful submission, a "Thank You" page summarizes the user's input.

---

## **Usage**

### **Endpoints**
- **`GET /`**: Displays the contact form.
- **`POST /thanks`**: Processes the submitted form and displays feedback or errors.

### **Form Fields**
| Field          | Type         | Required?  | Notes                                                                 |
|----------------|--------------|------------|----------------------------------------------------------------------|
| First Name     | Text         | Yes        | The user's first name.                                               |
| Last Name      | Text         | Yes        | The user's last name.                                                |
| Email          | Email        | Yes        | Must be in a valid email format.                                     |
| Country        | Dropdown     | Yes        | Dropdown menu with preset country options.                           |
| Gender         | Radio Button | Yes        | Choose between "Male" and "Female".                                  |
| Message        | Textarea     | Yes        | User's message to the technical support team.                        |
| Topics         | Checkbox     | No         | Choose one or multiple topics: "Repair", "Order", or "Others".       |
| Honeypot       | Hidden Field | No         | Anti-spam field. Should always be left empty by legitimate users.    |

---

## **Security Considerations**

### **1. Cross-Site Scripting (XSS) Protection**
All user inputs are sanitized using the `escape()` function to prevent malicious scripts from being executed.

### **2. Server-Side Validation**
The application ensures all required fields are filled and valid before processing the data.

### **3. Server-Side Template Injection (SSTI) Prevention**
Flask's `Jinja2` template engine automatically escapes variables by default, mitigating SSTI risks.

