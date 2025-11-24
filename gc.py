

# Exercise Title: The Smart Grocer Calculator

# Scenario:
# A grocery store sells three items:
# - Rice – ₹60 per kg
# - Sugar – ₹45 per kg
# - Oil – ₹120 per litre
 # The customer enters the quantity of each item they wish to buy.
# If the total cost exceeds ₹500, they get a 10% discount.
# Your Task:
# 1. Ask the user to input the quantities of each item.
# 2. Calculate the total cost based on prices.
# 3. If the total is above ₹500, apply a 10% discount.
# 4. Display the total before discount, discount applied, and final amount to pay.

import streamlit as st

st.title("🛒 The Smart Grocery Calculator")

# Get user name
name = st.text_input("Enter Your Name")
if name:
    st.success(f"🤗 Welcome To Our Store ***{name.upper()}*** 🙏") 

# Grocery items with prices
items = {
    "🍚 Rice": 60,
    "🍬 Sugar": 45,
    "🛢️ Oil": 120,    
}

st.header("⚖️ Quantity")
st.subheader("Please Enter Your Quantity Here:")

# Dictionary to store quantities
quantities = {}

# Dynamically generate number inputs for each item
for item, price in items.items():
    quantities[item] = st.number_input(f"{item} qty:", min_value=0.0, format="%.2f")

# Calculate and display bill only when the button is clicked
if st.button("Calculate"):
    st.subheader("🧾 Your Bill:")
    
    total = 0  # Initialize total
    for item, price in items.items():
        if quantities[item] > 0:
            item_total = quantities[item] * price
            st.write(f"{item} {quantities[item]} × {price} = {item_total:.2f}")
            total += item_total
    
    st.write("---")
    st.success(f"Total: {total:.2f}")

    # Apply discount if applicable
    if total >= 500:
        discount = total * 0.10
        discounted_total = total - discount
        st.success(f"🎉 Congrats! You got 10% discount: {discount:.2f}")
        st.success(f"💰 You have to pay: {discounted_total:.2f}")
    else:
        st.write("☹️ Sorry, you can't get any discount")
 







    
    
