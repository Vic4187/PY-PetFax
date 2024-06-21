from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return 'Hello, PetFax!'

    #Register Blueprint
    from . import pet
    app.register_blueprint(pet.bp)

    return app