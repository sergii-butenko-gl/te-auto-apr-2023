
def test_signup_initial():
    user = dict(name="non_existing_user")
    
    assert user.name == "non_existing_user"

    user = None


def test_signup_final():
    user_name = "automation_test_removein_30_days_non_existing_user"
    user = dict(name=user_name)  # user.create()

    print(f"User '{user_name}' created")

    assert user.get('name') == 'jhbsdfbsdf'

    user = None  # user.remove()

    print(f"User '{user_name}' removed")
