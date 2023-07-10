# Raspberrypi_academic-project
Environmental sensors data retrieval
Raspberry Pi Academic Project: Environmental Sensors Data Retrieval

This project aims to retrieve data from environmental sensors using a Raspberry Pi. The data collected includes pressure, temperatures from the humidity sensor and pressure sensor, and humidity level.
Project Requirements

To run this project, you will need the following:

    Raspberry Pi board
    Establishing secure shell connection
    Environmental sensors compatible with Raspberry Pi
    Python 3 installed on the Raspberry Pi

Installation and Setup

    Clone the project repository from GitLab:

    shell

git clone <repository_url>

Connect the environmental sensors to the Raspberry Pi following the manufacturer's instructions.

Install the required Python packages:

shell

    pip install -r requirements.txt

Usage

The project consists of the following main files:

    env_sensors.py: Contains functions to retrieve and display sensor data, as well as calculate averages.
    main.py: Implements the main program to collect and display the average sensor data over a specified period.

To use the project, follow these steps:

    Open the terminal on the Raspberry Pi.

    Navigate to the project directory:

    shell

cd RaspberryPi_academic-project

Run the main.py file:

shell

    python main.py

    This will start collecting sensor data every second for one minute and display the average values.

Documentation

Detailed documentation for each function can be found within the source code files.

    env_sensors.py:
        get_sensors_data(): Retrieves data from the environmental sensors and returns a dictionary of the collected values.
        display_sensors_data(data): Takes the sensor data dictionary as input and displays the data with one decimal place for each value.
        get_sensors_data_list(nb_data=60, frequency=1): Retrieves a series of sensor data points with a specified number of data points and frequency and returns a list of the collected data.
        get_sensors_data_average(data_list): Calculates the average of a series of sensor data points provided as a list and returns the averaged data.

Contribution

Contributions to this project are welcome. If you find any issues or have suggestions for improvement, please open an issue or submit a pull request on the project's GitLab repository.

Note: This README file provides an overview of the project and its usage. For detailed instructions and documentation, please refer to the source code files and comments.
