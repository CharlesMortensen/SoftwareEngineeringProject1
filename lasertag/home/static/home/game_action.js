interval = 0;
time = 6*60;
timer_running = false;
warning_time = 30;
warning_timer_running = false;
const timer_display = document.getElementById("timer");
const combat_log = document.getElementById("combatLog");
const redPoints = document.getElementById("redPoints");
const bluePoints = document.getElementById("bluePoints");
const warning_timer_display = document.getElementById("warning_timer");

const gameSocket = new WebSocket('wss://'+ window.location.host + '/ws/game/');
const controlSocket = new WebSocket('wss://' + window.location.host + '/ws/control/');

gameSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    for (const x in data["messages"]) {
        combat_log.innerHTML = JSON.stringify(data["messages"][x]) + "<br>" + combat_log.innerHTML;
        for (var id in data.ids) {
            var playerScore = document.getElementById("table-" + id);
            playerScore.innerHTML = data.ids[id];
            //console.log(data.ids[id]);
        }
        redPoints.innerHTML = data.redpoints;
        bluePoints.innerHTML = data.bluepoints;
        //console.log(JSON.stringify(data["ids"]));
    }
}

function start_warning(){
    if(warning_timer_running == false && timer_running == false){
        warning_time = 30;
        interval = setInterval(display_time, 1000);
        warning_timer_running = true;
    }

}
function start_timer(){
    if(timer_running == false){
        controlSocket.send("start");
        interval = setInterval(display_time, 1000);
        timer_running = true;
    }

}
function reset_timer(){
    if(warning_timer_running == true){
        warning_time = 0;
        display_time();
    }
    if(timer_running == true){
        controlSocket.send("end");
        time = 0;
        combat_log.innerHTML = "";
        display_time();
    }
    
}

function display_time(){
    score_blink();
    if(warning_timer_running == true){
        if(warning_time < 1){
            clearInterval(interval);
            warning_time = 30;
            warning_timer_running = false;
            warning_timer_display.style.visibility = "hidden";
            var scores = document.getElementsByClassName("resettable");

            for (var i = 0; i < scores.length; i++) {
                scores[i].innerHTML = "0";
            }
            start_timer();
        }else{
            warning_timer_display.style.visibility = "visible";
        }
    
        warning_timer_display.innerHTML = "<p id='warning_timer_text'>Game Starts In: </p>" + warning_time;
        warning_time -= 1;
    }else{
        if(time < 0){
            clearInterval(interval);
            time = 6*60;
            timer_running = false;
            return;
        }
        
        min = Math.floor(time/60);
        sec = time%60;
        timer_display.innerHTML = String(min).padStart(2,'0') + ":" + String(sec).padStart(2,'0');
        time -= 1;
        gameSocket.send("a");
    }
}

function score_blink(){
    var red_score = document.getElementById("redPoints");
    var blue_score = document.getElementById("bluePoints");
    if(timer_running == true){
        console.log(red_score.innerHTML);
        if(parseInt(red_score.innerHTML) > parseInt(blue_score.innerHTML)){
            red_score.classList.add("blink_text");
            if (blue_score.classList.contains("blink_text")) {
                blue_score.classList.remove("blink_text");
            }
        }else if(parseInt(red_score.innerHTML) < parseInt(blue_score.innerHTML)){
            blue_score.classList.add("blink_text");
            if (red_score.classList.contains("blink_text")) {
                red_score.classList.remove("blink_text");
            }
        }else{
            red_score.classList.add("blink_text");
            blue_score.classList.add("blink_text");
        }
    }else{
        if (red_score.classList.contains("blink_text")) {
            red_score.classList.remove("blink_text");
        }
        if (blue_score.classList.contains("blink_text")) {
            blue_score.classList.remove("blink_text");
        }
    }
}