var scale = document.getElementById('scale');
var thresh = document.getElementById('thresh');
var range = document.getElementById('range');
var range2 = document.getElementById('range2');
var submit = document.getElementById('submit');
var setup = document.getElementById('setup');
var thanks = document.getElementById('thanks');
var error = document.getElementById('error');
var loading = document.getElementById('lds-grid');
var rendered = document.getElementById('starter-image');
var isloading = false; 
var render_image = true;

loading.style.display = "none";

document.addEventListener("remove", function(){
  rendered.style.display = "none";
});

submit.addEventListener('click', function (e) { 
  e.preventDefault();
  submit.style.display = "none";
  isloading = !isloading; 
  if (isloading){ 
    loading.style.display = "block";
  }
  else{ 
    loading.style.display = "none";
  }
  $.ajax({
    type: "GET",
    url: '/sketch/' + scale.value + '/' + thresh.value,
    success: function(data) {
      console.log(data.status);
      if (data.status === 200){ 
        setup.style.display = "none";
        thanks.style.display = "flex";
      }
      else{
        error.style.display = "block";
      }
      loading.style.display = "none";
    },
  })
}, false);

scale.addEventListener('input', function () {
  range.innerHTML = scale.value;
}, false);

scale.addEventListener('change', function () { 
  callPlot(range.value, range2.value);
})

thresh.addEventListener('input', function () {
  range2.innerHTML = thresh.value;
}, false);

thresh.addEventListener('change', function () { 
  callPlot(range.value, range2.value);
})

var image_path = document.getElementById('image_path').innerHTML.slice(8);
var elem = document.createElement("img");
elem.setAttribute("id", "image-api");
document.getElementById("image-wrapper").appendChild(elem);

callPlot = () => { 
  if (render_image){
    var event = new CustomEvent("remove", { "detail": "api has been called" });
    document.dispatchEvent(event);
    var turn_on = document.getElementById("image-wrapper");
    turn_on.style.display = 'flex';
    render_image = false;
  }
  $.ajax({
    type: "GET",
    url: '/query/' + image_path + '/' + scale.value + '/' + thresh.value,
    success: function(data) {
      document.getElementById('image-api').setAttribute('src', data.html);
    },
  })
} 
