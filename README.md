# Digital Twin Backend

## Overview

This is the backend system for the Digital Twin project. It provides functionalities for managing digital twins and handling data processing.

## Prerequisites

- Python 3.11.6 or later

## Installation

### Install Python

If you don't have Python installed, follow these steps:

1. Download Python from the [official website](https://www.python.org/downloads/).
2. Run the installer and follow the instructions.

### Create Virtual Environment

1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command to create a virtual environment:

   ```bash
   python3.11 -m venv venv
   ```

### Activate Virtual Environment

Before installing the project dependencies, activate the virtual environment:

- On macOS/Linux:

  ```bash
  source venv/bin/activate
  ```

- On Windows:

  ```bash
  venv\Scripts\activate
  ```

### Install Requirements

Once the virtual environment is activated, install the required packages using the following command:

```bash
pip install -r requirements.txt
```

### Configuration

1. Inside the `modules/config` directory, create a file named `.env`.
2. Add the necessary environment variables to the `.env` file. For example:

   ```plaintext
   DATABASE_URL=your_database_url_here
   OTHER_VARIABLE=other_value
   ```

## Usage

To run the backend server, execute the following command:

```bash
python main.py
```

The server should start running on the specified port.

## Additional Instructions

- Ensure that the required database is set up and accessible.
- Configure any other settings in the `.env` file as needed.
- Make sure to update the `.gitignore` file to exclude sensitive information like the `.env` file and any local cache or temporary files.