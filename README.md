# GestureCalc

**GestureCalc** is an interactive AI-powered calculator that allows users to solve math problems using hand gestures. The app utilizes OpenCV, cvzone, and hand-tracking to capture user gestures, and Google's Gemini AI to process and solve the drawn equations. The UI is built using Streamlit for real-time interaction.

## Features

- **Hand Gesture Recognition**: Tracks and recognizes specific hand gestures to draw, erase, and send input.
- **AI-Generated Solutions**: Sends drawn math problems to Google's Gemini AI for solution processing.
- **Real-Time Processing**: Uses Streamlit for live video feed and AI output display.
- **Eraser Tool**: Includes a gesture-controlled eraser to modify the drawn input.

## Tech Stack

- **OpenCV**: For video capture and image processing.
- **cvzone**: For easy hand gesture detection.
- **Streamlit**: For the front-end UI and live feed integration.
- **Google Gemini AI**: For solving math problems based on drawn input.
- **PIL (Python Imaging Library)**: To handle image format conversion for AI processing.
- **NumPy**: To handle the drawing canvas.

## How It Works

1. **Hand Gestures**:
   - Index finger up: Draw on the canvas.
   - Two fingers up: Erase parts of the drawing.
   - Flat hand (five fingers up): Send the drawing to AI for processing.
   - Three fingers up: Clears the entire canvas.

2. **AI Processing**:
   - Once the equation is drawn, a flat-hand gesture triggers AI processing.
   - The AI processes the drawing and displays the solution.

3. **Streamlit Interface**:
   - The live video feed is displayed alongside the AI output text.
   - Users can start and stop the gesture-based drawing process.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Jason-Ampere/GestureCalc.git
    cd GestureCalc
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the Google Gemini AI API key by replacing the placeholder in the code:

    ```python
    genai.configure(api_key="your-api-key")
    ```

4. Run the app:

    ```bash
    streamlit run app.py
    ```

## Usage

- To start drawing, ensure the **Run** checkbox is checked in the UI.
- Use hand gestures to draw and erase as described above.
- The AI-generated solution will be displayed in real-time once the flat-hand gesture is recognized.

## Future Improvements

- **Mobile Compatibility**: Enhance for mobile usage.
- **Additional Math Functions**: Add support for more complex math functions.

## Author

- **Sarthak Maiti**  
  [GitHub](https://github.com/Jason-Ampere)  
  [LinkedIn](https://www.linkedin.com/in/sarthakmaiti1234/)
