var currentImage = 0;
var scale_x, scale_y;
var wm_x = 0, wm_y = 0;
var mouse_x, mouse_y;
var imageInput = document.getElementById('inputImage')
var watermarkInput = document.getElementById('inputWatermark')
var image = document.getElementById('image')
var watermark = document.getElementById('watermark')
var imageBackupUrl = ''

imageInput.addEventListener('change', () => loadImage())
watermarkInput.addEventListener('change', () => loadWatermark())
document.addEventListener('keydown', moveWatermark)
document.getElementById('overlayMode').addEventListener('change', function(){
    watermark.style.mixBlendMode = this.value
})

function loadImage() {
    if (imageInput.files.length > currentImage) {
        image.onload = function () {
            if (this.naturalHeight > 32000 || this.naturalWidth > 32000 || this.naturalWidth*this.naturalHeight > 250000000) {
                alert('Image is too large. (Browser limitation)')
                this.width = 0
                this.height = 0
            }
            this.width = this.naturalWidth
            var div = document.getElementById('imageContainer')
            this.style.maxWidth = '100%'
            div.style.maxWidth = '100%'
            //reset previous styles
            div.style.height = 'unset'
            div.style.width = 'unset'
            this.style.height = 'unset'
            this.style.width = 'unset'
            var computedStyle = window.getComputedStyle(this)
            div.style.width = computedStyle.width
            div.style.height = computedStyle.height
            scale_x = parseFloat(computedStyle.width.replace('px','')) / parseInt(this.naturalWidth)
            scale_y = parseFloat(computedStyle.height.replace('px','')) / parseInt(this.naturalHeight)
            div.style.maxWidth = 'unset'
            this.style.maxWidth = 'unset'
            this.style.width = div.style.width
            this.style.height = div.style.height
        }
        image.src = URL.createObjectURL(imageInput.files[currentImage])
    } else {
        alert('No more images loaded.')
        currentImage = 0
    }
}
function loadWatermark() {
    if(scale_x && scale_y) {
        watermark.onload = function () {
            var position = document.getElementById('defaultPosition').value
            if (position == 'center') {
                wm_x = Math.round((image.naturalWidth - this.naturalWidth) / 2)
                wm_y = Math.round((image.naturalHeight - this.naturalHeight) / 2)
            } else {
                if (position.indexOf('right') > -1) {
                    wm_x = image.naturalWidth - this.naturalWidth
                } else {
                    wm_x = 0
                }
                if (position.indexOf('bottom') > -1) {
                    wm_y = image.naturalHeight - this.naturalHeight
                } else {
                    wm_y = 0
                }
            }
            this.style.top = String(wm_y * scale_y) + 'px'
            this.style.left = String(wm_x * scale_x) + 'px'
            this.style.width = String(scale_x * this.naturalWidth) + 'px'
            this.style.height = String(scale_y * this.naturalHeight) + 'px'
            this.onmousedown = dragWatermarkStart
        }
        watermark.src = URL.createObjectURL(watermarkInput.files[0])
    } else {
        alert('Load image first.')
    }
}
function moveWatermark (e) {
    if (watermark.src) {
        switch (e.keyCode) {
            case 37:
                wm_x -= e.ctrlKey ? 0.05 : 1
                break
            case 38:
                wm_y -= e.ctrlKey ? 0.05 : 1
                break
            case 39:
                wm_x += e.ctrlKey ? 0.05 : 1
                break
            case 40:
                wm_y += e.ctrlKey ? 0.05 : 1
                break
            default:
                return
            
        }
        e.preventDefault()
        watermark.style.top = String(wm_y * scale_y) + 'px'
        watermark.style.left = String(wm_x * scale_x) + 'px'
    }
}
function dragWatermarkStart(e) {
    e = e || window.event;
    e.preventDefault();
    // get the mouse cursor position at startup:
    mouse_x = e.clientX;
    mouse_y = e.clientY;
    document.onmouseup = dragWatermarkEnd;
    // call a function whenever the cursor moves:
    document.onmousemove = dragWatermark;
}
function dragWatermark(e) {
    e = e || window.event;
    e.preventDefault();
    // calculate the new cursor position:
    wm_x -= Math.round((mouse_x - e.clientX) / scale_x);
    wm_y -= Math.round((mouse_y - e.clientY) / scale_y);
    mouse_x = e.clientX;
    mouse_y = e.clientY;
    // set the element's new position:
    watermark.style.top = String(wm_y * scale_y) + 'px'
    watermark.style.left = String(wm_x * scale_x) + 'px'
}
function dragWatermarkEnd(e) {
    // stop moving when mouse button is released:
    document.onmouseup = null;
    document.onmousemove = null;
}
function unwatermark() {
    var imagedata_image, imagedata_watermark;
    var w = watermark.naturalWidth
    if (wm_x + w > image.naturalWidth) {
        w -= (wm_x + w) - image.naturalWidth
    }
    var h = watermark.naturalHeight
    if (wm_y + h > image.naturalHeight) {
        h -= (wm_y + h) - image.naturalHeight
    }
    var x = Math.floor(wm_x)
    var x_sub = wm_x % 1
    var y = Math.floor(wm_y)
    var y_sub = wm_y % 1
    
    //prepare image canvas
    var c = document.createElement('canvas')
    var ctx = c.getContext('2d')
    c.width = image.naturalWidth
    c.height = image.naturalHeight
    ctx.drawImage(image, 0, 0)
    
    //prepare watermark canvas
    var c_wm = document.createElement('canvas')
    var ctx_wm = c_wm.getContext('2d')
    c_wm.width = watermark.naturalWidth
    c_wm.height = watermark.naturalHeight
    if (x_sub || y_sub) {
        ctx_wm.translate(x_sub, y_sub)
    }
    ctx_wm.drawImage(watermark, 0, 0)
    
    imagedata_image = ctx.getImageData(x, y, w, h)
    imagedata_watermark = ctx_wm.getImageData(0, 0, w, h)
    
    const transparencyThreshold = parseInt(document.getElementById('transparencyThreshold').value)
    const opaqueThreshold = parseInt(document.getElementById('opaqueThreshold').value)
    
    //unwatermark according to Fire's formula
    var alpha_img, alpha_wm, factor1
    for (var i = 0; i < w*h*4; i+=4) {
        //format: RGBA
        //(new pixel)=(1/(1-alpha))*(old pixel)+(-alpha/(1-alpha))*(watermark's pixel)
        if (imagedata_watermark.data[i+3] > transparencyThreshold) {
            alpha_img = 255 / (255 - imagedata_watermark.data[i+3])
            alpha_wm = -imagedata_watermark.data[i+3] / (255 - imagedata_watermark.data[i+3])
            imagedata_image.data[i] = Math.round(alpha_img * imagedata_image.data[i] + alpha_wm * imagedata_watermark.data[i])
            imagedata_image.data[i+1] = Math.round(alpha_img * imagedata_image.data[i+1] + alpha_wm * imagedata_watermark.data[i+1])
            imagedata_image.data[i+2] = Math.round(alpha_img * imagedata_image.data[i+2] + alpha_wm * imagedata_watermark.data[i+2])
            if (imagedata_watermark.data[i+3] > opaqueThreshold) {
                //smoothing of very opaque pixels
                factor1 = (imagedata_watermark.data[i+3] - opaqueThreshold) / (255 - opaqueThreshold)
                imagedata_image.data[i] = Math.round(factor1 * imagedata_image.data[i-4] + (1 - factor1) * imagedata_image.data[i])
                imagedata_image.data[i+1] = Math.round( factor1 * imagedata_image.data[i-3] + (1 - factor1) * imagedata_image.data[i+1])
                imagedata_image.data[i+2] = Math.round( factor1 * imagedata_image.data[i-2] + (1 - factor1) * imagedata_image.data[i+2])
            }
        }
    }
    
    ctx.putImageData(imagedata_image, wm_x, wm_y)
    if (c.toBlob) {
        c.toBlob((blob) => {
            url = URL.createObjectURL(blob)
            triggerDownload(url)
        }, 'image/png')
    } else {
        url = c.toDataURL('image/png')
        triggerDownload(url)
    }
}
function triggerDownload(url) {
    imageBackupUrl = image.src
    image.src = url
    if (document.getElementById('preview').checked) {
        watermark.style.display = 'none'
        document.getElementById('confirm').style.display = 'initial'
    } else {
        confirmYes()
    }
}
function confirmYes() {
    var a = document.createElement('a')
    a.href = image.src
    a.download = imageInput.files[currentImage].name.replace(/\.[^\.]*$/, '_uwm.png')
    a.click()
    if (imageInput.files.length > currentImage + 1) {
        currentImage++
        loadImage()
    }
    imageBackupUrl = ''
    watermark.style.display = 'initial'
    document.getElementById('confirm').style.display = 'none'
}
function confirmNo() {
    image.src = imageBackupUrl
    watermark.style.display = 'initial'
    document.getElementById('confirm').style.display = 'none'
}


//front end stuff

function toggleOptions() {
    var settings = document.getElementById('settings')
    if (settings.style.display == 'none') {
        settings.style.display = 'initial'
    } else {
        settings.style.display = 'none'
    }
}
