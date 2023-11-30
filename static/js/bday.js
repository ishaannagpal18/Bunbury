const canvas = document.getElementById('canvas')
const ctx = canvas.getContext('2d')
const nameInput = document.getElementById('name')
const downloadBtn = document.getElementById('download-btn')
  let name = document.getElementById("p").innerHTML;
  let bday_img = document.getElementById("p1");

  let myFont = new FontFace(
    "Roboto",
    "url(https://fonts.googleapis.com/css2?family=Abril+Fatface&display=swap)"
  );



const image = new Image()
// var pat = ctx.createPattern(bday_img, "repeat");
image.src = '/static/img/bday1.png'


image.onload = function () {
	drawImage()
}


function drawImage() {
	ctx.clearRect(0, 0, canvas.width, canvas.height)
  ctx.drawImage(bday_img, 168, 126, 154, 174)
	// ctx.drawImage(image, 0, 0, canvas.width, canvas.height)
	ctx.font = 'bold 20px Garamond'
	ctx.fillStyle = '#000'
	ctx.fillText(name, 330, 230)

}

// nameInput.addEventListener('input', function () {
// 	drawImage()
// })

downloadBtn.addEventListener('click', function () {
	 downloadBtn.href = canvas.toDataURL('image/jpg',1)
	 downloadBtn.download = 'Birthday-' + name
})
