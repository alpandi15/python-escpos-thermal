from waitress import serve
import main

serve(main.app, host='localhost', port=5000)
