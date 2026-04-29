import streamlit as st

st.set_page_config(page_title="Smart Mom Assistant", layout="centered")

st.title(" Smart Mom Decision Assistant")
st.markdown("Helping moms make confident decisions, faster ")

user_input = st.text_input(
    "Describe your baby's needs",
    placeholder="e.g. Best diaper for 6-month baby with sensitive skin under AED 150"
)

def detect_category(text):
    text = text.lower()
    if "diaper" in text:
        return "diaper"
    elif "cream" in text or "rash" in text:
        return "skincare"
    elif "bottle" in text or "feeding" in text:
        return "feeding"
    else:
        return "general"

def generate_response(text):
    text = text.lower()
    category = detect_category(text)

    results = []

    if category == "diaper":
        if "sensitive" in text:
            results.append({
                "name": " GentleCare Baby Diapers",
                "desc": "Designed for sensitive skin with rash protection.",
                "pros": ["Hypoallergenic", "Very soft", "Dermatologist tested"],
                "cons": ["Higher price"]
            })
        if "budget" in text or "under" in text:
            results.append({
                "name": " SoftTouch Premium Diapers",
                "desc": "Affordable everyday diaper with good absorption.",
                "pros": ["Budget-friendly", "Good absorption"],
                "cons": ["Less soft than premium options"]
            })

        results.append({
            "name": " ComfortPlus Daily Diapers",
            "desc": "Balanced option for daily comfort and value.",
            "pros": ["Comfortable", "Reliable"],
            "cons": ["Average for sensitive skin"]
        })

    elif category == "skincare":
        results.append({
            "name": " BabySoft Rash Cream",
            "desc": "Helps reduce irritation and soothe skin.",
            "pros": ["Quick relief", "Safe ingredients"],
            "cons": ["Needs frequent application"]
        })

    elif category == "feeding":
        results.append({
            "name": " EasyFeed Baby Bottle",
            "desc": "Anti-colic bottle for smooth feeding.",
            "pros": ["Reduces gas", "Easy to clean"],
            "cons": ["Slightly expensive"]
        })

    else:
        results.append({
            "name": " Starter Kit Bundle",
            "desc": "Includes essential baby products.",
            "pros": ["All-in-one", "Good for new moms"],
            "cons": ["May include unnecessary items"]
        })

    return results


if st.button(" Get Recommendations"):

    if user_input:

        st.subheader(" Recommended for You")

        products = generate_response(user_input)

        for product in products:
            st.markdown(f"### {product['name']}")
            st.write(product["desc"])

            st.write("**Pros:**")
            for p in product["pros"]:
                st.write(f"- {p}")

            st.write("**Cons:**")
            for c in product["cons"]:
                st.write(f"- {c}")

            st.markdown("---")

        st.subheader(" Why these recommendations?")

        if "sensitive" in user_input.lower():
            st.write(
                "Since you mentioned sensitive skin, I focused on products that are gentle, hypoallergenic, "
                "and less likely to cause irritation."
            )
        elif "budget" in user_input.lower() or "under" in user_input.lower():
            st.write(
                "Because budget is important here, I selected options that balance affordability with decent quality."
            )
        else:
            st.write(
                "I matched your needs with products that are commonly preferred for comfort, safety, and ease of use."
            )

        st.subheader(" Arabic Summary")
        st.write("تم اختيار هذه المنتجات بناءً على احتياجات طفلك من حيث الراحة والأمان والسعر.")

    else:
        st.warning("Please enter your requirement.")