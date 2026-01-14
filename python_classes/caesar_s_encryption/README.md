# 🔐 Caesar Cipher (Python)

## 📌 Description

This project was completed during the **FreeCodeCamp Python Certification** learning path.
It implements a **Caesar cipher**, a classic encryption technique that shifts letters in the alphabet by a fixed number of positions.

The project demonstrates how to:
- validate function inputs
- manipulate strings efficiently
- handle optional parameters
- implement both encryption and decryption logic in Python

## ⚙️ Features

### 🔹 Encryption and Decryption
- Encrypts text by shifting letters forward in the alphabet
- Decrypts text by shifting letters backward when `encrypt=False`
- Preserves letter casing (uppercase and lowercase)
- Leaves non-alphabetical characters unchanged

### 🔹 Input Validation
- Ensures the shift value is an integer
- Ensures the shift value is between **1 and 25**
- Returns clear error messages when validation fails

## 📤 Usage

### Encrypting text
```python
caesar("hello", 3)
```
Output:
```
khoor
```

### Decrypting text
```python
caesar("khoor", 3, False)
```
Output:
```
hello
```

### Helper functions
```python
encrypt(text, shift)
decrypt(text, shift)
```

## 🧪 Example (ROT13)

```python
encrypted_text = "Pbhentr vf sbhaq va hayvxryl cynprf."
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)
```

Output:
```
Counter is found in unlikely places.
```

## 🧠 Concepts Practiced

- Caesar cipher logic
- Input validation with `isinstance`
- Optional function parameters
- String translation with `str.maketrans()`

## 👤 Author

**Julien Hinlang**  
Project completed during the **FreeCodeCamp Python Certification** learning path.
