import streamlit as st
import cv2
import numpy as np
from io import BytesIO

st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Random Filter App")
st.write("by: A. Vera")

# Adding a function to cartoonize
import random

def cartoonize(img):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply median blur
    img_gray = cv2.medianBlur(img_gray, 5)

    # Create edge map
    edges = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

    # Color the edges
    color = cv2.bilateralFilter(img, 9, 250, 250)
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Apply random color map
    color_maps = [cv2.COLORMAP_WINTER, cv2.COLORMAP_COOL, cv2.COLORMAP_SUMMER, cv2.COLORMAP_AUTUMN, cv2.COLORMAP_BONE, cv2.COLORMAP_JET, cv2.COLORMAP_AUTUMN,
                  cv2.COLORMAP_RAINBOW, cv2.COLORMAP_SPRING, cv2.COLORMAP_HSV, cv2.COLORMAP_PINK, cv2.COLORMAP_HOT, cv2.COLORMAP_PARULA, cv2.COLORMAP_MAGMA,
                  cv2.COLORMAP_INFERNO, cv2.COLORMAP_PLASMA, cv2.COLORMAP_VIRIDIS, cv2.COLORMAP_CIVIDIS, cv2.COLORMAP_TWILIGHT, cv2.COLORMAP_TWILIGHT_SHIFTED,
                  cv2.COLORMAP_TURBO, cv2.COLORMAP_DEEPGREEN]
    random_color_map = random.choice(color_maps)
    cartoon = cv2.applyColorMap(cartoon, random_color_map)

    return cartoon

# Adding a file uploader
st.sidebar.header("Upload your image")
file_uploader = st.sidebar.file_uploader("Choose your image", type=["jpg", "png", "jpeg"])

# Display Image and Cartoonized version
if file_uploader is not None:
    file = BytesIO(file_uploader.read())
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), -1)
    cartoon = cartoonize(image)
    st.image(image, caption="Original Image", use_column_width=True)
    st.image(cartoon, caption="Cartoonized Image", use_column_width=True)



