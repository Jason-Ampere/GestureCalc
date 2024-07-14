import cv2
import cvzone
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from PIL import Image
import streamlit as st
import google.generativeai as genai

# Streamlit UI setup
st.set_page_config(layout="wide")
st.title("GestureCalc")
st.text("by Sarthak Maiti")

col1, col2 = st.columns([2, 1])

with col1:
    run = st.checkbox("Run", value=False)
    FRAME_WINDOW = st.image([])

with col2:
    st.title("Answer")
    outputTextArea = st.empty()

# Configure the AI model with the provided API key
genai.configure(api_key="api-key")
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize video capture and hand detector
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(staticMode=False, maxHands=1, modelComplexity=1, detectionCon=0.7, minTrackCon=0.5)

prev_pos = None
canvas = None
ai_processing = False
eraser_radius = 50  # Radius of the eraser

def send_to_ai(model, canvas):
    pil_image = Image.fromarray(canvas)
    response = model.generate_content(["Solve this math problem", pil_image])
    return response.text

def draw(info, prev_pos, canvas):
    fingers, lmList = info
    current_pos = None
    if fingers == [0, 1, 0, 0, 0]:  # Index finger up
        current_pos = tuple(map(int, lmList[8][0:2]))  # Ensure coordinates are integers
        if prev_pos is None:
            prev_pos = current_pos
        cv2.line(canvas, prev_pos, current_pos, (246, 52, 126), 10)
    elif fingers == [0, 1, 1, 1, 0]:
        canvas = np.zeros_like(canvas)
    elif fingers == [0, 1, 1, 0, 0]:  # Eraser gesture (index and middle fingers up)
        eraser_pos = tuple(map(int, lmList[12][0:2]))  # Use middle finger for eraser position
        cv2.circle(canvas, eraser_pos, eraser_radius, (0, 0, 0), -1)  # Draw black circle to "erase"
    return current_pos, canvas

def get_hand_info(img):
    hands, _ = detector.findHands(img, draw=False, flipType=True)
    if hands:
        hand = hands[0]
        lmList = hand["lmList"]
        fingers = detector.fingersUp(hand)
        return fingers, lmList
    return None

while True:
    if run:
        success, img = cap.read()
        if not success:
            st.error("Failed to read from webcam.")
            break

        img = cv2.flip(img, 1)  # Flip the image horizontally

        if canvas is None:
            canvas = np.zeros_like(img)

        info = get_hand_info(img)

        if info:
            fingers, lmList = info
            prev_pos, canvas = draw(info, prev_pos, canvas)
            if fingers == [1, 1, 1, 1, 1] and not ai_processing:
                ai_processing = True
                st.info("Processing...")
                outputText = send_to_ai(model, canvas)
                ai_processing = False
                outputTextArea.empty()  # Clear previous text
                outputTextArea.text(outputText)  # Display new text
        else:
            prev_pos = None  # Reset the previous position when the hand is not detected

        # Combine the image with the canvas
        image_combined = cv2.addWeighted(img, 0.5, canvas, 0.5, 0)
        FRAME_WINDOW.image(image_combined, channels="BGR")

        if not run:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
