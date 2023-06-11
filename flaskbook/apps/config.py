from pathlib import Path

basedir = Path(__file__).parent.parent

class BaseConfig:
    SECRET_KEY = "viceversa"
    WTF_CSRF_SECRET_KEY = "aegis"
    
class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'local.sqlite'}"
    SQLAlchemy_TRACK_MODIFICATIONS = False
    SQLAlchemy_ECHO = True
    
class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'testing.sqlite'}"
    SQLAlchemy_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    
config = {
    "testeing": TestConfig,
    "local": LocalConfig
}