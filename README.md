# UAlbany Virtual Tour Campus Map
Programmed by Akinde Mendoza, Jeremy J. Lam, Joseph A. Zarakas, Othmane Benkhalifa, & Godswill Utionkpan, for Professor Kimberly Cornell's Fall 2023 CINF 405 class.
# Setup Instructions

## Prerequisites

Ensure you have Python 3.9 or later installed on your system. If not, follow the instructions below to install Python and Git.

### Install Python (if not already installed)

1. Visit the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/)
2. Download the latest version of Python 3 for your operating system.
3. Follow the installation instructions for your operating system.

### Install Git for (if Python is not installed)

1. Visit the official Git website(Windows): [https://gitforwindows.org/](https://gitforwindows.org/)
3. Download the latest version of Git for your platform.
4. Follow the installation instructions for your operating system.

## Project Setup

1. Clone the private repository using SSH:

    ```bash
    git clone git@github.com:your-username/UAlbanyVirtualTour.git
    ```

    Replace `your-username` with your actual GitHub username.

2. Navigate to the project directory:

    ```bash
    cd UAlbanyVirtualTour
    ```

3. Install the required dependencies and set up the Django project:

    ```bash
    python manage.py setup
    ```

    This script will check for and install the required dependencies, create and activate a virtual environment, and set up the Django project.

    The virtual tour map will be accessible at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## In Case of Errors

While the script should install any missing dependencies, there are still certain situations that it cannot account for. 

If the setup command crashes before it can start the server, make sure that Python 3, Pip, and Git are installed on your device.  

If you still continue to have issues, ensure that Python is installed in your computer's system path and run the following command in Command Prompt to install Django under it:

```bash
py -m pip install Django
```

After you complete this process, navigate back to the UAlbanyVirtualTour repository, and run the setup command again. 

## Project Structure

- **campusmap/**: Django project directory.
- **venv/**: Virtual environment directory.
- **requirements.txt**: List of Python packages required for the project.


## License

This project is licensed under the [MIT License](LICENSE)
