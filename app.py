import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Election Guide Assistant",
    page_icon="🗳️",
    layout="centered"
)

# 2. Custom Styling
st.markdown("""
    <style>
    .main {
        background-color: #fafafa;
    }
    .stAlert {
        border-radius: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Data Structure
election_phases = {
    "Voter Registration": {
        "icon": "📝",
        "summary": "The foundation of your participation. You must be on the rolls to vote.",
        "steps": ["Check eligibility (Age 18+)", "Fill out Form 6 (or local equivalent)", "Verify your name in the Electoral Roll"],
        "timeline": "Best done 2-3 months before; usually closes weeks before polling.",
        "progress": 25
    },
    "Candidate Research": {
        "icon": "🔍",
        "summary": "Know who is asking for your vote. Review their history and promises.",
        "steps": ["Read Party Manifestos", "Check Candidate Affidavits (Criminal/Financial records)", "Watch debates or public meetings"],
        "timeline": "Active during the 3-4 weeks leading up to the election.",
        "progress": 50
    },
    "The Silence Period": {
        "icon": "🤫",
        "summary": "A 48-hour window for voters to reflect without campaign noise.",
        "steps": ["Campaigning stops", "Check your designated Polling Booth location", "Keep your Voter ID/Identity proof ready"],
        "timeline": "Starts 48 hours before polling begins.",
        "progress": 75
    },
    "Polling & Results": {
        "icon": "🗳️",
        "summary": "The final step: casting your ballot and waiting for the outcome.",
        "steps": ["Visit the booth", "Verify identity & get the ink mark", "Cast vote on EVM/Paper", "Wait for Result Day"],
        "timeline": "Polling day is a set date; Results usually follow within days.",
        "progress": 100
    }
}

# 4. Header Section
st.title("🗳️ Election Process Assistant")
st.markdown("#### Your interactive guide to understanding democracy, step-by-step.")
st.divider()

# 5. Interactive Assistant Logic
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Navigation")
    choice = st.radio("Go to phase:", list(election_phases.keys()))

with col2:
    phase_data = election_phases[choice]
    st.subheader(f"{phase_data['icon']} {choice}")
    st.info(phase_data['summary'])
    
    st.write("**Key Actions:**")
    for step in phase_data['steps']:
        st.write(f"- {step}")
    
    st.warning(f"**Timeline:** {phase_data['timeline']}")
    
    # Progress Tracking
    st.write(f"Guide Completion:")
    st.progress(phase_data['progress'])

# 6. FAQ Section (Makes the app feel complete)
st.divider()
with st.expander("Common Questions (FAQ)"):
    st.write("**What if I lost my Voter ID?**")
    st.write("You can often use other government-approved photo IDs (like a Passport or Driver's License) if your name is already in the electoral roll.")
    
    st.write("**How do I find my polling station?**")
    st.write("Most election commissions provide an 'Online Voter Portal' where you can search by your ID number or name.")

# 7. Footer
st.caption("Developed to promote civic awareness. Check your local Election Commission website for official dates.")