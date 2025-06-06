# Import Flask and extensions
from flask import Flask, request, jsonify
from flask_cors import CORS

# Import your Blueprints
from routes.authroutes import auth_bp
from routes.otp import otp_bp
from routes.analysis_routes import ana_bp
from routes.case_routes import case_bp
from routes.report import report_bp
from routes.invitation import invitation_bp
from routes.conversation_routes import conversation_bp

# Import your config & initialization
from config.config import init_mail, mail, get_mongo_connection

# Create Flask app
app = Flask(__name__)

# Initialize Flask-Mail
init_mail(app)

# Setup CORS for frontend dev environments (macOS, React/Vue)
CORS(app,
     resources={r"/*": {
         "origins": [
             "http://localhost:3000",
             "http://127.0.0.1:3000",
             "http://localhost:8080",
             "http://127.0.0.1:8080"
         ],
         "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
         "allow_headers": [
             "Content-Type",
             "Authorization",
             "X-Requested-With",
             "x-auth-token",
             "Accept"
         ],
         "supports_credentials": True
     }})

# Disable trailing slash redirection
app.url_map.strict_slashes = False

# Register your Blueprints
app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(otp_bp, url_prefix='/api/otp')
app.register_blueprint(ana_bp, url_prefix='/api/analysis')
app.register_blueprint(case_bp, url_prefix='/api/cases')
app.register_blueprint(report_bp, url_prefix='/api/report')
app.register_blueprint(conversation_bp, url_prefix='/api/messages')
app.register_blueprint(invitation_bp, url_prefix='/api/invitation')

# Initialize MongoDB connection
m = get_mongo_connection()
print("MongoDB connected to:", m.db.name)



@app.after_request
def apply_cors_headers(response):
    origin = request.headers.get("Origin")
    if origin:
        response.headers["Access-Control-Allow-Origin"] = origin
    response.headers["Access-Control-Allow-Credentials"] = "true"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization,x-auth-token"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    return response



# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7070)







# # Import Flask and other necessary modules
# from flask import Flask

# from flask_cors import CORS

# # Import your Blueprints
# from routes.report import report_bp
# from routes.authroutes import auth_bp
# from routes.otp import otp_bp
# from routes.analysis_routes import ana_bp
# from routes.case_routes import case_bp
# # from routes.report import report_bp
# from config.config import init_mail, mail,get_mongo_connection
# from routes.invitation import invitation_bp
# # Create Flask app
# app = Flask(__name__)

# # Initialize mail
# init_mail(app)

# # Configure CORS properly
# CORS(app, 
#      resources={r"/*": {
#          "origins": [
#              "http://localhost:8080", 
#              "http://127.0.0.1:8080", 
#              "http://localhost:3000", 
#              "http://127.0.0.1:3000"
#          ],
#          "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
#          "allow_headers": ["Content-Type", "Authorization", "X-Requested-With", "x-auth-token", "Accept"],
#          "supports_credentials": True
#      }})

# # Disable strict slashes to prevent redirects
# app.url_map.strict_slashes = False

# # Register Blueprints with correct prefixes
# app.register_blueprint(auth_bp, url_prefix='/api/auth')
# app.register_blueprint(otp_bp, url_prefix='/api/otp')
# app.register_blueprint(ana_bp, url_prefix='/api/analysis')
# app.register_blueprint(case_bp, url_prefix='/api/cases')
# app.register_blueprint(report_bp,url_prefix='/api/report')
# app.register_blueprint(invitation_bp, url_prefix='/api/invitation')
# # app.register_blueprint(report_bp, url_prefix='/api/reports')
# m=get_mongo_connection()
# print("The value is ",m.db.name)

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
