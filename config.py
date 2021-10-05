class Config:
    ENV = 'dev'
    if ENV == 'dev':
        user = 'postgres'
        pwd = 'startadventure'
        port = 5432
        SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pwd}@localhost:{port}/getadventure'.format(user=user, pwd=pwd, port=port)
    else:
        SQLALCHEMY_DATABASE_URI = 'postgresql://dvsryfmfnohvjy:d44c0493ff026c017e1d6d1967f593e8d41cd95edb3d26bd2dfb5175a6ed82c9@ec2-44-199-83-229.compute-1.amazonaws.com:5432/d5q9uqdl9ak143'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

