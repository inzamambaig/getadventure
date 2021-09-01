class Config:
    ENV = 'dev'
    if ENV == 'dev':
        user = 'postgres'
        pwd = 'Getanadventure'
        port = 5432
        SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pwd}@localhost:{port}/getadventure'.format(user=user, pwd=pwd, port=port)
    else:
        SQLALCHEMY_DATABASE_URI = ''

    SQLALCHEMY_TRACK_MODIFICATIONS = False