$('#image').change(function() {
    var i = $(this).prev('label').clone();
    var file = $('#image')[0].files[0].name;
    $('.image-label').attr('data-text', file);
});

// document.querySelector("#image").onchange = function(){
//     document.querySelector(".image-label").style.content = this.files[0].name;
//   }