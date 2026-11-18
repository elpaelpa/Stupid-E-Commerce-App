# E-Commerce Database Schema

## ER Diagram

```mermaid
erDiagram
    CATEGORY ||--o{ PRODUCT : "contains"
    VENDOR ||--o{ PRODUCT : "sells"
    PRODUCT ||--o{ INVENTORY : "stocked as"
    WAREHOUSE ||--o{ INVENTORY : "holds"
    PRODUCT ||--o{ REVIEW : "receives"

    CATEGORY {
        int category_id PK
        varchar name "NOT NULL, UNIQUE"
        text description
    }

    VENDOR {
        int vendor_id PK
        varchar name "NOT NULL"
        varchar email
        varchar phone
        varchar address
    }

    PRODUCT {
        int product_id PK
        varchar name "NOT NULL"
        text description
        decimal price "NOT NULL"
        int category_id FK
        int vendor_id FK
    }

    WAREHOUSE {
        int warehouse_id PK
        varchar name "NOT NULL"
        varchar address
        varchar city
        varchar state
        int capacity
    }

    INVENTORY {
        int product_id PK, FK
        int warehouse_id PK, FK
        int quantity "NOT NULL, DEFAULT 0"
        datetime last_updated
    }

    REVIEW {
        int review_id PK
        int product_id FK
        varchar reviewer_name
        int rating "CHECK 1-5"
        text comment
        date review_date
    }
```

## Tables

| Table | Purpose |
|---|---|
| **Category** | Product categories (e.g. Electronics, Books) |
| **Vendor** | Sellers who list products |
| **Product** | Product name, description, price; links to its category and vendor |
| **Warehouse** | Storage locations |
| **Inventory** | Quantity of each product in each warehouse (junction table) |
| **Review** | Customer ratings (1–5) and comments for products |

## Relationships

- **Category → Product** (1:N): each product belongs to one category.
- **Vendor → Product** (1:N): each product is sold by one vendor.
- **Product ↔ Warehouse** (M:N): resolved through **Inventory**, which stores the quantity per warehouse.
- **Product → Review** (1:N): a product can have many reviews.

## Derived Values

- **Average rating** = `AVG(Review.rating)` per product (computed, not stored).
- **Current availability** = `SUM(Inventory.quantity)` per product; "In Stock" if > 0.
