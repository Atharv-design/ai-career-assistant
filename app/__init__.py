from flask import Flask
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Import blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.resume_routes import resume_bp
    from app.routes.job_routes import job_bp
    from app.routes.interview_routes import interview_bp
    from app.routes.roadmap_routes import roadmap_bp

    # Register
    app.register_blueprint(auth_bp)
    app.register_blueprint(resume_bp)
    app.register_blueprint(job_bp)
    app.register_blueprint(interview_bp)
    app.register_blueprint(roadmap_bp)

    return app