$(document).ready(function(){
    $("#registroForm").submit(function(event){

        event.preventDefault();
        // Es la validacion de usted con cambios para hacerlo mas "eficiente"
    
        var rut = $("#rut").val();
        var nombre = $("#nombre").val();
        var apellidoPaterno = $("#apellidoPaterno").val();
        var apellidoMaterno = $("#apellidoMaterno").val();
        
        var genero = $("#genero").val();
        var celular = $("#celular").val();

   
        if(!/^[\d]+[kK]?$/g.test(rut)){
            alert("Rut must only contain numbers and optionally end with a 'k'.");
            return;
        }

        
        // ^ inico de linea
        // [\d]+ del 0 al 9 
        // [kK]? cualquira de las 2 letras
        // $ marca al final de la linea
        // g =global
        // esta muy bacan XD



        if(nombre.length < 3 || nombre.length > 20 || !isNaN(nombre) ||
    apellidoPaterno.length < 3 || apellidoPaterno.length > 20 ||
    apellidoMaterno.length < 3 || apellidoMaterno.length > 20){
    alert("The First and Last Name must be between 3 and 20 characters and must not be numbers.");
    return;
}



    
        if(genero === ""){
            alert("You must select a gender.");
            return;
        }


        if(celular.length < 9 || celular.length > 12){
            alert("Phone number must be 9 to 12 characters.");
            return;
        }


        alert("Successful registration!");

    });
});
window.onload = function() {
    document.getElementById("Regbtn").addEventListener("click", function () {
    document.querySelector(".loginPopup").style.display = "flex";
    });

    document.getElementById("closeBtn").addEventListener("click", function () {
    document.querySelector(".loginPopup").style.display = "none";
    });
    }

//Funcion para el carrusel jeje creo sacarlo de stackoverflow iirc

// $(document).ready(function () {
//     var currentSlide = 0;
//     var images = ['https://nmrcdn.s3.amazonaws.com/assets/787/assets/responsive/297000/297000/web_cat.jpg',
//         'https://live.staticflickr.com/2233/4218517831_7ecd5f876b.jpg',
//         'https://www.guildinsurance.com.au/images/librariesprovider3/breed-images/500x500/tabby-(1)-(1).jpg?sfvrsn=b28f650b_2'];

//     function changeSlide(next) {
//         currentSlide = (currentSlide + (next ? 1 : images.length - 1)) % images.length;
//         $('#carouselImg').attr('src', images[currentSlide]);
//     }

//     $('#prevBtn').click(function () {
//         changeSlide(false);
//     });

//     $('#nextBtn').click(function () {
//         changeSlide(true);
//     });
// });

