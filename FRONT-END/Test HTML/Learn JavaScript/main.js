// console.log('log')
// console.error('Erreur')
// console.table(["Abdellah","Zoubair","Hamza","Youssef","Anas","Amine"])
// console.log("%cHello %cNsila","color: red; font-size: 40px; background: green;","color: blue; font-size: 40px;")
// btn = document.querySelector("button")
//var text =  document.getElementById("asw").innerHTML

all_answer = ["Who is the winner in world cup Qatar 2022 ?","Where'is the css property to decorate a text ?","Last Name of Hamza ?","The method used to order a list of numbers ?","Favorite teacher of Amine ?","Basic Structure of Algorithme","Best OS systeme's windows for Anas ?","The speed of Youssef's motorcycle ?","How to get a code-Ascci of a caractere ?","Favorite store of Soupira 7m.. (Zoubair Najdaoui) ?","Who is fast ?","What'is number of my question ?","Your level in programation is ?",] ;
choix = [["Morocco","Brasile","Argentine","Italy"],["list-style","text_decoration","text-align","font-size"],["Wahmani","Wahmane","GiGACHAD","TheKing"],["insert()","sort()","join()","rstrip()"],["Rifai","Oumada","Arrabane","Ait Lhsen"],["nameAlgo Var Début Fin","Début Var Fin","Const Début Fin","Var Début Const Fin"],["Windows XP","Windows 7","Last version","Windows 11"],["36 m/s","80 km/h","speed of light","import turtle"],["char()","ord()","code()","strAscii()"],["amazon","Marjan","Carefoure","Lkhmiss"],["C#","Python","C","C++"],["13","12","20","10"],["Midlle","Good","Insane","I'am Noob:)"]] ;
coreect_answer = ["Argentine","text_decoration","GiGACHAD","sort()","Arrabane","nameAlgo Var Début Fin","Last version","36 m/s","ord()","Lkhmiss","C","13","I'am Noob:)"] ;

function aud1(){
    const audio1 = new Audio(); 
    audio1.src = "./correct.wav" ;
    audio1.play();
} 
function aud2(){
    const audio2 = new Audio(); 
    audio2.src = "./false.wav";
    audio2.play();
} 
function aud3(){
    const audio3 = new Audio(); 
    audio3.src = "./Congratulations-sound.mp3";
    audio3.play();
} 

var score = 0 ;
var end = false ;
var asw = "" ;
var n = 0 ;

var btn1 = document.getElementById("result1");
var btn2 = document.getElementById("result2");
var btn3 = document.getElementById("result3");
var btn4 = document.getElementById("result4");
var btnS = document.getElementById("statut");

t_butt =[btn1, btn2, btn3, btn4] ;
function next_answer(){
    n += 1 ;
    if (n <= 13){
        end = false
        btnS.style.display = "none"
        asw = coreect_answer[n-1] ;
        document.getElementById("question").innerHTML = all_answer[n-1];
        for (var i = 0 ; i <= 3; i++){
            t_butt[i].style.display = "block" ;
            t_butt[i].innerHTML = choix[n-1][i];
            t_butt[i].style.backgroundColor = '#e6e6e6';
        }
    }
    if(n > 13){
        aud3()
        document.write("<h1>Your Ranke :</h1>");
        document.querySelector("h1").style.marginLeft = "38%" ;
        document.querySelector("h1").style.marginTop = "30vh" ;
        document.querySelector("h1").style.fontFamily = "Trebuchet MS" ;
        document.querySelector("h1").style.fontSize = "60px" ;
        document.querySelector("h1").style.fontWeight = "bold" 
        document.write('<h3 id="rank"></h3>');
        document.querySelector("h3").style.marginLeft = "45%" ;
        document.querySelector("h3").style.marginTop = "10px" ;
        document.querySelector("h3").style.fontFamily = "Trebuchet MS" ;
        document.querySelector("h3").style.fontSize = "60px" ;
        document.querySelector("h3").style.fontWeight = "bold" ;
        document.getElementById("rank").innerHTML = String(score) + "/13" ;
        document.querySelector("body").style.backgroundImage = "linear-gradient(45deg,#ffa500,#ff9668,#ff00ee,#0000ff)"
    }
}


btnS.style.backgroundColor = "#0a0";
function answer(btn){
    if (end == false){
        end = true
        let text = btn.innerHTML
        btnS.style.display = "none"
        if (text == asw){
            aud1()
            score += 1
            btnS.style.display = "block";
            btnS.style.backgroundColor = "#0c0";
            btnS.innerHTML = "Next (:";
            btn.style.backgroundColor = "#0c0"; 
        }
        else{
            aud2()
            btn.style.backgroundColor = "#f00";
            btnS.style.display = "block";
            btnS.innerHTML = "Next ):";
            btnS.style.backgroundColor = "#f00";
            for (var i = 0 ; i <= 3; i++){
                if (t_butt[i].innerHTML == asw){
                    t_butt[i].style.backgroundColor = "#0c0";
                }
            } 
        }
    }  
}

function answer1(){
    answer(btn1)
}
function answer2(){
    answer(btn2)
}
function answer3(){
    answer(btn3)
}
function answer4(){
    answer(btn4)
}

