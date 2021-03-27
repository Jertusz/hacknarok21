var video = document.querySelector("#videoElement");
var pauseBtn = document.querySelector("#pause");
var resumeBtn = document.querySelector("#resume");

webgazer
    .setGazeListener(function (data, elapsedTime) {
        if (data == null) {
            return;
        }
        var xprediction = data.x; //these x coordinates are relative to the viewport
        var yprediction = data.y; //these y coordinates are relative to the viewport
        console.log(elapsedTime); //elapsed time is based on time since begin was called
        console.log(xprediction);
        console.log(yprediction);
    })
    .begin();

pauseBtn.addEventListener("click", webgazer.pause);
resumeBtn.addEventListener("click", webgazer.resume);

// function stop(e) {
//     var stream = video.srcObject;
//     var tracks = stream.getTracks();

//     for (var i = 0; i < tracks.length; i++) {
//         var track = tracks[i];
//         track.stop();
//     }

//     video.srcObject = null;
// }

// function start() {
//     if (navigator.mediaDevices.getUserMedia) {
//         navigator.mediaDevices
//             .getUserMedia({ video: true })
//             .then(function (stream) {
//                 video.srcObject = stream;
//             })
//             .catch(function (err0r) {
//                 console.log(err0r);
//             });
//     } else {
//         console.log("Not supported for your browser");
//     }
// }

// stopBtn.addEventListener("click", stop);
// startBtn.addEventListener("click", start);
