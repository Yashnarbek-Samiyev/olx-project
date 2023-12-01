# OLX Project

## Overview

The OLX Project is an online marketplace where users can buy and sell various products. This project is built using the Django web framework, providing a scalable and feature-rich platform for users to interact with the marketplace.

## Features

- **User Authentication:** Users can sign up, log in, and manage their profiles.
- **Product Listings:** Users can create, view, update, and delete product listings.
- **Category Management:** Products can be categorized, allowing users to easily navigate through different types of products.
- **Transactions:** Facilitate buying and selling transactions between users.
- **Internationalization:** Support for multiple languages using Django's internationalization framework.

## Technologies Used

- **Django:** The web framework used to build the backend.
- **Django Rest Framework:** Facilitates the creation of APIs for the project.
- **Django Modeltranslation:** Enables translation of model fields for internationalization.
- **HTML, CSS, JavaScript:** Used for building the frontend interface.
- **Bootstrap:** Frontend framework for responsive and modern design.
- **SQLite (or your preferred database):** Database system for storing application data.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Django Rest Framework
- Django Modeltranslation
- Django Rosetta


### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/olx-project.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:

    ```bash
    python manage.py migrate
    ```

4. Create a superuser:

    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:

    ```bash
    python manage.py runserver
    ```

6. Access the admin panel at `http://127.0.0.1:8000/admin/` to add initial categories and manage the application.

## Usage

1. Visit `http://127.0.0.1:8000/admin/` to log in and manage categories and user profiles.
2. Access the main application at `http://127.0.0.1:8000/` to browse and interact with product listings.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-name`
5. Submit a pull request.

## License

This project is licensed under the [UIC Group](LICENSE).

## Acknowledgments

- Thanks to the Django and Django Rest Framework communities for providing robust tools for web development.
- Inspired by the OLX platform, creating a simplified version to demonstrate Django development skills.
