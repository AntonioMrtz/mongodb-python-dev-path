## 📌 Schema Design Analysis

### 1️⃣ Identify & Quantify Data Needs
- Define **items** and quantify them (size, frequency of access).
- Identify **application read and write patterns**.
- Quantify **read/write frequency** and determine the most common operations.
- Design schema **optimized for frequent operations**.

### 2️⃣ Identify Relationships Between Objects
- **One-to-One**  
- **One-to-Many**  
- **Many-to-Many**  

### 3️⃣ Embedding vs. References
#### 📍 Key Considerations
✅ **Embedding** → Store data **together** for efficiency.  
✅ **Referencing** → Normalize data for **scalability and flexibility**.

- **Data that is accessed together should be stored together.**
- **Is the app read-heavy or write-heavy?**  
  - Read-heavy → Consider **embedding**.  
  - Write-heavy → Consider **referencing** to avoid document growth issues.

---

## 📌 When to Embed?
✅ **Use embedding when:**
- **Simplicity is preferred**.
- There is a **"has-a" or "contains"** relationship.
- **Data is frequently retrieved together**.
- Updates **should be atomic**.
- **Minimal data duplication** is required.
- The **document size is manageable** (MongoDB 16MB limit).
- **Child cannot exist without the parent**.

❌ **Avoid embedding if:**
- Large amounts of embedded data cause document bloat.
- Data duplication makes updates **hard to manage**.
- **Children can exist independently** (use references instead).

## 📌 One-to-One Relationships
#### ✅ When to Embed?
- If both entities are always queried together.
- Example: **User Profile → User Settings** (single document).

```json
{
  "_id": ObjectId("123"),
  "name": "John Doe",
  "settings": {
    "theme": "dark",
    "notifications": true
  }
}
```

#### ✅ When to Reference?
- When the child object may exist **independently**.
- Types of referencing:
  - One object has a foreign key of the other.The most accessed document should store the foreign key.
  - Both reference each other with foreign keys.

```json
{
  "_id": ObjectId("123"),
  "name": "John Doe",
  "profile_id": ObjectId("456")
}
```
```json
{
  "_id": ObjectId("456"),
  "user_id": ObjectId("123"),
  "bio": "Software Developer"
}
```

## 📌 One-to-Many Relationships
#### ✅ When to Embed?
- **Few child documents per parent.**
- **Data is always queried together.**
- Example: **Blog → Comments**.

```json
{
  "_id": ObjectId("123"),
  "title": "MongoDB Best Practices",
  "comments": [
    { "user": "Alice", "text": "Great article!" },
    { "user": "Bob", "text": "Thanks for sharing." }
  ]
}
```

#### ✅ When to Reference?
- **If the child collection grows indefinitely**.
- Types of referencing:
  - Parent or children has the foreign key of each other.
  - Both parent and children have foreign key.
- Example: **User → Orders**.

```json
{
  "_id": ObjectId("123"),
  "name": "John Doe",
  "orders": [ ObjectId("order1"), ObjectId("order2") ]
}
```

```json
{
  "_id": ObjectId("order1"),
  ...
}
```

## 📌 Many-to-Many Relationships
#### ✅ When to Embed?
- Data duplication is acceptable.
- Example: **Author → Books (Embedded List)**.

```json
{
  "_id": ObjectId("123"),
  "name": "J.K. Rowling",
  "books": [
    { "title": "Harry Potter 1" },
    { "title": "Harry Potter 2" }
  ]
}
```

#### ✅ When to Reference?
- **Avoid bidirectional references (expensive joins).**
- Use an **intermediate "junction" collection**.
- Example: **Students & Courses (Many-to-Many Reference)**.

```json
// Students Collection
{
  "_id": ObjectId("s1"),
  "name": "Alice",
  "enrolled_courses": [ ObjectId("c1"), ObjectId("c2") ]
}

// Courses Collection
{
  "_id": ObjectId("c1"),
  "title": "MongoDB 101",
  "students_enrolled": [ ObjectId("s1"), ObjectId("s2") ]
}

// Junction Collection (Enrollment)
{
  "_id": ObjectId("e1"),
  "student_id": ObjectId("s1"),
  "course_id": ObjectId("c1"),
  "enrollment_date": "2024-03-08"
}
```


## 📌 Final Takeaways
| **Use Case**     | **Embedding** ✅ | **Referencing** ✅ |
|------------------|----------------|-----------------|
| **One-to-One**   | ✔️ If always accessed together | ✔️ If separate access is needed |
| **One-to-Many**  | ✔️ If small & accessed together | ✔️ If array is unbounded |
| **Many-to-Many** | ❌ Not recommended | ✔️ Use an intermediate collection |
