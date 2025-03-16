let index = 0;
    const images = document.querySelectorAll(".slider-container img");
    const totalImages = images.length;
    function showSlide() {
        document.querySelector(".slider-container").style.transform = `translateX(${-index * 100}%)`;
    }
    function nextSlide() {
        index = (index + 1) % totalImages;
        showSlide();
    }
    function prevSlide() {
        index = (index - 1 + totalImages) % totalImages;
        showSlide();
    }
    setInterval(nextSlide, 5000);

function updateRoomImage() {
    let roomSelect = document.getElementById("room").value;
    let roomImage = document.getElementById("room-image");

    let images = {
        "room1": "images/room1.jpg",
        "room2": "images/room2.jpg",
        "room3": "images/room3.jpg"
    };

    roomImage.src = images[roomSelect] || "images/default-room.jpg";
}