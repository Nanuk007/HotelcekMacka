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