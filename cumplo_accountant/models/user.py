from cumplo_common.models import Credentials, Session, User


class LoggedUser(User):
    """User with Cumplo credentials configured and a valid session."""

    credentials: Credentials
    session: Session
