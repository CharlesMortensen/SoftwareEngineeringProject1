interval = 0;
time = 5*60;
timer_running = false;
const element = document.getElementById("timer");
function start_count(){
    if(timer_running == false){
        interval = setInterval(display_time, 1000);
        timer_running = true;
    }

}
function reset_count(){
    if(timer_running == true){
        time = 0;
        display_time();
    }
}

function display_time(){
    if(time < 0){
        clearInterval(interval);
        time = 5*60;
        timer_running = false;
        return;
    }
    
    min = Math.floor(time/60);
    sec = time%60;
    element.innerHTML = String(min).padStart(2,'0') + ":" + String(sec).padStart(2,'0');
    time -= 1;
}