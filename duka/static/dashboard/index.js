let loadBtnContainer = document.querySelector('#load-btn-container');
let loadMoreBtn = document.querySelector("#load-btn");
let currentItem = 3;
let items = [...document.querySelectorAll('.my-item')];

loadMoreBtn.onclick = () => {
    for (var i = currentItem; i < currentItem + 3; i++){
        if (i >= items.length) {
            break; // Break the loop if the end of the array is reached
        }
        items[i].style.display = 'block';
    }
    currentItem += 3;

    if (items.length > 3 && currentItem >= items.length){
        loadBtnContainer.style.display = "none";
    } else {
        loadBtnContainer.style.display = "block";
    }
};

if (items.length <= 3) {
    loadBtnContainer.style.display = "none";
}