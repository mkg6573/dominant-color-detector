

# 🎨 Dominant Color Detector

A simple and interactive **Streamlit web app** that extracts the **top 3 dominant colors** from any uploaded image using **K-Means Clustering**.

🔗 **Live App:** [https://dominant-color-detector.streamlit.app/](https://dominant-color-detector.streamlit.app/)

---

## 🚀 Features

* 📤 Upload any image (JPG, PNG, JPEG)
* 🎯 Extract **Top 3 Dominant Colors**
* 🎨 Visualize colors as a **beautiful palette**
* ⚡ Fast and interactive UI using Streamlit
* 🧠 Uses **K-Means Clustering** for color extraction

---

## 🧠 How It Works

1. Image is uploaded by the user
2. Converted into a NumPy array
3. Reshaped into pixel format `(n_pixels, 3)`
4. Normalized to range `[0, 1]`
5. **K-Means clustering** is applied
6. Cluster centers represent **dominant colors**
7. Colors are displayed in:

   * RGB format
   * Visual palette

---

## 🖼️ Demo

👉 Upload an image and instantly get its top 3 dominant colors!

---

## 🛠️ Tech Stack

* Python 🐍
* Streamlit
* NumPy
* Pillow (PIL)
* Scikit-learn (KMeans)

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/your-username/dominant-color-detector.git
cd dominant-color-detector
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

OR (recommended):

```bash
python -m streamlit run app.py
```

---

## 📁 Project Structure

```
dominant-color-detector/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 💡 Future Improvements

* 🔢 Allow user to select number of colors (k)
* 📊 Show percentage of each color
* 🎨 Display HEX color codes
* 📱 Improve UI/UX

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and improve it 🚀

---

## 📬 Contact

If you like this project, feel free to connect!

---

## ⭐ Show Your Support

Give a ⭐ if you found this project helpful!

---

> Built with ❤️ using Streamlit & Machine Learning


