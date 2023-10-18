from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField
from wtforms.validators import InputRequired, Email

class LoginForm(FlaskForm):
    email = EmailField(
      "Email",
      validators=[
        InputRequired("メールアドレスを入力してください。"),
        Email("メールアドレス形式で入力してください。")
      ]
    )
    password = PasswordField(
      "Password",
      validators=[InputRequired("パスワードを入力してください。")]
    )