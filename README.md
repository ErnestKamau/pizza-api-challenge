# Pizza Restaurants API

A RESTful API for managing pizza restaurants, pizzas, and their relationships.

---

## Setup Instructions

1. **Clone the repository**  
   ```sh
   git clone <git@github.com:ErnestKamau/pizza-api-challenge.git>
   cd pizza-api-challenge/server
   ```

2. **Install dependencies using Pipenv**  
   ```sh
   pipenv install
   pipenv shell
   ```

3. **Set Flask environment variables**  
   ```sh
   export FLASK_APP=app.py
   export FLASK_ENV=development
   ```

4. **Run the Flask server**  
   ```sh
   flask run
   ```
   > **Note:** You must be in the `server` directory to run the above command.

---

## Database Migration & Seeding

1. **Initialize migrations (first time only):**
   ```sh
   flask db init
   ```

2. **Generate migration scripts:**
   ```sh
   flask db migrate -m "Initial migration"
   ```

3. **Apply migrations:**
   ```sh
   flask db upgrade
   ```

4. **Seed the database:**
   ```sh
   python seed.py
   ```

---

## Route Summary

| Method | Endpoint                        | Description                                 |
|--------|---------------------------------|---------------------------------------------|
| GET    | `/restaurants`                  | List all restaurants                        |
| GET    | `/restaurants/<int:id>`         | Get a single restaurant by ID               |
| DELETE | `/restaurants/<int:id>`         | Delete a restaurant by ID                   |
| GET    | `/pizzas`                       | List all pizzas                             |
| POST   | `/restaurant_pizzas`            | Add a pizza to a restaurant (with price)    |

---

## Example Requests & Responses

### 1. List all restaurants

**Request:**  
```sh
GET /restaurants
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "Mama's Pizza",
    "address": "123 Main St",
    "pizzas": [
      { "id": 1, "name": "Margherita", "ingredients": "Tomato, Mozzarella, Basil" }
    ]
  }
]
```

---

### 2. Get a single restaurant

**Request:**  
```sh
GET /restaurants/1
```

**Response:**
```json
{
  "id": 1,
  "name": "Mama's Pizza",
  "address": "123 Main St",
  "pizzas": [
    { "id": 1, "name": "Margherita", "ingredients": "Tomato, Mozzarella, Basil" }
  ]
}
```

**If not found:**
```json
{ "error": "Restaurant not found" }
```

---

### 3. Delete a restaurant

**Request:**  
```sh
DELETE /restaurants/1
```

**Response:**  
Status: `204 No Content`  
(Empty body)

**If not found:**
```json
{ "error": "Restaurant not found" }
```

---

### 4. List all pizzas

**Request:**  
```sh
GET /pizzas
```

**Response:**
```json
[
  { "id": 1, "name": "Margherita", "ingredients": "Tomato, Mozzarella, Basil" }
]
```

---

### 5. Add a pizza to a restaurant

**Request:**  
```sh
POST /restaurant_pizzas
Content-Type: application/json

{
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2
}
```

**Response:**
```json
{
  "id": 7,
  "price": 15,
  "pizza_id": 1,
  "restaurant_id": 2,
  "pizza": {
    "id": 1,
    "name": "Margherita",
    "ingredients": "Tomato, Mozzarella, Basil"
  },
  "restaurant": {
    "id": 2,
    "name": "Pizza Palace",
    "address": "456 Side St"
  }
}
```

**If validation fails:**
```json
{ "error": ["Price must be between 1 and 30."] }
```

---

## Validation Rules

- **RestaurantPizza.price**: Must be between 1 and 30 (inclusive).  
  If not, returns error: `"Price must be between 1 and 30."`

---

## Using Postman

1. **Import Endpoints:**  
   - Use the route summary above to create requests in Postman.
   - Set the request type (GET, POST, DELETE) and URL (e.g., `http://localhost:5000/restaurants`).

2. **For POST requests:**  
   - Set `Content-Type` to `application/json`.
   - Provide a JSON body as shown in the examples above.

3. **View Responses:**  
   - Inspect the response body and status code for each request.

---

## Notes

- Make sure to run all commands from the `server` directory.
- The database file (`pizza_restaurants.db`) will be created in the `instance` directory.