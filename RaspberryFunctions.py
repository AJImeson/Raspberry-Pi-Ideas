<<<<<<< HEAD
# Functions for Raspberry Pi Project
=======
import flask

>>>>>>> a325805876ddd8eceea16de88165024bcabbdcd1

def Start(): # Booting script
    
	print('Hello from Raspberry Pi! 🍓')
	print('Connecting to Raspberry Pi...')

Start()

<<<<<<< HEAD

 
        
=======
def File_Storage(): # File Storing Function
    
	def Files(directory: str) -> list: # Return files from directory
		
		return [f for f in os.listdir(directory)if os.path.isfile(os.path.join(directory, f))]

	def Save_Files(uploaded_file, save_path: str): # Save uploaded file to directory
		
		with open(save_path, 'wb') as f:
			f.write(uploaded_file.read())
   
File_Storage()
  
def Media_Streaming():
        
	from flask import Flask, send_file # For web based application 

	app = Flask(__name__) # Creates Object 

	@app.route('/stream/<filename>') # When web application is being used, boots media and returns to user
	def stream_media(filename):
    		return send_file(f"/home/pi/media/{filename}", as_attachment=False)

Media_Streaming()
>>>>>>> a325805876ddd8eceea16de88165024bcabbdcd1
