let boxes = document.querySelectorAll('.box')
let display = document.querySelector(".turn")
let turn ='X'
boxes.forEach(function(box){
    box.addEventListener('click',function(){
        if(box.innerText === ""){
            box.innerText=turn;

            if (turn === 'X'){
                box.style.color="red";
                display.innerText= " O's Turn"
                turn ="O";
            }
            else{
                box.style.color = "cyan"
                turn = "X"
                display.innerText= " X's Turn"
                display.c
            }
            checkWinner(); 
        }
    });
});


let reset = document.querySelector('.btn2')
reset.addEventListener("click",()=>{
    let boxes = document.querySelectorAll('.box')
    boxes.forEach((box)=>{
        box.style.pointerEvents = "auto";
        box.innerText=""
    })
})


let new_game = document.querySelector('.btn1')
new_game.addEventListener("click",()=>{
    let boxes = document.querySelectorAll('.box')
    boxes.forEach((box)=>{
        box.style.pointerEvents = "auto";
        box.innerText=""
    })
    let score1 = document.querySelector('.score0')
    score1.innerText = '0'
    let score2 = document.querySelector('.scoreX')
    score2.innerText = "0"

})

let winPatterns = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
];

function checkWinner(){
    for(let pattern of winPatterns){

        let pos1 = boxes[pattern[0]].innerText;
        let pos2 = boxes[pattern[1]].innerText;
        let pos3 = boxes[pattern[2]].innerText;

        if(pos1 !== "" && pos1 === pos2 && pos2 === pos3){
            display.style.color="red";
            display.innerText = "congrats "+pos1+ " Wins The Game " ;
            if (pos1=="X"){
                let score2 = document.querySelector('.scoreX')
                score2.innerText = parseInt(score2.innerText) + 1
            }
            else{
                let score1 = document.querySelector('.score0')
                score1.innerText = parseInt(score1.innerText)+1
            }

            boxes.forEach((box)=>{
                box.style.pointerEvents = "none";
            });
            return;
        }
    }
}

