
# Password Manager Project

Welcome to the Password Manager Project! 🎉

This project started as a simple script to manage passwords but evolved into a robust application leveraging Hexagonal Architecture and SOLID Design Principles. The goal was to create a flexible and maintainable password management system tailored to specific needs.

---

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [Adding the Password Manager to PATH](#adding-the-password-manager-to-path)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Introduction

Managing passwords securely and efficiently is crucial in today's digital age. This Password Manager provides a command-line interface (CLI) tool that allows users to generate, store, update, and retrieve passwords with ease. By adopting advanced architectural patterns, the project ensures scalability, testability, and adaptability to future requirements.

---

## Features
- **Generate New Passwords**: Create strong, random passwords for your accounts.
- **Store Passwords Securely**: Save passwords in a local file or integrate with cloud services like Google Drive.
- **Update Existing Passwords**: Modify passwords for existing accounts.
- **Retrieve Passwords**: Fetch stored passwords when needed.
- **Extensible Design**: Easily integrate with different storage backends or password generators.
- **Testable Codebase**: Comprehensive unit and integration tests for reliability.

---

## Architecture

### Hexagonal Architecture
The project follows the **Hexagonal Architecture (Ports and Adapters)** pattern, promoting separation of concerns and independence from external technologies:
- **Domain Layer**: Contains business logic and domain models.
- **Application Layer**: Handles application-specific logic and orchestrates domain operations.
- **Infrastructure Layer**: Contains implementations of external services (e.g., file storage, cloud services).

### SOLID Design Principles
The codebase adheres to **SOLID Principles** to enhance maintainability and scalability:
1. **Single Responsibility Principle**: Each class has one responsibility.
2. **Open/Closed Principle**: Classes are open for extension but closed for modification.
3. **Liskov Substitution Principle**: Objects of a superclass should be replaceable with objects of subclasses.
4. **Interface Segregation Principle**: Many client-specific interfaces are better than one general-purpose interface.
5. **Dependency Inversion Principle**: Depend upon abstractions, not concretions.

---

## Installation

### Prerequisites
- Python 3.6+
- `pip` package installer
- Virtual Environment (Optional but Recommended)

### Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/password-manager.git
   cd password-manager
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts ctivate
   # On Unix or Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install the Package in Editable Mode**
   ```bash
   pip install -e .
   ```

---

## Usage

Run the main script to interact with the Password Manager:

```bash
python main.py
```

### Available Commands
- **Generate a New Password**:
  ```bash
  python main.py new_password --username your_username
  ```

- **Update an Existing Password**:
  ```bash
  python main.py update_password --username your_username
  ```

- **Retrieve a Password**:
  ```bash
  python main.py get_password --username your_username
  ```

- **Upload Passwords to Google Drive**:
  ```bash
  python main.py upload_passwords
  ```

### Configuration
#### Password Storage
- Passwords are stored in `passwords.txt` by default.
- Storage paths and adapters can be configured.

#### Password Generator
- Generates random passwords of a specified length.
- Custom generators can be implemented by following the `PasswordGenerator` interface.

---

## Adding the Password Manager to PATH
To run the password manager from any directory in your command prompt, you can create a batch file and add it to your system PATH on Windows.

### Steps

1. **Create a Batch File:**
    - Create a new file named `password_manager.bat` (or any name you like)
    - Place the code described in `password_manager.txt` into the file

2. **Move the Batch File to a Directory in PATH:**
    - Go to your `Enviromental Varibles` if using Windows. If not using windows, raise LookForHelpElsewhere( IdontKnowHow2Help Sorry )
    - Add directory to PATH

3. **Test the Command:**
    - Try running `password_manager -help` it should work 👌

---

## Project Structure

```plaintext
password-manager/
├── application/
│   ├── commands/
│   ├── input_handler/
│   └── __init__.py
├── domain/
│   ├── models/
│   ├── services/
│   ├── ports/
│   └── __init__.py
├── infrastructure/
│   ├── adapters/
│   └── __init__.py
├── tests/
│   ├── application/
│   ├── domain/
│   ├── infrastructure/
│   └── __init__.py
├── main.py
├── setup.py
├── requirements.txt
└── README.md
```

- **`application/`**: Application layer containing command, and input handlers.
- **`domain/`**: Domain layer with business logic and models.
- **`infrastructure/`**: Infrastructure layer with external service implementations.
- **`tests/`**: Test suite for unit tests.
- **`main.py`**: Entry point for running the CLI application.
- **`setup.py`**: Setup script for package installation.
- **`requirements.txt`**: List of project dependencies.

---

## Contributing

Contributions are welcome! Please follow these steps:

1. **Fork the Repository**
2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Commit Your Changes**
   ```bash
   git commit -m "Add your message"
   ```
4. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```
5. **Create a Pull Request**

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Happy coding! 😊 If you have any questions or need assistance, feel free to open an issue or reach out.

personal email: rigomoreirar@gmail.com (Might change later)
