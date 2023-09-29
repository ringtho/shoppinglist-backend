# Shopping API

The Shopping API is a Django project designed to help users maintain a list of items they intend to purchase from a shopping store. This project provides a robust API for creating, updating, and managing shopping lists conveniently. It also includes features for user management.

## Features

- Create Shopping Lists: Users can create multiple shopping lists, each with its own set of items.

- Add and Remove Items: Users can add and remove items from their shopping lists.

- Update Item Details: Users can modify the details of items, such as quantity, category, or priority.

- Mark Items as Purchased: Items can be marked as purchased to keep track of what has already been bought.

- User Management: Users can sign up, login, manage their orders, and logout when done.

### Getting Started

#### Prerequisites

- Python 3.x
- Django
- Django Rest Framework... <b><i>(see requirements.txt for complete list)</i></b>

#### Installation

- Clone the repository:

```
git clone https://github.com/ringtho/shoppinglist-backend.git
cd shoppinglist-backend
```

- Create and activate a virtual environment using [this guide](https://docs.python.org/3/library/venv.html)

- Install the required packages:

```
pip install -r requirements.txt
```

- Apply migrations:

```
python3 manage.py migrate
```

- Start the development server:

```
python3 manage.py runserver [port]
```

The API will be accessible at http://127.0.0.1:8000/ or any port specified above

### Usage

#### 1. Authentication:

- The API supports token-based authentication. Obtain a token by sending a POST request to /api/v1/login/ with your username and password.

#### 2. Endpoints:

- /api/v1/orders/: Get a list of all ordered items or create a new one.
- /api/v1/orders/<order_id>/: Get details of a specific order item.
- /api/v1/login/: Login user.
- /api/v1/logout/: Logout user.
- /api/v1/register/: Register new user.
- /api/v1/me/: Get profile information of the logged in user.

#### 3. Examples:

- Create Shopping List:

```
curl -X POST -H "Authorization: Bearer <your_token>" -d "name=Groceries" http://127.0.0.1:8000/api/v1/orders/
```

- Add Item:

```
curl -X POST -H "Authorization: Bearer <your_token>" -d "name=Milk&quantity=2&list=1" http://127.0.0.1:8000/api/items/
```

### Contributing

If you'd like to contribute to this project, please follow these steps:

- Fork the repository
- Create a new branch (<b>git checkout -b feature/new-feature</b>)
- Make your changes and commit them (<b>git commit -m 'Add new feature'</b>)
- Push to the branch (<b>git push origin feature/new-feature</b>)
- Create a pull request

### License

This project is licensed under the MIT License - see the LICENSE file for details.
