# FastAPI Library Management System

This project implements a backend system for a Library Management System using FastAPI and MongoDB. It provides a set of APIs for creating, listing, updating, and deleting student records in the system.

## Features

- Create new student records
- List students with optional filtering by country and age
- Retrieve individual student records by ID
- Update existing student records
- Delete student records

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** MongoDB

## Requirements

To run this project locally, you need to have the following installed:

- Python 3.x
- MongoDB
- Pip (Python package manager)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/library-management-system.git
```

2. Navigate to the project directory:

```bash
cd library-management-system
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up MongoDB:
   - Install MongoDB locally or use a cloud-based MongoDB service like MongoDB Atlas.
   - Update the MongoDB connection string in `app/db/connection.py`.

## Usage

1. Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

2. Open your web browser and navigate to http://localhost:8000/docs to access the Swagger UI.

   - Alternatively, you can use tools like Postman to interact with the APIs directly.

3. Use the provided APIs to perform CRUD operations on student records.

## Deployment

You can check out the application at [LINK](https://library-management-system-cu0l.onrender.com/docs)

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

![Our Application](https://github.com/N-epiphany/FastAPI_Library_Management_System/blob/main/applicationimage.png)
