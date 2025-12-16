class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.user_id = user_id
        self.name = name
        self.email = email

    # 1️⃣ Constructor from a string
    @classmethod
    def from_string(cls, data_str: str):
        """
        Expected format: "id,name,email"
        """
        try:
            user_id, name, email = data_str.split(",")
            return cls(int(user_id), name.strip(), email.strip())
        except ValueError:
            raise ValueError("Invalid string format. Use 'id,name,email'")

    # 2️⃣ Constructor from a dictionary
    @classmethod
    def from_dict(cls, data_dict: dict):
        """
        Expected keys: user_id, name, email
        """
        try:
            return cls(
                user_id=data_dict["user_id"],
                name=data_dict["name"],
                email=data_dict["email"]
            )
        except KeyError as e:
            raise KeyError(f"Missing key: {e}")

    # 3️⃣ Constructor with default values
    @classmethod
    def guest_user(cls):
        return cls(0, "Guest", "guest@example.com")

    def __repr__(self):
        return f"User(id={self.user_id}, name='{self.name}', email='{self.email}')"
