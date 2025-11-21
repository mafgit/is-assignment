import re


def isUsernameValid(username: str):
    return re.match(r"^[a-zA-Z0-9_]{3,20}$", username)


def isPasswordValid(password: str):
    if password != password.strip():
        return False
    if len(password) < 6:
        return False

    return True


def isLoggedIn(session_state):
    return session_state.get("role") in ["admin", "doctor", "receptionist"] and session_state.get("user_id", 0) > 0
