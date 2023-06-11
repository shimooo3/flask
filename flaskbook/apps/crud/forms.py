from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, length


# ユーザー新規作成とユーザー編集フォームクラス
class UserForm(FlaskForm):
    # ユーザーフォームのusername属性のラベルとバリデータを設定する
    username = StringField(
        "username",
        validators=[
            DataRequired(message="need username"),
            length(max=30, message="under 30"),
        ],
    )

    # ユーザーフォームemail属性のラベルとバリデータを設定する
    email = StringField(
        "mail",
        validators=[
            DataRequired(message="need mail"),
            Email(message="xxx@yyy"),
        ],
    )

    # ユーザーフォームpassword属性のラベルとバリデータを設定する
    password = PasswordField("password", validators=[DataRequired(message="need password")])

    # ユーザーフォームsubmitの文言を設定する
    submit = SubmitField("register new")