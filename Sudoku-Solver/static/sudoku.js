solve = function(){
    let arr = [];
    let domArr = [];
    for(let i = 1; i <= 9; i++){
        let row = [];
        let domRow = [];
        for(let j = 1; j <= 9; j++){
            domRow.push(document.getElementById(i + "-" + j));
            cell = domRow[domRow.length - 1].value;
            if(cell === ""){
                row.push(0);
            }
            else{
                row.push(parseInt(cell));
            }
        }
        arr.push(row);
        domArr.push(domRow);
    }
    fetch("/solver", 
        {
            method: "POST",
            body: JSON.stringify({
                values: arr
            }),
            headers: {
                "Content-type": "application/json; charset = UTF-8"
            }
        }
    )
    .then((response) => response.json())
    .then((json) =>{
        if(json['values']){
            let arr = json['values']
            for(let i = 0; i < 9; i++){
                for(let j = 0; j < 9; j++){
                    domArr[i][j].setAttribute("value", arr[i][j]);
                }
            }
        }
    });
    
}