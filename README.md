# Weather Data Visualization

Weather Data Visualization is a Streamlit-based application that allows users to analyze and visualize real-time weather data. Leveraging the OpenWeatherMap API, the app provides interactive visualizations and insights into weather patterns.

## Features

- **Real-time Weather Data Fetching**: Retrieves current weather data for specified locations using the OpenWeatherMap API.
- **Interactive Visualizations**: Displays dynamic charts and graphs to help users understand weather trends.
- **User-Friendly Interface**: Designed with Streamlit to offer an intuitive and responsive user experience.

## Deployment

The Weather Data Visualization app is deployed on Streamlit Community Cloud, enabling easy access and sharing.

To access the deployed app:

1. **Visit the App URL**: Navigate to [https://weather-data-visualization.streamlit.app/](https://weather-data-visualization.streamlit.app/) in your web browser.
2. **Interact with the App**: Use the provided interface to input location details and view corresponding weather visualizations.

## Local Setup and Usage

To run the Weather Data Visualization app locally:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/dattatejaofficial/Weather-Data-Visualization.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd Weather-Data-Visualization
   ```

3. **Set Up a Virtual Environment (Optional but Recommended)**:

   ```bash
   python3 -m venv env
   ```

   Activate the virtual environment:

   - On Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source env/bin/activate
     ```

4. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

5. **Obtain an OpenWeatherMap API Key**:

   - Visit [OpenWeatherMap](https://openweathermap.org/api) to register and get your free API key.

6. **Set Your API Key**:

   - In the `app.py` file, replace the placeholder with your actual API key.

7. **Run the Streamlit App**:

   ```bash
   streamlit run app.py
   ```

   This command will start the Streamlit server and open the app in your default web browser.

## Project Structure

- `app.py`: Main Streamlit application script that runs the weather data visualization app.
- `requirements.txt`: List of required Python packages for the project.
- `weather_api.ipynb`: Jupyter Notebook for fetching and visualizing weather data (optional for local analysis).

## Dependencies

- `streamlit`
- `requests`
- `matplotlib`
- `plotly`
- `pandas`
- `numpy`

Ensure all dependencies are installed by running `pip install -r requirements.txt`.

## Acknowledgments

- OpenWeatherMap for providing the weather data API.
- Streamlit for enabling easy deployment and sharing of the app.
- Matplotlib and Seaborn for data visualization.
- Pandas and NumPy for data manipulation.

For more detailed information, please refer to the project's GitHub repository: 
