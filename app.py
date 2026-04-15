import streamlit as st
import numpy as np
from PIL import Image, ImageDraw
from sklearn.cluster import KMeans

# -------------------------------
# Function: Create Color Palette
# -------------------------------
def create_color_palette(dominant_colors, palette_size=(300, 50)):
    palette = Image.new("RGB", palette_size)
    draw = ImageDraw.Draw(palette)

    swatch_width = palette_size[0] // len(dominant_colors)

    for i, color in enumerate(dominant_colors):
        draw.rectangle(
            [i * swatch_width, 0, (i + 1) * swatch_width, palette_size[1]],
            fill=tuple(color)
        )

    return palette


# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🎨 Top 3 Color Extractor")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert to numpy
    image = image.convert("RGB")  # remove alpha if present
    img_array = np.array(image)

    # Reshape image for KMeans
    pixels = img_array.reshape(-1, 3)

    # Normalize
    pixels = pixels / 255.0

    # Apply KMeans
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    kmeans.fit(pixels)

    # Get dominant colors
    colors = kmeans.cluster_centers_

    # Convert back to 0-255
    colors = (colors * 255).astype(int)

    st.write("### 🎯 Dominant Colors (RGB):")
    st.write(colors)

    # Create and show palette
    palette = create_color_palette(colors)
    st.image(palette, caption="Color Palette")