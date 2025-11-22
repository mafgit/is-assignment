# Mini Hospital Dashboard

### Instructions/Steps:
From root of codebase, do the following
1. Make a virtual environment: `python -m venv venv`
1. Create a new terminal OR write this command to activate it: `venv\Scripts\activate` (cmd) or `source venv\\Scripts\\activate` (bash)
1. Run `pip install -r requirements.txt`
1. Make `.env` file and add environment variable: `FERNET_KEY=FL412z9eXAQmFJSMhREWbAdr0FuIax4I-BDM-ezHzXA=` as an example
1. Or generate a new key using `generate_key()` function in `src/encryption_utils.py`
1. Reset database by deleting `hospital.db` and running `reset()` function inside `database.py`
1. Run `streamlit run src/home.py`
1. Sample username and passwords:
    - Dr_Bob: doc123
    - Alice_recep: rec123
    - admin: admin123
    
### This project features:
- Fernet Encryption & Decryption
- Hashing
- Masking
- GDPR
- Asking Consent
- Role-Based Access (Doctors, Receptionists, Admins)
- Date Retention Policy
- Action Logging
- Analytic Graph
- Adding/Editing Patients
- Navigation
- Login/Logout

### Made using:
- Streamlit
- SQLite
- Python