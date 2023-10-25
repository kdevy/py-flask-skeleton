from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, StringField
from wtforms.validators import InputRequired, Email, Length, EqualTo, Regexp

class SginUpForm(FlaskForm):
    name = StringField(
        "Name",
        validators=[
            InputRequired("名前を入力してください。"),
        ],
        render_kw={"placeholder": "Name"}
    )
    email = EmailField(
        "Email",
        validators=[
            InputRequired("メールアドレスを入力してください。"),
            Email("メールアドレス形式で入力してください。")
        ],
        render_kw={"placeholder": "Email"}
    )
    password = PasswordField(
        "Password",
        validators=[
            InputRequired("パスワードを入力してください。"),
            Length(min=8, message="パスワードは8文字以上で入力してください。"),
            Regexp(regex="[0-9A-Za-z]+", message="パスワードは英数字のみ利用できます。"),
        ],
        render_kw={"placeholder": "Password"}
    )
    confirm_password = PasswordField(
        "Confirm password",
        validators=[
            InputRequired("確認用パスワードを入力してください。"),
            EqualTo("password", message="パスワードが一致しません。"),
        ],
        render_kw={"placeholder": "Password"}
    )