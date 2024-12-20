# Criminal Face Detection Surveillance System  

This project is a real-time face recognition surveillance system designed for identifying individuals and providing detailed information from a pre-existing database.  

---

## Features  
- Detect and recognize faces in real-time using a webcam.  
- Integrates a customizable database (`known_faces` directory) for storing images of known individuals.  
- Displays details such as name, age, and criminal history for recognized faces.  
- Highlights recognized faces with green rectangles and provides zoomed-in details for suspects, while marking unrecognized faces in red.  

---

![Website-FrontEnd](https://github.com/user-attachments/assets/c2cd0c91-7280-48d2-b507-0d2d3b6df0e9)


---

## How to Set Up and Run  

Follow these steps to set up and use the application:  

1. **Download the Repository**  
   - Click the green **Code** button to download the ZIP file or clone the repository using:  
     ```bash  
     git clone <repository-url>  
     ```  

2. **Extract Files**  
   - If downloaded as a ZIP file, extract the contents to your desired directory.  

3. **Install Dependencies**  
   - Ensure Python is installed. Install required libraries using:  
     ```bash  
     pip install flask opencv-python deepface  
     ```  

4. **Open in VS Code**  
   - Navigate to the project directory in your terminal and open it in Visual Studio Code:  
     ```bash  
     cd <project-folder>  
     code .  
     ```  

5. **Add Known Faces**  
   - Place images of known individuals in the `known_faces` directory. Ensure filenames match the identifiers in the `FACE_INFO` dictionary in `app.py`.  
   - Example: Add an image named `luqmaan_rasheed.jpg` to match the `luqmaan_rasheed` entry in the dictionary.  

6. **Edit the `FACE_INFO` Dictionary**  
   - Update `FACE_INFO` in `app.py` with relevant details for each individual:  
     ```python  
     "name_in_directory": {"age": XX, "crime": "Description of the crime"}  
     ```  

7. **Run the Application**  
   - Start the Flask server:  
     ```bash  
     python app.py  
     ```  

8. **Access the Application**  
   - Open your web browser and navigate to `http://127.0.0.1:5000/` to access the interface.  

---

## Notes  
- To test live recognition, ensure your webcam is connected and functioning.  
- Logs and errors during recognition are displayed in the terminal for debugging.  
- Modify `index.html` in the `templates` folder for UI customization.  

---

## Screenshots  
(Add a screenshot of your interface or a snapshot of live detection in action here.)  

---

## Technologies Used  
- **Backend**: Python, Flask  
- **Frontend**: HTML, CSS  
- **Libraries**: OpenCV, DeepFace  
