
# User Management API

This project is a **User Management API** built using **Django REST Framework (DRF)** and deployed using **Docker** on an **AWS EC2 Ubuntu instance**. It provides basic CRUD functionality for managing users in a MongoDB database.

---

## **Features**
- Create, Read, Update, and Delete (CRUD) operations for User Management.
- Validations for fields like email format and phone number length.
- Deployed with Docker for portability and scalability.
- Accessible publicly via AWS EC2.

---

## **User Schema**
The User object schema contains the following fields:
- `lastname` (string): User's last name.
- `dob` (date): User's date of birth.
- `address` (string): User's address.
- `gender` (string): User's gender.
- `email` (string): User's email address.
- `phone_number` (string): User's 10-digit phone number.

---

## **API Endpoints**
| Method | Endpoint          | Description                |
|--------|-------------------|----------------------------|
| POST   | `/users`          | Create a new user.         |
| GET    | `/users/{user_id}`| Retrieve a user by ID.     |
| PUT    | `/users/{user_id}`| Update a user's details.   |
| DELETE | `/users/{user_id}`| Delete a user.             |

---

## **Setup Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/GPrakashSivam/user_management_api
cd <your-project-directory>
```

### **2. Set Up Python Virtual Environment**
1. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### **3. Set Up Environment Variables**
Create a `.env` file in the project root directory and add the following:
```plaintext
SECRET_KEY=secret_key
MONGO_URI=mongo_connection_uri
MONGO_DB_NAME=user_management_db
```

### **4. Run the Project Locally**
Run and start the server:
```bash
python manage.py runserver
```

### **5. Docker Deployment (Optional)**
1. Build the Docker image:
   ```bash
   docker build -t user-management-api .
   ```

2. Run the container:
   ```bash
   docker run -d -p 8000:8000 user-management-api
   ```

---

## **Testing the API**

### **Base URL**
Use the following base URL to access the API:
```plaintext
http://<aws-ec2-public-ip>:8000
```

### **API Endpoints with Examples**

#### **1. Create a New User**
**Endpoint**: `/users`  
**Method**: `POST`  
**Request Body**:
```json
{
    "lastname": "Doe",
    "dob": "1990-01-01",
    "address": "123 Main St",
    "gender": "Male",
    "email": "john.doe@example.com",
    "phone_number": "1234567890"
}
```
**Response**:
```json
{
    "message": "User created successfully.",
    "user_id": "648c8f8e1d2f9b00017a8c5f"
}
```

---

#### **2. Retrieve a User by ID**
**Endpoint**: `/users/{user_id}`  
**Method**: `GET`  
**Example Request**:
```bash
curl http://<aws-ec2-public-ip>:8000/users/648c8f8e1d2f9b00017a8c5f
```
**Response**:
```json
{
    "lastname": "Doe",
    "dob": "1990-01-01",
    "address": "123 Main St",
    "gender": "Male",
    "email": "john.doe@example.com",
    "phone_number": "1234567890"
}
```

---

#### **3. Update a User**
**Endpoint**: `/users/{user_id}`  
**Method**: `PUT`  
**Request Body**:
```json
{
    "lastname": "Smith"
}
```
**Response**:
```json
{
    "message": "User updated successfully."
}
```

---

#### **4. Delete a User**
**Endpoint**: `/users/{user_id}`  
**Method**: `DELETE`  
**Example Request**:
```bash
curl -X DELETE http://<aws-ec2-public-ip>:8000/users/648c8f8e1d2f9b00017a8c5f
```
**Response**:
```json
{
    "message": "User deleted successfully."
}
```

---

## **Deployment on AWS EC2**
1. Launch an EC2 Ubuntu instance.
2. Install Docker and Docker Compose.
3. Transfer the project to the server and follow the Docker deployment steps mentioned above.

---

## **Security Notes**
- Set `DEBUG=False` in production.
- Restrict `ALLOWED_HOSTS` to specific IPs or domains.

---

## **Contributors**
- Gnanaprakash

---

## **License**
This project is licensed under the MIT License.
