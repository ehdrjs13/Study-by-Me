var time = 0;
var state = true;
var timeRecorded = 0;
var intervalId;
var timeClearIntervalId;

    
var domhour;
var dommin;
var domsec;

const DISPLAYID = 'timeDisplay';

//타이머 종료&초기화
async function timeClear(){
    console.log('Timer Stopped. ')
    timeRecorded = getSepTime(time);
    // await updateTime(timeRecorded);

    timerEnd(timeRecorded);
    state = false;
    time = 0;

    

}

function addTime(){
    if (state) {
        time++;
        updateTime(time)

    } else {
        clearInterval(intervalId); 
        clearInterval(timeClearIntervalId);
    }
}

//타이머 진행
function timeStart(){
    if (state) {

        intervalId = setInterval(addTime, 1000);
    }
}


//시간 디스플레이
function updateTime(time){
    time = getSepTime(time);

    text = (time[0]+':'+time[1]+':'+time[2]);
    
    document.getElementById(DISPLAYID).innerHTML = text

    console.log(text);
}

//초를 시분초로
function getSepTime(time){
    hour = Math.floor(time/3600)
    minuit = Math.floor((time-(hour*3600))/60)
    second = time - (hour*3600) - (minuit*60)

    return [hour,minuit,second]
}

function fetchTime(time){
    domhour = time[0]
    dommin = time[1]
    domsec = time[2]
}

//기록 완료된 시간 서버로 보내기
function timerEnd(time){
    var usrName = prompt('닉네임을 입력해주세요!')
    var memo = prompt('공부한 내용을 짧게 입력해주세요!')

    var usrData = {
        "name": usrName,
        "time": time,
        "memo": memo
    };

    fetch('http://127.0.0.1:5000/upload', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(usrData)
        
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
    })
    .catch((error) => {
        console.error('Error:', error);
    });


}

timeStart();

// timeClearIntervalId = setInterval(timeClear, 10000);
