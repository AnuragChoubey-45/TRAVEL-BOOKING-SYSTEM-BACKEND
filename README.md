# 🚖 Travel Booking System (Python + MySQL)

A fully functional **ride booking backend system** built using **Python** and **MySQL**. This project simulates a real-world travel booking experience — from account creation and ride selection to billing and travel history — all managed through a command-line interface and backed by a relational database.

---

## 🔍 Features

- ✅ **User Registration & Login**
  - Secure account creation using phone number and password
  - Login authentication system

- 🚗 **Ride Booking with Preferences**
  - Choose between **urgent** or **normal** rides
  - Add **gender preference** for comfort/safety
  - Get a real-time ride confirmation message

- 💰 **Billing System**
  - Enter travel distance
  - Instant bill calculation based on rate logic

- 📜 **Travel Log**
  - All journeys stored in a dedicated `customer_booking` table
  - View travel history anytime

- ❌ **Account Deletion**
  - User can delete their account and associated ride history

---

## 🧰 Tech Stack

| Component       | Tech Used            |
|----------------|----------------------|
| **Language**    | Python               |
| **Database**    | MySQL                |
| **Connector**   | `mysql.connector`    |
| **Interface**   | Command Line (CLI)   |

---

## 🗂️ Database Schema Overview

### `accounts` Table
+--------------+-------------+------+-----+---------+-------+
| Field        | Type        | Null | Key | Default | Extra |
+--------------+-------------+------+-----+---------+-------+
| Phone_number | bigint      | NO   | PRI | NULL    |       |
| name         | varchar(30) | YES  |     | NULL    |       |
| password     | varchar(10) | YES  |     | NULL    |       |
+--------------+-------------+------+-----+---------+-------+
### `customer_booking` Table
+------------------+-------------+------+-----+---------+-------+
| Field            | Type        | Null | Key | Default | Extra |
+------------------+-------------+------+-----+---------+-------+
| Phone_number     | bigint      | YES  | MUL | NULL    |       |
| Your_location    | varchar(30) | YES  |     | NULL    |       |
| Your_destination | varchar(30) | YES  |     | NULL    |       |
| time             | varchar(30) | YES  |     | NULL    |       |
| Driver           | varchar(60) | YES  |     | NULL    |       |
| Urgency          | varchar(30) | YES  |     | NULL    |       |
| date_booked      | varchar(90) | YES  |     | NULL    |       |
+------------------+-------------+------+-----+---------+-------+

## 📸 Sample Features in Action

> _Screenshots or sample command-line outputs can go here if available._  
> (E.g., Booking message: `"Your ride is scheduled and will be at your service at 5:30 PM."`)

---


