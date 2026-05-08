# Domain Entities - Backend

## Entity Relationship

```
+------------+       +------------+       +-----------+       +-------+
|  Expense   | *---1 |   Card     |       | Category  |       | User  |
+------------+       +------------+       +-----------+       +-------+
| id (PK)    |       | id (PK)    |       | id (PK)   |       | id(PK)|
| date       |       | name       |       | name      |       | name  |
| amount     |       | created_at |       | created_at|       | created_at|
| memo       |       | updated_at |       | updated_at|       | updated_at|
| card_id(FK)|       +------------+       +-----------+       +-------+
| category_id(FK)|
| user_id(FK)|
| created_at |
| updated_at |
+------------+
```

## Entities

### Expense
| Field | Type | Constraints |
|-------|------|-------------|
| id | Integer (PK) | Auto-increment |
| date | Date | NOT NULL |
| amount | Integer | NOT NULL, > 0 |
| memo | String(255) | Nullable |
| card_id | Integer (FK → cards.id) | Nullable, SET NULL on delete |
| category_id | Integer (FK → categories.id) | Nullable |
| user_id | Integer (FK → users.id) | Nullable, SET NULL on delete |
| created_at | DateTime | Auto, NOT NULL |
| updated_at | DateTime | Auto on update |

### Card
| Field | Type | Constraints |
|-------|------|-------------|
| id | Integer (PK) | Auto-increment |
| name | String(100) | NOT NULL, UNIQUE |
| created_at | DateTime | Auto, NOT NULL |
| updated_at | DateTime | Auto on update |

### Category
| Field | Type | Constraints |
|-------|------|-------------|
| id | Integer (PK) | Auto-increment |
| name | String(100) | NOT NULL, UNIQUE |
| is_default | Boolean | Default: False |
| created_at | DateTime | Auto, NOT NULL |
| updated_at | DateTime | Auto on update |

### User
| Field | Type | Constraints |
|-------|------|-------------|
| id | Integer (PK) | Auto-increment |
| name | String(100) | NOT NULL, UNIQUE |
| created_at | DateTime | Auto, NOT NULL |
| updated_at | DateTime | Auto on update |

## Notes
- 금액은 Integer (원 단위, 소수점 없음)
- Category 삭제 시: 관련 expense의 category_id를 "기타" 카테고리 ID로 변경
- Card/User 삭제 시: 관련 expense의 FK를 NULL로 설정
