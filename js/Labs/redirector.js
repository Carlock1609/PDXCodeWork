
function getRandomLink() {
    let links = ["https://www.google.com/", "https://www.bing.com/", "https://www.facebook.com/", "https://unsplash.com/", "https://fonts.google.com/", "https://www.codewars.com/dashboard", "https://www.codewars.com/dashboard", "https://colours.neilorangepeel.com/"]
    return links[Math.floor(Math.random() * 8)] 
}

function initiateTimer() {
    let redirect = document.querySelector("a");

    redirect.addEventListener("click", function() {
        redirect.setAttribute("href", getRandomLink());
    });
};

setTimeout(initiateTimer(), 5000);