function rank_update() {
    fetch('http://127.0.0.1:5000/top3', {
        method: "GET"
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); // 받아온 데이터를 콘솔에 출력하여 확인
        
        // 데이터 처리
        const name1 = data.first.name;
        const time1 = timeArray2str(data.first.time);
        const memo1 = data.first.memo;
        
        const name2 = data.second.name;
        const time2 = timeArray2str(data.second.time);
        const memo2 = data.second.memo;
        
        const name3 = data.third.name;
        const time3 = timeArray2str(data.third.time);
        const memo3 = data.third.memo;

        // HTML 업데이트
        document.getElementById('name1').innerHTML = name1;
        document.getElementById('time1').innerHTML = time1;
        document.getElementById('memo1').innerHTML = memo1;

        document.getElementById('name2').innerHTML = name2;
        document.getElementById('time2').innerHTML = time2;
        document.getElementById('memo2').innerHTML = memo2;

        document.getElementById('name3').innerHTML = name3;
        document.getElementById('time3').innerHTML = time3;
        document.getElementById('memo3').innerHTML = memo3;
    })
    .catch(error => {
        console.error('데이터를 불러오는 도중 에러가 발생했습니다:', error);
        // 에러 처리 로직을 추가할 수 있습니다.
    });
}


function timeArray2str(arr){
    const hours = String(arr[0]).padStart(2, '0');
    const minutes = String(arr[1]).padStart(2, '0');
    const seconds = String(arr[2]).padStart(2, '0');
    
    return `${hours}:${minutes}:${seconds}`
}

rank_update()

