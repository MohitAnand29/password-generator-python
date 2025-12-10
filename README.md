# 🔐 Password Generator (Python)

A simple and customizable **Password Generator** built using Python.  
This script allows users to generate secure passwords by choosing:

- Number of **letters**
- Number of **symbols**
- Number of **numbers**

It then **shuffles** the characters to create a strong, unpredictable password.

This project is great for beginners learning:
- Python loops  
- Random module  
- Lists and string manipulation  
- Functions  
- Error handling (try/except)  
- Input validation  

---

## 🚀 Features

✔ User-defined password structure  
✔ Random selection of letters, numbers, and symbols  
✔ Characters are shuffled for stronger security  
✔ Clean and simple Python functions  
✔ Error handling for invalid inputs  
✔ Beginner-friendly code structure  

---

## 📌 Example Output

How many letters would you like in your password?
5
How many symbols would you like?
2
How many numbers would you like?
3

Before Shuffle: ['a', 'Q', 'm', 'x', 'k', '$', '&', '4', '9', '0']
After Shuffle: ['x', 'k', '4', '&', 'Q', 'm', '$', 'a', '0', '9']

Your password is: xk4&Qm$a09

---

## 🛠 Technologies Used

- **Python 3**
- `random` module

---

## 📂 Project Structure

Password_generator/
│
├── password_generator.py # Main Python script
├── README.md # Documentation


---

## 📜 Code Overview

### **Functions:**
- `letters_gen(count)` → Generates random letters
- `symbols_gen(count)` → Generates random symbols
- `numbers_gen(count)` → Generates random numbers
- Final list is shuffled using `random.shuffle()`
- `''.join()` converts list → final password string

---

## ▶️ How to Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/MohitAnand29/password-generator-python.git


### 2️⃣ Navigate into folder
cd password-generator-python

3️⃣ Run the Python script
python password_generator.py

📄 License
This project is open-source and free to use.

👨‍💻 Author
Mohit Anand
Python | JavaScript | React | C | C++
Learning full-stack development & improving problem-solving skills.
