import streamlit as st
import heapq

# -----------------------------------------------------------
#                  🎨 CLEAN MODERN UI SETUP
# -----------------------------------------------------------

st.set_page_config(
    page_title="A* Medical Diagnostic Assistant",
    page_icon="🩺",
    layout="centered"
)

st.markdown(
    """
    <style>
        body { background-color: #f7f7f7; }
        .title { text-align:center; font-size: 40px; font-weight:700; margin-bottom:20px; }
        .subtitle { text-align:center; font-size: 18px; color:#666; margin-bottom:40px;}
        .card {
            background: white;
            padding: 25px;
            border-radius: 18px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.06);
            margin-bottom: 20px;
        }
        .result-card {
            background: #ffffff;
            padding: 20px;
            border-radius: 16px;
            margin-bottom: 16px;
            border: 1px solid #eee;
        }
        .condition-title {
            font-size: 22px; 
            font-weight: 700; 
            margin-bottom: 6px;
            color: #333;
        }
        .score {
            font-size: 16px; 
            color:#4CAF50; 
            font-weight:600;
            margin-bottom:12px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<div class='title'>🩺 AI Diagnostic Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Powered by A* Medical Reasoning</div>", unsafe_allow_html=True)


# -----------------------------------------------------------
#       🧠 MEDICAL KNOWLEDGE GRAPH (A* SEARCH SPACE)
# -----------------------------------------------------------

medical_graph = {
    "Psoriasis": {
        "symptoms": ["redness", "scaling", "itching", "thick patches"],
        "severity": 0.9,
        "next_steps": "Use topical steroids, moisturizers, avoid triggers. See dermatologist for chronic cases."
    },
    "Eczema": {
        "symptoms": ["itching", "dryness", "red patches", "flaking"],
        "severity": 0.7,
        "next_steps": "Moisturize regularly, use mild soaps, avoid allergens. Consult dermatologist if severe."
    },
    "Fungal Infection": {
        "symptoms": ["redness", "itching", "ring-shaped rash", "peeling"],
        "severity": 0.65,
        "next_steps": "Use antifungal creams, keep skin dry. Seek medical care if spreading rapidly."
    },
    "Contact Dermatitis": {
        "symptoms": ["rash", "redness", "itching", "burning"],
        "severity": 0.5,
        "next_steps": "Avoid irritants, use soothing creams. Visit doctor if symptoms persist."
    },
    "Rosacea": {
        "symptoms": ["facial redness", "bumps", "sensitivity", "burning"],
        "severity": 0.6,
        "next_steps": "Avoid spicy foods/sun exposure, use gentle skin care. Dermatologist may prescribe medication."
    }
}


# -----------------------------------------------------------
#                 ⭐ A* DIAGNOSTIC ALGORITHM
# -----------------------------------------------------------

def heuristic(symptom_matches: int, total_symptoms: int, severity: float) -> float:
    """Higher = more likely disease"""
    if total_symptoms == 0:
        return 0
    match_score = (symptom_matches / total_symptoms) * 0.7
    severity_score = severity * 0.3
    return match_score + severity_score


def a_star_diagnosis(user_symptoms):
    """Returns ranked list of most likely diseases via A* reasoning."""
    pq = []
    results = []

    for disease, data in medical_graph.items():
        symptom_matches = len(set(user_symptoms) & set(data["symptoms"]))
        h_score = heuristic(symptom_matches, len(data["symptoms"]), data["severity"])

        heapq.heappush(pq, (-h_score, disease))  # max-heap via negative score

    # Extract sorted results
    while pq:
        score, disease = heapq.heappop(pq)
        score = -score
        results.append((disease, score))

    return results


# -----------------------------------------------------------
#                       🧑‍⚕ USER INPUT
# -----------------------------------------------------------

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    st.write("### Describe your symptoms")
    user_input = st.text_area("Enter symptoms separated by commas:", placeholder="redness, itching, flaking...")

    submit = st.button("Analyze Condition 🩺", type="primary")

    st.markdown("</div>", unsafe_allow_html=True)


# -----------------------------------------------------------
#                       📊 RESULT OUTPUT
# -----------------------------------------------------------

if submit and user_input.strip() != "":
    symptoms = [s.strip().lower() for s in user_input.split(",")]

    results = a_star_diagnosis(symptoms)

    st.markdown("## 🔍 Most Likely Conditions")
    st.markdown("### (Based on symptom match + severity weighting + A* reasoning)\n")

    for disease, score in results:
        data = medical_graph[disease]
        match_count = len(set(symptoms) & set(data["symptoms"]))

        st.markdown("<div class='result-card'>", unsafe_allow_html=True)
        st.markdown(f"<div class='condition-title'>{disease}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='score'>Probability Score: {round(score*100)}%</div>", unsafe_allow_html=True)

        st.write("*Matched Symptoms:*", match_count)
        st.write("*Disease Symptoms:*", ", ".join(data["symptoms"]))
        st.write("*Recommended Next Steps:*", data["next_steps"])

        st.markdown("</div>", unsafe_allow_html=True)

else:
    st.info("Enter symptoms above and press *Analyze*.")