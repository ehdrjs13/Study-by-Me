var time = 0;
var state = true;
var timeRecorded = 0;

function timeClear(){
    let timeRecorded = time;
    let state = false;

    let time = 0;

}

function addTime(){
    time++;
    updateTime(time)
}
function timeStart(){
    if (state) {
        setInterval(addTime, 1000);

    }
}

function updateTime(time){
    console.log(time)

}

timeStart();

