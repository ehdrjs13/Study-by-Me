function rank_update(){
    fetch('http://127.0.0.1:5000/top3', methods=["GET"])
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
}

rank_update()