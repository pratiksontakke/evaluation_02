# Simple Transaction API

This project is a simple RESTful API for managing user accounts and financial transactions, built with FastAPI and SQLAlchemy.

## Features

*   **User Management:** Create, update, and retrieve user information.
*   **Transaction Management:**
    *   Deposit (add) and withdraw funds from an account.
    *   Transfer funds between users.
    *   View user balance and transaction history.
*   **Database Integration:** Uses SQLAlchemy to interact with a PostgreSQL database.

## Technology Stack

*   **Backend:** FastAPI
*   **ORM:** SQLAlchemy
*   **Database:** PostgreSQL (via Supabase)
*   **Schema Validation:** Pydantic
*   **Server:** Uvicorn

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd pratiksontakke-evaluation_02
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r backend/app/requirement.txt
    ```

4.  **Set up environment variables:**
    *   Rename `.env_example` in the `backend` directory to `.env`.
    *   Update the `SUPABASE_URI` with your actual PostgreSQL connection string:
    ```env
    SUPABASE_URI=postgresql://user:password@host:port/dbname
    ```

5.  **Run the application:**
    ```bash
    uvicorn backend.app.main:app --reload
    ```

6.  **Access the API documentation:**
    Navigate to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) in your browser to view and interact with the API endpoints via Swagger UI.