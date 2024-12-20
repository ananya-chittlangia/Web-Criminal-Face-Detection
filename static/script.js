document.addEventListener('DOMContentLoaded', function() {
    // Fetch and display known faces
    fetch('/known_faces')
        .then(response => response.json())
        .then(faces => {
            const knownFacesList = document.getElementById('known-faces-list');
            faces.forEach(face => {
                const listItem = document.createElement('li');
                listItem.textContent = face;
                knownFacesList.appendChild(listItem);
            });
        })
        .catch(error => {
            console.error('Error fetching known faces:', error);
        });
});
