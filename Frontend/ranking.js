function rank_update() {
    fetch('http://127.0.0.1:5000/top3', {
        method: "GET"
    })
    .then(response => response.json())
    .then(data => {
        console.log(data); 
        
        const name1 = data.first.name;
        const time1 = timeArray2str(data.first.time);
        const memo1 = data.first.memo;
        
        const name2 = data.second.name;
        const time2 = timeArray2str(data.second.time);
        const memo2 = data.second.memo;
        
        const name3 = data.third.name;
        const time3 = timeArray2str(data.third.time);
        const memo3 = data.third.memo;

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
        console.error(error);

    });
}


function timeArray2str(arr){
    const hours = String(arr[0]).padStart(2, '0');
    const minutes = String(arr[1]).padStart(2, '0');
    const seconds = String(arr[2]).padStart(2, '0');
    
    return `${hours}:${minutes}:${seconds}`
}

rank_update()

