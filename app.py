import streamlit as st

# --- App Configuration ---
st.set_page_config(page_title="🔄 Unit Converter", layout="centered")

# --- Dark Mode Toggle ---
dark_mode = st.sidebar.toggle("🌙 Dark Mode")

# --- Apply Dark Mode Style ---
if dark_mode:
    st.markdown(
        """
        <style>
        body {
            background-color: #1e1e1e;
            color: white;
        }
        .stApp {
            background-color: #1e1e1e;
            color: white;
        }
        .stTextInput, .stSelectbox, .stNumberInput {
            background-color: #333 !important;
            color: white !important;
        }
        .css-1cpxqw2 {
            background-color: #333 !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# --- Title ---
st.title("🔄 Unit Converter App")
st.caption("Convert between units of length, weight, temperature, and more — now with dark mode!")

st.markdown("---")

# --- Conversion Logic ---
def convert_units(value, from_unit, to_unit, category):
    if category == "Length":
        factors = {
            "Meter": 1,
            "Kilometer": 1000,
            "Centimeter": 0.01,
            "Millimeter": 0.001,
            "Mile": 1609.34,
            "Yard": 0.9144,
            "Foot": 0.3048,
            "Inch": 0.0254
        }
        return value * factors[from_unit] / factors[to_unit]

    elif category == "Weight":
        factors = {
            "Kilogram": 1,
            "Gram": 0.001,
            "Pound": 0.453592,
            "Ounce": 0.0283495
        }
        return value * factors[from_unit] / factors[to_unit]

    elif category == "Temperature":
        if from_unit == to_unit:
            return value
        elif from_unit == "Celsius":
            return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
        elif from_unit == "Fahrenheit":
            return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin":
            return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
    return None

# --- Unit Categories ---
unit_categories = {
    "Length": ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile", "Yard", "Foot", "Inch"],
    "Weight": ["Kilogram", "Gram", "Pound", "Ounce"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin"]
}

# --- UI Controls ---
category = st.sidebar.selectbox("Select Unit Category", list(unit_categories.keys()))
from_unit = st.selectbox(f"From Unit ({category})", unit_categories[category])
to_unit = st.selectbox(f"To Unit ({category})", unit_categories[category])
value = st.number_input("Enter Value", min_value=0.0, format="%.4f")

# --- Convert Button ---
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    if result is not None:
        st.success(f"{value} {from_unit} = {round(result, 4)} {to_unit}")
    else:
        st.error("Conversion not supported.")

# --- Footer ---
st.markdown("---")
st.caption("🛠️ Developed using Python & Streamlit for seamless conversions ")
