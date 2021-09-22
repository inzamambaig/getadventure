
class Config:
    ENV = 'prod'
    if ENV == 'dev':
        user = 'postgres'
        pwd = 'startadventure'
        port = 5432
        SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pwd}@localhost:{port}/getadventure'.format(user=user, pwd=pwd, port=port)
    else:
        SQLALCHEMY_DATABASE_URI = 'postgres://usulnouomwtgla:3bc225afca6eb152cb470cafa5200b08b49127f6fbd4c378a3199744225b2a45@ec2-54-209-52-160.compute-1.amazonaws.com:5432/d1ltf69ig2melb'

    SQLALCHEMY_TRACK_MODIFICATIONS = False

