

let openShopping = document.querySelector('.shopping');
let closeShopping = document.querySelector('.closeShopping');
let body = document.querySelector('body');


openShopping.addEventListener('click', ()=>{
    body.classList.add('active');
})
closeShopping.addEventListener('click', ()=>{
    body.classList.remove('active');
})

    window.onload = function () {
        document.querySelector(".Regbtn").addEventListener("click", function () {
            document.querySelector(".loginPopup").style.display = "flex";
        });
    }

    document.getElementById("closeBtn").addEventListener("click", function () {
        document.querySelector(".loginPopup").style.display = "none";
    });
    document.addEventListener('DOMContentLoaded', function() {
        // Select both containers
        const productLists = document.querySelectorAll('.product-list, .product-list2, .product-list3, .product-list4');
        const quantitySpan = document.querySelector('.quantity');
    
        // Iterate over both containers to add the event listener to each
        productLists.forEach(function(productList) {
            productList.addEventListener('click', function(event) {
                if (event.target.classList.contains('addtocart')) {
                    let currentQuantity = parseInt(quantitySpan.textContent);
                    quantitySpan.textContent = currentQuantity + 1;
                }
            });
        });
    });

function addToCart(button) {
    var imgSrc = button.getAttribute('data-img');
    var price = parseInt(button.getAttribute('data-price'));
    var productName = button.getAttribute('data-name'); 

    var img = document.createElement('img');
    img.src = imgSrc;

    var li = document.createElement('li');

    var li = document.createElement('li');
    li.appendChild(img);

    var nameSpan = document.createElement('span');
    nameSpan.textContent = productName; 
    li.appendChild(nameSpan);

    function addOneMorePlant(imgSrc, price) {
    var img = document.createElement('img');
    img.src = imgSrc;

    var li = document.createElement('li');
    li.appendChild(img);

    addToCart({getAttribute: function(attr) {
        if(attr === 'data-img') return imgSrc;
        if(attr === 'data-price') return parseInt(price).toString();
        if(attr === 'data-name') return productName;
    }});

    updateQuantity(1); 
}


    var removeBtn = document.createElement('button');
    removeBtn.textContent = '-';
    removeBtn.className = 'buttonmylist';
    removeBtn.onclick = function() {
        removePlant(li,parseInt(price));
        updateQuantity(-1);
    };

    function updateQuantity(amount) {
    var quantitySpan = document.querySelector('.quantity');
    var currentQuantity = parseInt(quantitySpan.textContent, 10);
    var newQuantity = currentQuantity + amount;
    if (newQuantity >= 0) { 
        quantitySpan.textContent = newQuantity;
    }
}

    var addOneMoreBtn = document.createElement('button');
    addOneMoreBtn.textContent = '+';
    addOneMoreBtn.className = 'buttonmylist';
    addOneMoreBtn.onclick = function() {
        addOneMorePlant(imgSrc, parseInt(price), productName);
        
    };
 
    li.appendChild(removeBtn);
    li.appendChild(addOneMoreBtn);
    li.appendChild(addOneMoreBtn);

    document.querySelector('.listCard').appendChild(li);

    updateTotal(parseInt(price)); 
}

function updateTotal(price) {
    var totalDiv = document.querySelector('.total');
    var currentTotal = parseInt(totalDiv.textContent);
    var newTotal = currentTotal + parseInt(price);
    totalDiv.textContent = newTotal.toFixed(2);
}

function removePlant(li, price) {
    li.remove(); 
    updateTotal(-parseInt(price)); 
}

function addOneMorePlant(imgSrc, price, productName) {
    var img = document.createElement('img');
    img.src = imgSrc;
    
    var li = document.createElement('li');
    li.appendChild(img);

 
    addToCart({getAttribute: function(attr) {
        if(attr === 'data-img') return imgSrc;
        if(attr === 'data-price') parseInt(price).toString();
        if(attr === 'data-name') return productName; 
    }});
}

document.querySelectorAll('button.e').forEach(function(button) {
    if (button.textContent.trim() === 'Plantas') {
        button.addEventListener('click', function() {
            var productList = document.querySelector('.product-list');
            var productList2 = document.querySelector('.product-list2');
            var productList3 = document.querySelector('.product-list3');
            var productList4 = document.querySelector('.product-list4');


            productList.style.display = 'grid';

            productList2.style.display = 'none';

            productList3.style.display = 'none';

            productList4.style.display = 'none';
        });
    }
});
document.querySelectorAll('button.e').forEach(function(button) {
    if (button.textContent.trim() === 'Maceteros') {
        button.addEventListener('click', function() {
            var productList = document.querySelector('.product-list');
            var productList2 = document.querySelector('.product-list2');
            var productList3 = document.querySelector('.product-list3');
            var productList4 = document.querySelector('.product-list4');


            productList.style.display = 'none';

            productList2.style.display = 'grid';

            productList3.style.display = 'none';

            productList4.style.display = 'none';
        });
    }
});
document.querySelectorAll('button.e').forEach(function(button) {
    if (button.textContent.trim() === 'Tierra de Hojas') {
        button.addEventListener('click', function() {
            var productList = document.querySelector('.product-list');
            var productList2 = document.querySelector('.product-list2');
            var productList3 = document.querySelector('.product-list3');
            var productList4 = document.querySelector('.product-list4');
            

            productList.style.display = 'none';
            productList2.style.display = 'none';


            productList3.style.display = 'grid';
            productList4.style.display = 'none';
        });
    }
});

document.querySelectorAll('button.e').forEach(function(button) {
    if (button.textContent.trim() === 'Decoraciones') {
        button.addEventListener('click', function() {
            var productList = document.querySelector('.product-list');
            var productList2 = document.querySelector('.product-list2');
            var productList3 = document.querySelector('.product-list3');
            var productList4 = document.querySelector('.product-list4');
            

            productList.style.display = 'none';
            productList2.style.display = 'none';


            productList3.style.display = 'none';
            productList4.style.display = 'grid';
        });
    }
});




