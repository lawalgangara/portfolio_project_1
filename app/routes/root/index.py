from app.create_app import create_app

app = create_app()

@app.route('/')
@app.route('/home')
def home_page():
    return "Hello, welcome to the home page of my biography"

if __name__ == '__main__':
    app.run()

