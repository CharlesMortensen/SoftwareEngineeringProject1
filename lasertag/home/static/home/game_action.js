interval = 0;
time = 5*60;
timer_running = false;
warning_time = 10;
warning_timer_running = false;
const timer_display = document.getElementById("timer");
const combat_log = document.getElementById("combatLog");
const warning_timer_display = document.getElementById("warning_timer");
const gameSocket = new WebSocket('ws://'+ window.location.host + '/ws/game/');

gameSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    let text = "";
    for (const x in data["messages"]) {
        combat_log.innerHTML = JSON.stringify(data["messages"][x]) + "<br>" + combat_log.innerHTML;
    }
    console.log(text);
    //combat_log.innerHTML = data.messages + combat_log.innerHTML;
}

function start_warning(){
    if(warning_timer_running == false && timer_running == false){
        warning_time = 10;
        interval = setInterval(display_time, 1000);
        warning_timer_running = true;
    }

}
function start_timer(){
    if(timer_running == false){
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
        time = 0;
        combat_log.innerHTML = "";
        display_time();
    }
    
}

function display_time(){
    if(warning_timer_running == true){
        if(warning_time < 1){
            clearInterval(interval);
            warning_time = 10;
            warning_timer_running = false;
            warning_timer_display.style.visibility = "hidden";
            start_timer();
        }else{
            warning_timer_display.style.visibility = "visible";
        }
    
        warning_timer_display.innerHTML = "<p id='warning_timer_text'>Game Starts In: </p>" + warning_time;
        warning_time -= 1;
    }else{
        if(time < 0){
            clearInterval(interval);
            time = 5*60;
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